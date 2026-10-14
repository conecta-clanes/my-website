# ✏️ Diagrama 4: Progresión en la Tropa

## Introducción

Ésta propuesta no sustituyen la documentación oficial, no nos hacemos responsables del mal uso.

## Tecnologías usadas

- [Claude Code](https://claude.com/product/claude-code) 

## Diagrama Progresión en Tropa

```mermaid
flowchart TD
    INI(["⚜️ INGRESO A LA TROPA<BR>Actividades de bienvenida y orientación"])

    subgraph SENDAS["4 SENDAS (Planos de Relación)(cada Rumbo trabaja las 4 Sendas)"]
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

    subgraph ESP["ESPECIALIDADES · 8 campos del conocimiento, Proceso: Conozco → Aplico → Comparto"]
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

##### Autora

    - Yolanda Castillo