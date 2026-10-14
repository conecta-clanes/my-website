# ✏️ Proceso de Selección de Proyectos y Actividades — Ciclo PER

## Introducción

Ésta propuesta no sustituyen la documentación oficial, no nos hacemos responsables del mal uso.

## Tecnologías usadas

- [Claude Code](https://claude.com/product/claude-code) 

## Diagrama Selección de Proyectos en el Cliclo de Programa del Clan

```mermaid
flowchart TD
    INICIO(["🌟 Inicio del ciclo"])

    %% ─── PLANEAR ───────────────────────────────────────────
    subgraph PLANEAR ["📋 PLANEAR"]
        P1["1️⃣ Inspirarse<BR>Identificar necesidades<BR>de la comunidad"]
        P2["2️⃣ Explorar<BR>Investigar soluciones<BR>existentes e innovadoras"]
        P3{"¿Qué alcance<BR>tiene la idea?"}
        P4A["🗂️ PROYECTO<BR>Largo plazo<BR>Varias semanas / meses<BR>Múltiples actividades"]
        P4B["📌 ACTIVIDAD<BR>Corta duración<BR>Evento único o puntual"]
        P5["3️⃣ Definir actividades CENTRALES<BR>(obligatorias, dan identidad al proyecto)"]
        P6["4️⃣ Agregar actividades CONEXAS<BR>(enriquecen y amplían el alcance)"]
        P7["5️⃣ Evaluar viabilidad<BR>• Participantes y roles<BR>• Lugar y duración<BR>• Recursos y presupuesto"]
        P8["6️⃣ Definir objetivos INTELIGENTES<BR>Específico · Medible · Asignable<BR>Realista · Con plazo definido"]
        P9["7️⃣ Elaborar Plan de Acción<BR>• Cronograma<BR>• Plan de presupuesto<BR>• Plan de recursos<BR>• Plan de monitoreo"]

        P1 --> P2 --> P3
        P3 -->|"Largo plazo<BR>alta complejidad"| P4A
        P3 -->|"Corto plazo<BR>baja complejidad"| P4B
        P4A --> P5 --> P6 --> P7
        P4B --> P7
        P7 --> P8 --> P9
    end

    %% ─── EJECUTAR ───────────────────────────────────────────
    subgraph EJECUTAR ["🚀 EJECUTAR"]
        E1["Inicio<BR>Verificar que recursos<BR>estén listos para cada fase"]
        E2["Ejecución<BR>• Llevar a cabo las acciones acordadas<BR>• Tomar fotos, videos y testimonios<BR>• Registrar asistencia y horas de servicio"]
        E3["Monitoreo continuo<BR>• Seguimiento de tiempo y presupuesto<BR>• Documentar estadísticas y avances<BR>• Ajustar el plan si es necesario"]
        E4["Cierre de la actividad<BR>Reconocer los esfuerzos<BR>de todos los involucrados"]

        E1 --> E2 --> E3 --> E4
    end

    %% ─── REVISAR ────────────────────────────────────────────
    subgraph REVISAR ["🔍 REVISAR"]
        R1["Evaluar<BR>• Comparar resultados vs objetivos<BR>• Medir el impacto logrado<BR>• Evaluar planes y presupuesto"]
        R2["Registrar<BR>• Anotar lecciones aprendidas<BR>• Documentar lo que funcionó<BR>y lo que debe mejorar"]
        R3["Reportar y Compartir<BR>• Elaborar reporte final<BR>• Presentar resultados a la comunidad<BR>• Compartir en la Red Scout"]

        R1 --> R2 --> R3
    end

    %% ─── FLUJO PRINCIPAL ────────────────────────────────────
    INICIO --> PLANEAR
    PLANEAR --> EJECUTAR
    EJECUTAR --> REVISAR
    REVISAR -->|"♻️ Mejora continua<BR>nuevo ciclo"| PLANEAR
```


##### Autora

    - Yolanda Castillo