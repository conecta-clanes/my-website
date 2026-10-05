# Estructura del Clan de Rovers

Esta propuesta no sustituyen la documentación oficial, no nos hacemos responsables del mal uso.


**Sección:** Clan de Rovers · **Edades:** 18 a 21 años · **Lema:** ¡Servir!

> Fuentes: *Las Rutas del Rover* (ASMAC, 2024) · *Guía de Scouter de Clan de Rovers* (DNME/CNAM, 2024)

---

```mermaid
flowchart LR
    CRR["**CRR**\nConsejero Rover Responsable\nmín. 27 años\nvoto igual al Rover · veto limitado"]
    CR["**CR**\nConsejeros Rover\nmín. 25 años\n1 por cada 5 Rovers"]

    subgraph PARL["PARLAMENTO ROVER · órgano legislativo · voz y voto igualitario"]
        RV["**ROVERS**\n18-21 años\nProtagonistas del Programa"]
        PR["**Promotor Rover**\nElegido democráticamente\nmáx. 1 año · Presidenta-e"]
        ES["**Equipo de Seguimiento ES**\n1 por cada 5 Rovers · máx. 1 año"]
        EAP["**Equipo de Apoyo a Proyecto EAP**\nTemporal · Líder elegido por el equipo"]
        REP_G["**Representantes Juveniles**\nnivel Grupo"]
        IA["**Individuo Asociado**\nRover sin Clan activo"]
    end

    subgraph GRUPO["NIVEL GRUPO"]
        CG["**Consejo de Grupo**\nVeto sobre acuerdos contrarios\na ordenamientos o seguridad"]
        ASC["**Asociado Rover**\nEx-Rover con registro vigente"]
    end

    subgraph INST["VINCULACIÓN INSTITUCIONAL"]
        FOROS["**Foros**\nProvinciales y Nacionales"]
        RJ["**Red de Jóvenes**\nRepresentantes elegidos por Foros"]
        COP["**COP**\nConsejo de Provincia"]
        CEP["**CEP**\nComisión Ejecutiva de Provincia"]
    end

    CRR -->|"voto + veto limitado"| PR
    CR -.->|"asesoran y acompañan PPV"| RV
    RV -->|"eligen"| PR
    RV -->|"eligen"| ES
    RV --- EAP
    CRR -->|"representa al Clan"| CG
    REP_G -->|"portavoz jóvenes del Grupo"| CG
    PR -->|"remite decisiones vetadas"| CG
    CG -.->|"veto"| PR
    RV -->|"Foristas"| FOROS
    FOROS -->|"eligen Representantes"| RJ
    RJ -->|"voz y voto"| COP
    RJ -->|"voz y voto"| CEP

    classDef rover fill:#c0392b,stroke:#922b21,color:#fff,font-weight:bold
    classDef scouter fill:#1a5276,stroke:#154360,color:#fff,font-weight:bold
    classDef grupo fill:#d35400,stroke:#a04000,color:#fff
    classDef ext fill:#1e8449,stroke:#196f3d,color:#fff
    classDef neut fill:#566573,stroke:#424949,color:#fff

    class RV,PR,ES,REP_G rover
    class CRR,CR scouter
    class CG,ASC grupo
    class FOROS,RJ,COP,CEP ext
    class EAP,IA neut
```

| Elemento | Quiénes | Edad | Función clave |
|---|---|---|---|
| **Rovers** | Jóvenes protagonistas | 18-21 años | Planean, ejecutan y evalúan su PPV; voz y voto igualitario en el Parlamento |
| **Promotor Rover** | Rover elegido por el Parlamento | 18-21 años | Preside el Parlamento; administra y coordina el Clan; máx. 1 año |
| **Equipo de Seguimiento (ES)** | Rovers elegidos por el Parlamento | 18-21 años | Seguimiento al PPV; informa al Parlamento; 1 por cada 5 Rovers; máx. 1 año |
| **Equipo de Apoyo a Proyecto (EAP)** | Rovers por proyecto | 18-21 años | Equipo temporal; Líder elegido por el equipo |
| **Representantes Juveniles** | Rovers elegidos por sus pares | 18-21 años | Portavoces de todos los jóvenes del Grupo ante el Consejo de Grupo |
| **Consejero Rover Responsable (CRR)** | Adulto voluntario | mín. 27 años | Único representante del Clan ante el CG; miembro permanente del Parlamento; voto + veto limitado |
| **Consejeros Rover (CR)** | Adultos voluntarios | mín. 25 años | Asesoría educativa y acompañamiento del PPV; 1 por cada 5 Rovers |
| **Individuo Asociado** | Rover sin Clan activo | 18-21 años | Registrado en ASMAC; recibe acompañamiento de su Consejero |
| **Asociado Rover** | Ex-Rover | +22 años | Concluyó el Programa; mantiene registro vigente |
| **Consejo de Grupo** | Jefes de Sección + CRR | — | Veto sobre acuerdos contrarios a ordenamientos o que pongan en riesgo la seguridad |
| **Foros Provinciales/Nacionales** | Rovers Foristas | 18-21 años | Participación juvenil; elección democrática de Representantes al Comité Red de Jóvenes |
| **Red de Jóvenes** | Representantes elegidos en Foros | 18-21 años | Voz y voto ante COP y CEP de Provincia |

##### Autora

- Yolanda Castillo