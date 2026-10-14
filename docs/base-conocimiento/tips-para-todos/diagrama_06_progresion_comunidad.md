# ✏️ Diagrama 6: Progresión en la Comunidad

## Introducción

Ésta propuesta no sustituyen la documentación oficial, no nos hacemos responsables del mal uso.

## Tecnologías usadas

- [Claude Code](https://claude.com/product/claude-code) 

## Diagrama Progresión en la Comunidad de Caminantes

```mermaid
flowchart TD
    INI(["🏔️ INGRESO A LA COMUNIDAD<BR>Encuentro de orientación · Promesa de Equipo"])

    subgraph CAMINOS["4 CAMINOS (Planos de Relación)(cada Sendero trabaja los 4 Caminos)"]
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

    subgraph ESP["ESPECIALIDADES · 8 campos del conocimiento, Proceso: Conozco → Aplico → Comparto"]
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