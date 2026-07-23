# Diagrama: Funcionamiento del Clan de Rovers

```mermaid
flowchart TD
    subgraph VIDA["⛵  CICLO DE VIDA EN EL CLAN  ·  18 a 22 años"]
        direction TB
        A["Ingreso al Clan\n18 años\n(desde Caminantes o nuevo ingreso)"]
        A --> B["Período de Inducción\n3 – 6 meses\nOrientadores asignados por el Parlamento"]
        B --> C["Ceremonia de Compromiso Rover\nVigilia  ·  Investidura\nPromesa Scout  ·  Horquilla  ·  Escudo de Clan"]
        C --> D["Proyecto Personal de Vida  —  PPV\nAutodiagnóstico  ·  Metas SMART\nDentro y fuera del Movimiento"]
        D --> E["Acciones Educativas\nActividades  ·  Proyectos  ·  Eventos\nMetodología PER  ·  Criterio DURASLI"]
        E --> F["Progresión Personal\nInsignias  ·  Rutas Rover"]
        F --> G["Enlace a la Vida\n21.5 años  ·  Manifiesto Rover"]
        G --> H["Partida Rover\nCeremonia final"]
    end

    subgraph GOB["🏛  GOBIERNO DEL CLAN"]
        direction TB
        I["Parlamento Rover\nCuerpo legislativo\nTodos los Rovers con voz y voto\nSesión mensual"]
        I --> J["Promotor Rover\nDirige y coordina\nElecto democráticamente  ·  máx. 1 año"]
        I --> K["Equipo de Seguimiento  ES\n1 por cada 5 Rovers\nSeguimiento al PPV de cada Rover"]
        I --> L["Equipos de Apoyo a Proyecto  EAP\nConformados por proyecto específico"]
        M["Consejero Rover Responsable  CRR  ≥ 27 años\nConsejeros  ≥ 25 años  ·  1 por 5 Rovers\nAsesoramiento  —  sin dirigir"]
        M -. "1 voto compartido\nPoder de veto solo\npor ordenamientos" .-> I
    end

    subgraph EJES["📌  4 EJES TEMÁTICOS DEL PPV"]
        direction LR
        N1["Salud y\nBienestar"]
        N2["Habilidades\npara la Vida"]
        N3["Paz y\nParticipación Comunitaria"]
        N4["Medio Ambiente\ny Sustentabilidad"]
    end

    subgraph RUTAS["🏅  RUTAS DE PROGRESIÓN"]
        direction LR
        O1["Aventuras en\nla Naturaleza"]
        O2["Especialidades\npara la Vida"]
        O3["Punta de Flecha\nLiderazgo"]
        O4["Mundo Mejor\ny ODS"]
        O5["Mensajeros\nde la Paz"]
        O6["Insignia\nTerminal"]
    end

    subgraph METODO["⚜️  MÉTODO SCOUT  —  8 Elementos"]
        direction LR
        P1["1 · Promesa\ny Ley Scout"]
        P2["2 · Aprender\nHaciendo"]
        P3["3 · Progresión\nPersonal"]
        P4["4 · Sistema\nde Equipos"]
        P5["5 · Apoyo\ndel Adulto"]
        P6["6 · Marco Simbólico\nLema: ¡Servir!"]
        P7["7 · Naturaleza"]
        P8["8 · Participación\nComunitaria"]
    end

    %% Conexiones entre subgrafos
    METODO -->|"guía educativa\ntransversal"| VIDA
    GOB -->|"estructura,\ndecisiones y seguimiento"| D
    D --> EJES
    EJES --> E
    F --> RUTAS
```

---

## Resumen del funcionamiento

| Elemento | Descripción |
|---|---|
| **Edad** | 18 años – un día antes de cumplir 22 |
| **Lema** | ¡Servir! |
| **Marco Simbólico** | "Vivir mi propia aventura mediante un proyecto de vida" |
| **Órgano legislativo** | Parlamento Rover (todos los Rovers, voto igual) |
| **Herramienta central** | Proyecto Personal de Vida (PPV) |
| **Metodología de proyectos** | PER — Planeo · Ejecuto · Reviso |
| **Objetivos** | SMART — Específico · Medible · Alcanzable · Realista · Tiempo |
| **Ceremonias** | Compromiso Rover (Vigilia + Investidura) y Partida Rover |
| **Consejero** | Asesora y acompaña, no dirige; CRR ≥ 27 años |

#### Herramientas usadas para generar los diargramas

- [Claude Code](https://claude.com/pricing) 
- [Microsoft Marktdown](https://github.com/microsoft/markitdown) 

##### Redactora

- Yolanda Castillo

```