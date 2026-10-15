# ✏️ Ciclo de Programa — La Gran Exploración (Tropa)

## Introducción

Ésta propuesta no sustituyen la documentación oficial, no nos hacemos responsables del mal uso.

## Tecnologías usadas

- [Claude Code](https://claude.com/product/claude-code) 

## Diagrama Ciclo de Programa en Tropa

```mermaid
flowchart TD
    TITLE(["⚜️ LA GRAN EXPLORACIÓN<BR>Ciclo de Programa · Tropa de Scouts · 10–14 años<BR>Duración: 3 a 4 meses · 3 o 4 ciclos por año · hasta 16 ciclos en la sección"])

    F1["📋 FASE 1<BR>DIAGNÓSTICO<BR>Evaluaciones personales o de Sección<BR>Define el énfasis del Ciclo de Programa"]

    F2["💡 FASE 2<BR>PROPUESTA Y SELECCIÓN DE ACTIVIDADES<BR>Consejo de Patrulla propone<BR>Asamblea de Tropa elige mediante juego democrático"]

    F3["🗓️ FASE 3<BR>ORGANIZACIÓN, DISEÑO Y PREPARACIÓN<BR>Calendario de actividades<BR>Asamblea de Tropa aprueba el calendario"]

    F4["🏃 FASE 4<BR>DESARROLLO Y EVALUACIÓN<BR>Fase de mayor duración del ciclo<BR>Evaluación por observación continua<BR>Seguimiento de la Progresión Personal"]

    subgraph GOB["ÓRGANOS DE GOBIERNO"]
        direction TB
        CP["Consejo de Patrulla<BR>Todos los miembros de la Patrulla<BR>Propone actividades para la Gran Exploración<BR>Define objetivos · Administra recursos"]
        AT["Asamblea de Tropa<BR>Todos los scouts + Scouters<BR>Espacio democrático · Elige actividades<BR>Aprueba calendario del ciclo"]
        CH["Corte de Honor<BR>Guías + Subguías + Jefe + Subjefe<BR>Define énfasis del ciclo<BR>Calendariza · Evalúa progresión"]
        CP -->|"lleva propuestas a"| AT
        AT -->|"informa a"| CH
    end

    subgraph HERR["HERRAMIENTAS DEL CICLO"]
        H1["Malla de Competencias<BR>Exploraciones · Escenarios de Aprendizaje"]
        H2["Preguntas Orientadoras<BR>Inicio · Desarrollo · Cierre"]
        H3["Libro de Patrulla<BR>Registro de acuerdos del Consejo de Patrulla"]
        H4["Evaluación por observación<BR>Continua durante la Fase 4"]
    end

    TITLE --> F1
    F1 -->|"Corte de Honor define énfasis"| F2
    F2 -->|"Actividades elegidas en Asamblea"| F3
    F3 -->|"Calendario aprobado"| F4
    F4 -->|"Nueva Gran Exploración"| F1

    GOB -.-> F1
    GOB -.-> F2
    GOB -.-> F3
    HERR -.-> F3
    HERR -.-> F4
```

##### Autora

    - Yolanda Castillo