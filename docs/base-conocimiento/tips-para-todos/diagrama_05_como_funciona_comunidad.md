# ✏️ Diagrama 5: Cómo Funciona la Comunidad

## Introducción

Ésta propuesta no sustituyen la documentación oficial, no nos hacemos responsables del mal uso.

## Tecnologías usadas

- [Claude Code](https://claude.com/product/claude-code) 

## Diagrama Cómo funciona la Comunidad de Caminantes

```mermaid
flowchart TD
    COM(["🏔️ COMUNIDAD DE CAMINANTES · 14 a 18 años<BR>Lema: Siempre Adelante"])

    subgraph ADU["ADULTOS — Scouters (rol de acompañamiento)"]
        direction TB
        JEF["Jefe de Sección"]
        SUBJ["Subjefe de Sección"]
        APO["Scouters de Apoyo · No directivos"]
        JEF --- SUBJ --- APO
    end

    subgraph EQU["JÓVENES — Equipos"]
        direction TB
        COORD["Coordinador/a de Equipo · Líder"]
        SUBCO["Subcoordinador/a"]
        LPROY["Líder de Proyecto · rol rotativo por proyecto"]
        INT["Demás integrantes del Equipo"]
        COORD --> SUBCO --> LPROY --> INT
    end

    subgraph GOB["ÓRGANOS DE GOBIERNO · Sistema democrático"]
        direction TB
        CE["Consejo de Equipo<BR>Miembros del Equipo<BR>Decisiones internas del Equipo"]
        CC["Comité de Comunidad<BR>Representantes + Scouters<BR>Coordinación cotidiana · órgano ejecutivo"]
        CON["Congreso de Comunidad<BR>Todos los Caminantes<BR>Decisiones estratégicas · órgano legislativo"]
        CS["Consejo de Sección<BR>Coordinadores + Scouters<BR>Seguimiento general"]
        ES["Equipo de Scouters<BR>Solo adultos · Planificación pedagógica"]
        CE --> CC
        CC --> CON
        CON --- CS
        CS --- ES
    end

    subgraph SIM["MARCO SIMBÓLICO — La propia aventura"]
        direction TB
        CONC["Concepto central:<BR>El desafío de vivir mi propia aventura"]
        PROM["Promesa Scout · Ley Scout · 10 artículos"]
        ORA["Oración del Caminante · reflexión profunda"]
        CONC --> PROM --> ORA
    end

    subgraph MET["METODOLOGÍA"]
        direction TB
        CIC["Ciclo de Programa · 3–4 meses"]
        HOJ["Hoja de Caminata<BR>herramienta central de planificación<BR>y seguimiento personal"]
        PER["PER: Planear → Ejecutar → Revisar"]
        SMART["SMART: Específico · Medible · Alcanzable · Realista · Tiempo"]
        PROY["Proyectos de Equipo<BR>metodología por proyectos"]
        CIC --> HOJ --> PER --> SMART --> PROY
    end

    COM --> ADU
    COM --> EQU
    ADU --> GOB
    EQU --> GOB
    COM --> SIM
    COM --> MET
```

##### Autora

    - Yolanda Castillo