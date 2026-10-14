# ✏️ Diagrama 2: Progresión en la Manada

## Introducción

Ésta propuesta no sustituyen la documentación oficial, no nos hacemos responsables del mal uso.

## Tecnologías usadas

- [Claude Code](https://claude.com/product/claude-code) 

## Diagrama Progresión en la Manada de Lobatos

```mermaid
flowchart TD
    INI(["🐾 MI PRIMER RASTRO<BR>Insignia de entrada a la Manada"])

    subgraph PLANOS["4 PLANOS DE RELACIÓN (cada Cazadero trabaja los 4 planos)"]
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

    subgraph ESP["ESPECIALIDADES · 8 grupos temáticos, Proceso: Conozco → Aplico → Comparto"]
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

##### Autora

    - Yolanda Castillo