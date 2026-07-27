"""
Chat con documentos ASMAC — multi-backend
LLM_BACKEND: claude | openai | gemini | kimi | glm | ollama
Configuración sensible via variables de ambiente o archivo .env
"""

import os
import re
import glob
import gradio as gr
from pathlib import Path

BASE_DIR = Path(__file__).parent
DOCS_DIR = BASE_DIR / "md"

# ── .env loader ───────────────────────────────────────────────────────────────
def _load_dotenv() -> None:
    env_file = BASE_DIR / ".env"
    if not env_file.exists():
        return
    for line in env_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        key = key.strip()
        if not os.environ.get(key):
            os.environ[key] = val.strip().strip('"').strip("'")

_load_dotenv()

def _env(key: str, default: str = "") -> str:
    return os.environ.get(key, default).strip()

# ── Registro de backends ──────────────────────────────────────────────────────
BACKENDS: dict[str, dict] = {
    "claude": {
        "label":         "Claude (Anthropic)",
        "key_env":       "ANTHROPIC_API_KEY",
        "model_env":     "ANTHROPIC_MODEL",
        "default_model": "claude-sonnet-4-6",
    },
    "openai": {
        "label":         "ChatGPT (OpenAI)",
        "key_env":       "OPENAI_API_KEY",
        "model_env":     "OPENAI_MODEL",
        "default_model": "gpt-4o",
        "base_url_env":  "OPENAI_BASE_URL",
    },
    "gemini": {
        "label":         "Gemini (Google)",
        "key_env":       "GEMINI_API_KEY",
        "model_env":     "GEMINI_MODEL",
        "default_model": "gemini-2.0-flash",
        "base_url":      "https://generativelanguage.googleapis.com/v1beta/openai/",
    },
    "kimi": {
        "label":         "Kimi (Moonshot AI)",
        "key_env":       "KIMI_API_KEY",
        "model_env":     "KIMI_MODEL",
        "default_model": "moonshot-v1-128k",
        "base_url":      "https://api.moonshot.cn/v1",
    },
    "glm": {
        "label":         "GLM (Zhipu AI)",
        "key_env":       "GLM_API_KEY",
        "model_env":     "GLM_MODEL",
        "default_model": "glm-4-flash",
        "base_url":      "https://open.bigmodel.cn/api/paas/v4/",
    },
    "ollama": {
        "label":         "Ollama (local)",
        "key_env":       "",
        "model_env":     "OLLAMA_MODEL",
        "default_model": "llama3.2",
        "base_url_env":  "OLLAMA_BASE_URL",
        "base_url":      "http://localhost:11434/v1",
        "api_key":       "ollama",
    },
}

BACKEND_NAME = _env("LLM_BACKEND", "claude").lower()
if BACKEND_NAME not in BACKENDS:
    print(f"⚠️  Backend '{BACKEND_NAME}' desconocido. Usando 'claude'.")
    BACKEND_NAME = "claude"
CFG = BACKENDS[BACKEND_NAME]

# ── Carga de documentos ───────────────────────────────────────────────────────
def _cargar_docs() -> dict[str, str]:
    if not DOCS_DIR.exists():
        print(f"⚠️  Carpeta no encontrada: {DOCS_DIR}")
        return {}
    docs = {}
    for path in sorted(DOCS_DIR.glob("*.md")):
        for enc in ("utf-8", "latin-1", "cp1252"):
            try:
                docs[path.name] = path.read_text(encoding=enc)
                break
            except (UnicodeDecodeError, LookupError):
                continue
        else:
            docs[path.name] = path.read_text(encoding="utf-8", errors="replace")
            print(f"  ⚠️ {path.name}: encoding desconocido, caracteres reemplazados")
    return docs

DOCS: dict[str, str] = _cargar_docs()
TOP_K: int = int(_env("DOCS_TOP_K", "6"))

def _seleccionar_docs(query: str) -> tuple[str, list[str]]:
    """Retorna los TOP_K documentos más relevantes para la consulta."""
    tokens = set(re.findall(r'\w+', query.lower()))
    scored = []
    for name, content in DOCS.items():
        cl = content.lower()
        score = sum(cl.count(t) for t in tokens if len(t) > 2)
        scored.append((score, name, content))
    scored.sort(reverse=True)
    seleccion = scored[:TOP_K]
    contexto = "\n\n---\n\n".join(
        f"## Documento: {name}\n\n{content}"
        for _, name, content in seleccion
    )
    nombres = [name for _, name, _ in seleccion]
    return contexto, nombres

SYSTEM_BASE = (
    "Eres un asistente experto en los documentos oficiales de la "
    "Asociación de Scouts de México (ASMAC). Responde preguntas basándote "
    "exclusivamente en los documentos que se te proporcionan.\n\n"
    "Reglas:\n"
    "- Responde siempre en español.\n"
    "- Cita el documento de origen cuando sea relevante.\n"
    "- Si la información no está en los documentos, dilo claramente.\n"
    "- Sé conciso pero completo.\n"
    "- Usa listas o encabezados cuando mejoren la legibilidad.\n\n"
    "DOCUMENTOS DE REFERENCIA:\n{contexto}"
)

