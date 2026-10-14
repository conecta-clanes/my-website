# ✏️ Liderazgo en el Clan de Rovers

## Introducción

Ésta propuesta no sustituyen la documentación oficial, no nos hacemos responsables del mal uso.



## Tecnologías usadas

- [Claude Code](https://claude.com/product/claude-code) 


## Diagrama Tipos y roles de liderazgo en el Clan de Rovers ASMAC — operativo, de proyecto, representativo y formativo.

```mermaid
flowchart TB

    RV(["ROVERS · 18-21 años<BR>Protagonistas de todos los liderazgos del Clan"])

    subgraph OP["LIDERAZGO OPERATIVO · elegido democráticamente en el Parlamento"]
        PR["Promotor Rover<BR>máx. 1 año consecutivo<BR>Preside el Parlamento<BR>Administra y coordina el Clan"]
        CAL["Calidades en apoyo al Promotor<BR>Orientadores · Secretario de acuerdos<BR>Tesorero · Encargado de redes<BR>Primeros auxilios · Mentores · Sinodales"]
        ES["Equipo de Seguimiento ES<BR>1 por cada 5 Rovers · máx. 1 año<BR>Seguimiento al PPV · informa al Parlamento<BR>Requisito: haber concluido al menos un proyecto"]
    end

    subgraph PROY["LIDERAZGO DE PROYECTO · dentro de los EAP"]
        LP["Líder de Proyecto<BR>Elegido por el equipo<BR>Dirige y coordina el EAP<BR>Toma decisiones y gestiona el equipo"]
        EAP["Equipo de Apoyo a Proyecto EAP<BR>Temporal · todos reciben reconocimiento al concluir"]
    end

    subgraph REP["LIDERAZGO REPRESENTATIVO · portavoces elegidos democráticamente"]
        REP_G["Representante Juvenil<BR>nivel Grupo<BR>Voz y voto en el Consejo de Grupo<BR>Período: 1 año calendario"]
        FOR["Foristas<BR>Asisten a Foros Provinciales y Nacionales<BR>Exponen propuestas del Clan"]
        REP_P["Representante Juvenil<BR>nivel Provincia<BR>Comité Red de Jóvenes<BR>Voz y voto en COP y CEP"]
        REP_N["Representante Juvenil<BR>nivel Nacional<BR>Comité Nacional Red de Jóvenes"]
    end

    subgraph FORM["LIDERAZGO FORMATIVO · espacios de desarrollo"]
        PF["Puntas de Flecha<BR>Evento Provincial o Nacional<BR>Talleres de liderazgo y autonomía<BR>Valor curricular y para proyectos"]
        EXT["Liderazgo fuera del Movimiento<BR>Brigadistas · Voluntarios<BR>Consejeros estudiantiles<BR>Capitanes · Representantes comunitarios"]
    end

    CRR["CRR · Consejero Rover Responsable<BR>mín. 27 años · Facilitador<BR>Miembro del Parlamento · voto + veto limitado"]
    CR["CR · Consejeros Rover<BR>mín. 25 años · Facilitadores<BR>Acompañan PPV y liderazgos · 1 por cada 5 Rovers"]

    RV -->|"eligen"| PR
    RV -->|"eligen"| ES
    PR -.->|"delega calidades"| CAL
    RV -->|"forman y eligen Líder"| LP
    LP -->|"coordina"| EAP
    RV -->|"elegidos por jóvenes del Grupo"| REP_G
    RV -->|"participan como"| FOR
    FOR -->|"eligen"| REP_P
    FOR -->|"eligen"| REP_N
    RV -->|"participan en"| PF
    RV -.->|"ejercen"| EXT
    CRR -.->|"orienta"| PR
    CR -.->|"facilitan y asesoran"| RV

    classDef rovers fill:#c0392b,stroke:#922b21,color:#fff,font-weight:bold
    classDef operativo fill:#8e44ad,stroke:#6c3483,color:#fff
    classDef proyecto fill:#2980b9,stroke:#1a5276,color:#fff
    classDef rep fill:#1e8449,stroke:#196f3d,color:#fff
    classDef formativo fill:#d35400,stroke:#a04000,color:#fff
    classDef adulto fill:#1a5276,stroke:#154360,color:#fff
    classDef calidad fill:#7f8c8d,stroke:#566573,color:#fff

    class RV rovers
    class PR,ES operativo
    class LP,EAP proyecto
    class REP_G,FOR,REP_P,REP_N rep
    class PF,EXT formativo
    class CRR,CR adulto
    class CAL calidad
```

| Tipo | Rol | Elección / origen | Duración |
|---|---|---|---|
| **Operativo** | Promotor Rover | Proceso democrático en el Parlamento | Máx. 1 año consecutivo |
| **Operativo** | Equipo de Seguimiento (ES) | Elegido por el Parlamento; requisito: ≥1 proyecto concluido | Máx. 1 año; máx. 2 períodos en vida de Clan |
| **Operativo** | Calidades en apoyo al Promotor | Designadas/reconocidas por el Promotor según necesidad | Variable |
| **Proyecto** | Líder de Proyecto | Elegido por el Equipo de Apoyo a Proyecto (EAP) | Duración del proyecto |
| **Representativo** | Representante Juvenil nivel Grupo | Elegido por todos los jóvenes del Grupo | 1 año calendario |
| **Representativo** | Forista | Participa en Foros Provinciales y Nacionales | Por evento |
| **Representativo** | Representante Juvenil Provincia | Elegido en Foros Provinciales | Período del Comité |
| **Representativo** | Representante Juvenil Nacional | Elegido en Foros Nacionales | Período del Comité |
| **Formativo** | Puntas de Flecha | Evento Provincial o Nacional | Por evento |
| **Formativo** | Liderazgo fuera del Movimiento | Brigadistas, consejeros, capitanes, representantes comunitarios | Variable |
| **Adultos** | Consejero Rover Responsable (CRR) | Designado · mín. 27 años | Período del cargo |
| **Adultos** | Consejeros Rover (CR) | Designados · mín. 25 años | Período del cargo |


## Fuentes

- [Las Rutas del Rover — ASMAC 2024](https://drive.scouts.org.mx/s/qnisYDHz4TNbDpi?dir=/&editing=false&openfile=true)
- [Guía de Scouter de Clan de Rovers — ASMAC 2024](https://drive.scouts.org.mx/s/nPfaxYwRB4Ryiyw?dir=/&editing=false&openfile=true)


---
#### Autora

- Yolanda Castillo 