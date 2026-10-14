# ✏️ Diagrama 1: Cómo Funciona la Manada

## Introducción

Ésta propuesta no sustituyen la documentación oficial, no nos hacemos responsables del mal uso.

## Tecnologías usadas

- [Claude Code](https://claude.com/product/claude-code) 

## Diagrama Cómo funciona laManada de Lobatos

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
##### Autora

    - Yolanda Castillo