# ── Llamada al LLM ────────────────────────────────────────────────────────────
def _llamar_llm(mensajes: list[dict], system: str, api_key: str, model: str) -> str:
    if BACKEND_NAME == "claude":
        import anthropic
        client = anthropic.Anthropic(api_key=api_key)
        r = client.messages.create(
            model=model,
            max_tokens=2048,
            system=system,
            messages=mensajes,
        )
        return r.content[0].text

    # Todos los demás backends usan la API compatible con OpenAI
    from openai import OpenAI

    cfg = BACKENDS[BACKEND_NAME]
    base_url = (
        _env(cfg.get("base_url_env", ""))
        or cfg.get("base_url", "")
        or None
    )
    key = api_key or cfg.get("api_key", "none")
    client = OpenAI(api_key=key, base_url=base_url)

    full_messages = [{"role": "system", "content": system}] + mensajes
    r = client.chat.completions.create(
        model=model,
        messages=full_messages,
        max_tokens=2048,
    )
    return r.choices[0].message.content

# ── Lógica de respuesta ───────────────────────────────────────────────────────
def responder(
    mensaje: str,
    historial: list,
    api_key: str,
    model: str,
) -> tuple[list, str, str]:
    key = api_key.strip() or _env(CFG["key_env"])
    if not key and BACKEND_NAME != "ollama":
        aviso = f"⚠️ Falta la API key para {CFG['label']}. Ingrésala en el panel izquierdo o en el archivo .env."
        return (
            historial + [{"role": "user", "content": mensaje}, {"role": "assistant", "content": aviso}],
            "",
            "",
        )

    contexto, docs_usados = _seleccionar_docs(mensaje)
    system = SYSTEM_BASE.format(contexto=contexto)
    msgs = [{"role": m["role"], "content": m["content"]} for m in historial]
    msgs.append({"role": "user", "content": mensaje})

    try:
        texto = _llamar_llm(msgs, system, key, model)
    except Exception as exc:
        texto = f"❌ Error al conectar con {CFG['label']}: {exc}"

    info = "📄 " + " · ".join(docs_usados)
    nuevo_historial = historial + [
        {"role": "user",      "content": mensaje},
        {"role": "assistant", "content": texto},
    ]
    return nuevo_historial, "", info

# ── Interfaz Gradio ───────────────────────────────────────────────────────────
DEFAULT_MODEL = _env(CFG["model_env"]) or CFG["default_model"]
DEFAULT_KEY   = _env(CFG["key_env"])

EJEMPLOS = [
    "¿Cuáles son las 4 rutas de progresión del Rover?",
    "¿Qué es el Proyecto Personal de Vida (PPV)?",
    "¿Cómo se obtiene la insignia Punta de Flecha?",
    "¿Qué es la Tribu de la Tierra?",
    "¿Cómo funciona Plastic Tide Turners?",
    "¿Cuáles son los valores del Método Scout?",
    "¿Qué es el CIM y cómo se accede?",
    "¿Cuáles son las responsabilidades del Scouter de Tropa?",
    "¿Qué es el Reconocimiento Scouts del Mundo (RSDM)?",
    "¿Cómo se organiza una Provincia Scout?",
]

lista_docs = "\n".join(f"- {d}" for d in sorted(DOCS))

with gr.Blocks(title="Chat Scouts · ASMAC") as demo:
    gr.Markdown(
        f"# 🏕️ Chat · Documentos ASMAC\n"
        f"**Backend activo:** {CFG['label']} &nbsp;|&nbsp; "
        f"**Documentos cargados:** {len(DOCS)} &nbsp;|&nbsp; "
        f"**Docs por consulta:** {TOP_K}"
    )

    api_key_input = gr.State(DEFAULT_KEY)
    model_input   = gr.State(DEFAULT_MODEL)

    with gr.Row():
        # ── Panel lateral ─────────────────────────────────────────────────────
        with gr.Column(scale=1, min_width=270):
            gr.Markdown(
                f"### 📄 Documentos disponibles ({len(DOCS)})\n"
                f"*Se seleccionan {TOP_K} por consulta según relevancia*"
            )
            gr.Markdown(lista_docs)

        # ── Panel de chat ─────────────────────────────────────────────────────
        with gr.Column(scale=3):
            chatbot = gr.Chatbot(
                height=460,
                show_label=False,
                avatar_images=(None, str(BASE_DIR / "popeye.jpeg")),
            )
            info_box = gr.Textbox(
                label="Documentos consultados en la última respuesta",
                interactive=False,
                lines=1,
            )
            entrada = gr.Textbox(
                placeholder="Escribe tu pregunta sobre los documentos ASMAC...",
                lines=2,
                label="Pregunta",
            )
            with gr.Row():
                btn_enviar  = gr.Button("Enviar",  variant="primary")
                btn_limpiar = gr.Button("Limpiar", variant="secondary")

            gr.Markdown("**💡 Ejemplos de preguntas:**")
            with gr.Row():
                for ej in EJEMPLOS:
                    gr.Button(ej, size="sm").click(fn=lambda e=ej: e, outputs=entrada)

    # ── Eventos ───────────────────────────────────────────────────────────────
    def chat(mensaje, historial, api_key, model):
        if not mensaje.strip():
            return historial, "", ""
        return responder(mensaje, historial, api_key, model)

    btn_enviar.click(
        chat,
        inputs=[entrada, chatbot, api_key_input, model_input],
        outputs=[chatbot, entrada, info_box],
    )
    entrada.submit(
        chat,
        inputs=[entrada, chatbot, api_key_input, model_input],
        outputs=[chatbot, entrada, info_box],
    )
    btn_limpiar.click(lambda: ([], "", ""), outputs=[chatbot, entrada, info_box])


if __name__ == "__main__":
    print(f"Backend : {CFG['label']}")
    print(f"Modelo  : {DEFAULT_MODEL}")
    print(f"Docs    : {len(DOCS)} archivos en {DOCS_DIR}")
    for d in sorted(DOCS):
        print(f"  · {d}")
    demo.launch(inbrowser=True, theme=gr.themes.Soft())
