# ✏️ Transferencia de Liderazgo por Sección

---

# Transferencia de Liderazgo por Sección

A lo largo del Programa de Jóvenes, el protagonismo se transfiere progresivamente del adulto al joven. En la **Manada** el adulto lidera y el niño sigue; en el **Clan** el Rover decide y actúa, y el adulto solo orienta.

## Tecnologías usadas

- [Claude Code](https://claude.com/product/claude-code) 

## Curvas de transferencia

```mermaid
%%{init: {'theme':'base','themeVariables':{'xyChart':{'plotColorPalette':'#7b2d8b,#95a5a6','backgroundColor':'#ffffff'}}}}%%
xychart-beta
    title "Transferencia de Liderazgo Adulto ↔ Juvenil"
    x-axis ["Manada", "Tropa", "Comunidad", "Clan"]
    y-axis "Nivel de responsabilidad %" 0 --> 100
    line [10, 35, 65, 90]
    line [90, 65, 35, 10]
```

- Línea **morada** — Liderazgo Juvenil: crece con cada sección
- Línea **gris** — Liderazgo Adulto: decrece a medida que el joven madura y gana autonomía

## Balance por sección

```mermaid
flowchart LR
    subgraph MAN["🟡 MANADA · 6-9 años"]
        MA1["Adulto\n━━━━━━━━━ 90 %"]
        MJ1["Joven\n━ 10 %"]
    end
    subgraph TRO["🟢 TROPA · 10-13 años"]
        TA1["Adulto\n━━━━━━ 65 %"]
        TJ1["Joven\n━━━━ 35 %"]
    end
    subgraph COM["🔵 COMUNIDAD · 14-17 años"]
        CA1["Adulto\n━━━━ 35 %"]
        CJ1["Joven\n━━━━━━ 65 %"]
    end
    subgraph CLA["🔴 CLAN · 18-21 años"]
        XA1["Adulto\n━ 10 %"]
        XJ1["Joven\n━━━━━━━━━ 90 %"]
    end

    MAN --> TRO --> COM --> CLA

    classDef adulto fill:#95a5a6,stroke:#7f8c8d,color:#fff
    classDef juvenil fill:#7b2d8b,stroke:#6c3483,color:#fff

    class MA1,TA1,CA1,XA1 adulto
    class MJ1,TJ1,CJ1,XJ1 juvenil
```

## Rol del adulto en cada extremo

| Sección | Rol del adulto | Rol del joven |
|---|---|---|
| **Manada** | Dirige · planea · decide | Participa · sigue · aprende |
| **Tropa** | Guía · propone · acompaña | Comienza a planear · asume roles |
| **Comunidad** | Asesora · da retroalimentación | Lidera · organiza · decide con apoyo |
| **Clan** | Facilita · orienta · veto limitado | Protagonista total · planea · ejecuta · evalúa |

## En el Clan: el adulto como Facilitador

En el Clan, los Consejeros Rover (CRR y CR) adoptan el rol de **Facilitadores**, no de directores. El Movimiento Scout reconoce y busca impulsar el liderazgo juvenil de manera natural, generando los espacios para que los Rovers ejerzan su autonomía.

```mermaid
flowchart LR
    RV["ROVERS\nProtagonistas\nDeciden · planean · evalúan"]
    CRR["CRR\nConsejero Rover\nResponsable\nFacilitador · voto + veto limitado"]
    CR["CR\nConsejeros Rover\nFacilitadores\nAsesoran el PPV"]

    CRR -.->|"orienta"| RV
    CR -.->|"acompaña PPV"| RV
    RV -->|"toman decisiones"| RV

    classDef rover fill:#c0392b,stroke:#922b21,color:#fff,font-weight:bold
    classDef adulto fill:#1a5276,stroke:#154360,color:#fff

    class RV rover
    class CRR,CR adulto
```


---
#### Autora

- Yolanda Castillo 