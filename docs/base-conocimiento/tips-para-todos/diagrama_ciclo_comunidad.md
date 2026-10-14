# Ciclo de Programa — PER (Comunidad)

## Introducción

Ésta propuesta no sustituyen la documentación oficial, no nos hacemos responsables del mal uso.

## Tecnologías usadas

- [Claude Code](https://claude.com/product/claude-code) 

## Diagrama Ciclo de Programa en la Comunidad de Caminantes

```mermaid
flowchart TD
    TITLE(["🏔️ CICLO DE PROGRAMA · PER<BR>Comunidad de Caminantes · 14–18 años<BR>Duración: 3 a 4 meses · 3 o 4 ciclos por año"])

    ENFA["📌 ÉNFASIS DEL CICLO<BR>Comité de Comunidad define la prioridad temática<BR>Equipos proponen actividades en respuesta al énfasis<BR>Congreso elige mediante juego democrático y aprueba calendario"]

    subgraph PLAN["🗺️ PLANEAR"]
        P1["Conoce y reflexiona sobre<BR>Planos de Relación y Ejes Temáticos<BR>(Senderos: Cenit · Cima · Cumbre · Cúspide)"]
        P2["Elige las competencias<BR>que quiere desarrollar"]
        P3["Establece metas personales<BR>con metodología SMART"]
        P4["Elabora cronograma de actividades<BR>y proyectos dentro y fuera del Movimiento"]
        P5["Comparte su plan<BR>en el Congreso de Comunidad"]
        P1 --> P2 --> P3 --> P4 --> P5
    end

    subgraph EJEC["⚡ EJECUTAR"]
        E1["Realiza actividades de<BR>su Hoja de Caminata"]
        E2["Desarrolla Proyectos de Equipo<BR>dentro y fuera del Movimiento"]
        E3["Revisa y evalúa<BR>el avance de sus acciones"]
        E1 --> E2 --> E3
    end

    subgraph REVI["🔍 REVISAR"]
        R1["Autoevaluación de acciones desarrolladas"]
        R2["Evaluación acompañada por Scouter,<BR>amigos y familia"]
        R3["Registra el avance en<BR>su Hoja de Caminata"]
        R4["Presenta el progreso<BR>ante el Congreso de Comunidad"]
        R1 --> R2 --> R3 --> R4
    end

    subgraph GOB["ÓRGANOS DE GOBIERNO"]
        direction LR
        CC["Comité de Comunidad<BR>Representantes + Scouters<BR>Define énfasis · Órgano ejecutivo"]
        CON["Congreso de Comunidad<BR>Todos los Caminantes<BR>Aprueba actividades y calendario<BR>Recibe reportes de progresión · Órgano legislativo"]
        ES["Equipo de Scouters<BR>Orientación educativa<BR>Acompañamiento no directivo"]
        CC --- CON
        CON --- ES
    end

    subgraph HERR["HERRAMIENTAS"]
        H1["Hoja de Caminata<BR>Herramienta central de planificación<BR>y seguimiento personal"]
        H2["Objetivos SMART<BR>Específico · Medible · Alcanzable · Realista · Tiempo"]
        H3["Preguntas Orientadoras<BR>Inicio · Desarrollo · Cierre"]
        H4["Escenarios de Aprendizaje<BR>Dentro y fuera del Movimiento"]
    end

    TITLE --> ENFA
    ENFA --> PLAN
    PLAN --> EJEC
    EJEC --> REVI
    REVI -->|"Nuevo Ciclo de Programa"| ENFA

    GOB -.-> ENFA
    GOB -.-> PLAN
    GOB -.-> REVI
    HERR -.-> PLAN
    HERR -.-> EJEC
    HERR -.-> REVI
```

##### Autora

    - Yolanda Castillo
