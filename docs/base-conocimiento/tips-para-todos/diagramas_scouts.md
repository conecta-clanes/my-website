# ✏️ Diagramas Scout en Mermaid

---

## Introducción

Ésta propuesta no sustituyen la documentación oficial, no nos hacemos responsables del mal uso.

## Tecnologías usadas

- [Claude Code](https://claude.com/product/claude-code) 

## Diagrama 1: Cómo Funciona la Manada

```mermaid
flowchart TD
    MANADA(["🐺 MANADA DE LOBATOS · 6 a 10 años<BR>Lema: Haremos lo mejor"])

    subgraph ADU["ADULTOS — Viejos Lobos"]
        direction TB
        AKELA["Akela<BR>Jefe de Sección · mín. 20 años"]
        SUB["Subjefe de Sección · mín. 18 años"]
        APO["Scouters de Apoyo"]
        AKELA --- SUB --- APO
    end

    subgraph SEI["JÓVENES — Seisenas (máx. 6 grupos · 36 miembros)"]
        direction TB
        SEIS["Seisenero/a · Líder de grupo"]
        SUBSEIS["Subseisenero/a"]
        INT["4 Integrantes"]
        COL["Colores: Amarilla · Blanca · Café · Gris · Negra · Roja"]
        SEIS --> SUBSEIS --> INT
        INT --- COL
    end

    subgraph GOB["ÓRGANOS DE GOBIERNO"]
        direction LR
        CR["Consejo de Roca<BR>Seiseneros + Viejos Lobos<BR>Decisiones del programa y evaluación"]
        ES["Equipo de Scouters<BR>Solo adultos<BR>Planificación pedagógica"]
    end

    subgraph SIM["MARCO SIMBÓLICO — La Selva del Seeonee"]
        direction TB
        KIP["Fuente: El Libro de las Tierras Vírgenes · Rudyard Kipling"]
        PERS["Roles adultos: Akela · Baloo · Bagheera · Raksha · Hermano Gris"]
        LEY["Ley de la Manada · 2 artículos<BR>Máximas de la Manada · Gran Aullido"]
        KIP --> PERS --> LEY
    end

    subgraph MET["METODOLOGÍA"]
        direction TB
        CAC["Ciclo: Gran Cacería · 3–4 meses"]
        PER["PER: Planear → Ejecutar → Revisar"]
        DUR["Actividades DURASIL<BR>Desafiantes · Útiles · Recompensantes<BR>Atractivas · Seguras · Inclusivas · Lúdicas"]
        LIB["Libro de Rastros · registro personal de progresión"]
        CAC --> PER --> DUR --> LIB
    end

    MANADA --> ADU
    MANADA --> SEI
    ADU --> GOB
    SEI --> GOB
    MANADA --> SIM
    MANADA --> MET
```

---

## Diagrama 2: Progresión en la Manada

```mermaid
flowchart TD
    INI(["🐾 MI PRIMER RASTRO<BR>Insignia de entrada a la Manada"])

    subgraph PLANOS["4 PLANOS DE RELACIÓN<BR>(cada Cazadero trabaja los 4 planos)"]
        PL1["Consigo Mismo"]
        PL2["Con los Demás"]
        PL3["Con el Entorno"]
        PL4["Con lo Trascendente"]
    end

    subgraph CAZ["4 CAZADEROS · Elección libre · No secuencial"]
        direction LR
        CUBIL["🏠 Cubil<BR>Guardián: Raksha<BR>Salud y Bienestar"]
        COLI["⛰️ Colinas del Seeonee<BR>Guardián: Baloo<BR>Habilidades para la Vida"]
        PANT["🌿 Pantanos del Norte<BR>Guardián: Bagheera<BR>Medio Ambiente"]
        DEKK["🌍 Dekkan<BR>Guardián: Hermano Gris<BR>Paz y Participación Comunitaria"]
    end

    subgraph PROCESO["PROCESO DENTRO DE CADA CAZADERO"]
        direction LR
        PRESA["Presa<BR>Competencia a lograr<BR>(11 Presas en total)"]
        DENT["Dentellada<BR>Habilidad específica<BR>dentro de la Presa"]
        RAST["Rastro<BR>Actividad concreta<BR>que deja huella de aprendizaje"]
        PRESA --> DENT --> RAST
    end

    subgraph EVAL["EVALUACIÓN"]
        direction LR
        E1["Autoevaluación<BR>del lobato"]
        E2["Coevaluación<BR>entre pares"]
        E3["Observación<BR>del Scouter"]
    end

    subgraph ESP["ESPECIALIDADES · 8 grupos temáticos<BR>Proceso: Conozco → Aplico → Comparto"]
        direction LR
        G1["Rikki-Tikki-Tavi · Mao/Mor<BR>Mysa · Jacala"]
        G2["Kotick · Mang<BR>Pukeena · Darzee"]
    end

    subgraph FIN["INSIGNIAS FINALES"]
        direction LR
        OBS["⬟ Alfa Obsidiana<BR>Primer nivel de culminación"]
        JAD["💎 Alfa Jade<BR>Nivel superior de culminación"]
        OBS --> JAD
    end

    INI --> PLANOS
    PLANOS --> CAZ
    CAZ --> PROCESO
    PROCESO --> EVAL
    EVAL --> ESP
    EVAL --> FIN
```

---

## Diagrama 3: Cómo Funciona la Tropa

```mermaid
flowchart TD
    TROPA(["⚜️ TROPA DE SCOUTS · 10 a 14 años<BR>Lema: Siempre Listos"])

    subgraph ADU["ADULTOS — Scouters"]
        direction TB
        JEF["Jefe de Sección"]
        SUBJ["Subjefe de Sección"]
        APO["Scouters de Apoyo"]
        JEF --- SUBJ --- APO
    end

    subgraph PAT["JÓVENES — Patrullas (máx. 4 grupos · 32 miembros)"]
        direction TB
        GUIA["Guía de Patrulla · Líder"]
        SUBG["Subguía de Patrulla"]
        MIEMB["2–6 Integrantes"]
        ROLES["Roles rotativos: Tesorero · Secretario<BR>Cronista · Botiquinero · Cocinero"]
        GUIA --> SUBG --> MIEMB
        MIEMB --- ROLES
    end

    subgraph GOB["ÓRGANOS DE GOBIERNO"]
        direction TB
        CP["Consejo de Patrulla<BR>Guía + Subguía + miembros<BR>Decisiones internas de la Patrulla"]
        AT["Asamblea de Tropa<BR>Todos los scouts + Scouters<BR>Decisiones generales"]
        CH["Corte de Honor<BR>Guías + Subguías + Jefe + Subjefe<BR>Evaluación de progresión"]
        ES["Equipo de Scouters<BR>Solo adultos · Planificación pedagógica"]
        CP --> AT
        AT --- CH
        CH --- ES
    end

    subgraph SIM["MARCO SIMBÓLICO — Tradición Scout B-P"]
        direction TB
        PROM["Promesa Scout · Honor personal"]
        LEY10["Ley Scout · 10 artículos<BR>Confianza · Lealtad · Servicio<BR>Amistad · Amabilidad · Obediencia<BR>Alegría · Frugalidad · Valentía · Pureza"]
        GRITO["Grito de Patrulla · identidad del grupo"]
        PROM --> LEY10 --> GRITO
    end

    subgraph MET["METODOLOGÍA"]
        direction TB
        EXP["Ciclo: Gran Exploración · 3–4 meses"]
        PER["PER: Planear → Ejecutar → Revisar"]
        TEC["Técnicas Scout<BR>Orientación · Campismo · Primeros Auxilios<BR>Nudos · Señalamiento"]
        NAT["Aventuras en la Naturaleza<BR>Salidas · Campamentos · Excursiones"]
        EXP --> PER --> TEC --> NAT
    end

    TROPA --> ADU
    TROPA --> PAT
    ADU --> GOB
    PAT --> GOB
    TROPA --> SIM
    TROPA --> MET
```

---

## Diagrama 4: Progresión en la Tropa

```mermaid
flowchart TD
    INI(["⚜️ INGRESO A LA TROPA<BR>Actividades de bienvenida y orientación"])

    subgraph SENDAS["4 SENDAS (Planos de Relación)<BR>(cada Rumbo trabaja las 4 Sendas)"]
        direction LR
        S1["Senda<BR>Consigo Mismo"]
        S2["Senda<BR>Con los Demás"]
        S3["Senda<BR>Con el Entorno"]
        S4["Senda<BR>Con lo Trascendente"]
    end

    subgraph RUM["4 RUMBOS · Elección libre · No secuencial"]
        direction LR
        TORT["🐢 Tortuga<BR>Bienestar · Consigo Mismo<BR>Iniciativa: Águila Solitaria"]
        OCEL["🐆 Ocelote<BR>Medio Ambiente · Entorno<BR>Iniciativa: Jaguar"]
        QUET["🦜 Quetzal<BR>Paz · Introspección<BR>Iniciativa: Mapache de Cozumel"]
        VEN["🦌 Venado<BR>Liderazgo · Con los Demás<BR>Iniciativa: Ajolote de Xochimilco"]
    end

    subgraph PROCESO["PROCESO DENTRO DE CADA RUMBO"]
        direction LR
        EXPLO["Exploración<BR>Competencia a lograr<BR>(12 Exploraciones en total)"]
        ESC["Escenario de Aprendizaje<BR>Actividad contextualizada<BR>concreta"]
        EXPLO --> ESC
    end

    subgraph EVAL["EVALUACIÓN"]
        direction LR
        E1["Autoevaluación<BR>del scout"]
        E2["Coevaluación<BR>entre pares de Patrulla"]
        E3["Observación<BR>del Scouter"]
        E4["Validación en<BR>Corte de Honor"]
        E1 --- E2 --- E3 --> E4
    end

    subgraph IMUND["INICIATIVAS MUNDIALES SCOUT"]
        direction LR
        IM1["Tribu de la Tierra"]
        IM2["Champions for Nature"]
        IM3["Scouts Go Solar"]
        IM4["Plastic Tide Turners"]
        IM5["Mensajeros de la Paz"]
    end

    subgraph ESP["ESPECIALIDADES · 8 campos del conocimiento<BR>Proceso: Conozco → Aplico → Comparto"]
        direction LR
        EC["8 grupos temáticos<BR>adaptados a 10–14 años"]
    end

    subgraph FIN["INSIGNIAS FINALES DE TROPA"]
        IF["Insignias de culminación<BR>de Tropa Scout"]
    end

    INI --> SENDAS
    SENDAS --> RUM
    RUM --> PROCESO
    PROCESO --> EVAL
    EVAL --> ESP
    EVAL --> IMUND
    ESP --> FIN
```

---

## Diagrama 5: Cómo Funciona la Comunidad

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

---

## Diagrama 6: Progresión en la Comunidad

```mermaid
flowchart TD
    INI(["🏔️ INGRESO A LA COMUNIDAD<BR>Encuentro de orientación · Promesa de Equipo"])

    subgraph CAMINOS["4 CAMINOS (Planos de Relación)<BR>(cada Sendero trabaja los 4 Caminos)"]
        direction LR
        C1["Camino<BR>Consigo Mismo"]
        C2["Camino<BR>Con los Demás"]
        C3["Camino<BR>Con el Entorno"]
        C4["Camino<BR>Con lo Trascendente"]
    end

    subgraph SEN["4 SENDEROS · Elección libre · No secuencial"]
        direction LR
        CEN["☀️ Cenit<BR>Salud y Bienestar"]
        CIM["🌲 Cima<BR>Medio Ambiente y Sustentabilidad"]
        CUM["🕊️ Cumbre<BR>Paz y Participación Comunitaria"]
        CUS["🛠️ Cúspide<BR>Habilidades para la Vida"]
    end

    subgraph PROCESO["PROCESO DENTRO DE CADA SENDERO"]
        direction LR
        DES["Desafío<BR>Competencia a lograr<BR>(11 Desafíos en total)"]
        ESC["Escenario de Aprendizaje<BR>Actividad concreta de aprendizaje"]
        PROY["Proyecto de Equipo<BR>aplicación comunitaria del Desafío"]
        DES --> ESC --> PROY
    end

    subgraph EVAL["EVALUACIÓN"]
        direction TB
        E1["Autoevaluación<BR>del Caminante<BR>protagonismo en su proceso"]
        E2["Coevaluación<BR>entre pares de Equipo"]
        E3["Observación<BR>del Scouter<BR>(acompañamiento)"]
        REG["Registro en<BR>Hoja de Caminata"]
        VAL["Validación en<BR>Consejo de Equipo<BR>Consejo de Sección"]
        E1 --- E2 --- E3 --> REG --> VAL
    end

    subgraph ESP["ESPECIALIDADES · 8 campos del conocimiento<BR>Proceso: Conozco → Aplico → Comparto"]
        EC["8 grupos temáticos<BR>adaptados a 14–18 años"]
    end

    subgraph FIN["INSIGNIAS FINALES"]
        direction LR
        OBS["⬟ Obsidiana<BR>Primer nivel de culminación"]
        JAD["💎 Jade<BR>Nivel superior de culminación"]
        OBS --> JAD
    end

    INI --> CAMINOS
    CAMINOS --> SEN
    SEN --> PROCESO
    PROCESO --> EVAL
    EVAL --> ESP
    ESP --> FIN
```

##### Autora

    - Yolanda Castillo
