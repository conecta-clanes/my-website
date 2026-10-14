# ✏️ Diagrama 3: Cómo Funciona la Tropa

## Introducción

Ésta propuesta no sustituyen la documentación oficial, no nos hacemos responsables del mal uso.

## Tecnologías usadas

- [Claude Code](https://claude.com/product/claude-code) 

## Diagrama

Cómo funciona la Tropa

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
##### Autora

    - Yolanda Castillo