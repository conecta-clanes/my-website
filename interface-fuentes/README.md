# Chat · Documentos ASMAC

Chatbot de consulta sobre los documentos oficiales de la **Asociación de Scouts de México (ASMAC)**. Responde preguntas en español basándose exclusivamente en los manuales, guías y políticas cargados desde la carpeta `md/` (37 documentos).

## Características

- Interfaz web con **Gradio** (se abre automáticamente en el navegador)
- Soporte para múltiples backends de LLM: Claude, OpenAI, Gemini, Kimi, GLM y Ollama (local)
- Selección automática de los `TOP_K` documentos más relevantes por consulta (puntuación por frecuencia de tokens)
- Avatar hablante con lip-sync vía **D-ID** y voz `es-MX-DaliaNeural` (opcional)
- Configuración 100 % por variables de entorno o archivo `.env`

## Requisitos

- Python 3.11+

```bash
pip install gradio anthropic openai requests
```

> Para Gemini, Kimi o GLM solo se necesita `openai` (APIs compatibles con OpenAI).  
> Para Ollama basta tener el servidor corriendo localmente — no necesita API key.

## Instalación y uso

```bash
# 1. Copiar la plantilla de configuración
cp .env.example .env

# 2. Editar .env con la API key del backend deseado
# 3. Ejecutar
python chat_scouts.py
```

Al arrancar imprime un resumen en consola y abre la interfaz en el navegador:

```
Backend : ChatGPT (OpenAI)
Modelo  : gpt-4o-mini
Docs    : 37 archivos en md/
```

## Configuración

### Variables de entorno

| Variable | Descripción | Default |
|---|---|---|
| `LLM_BACKEND` | Backend activo: `claude` \| `openai` \| `gemini` \| `kimi` \| `glm` \| `ollama` | `claude` |
| `DOCS_TOP_K` | Documentos incluidos por consulta | `6` |

### Claude (Anthropic)

| Variable | Default |
|---|---|
| `ANTHROPIC_API_KEY` | — |
| `ANTHROPIC_MODEL` | `claude-sonnet-4-6` |

### OpenAI

| Variable | Default |
|---|---|
| `OPENAI_API_KEY` | — |
| `OPENAI_MODEL` | `gpt-4o` |
| `OPENAI_BASE_URL` | `https://api.openai.com/v1` (compatible con otros servidores) |

### Gemini (Google)

| Variable | Default |
|---|---|
| `GEMINI_API_KEY` | — |
| `GEMINI_MODEL` | `gemini-2.0-flash` |

### Kimi (Moonshot AI)

| Variable | Default |
|---|---|
| `KIMI_API_KEY` | — |
| `KIMI_MODEL` | `moonshot-v1-128k` |

### GLM (Zhipu AI)

| Variable | Default |
|---|---|
| `GLM_API_KEY` | — |
| `GLM_MODEL` | `glm-4-flash` |

### Ollama (local)

| Variable | Default |
|---|---|
| `OLLAMA_BASE_URL` | `http://localhost:11434` |
| `OLLAMA_MODEL` | `llama3.2` |

### D-ID (avatar hablante, opcional)

| Variable | Descripción |
|---|---|
| `DID_API_KEY` | `Basic <base64>` — obtenida en d-id.com → Studio → API |

Si se configura `DID_API_KEY`, cada respuesta genera un video con la imagen `popeye.jpeg` sincronizada con voz `es-MX-DaliaNeural`. Sin la key, el chat funciona igual sin video.

## Backends soportados

| Backend | Proveedor | Necesita internet |
|---|---|---|
| `claude` | Anthropic | Sí |
| `openai` | OpenAI | Sí |
| `gemini` | Google | Sí |
| `kimi` | Moonshot AI | Sí |
| `glm` | Zhipu AI | Sí |
| `ollama` | Local | No |

## Documentos incluidos (37)

Los archivos `.md` en `md/` se cargan automáticamente al iniciar.

**Manuales de operación**
- Manual de Operación Nivel Provincia
- Manual de Operación Nivel Grupo 2018
- Políticas y Procedimientos de la Comisión Nacional de Formación
- Anexo 8 · Captación y Selección de Adultos

**Guías de Scouter por rama**
- Guía de Scouter de Manada de Lobatos 2024 (6–10 años)
- Guía de Scouter de Tropa de Scouts 2024 (10–14 años)
- Guía de Scouter de Comunidad de Caminantes 2024 (14–18 años)
- Guía de Scouter de Clan de Rovers 2024 (18–21 años)

**Progresión por rama**
- Mis Rastros en la Selva 2024 (Manada)
- Pistas de la Aventura 2024 (Tropa)
- El Desafío de ser Caminante 2024 (Comunidad)
- Las Rutas del Rover (Clan)

**Guías Punta de Flecha 2025**
- Tropa de Scouts
- Comunidad de Caminantes
- Clan de Rovers

**Carnets Aventuras en la Naturaleza 2024**
- Manada · Tropa · Comunidad · Rovers

**Formación de adultos**
- Manual del Curso de Inducción al Escultismo 2019
- Manual para la Implementación de los Módulos del CIM 2019
- Modelo de Actualización Continua para Adultos
- Modelo de Gestión de Adultos 2025
- Política Nacional AMS 2024

**Insignias e iniciativas mundiales**
- Guía Insignia Mensajeros de la Paz
- Guía Insignia Reconocimiento Scouts del Mundo (RSDM)
- Guía Insignia Go Solar
- Guía Champions for Nature
- Manual Plastic Tide Turners
- Guía Tribu de la Tierra 2021

**Políticas, gobierno y referencia**
- Declaración de Principios 2023
- Código de Ética ASMAC
- Política Nacional Programa de Jóvenes 2025
- Política Nacional Niñeces, Adolescencias y Juventudes
- Reglamento ASMAC 2023
- Proyecto Educativo ASMAC (dossier)
- Proyectos y Actividades

## Estructura del proyecto

```
libros/
├── chat_scouts.py        # Aplicación principal
├── .env                  # Variables de entorno (no versionar)
├── .env.example          # Plantilla de configuración
├── popeye.jpeg           # Imagen del avatar D-ID
├── AvatarMaker.png       # Avatar alternativo
├── LICENSE
└── md/                   # 37 documentos ASMAC en Markdown
```
