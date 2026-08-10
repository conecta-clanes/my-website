# Diagrama 4: Progresión en la Tropa

```mermaid
flowchart TD
    INI(["⚜️ INGRESO A LA TROPA\nActividades de bienvenida y orientación"])

    subgraph SENDAS["4 SENDAS (Planos de Relación)(cada Rumbo trabaja las 4 Sendas)"]
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

    subgraph ESP["ESPECIALIDADES · 8 campos del conocimiento, Proceso: Conozco → Aplico → Comparto"]
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
##### Redactora
    - Yolanda Castillo