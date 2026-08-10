# Diagramas Scout en Mermaid

---

## Diagrama 1: Cómo Funciona la Manada

```mermaid
flowchart TD
    MANADA(["🐺 MANADA DE LOBATOS · 6 a 10 años\nLema: Haremos lo mejor"])

    subgraph ADU["ADULTOS — Viejos Lobos"]
        direction TB
        AKELA["Akela\nJefe de Sección · mín. 20 años"]
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
        CR["Consejo de Roca\nSeiseneros + Viejos Lobos\nDecisiones del programa y evaluación"]
        ES["Equipo de Scouters\nSolo adultos\nPlanificación pedagógica"]
    end

    subgraph SIM["MARCO SIMBÓLICO — La Selva del Seeonee"]
        direction TB
        KIP["Fuente: El Libro de las Tierras Vírgenes · Rudyard Kipling"]
        PERS["Roles adultos: Akela · Baloo · Bagheera · Raksha · Hermano Gris"]
        LEY["Ley de la Manada · 2 artículos\nMáximas de la Manada · Gran Aullido"]
        KIP --> PERS --> LEY
    end

    subgraph MET["METODOLOGÍA"]
        direction TB
        CAC["Ciclo: Gran Cacería · 3–4 meses"]
        PER["PER: Planear → Ejecutar → Revisar"]
        DUR["Actividades DURASIL\nDesafiantes · Útiles · Recompensantes\nAtractivas · Seguras · Inclusivas · Lúdicas"]
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
    INI(["🐾 MI PRIMER RASTRO\nInsignia de entrada a la Manada"])

    subgraph PLANOS["4 PLANOS DE RELACIÓN\n(cada Cazadero trabaja los 4 planos)"]
        PL1["Consigo Mismo"]
        PL2["Con los Demás"]
        PL3["Con el Entorno"]
        PL4["Con lo Trascendente"]
    end

    subgraph CAZ["4 CAZADEROS · Elección libre · No secuencial"]
        direction LR
        CUBIL["🏠 Cubil\nGuardián: Raksha\nSalud y Bienestar"]
        COLI["⛰️ Colinas del Seeonee\nGuardián: Baloo\nHabilidades para la Vida"]
        PANT["🌿 Pantanos del Norte\nGuardián: Bagheera\nMedio Ambiente"]
        DEKK["🌍 Dekkan\nGuardián: Hermano Gris\nPaz y Participación Comunitaria"]
    end

    subgraph PROCESO["PROCESO DENTRO DE CADA CAZADERO"]
        direction LR
        PRESA["Presa\nCompetencia a lograr\n(11 Presas en total)"]
        DENT["Dentellada\nHabilidad específica\ndentro de la Presa"]
        RAST["Rastro\nActividad concreta\nque deja huella de aprendizaje"]
        PRESA --> DENT --> RAST
    end

    subgraph EVAL["EVALUACIÓN"]
        direction LR
        E1["Autoevaluación\ndel lobato"]
        E2["Coevaluación\nentre pares"]
        E3["Observación\ndel Scouter"]
    end

    subgraph ESP["ESPECIALIDADES · 8 grupos temáticos\nProceso: Conozco → Aplico → Comparto"]
        direction LR
        G1["Rikki-Tikki-Tavi · Mao/Mor\nMysa · Jacala"]
        G2["Kotick · Mang\nPukeena · Darzee"]
    end

    subgraph FIN["INSIGNIAS FINALES"]
        direction LR
        OBS["⬟ Alfa Obsidiana\nPrimer nivel de culminación"]
        JAD["💎 Alfa Jade\nNivel superior de culminación"]
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
    TROPA(["⚜️ TROPA DE SCOUTS · 10 a 14 años\nLema: Siempre Listos"])

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
        ROLES["Roles rotativos: Tesorero · Secretario\nCronista · Botiquinero · Cocinero"]
        GUIA --> SUBG --> MIEMB
        MIEMB --- ROLES
    end

    subgraph GOB["ÓRGANOS DE GOBIERNO"]
        direction TB
        CP["Consejo de Patrulla\nGuía + Subguía + miembros\nDecisiones internas de la Patrulla"]
        AT["Asamblea de Tropa\nTodos los scouts + Scouters\nDecisiones generales"]
        CH["Corte de Honor\nGuías + Subguías + Jefe + Subjefe\nEvaluación de progresión"]
        ES["Equipo de Scouters\nSolo adultos · Planificación pedagógica"]
        CP --> AT
        AT --- CH
        CH --- ES
    end

    subgraph SIM["MARCO SIMBÓLICO — Tradición Scout B-P"]
        direction TB
        PROM["Promesa Scout · Honor personal"]
        LEY10["Ley Scout · 10 artículos\nConfianza · Lealtad · Servicio\nAmistad · Amabilidad · Obediencia\nAlegría · Frugalidad · Valentía · Pureza"]
        GRITO["Grito de Patrulla · identidad del grupo"]
        PROM --> LEY10 --> GRITO
    end

    subgraph MET["METODOLOGÍA"]
        direction TB
        EXP["Ciclo: Gran Exploración · 3–4 meses"]
        PER["PER: Planear → Ejecutar → Revisar"]
        TEC["Técnicas Scout\nOrientación · Campismo · Primeros Auxilios\nNudos · Señalamiento"]
        NAT["Aventuras en la Naturaleza\nSalidas · Campamentos · Excursiones"]
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
    INI(["⚜️ INGRESO A LA TROPA\nActividades de bienvenida y orientación"])

    subgraph SENDAS["4 SENDAS (Planos de Relación)\n(cada Rumbo trabaja las 4 Sendas)"]
        direction LR
        S1["Senda\nConsigo Mismo"]
        S2["Senda\nCon los Demás"]
        S3["Senda\nCon el Entorno"]
        S4["Senda\nCon lo Trascendente"]
    end

    subgraph RUM["4 RUMBOS · Elección libre · No secuencial"]
        direction LR
        TORT["🐢 Tortuga\nBienestar · Consigo Mismo\nIniciativa: Águila Solitaria"]
        OCEL["🐆 Ocelote\nMedio Ambiente · Entorno\nIniciativa: Jaguar"]
        QUET["🦜 Quetzal\nPaz · Introspección\nIniciativa: Mapache de Cozumel"]
        VEN["🦌 Venado\nLiderazgo · Con los Demás\nIniciativa: Ajolote de Xochimilco"]
    end

    subgraph PROCESO["PROCESO DENTRO DE CADA RUMBO"]
        direction LR
        EXPLO["Exploración\nCompetencia a lograr\n(12 Exploraciones en total)"]
        ESC["Escenario de Aprendizaje\nActividad contextualizada\nconcreta"]
        EXPLO --> ESC
    end

    subgraph EVAL["EVALUACIÓN"]
        direction LR
        E1["Autoevaluación\ndel scout"]
        E2["Coevaluación\nentre pares de Patrulla"]
        E3["Observación\ndel Scouter"]
        E4["Validación en\nCorte de Honor"]
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

    subgraph ESP["ESPECIALIDADES · 8 campos del conocimiento\nProceso: Conozco → Aplico → Comparto"]
        direction LR
        EC["8 grupos temáticos\nadaptados a 10–14 años"]
    end

    subgraph FIN["INSIGNIAS FINALES DE TROPA"]
        IF["Insignias de culminación\nde Tropa Scout"]
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
    COM(["🏔️ COMUNIDAD DE CAMINANTES · 14 a 18 años\nLema: Siempre Adelante"])

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
        CE["Consejo de Equipo\nMiembros del Equipo\nDecisiones internas del Equipo"]
        CC["Comité de Comunidad\nRepresentantes + Scouters\nCoordinación cotidiana · órgano ejecutivo"]
        CON["Congreso de Comunidad\nTodos los Caminantes\nDecisiones estratégicas · órgano legislativo"]
        CS["Consejo de Sección\nCoordinadores + Scouters\nSeguimiento general"]
        ES["Equipo de Scouters\nSolo adultos · Planificación pedagógica"]
        CE --> CC
        CC --> CON
        CON --- CS
        CS --- ES
    end

    subgraph SIM["MARCO SIMBÓLICO — La propia aventura"]
        direction TB
        CONC["Concepto central:\nEl desafío de vivir mi propia aventura"]
        PROM["Promesa Scout · Ley Scout · 10 artículos"]
        ORA["Oración del Caminante · reflexión profunda"]
        CONC --> PROM --> ORA
    end

    subgraph MET["METODOLOGÍA"]
        direction TB
        CIC["Ciclo de Programa · 3–4 meses"]
        HOJ["Hoja de Caminata\nherramienta central de planificación\ny seguimiento personal"]
        PER["PER: Planear → Ejecutar → Revisar"]
        SMART["SMART: Específico · Medible · Alcanzable · Realista · Tiempo"]
        PROY["Proyectos de Equipo\nmetodología por proyectos"]
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
    INI(["🏔️ INGRESO A LA COMUNIDAD\nEncuentro de orientación · Promesa de Equipo"])

    subgraph CAMINOS["4 CAMINOS (Planos de Relación)\n(cada Sendero trabaja los 4 Caminos)"]
        direction LR
        C1["Camino\nConsigo Mismo"]
        C2["Camino\nCon los Demás"]
        C3["Camino\nCon el Entorno"]
        C4["Camino\nCon lo Trascendente"]
    end

    subgraph SEN["4 SENDEROS · Elección libre · No secuencial"]
        direction LR
        CEN["☀️ Cenit\nSalud y Bienestar"]
        CIM["🌲 Cima\nMedio Ambiente y Sustentabilidad"]
        CUM["🕊️ Cumbre\nPaz y Participación Comunitaria"]
        CUS["🛠️ Cúspide\nHabilidades para la Vida"]
    end

    subgraph PROCESO["PROCESO DENTRO DE CADA SENDERO"]
        direction LR
        DES["Desafío\nCompetencia a lograr\n(11 Desafíos en total)"]
        ESC["Escenario de Aprendizaje\nActividad concreta de aprendizaje"]
        PROY["Proyecto de Equipo\naplicación comunitaria del Desafío"]
        DES --> ESC --> PROY
    end

    subgraph EVAL["EVALUACIÓN"]
        direction TB
        E1["Autoevaluación\ndel Caminante\nprotagonismo en su proceso"]
        E2["Coevaluación\nentre pares de Equipo"]
        E3["Observación\ndel Scouter\n(acompañamiento)"]
        REG["Registro en\nHoja de Caminata"]
        VAL["Validación en\nConsejo de Equipo\nConsejo de Sección"]
        E1 --- E2 --- E3 --> REG --> VAL
    end

    subgraph ESP["ESPECIALIDADES · 8 campos del conocimiento\nProceso: Conozco → Aplico → Comparto"]
        EC["8 grupos temáticos\nadaptados a 14–18 años"]
    end

    subgraph FIN["INSIGNIAS FINALES"]
        direction LR
        OBS["⬟ Obsidiana\nPrimer nivel de culminación"]
        JAD["💎 Jade\nNivel superior de culminación"]
        OBS --> JAD
    end

    INI --> CAMINOS
    CAMINOS --> SEN
    SEN --> PROCESO
    PROCESO --> EVAL
    EVAL --> ESP
    ESP --> FIN
```
