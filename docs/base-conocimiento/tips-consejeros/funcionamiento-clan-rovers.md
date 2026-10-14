# ✏️ Diagrama: Funcionamiento del Clan de Rovers

## Introducción

Ésta propuesta no sustituyen la documentación oficial, no nos hacemos responsables del mal uso.

## Tecnologías usadas

- [Claude Code](https://claude.com/product/claude-code) 

## Fuentes

- [Las Rutas del Rover — ASMAC 2024](https://drive.scouts.org.mx/s/qnisYDHz4TNbDpi?dir=/&editing=false&openfile=true)
- [Guía de Scouter de Clan de Rovers — ASMAC 2024](https://drive.scouts.org.mx/s/nPfaxYwRB4Ryiyw?dir=/&editing=false&openfile=true)

### Diagrama CICLO DE VIDA EN EL CLAN

```mermaid
flowchart TD
    subgraph VIDA["⛵  CICLO DE VIDA EN EL CLAN  ·  18 a 22 años"]
        direction TB
        A["Ingreso al Clan<BR>18 años<BR>(desde Caminantes o nuevo ingreso)"]
        A --> B["Período de Inducción<BR>3 – 6 meses<BR>Orientadores asignados por el Parlamento"]
        B --> C["Ceremonia de Compromiso Rover<BR>Vigilia  ·  Investidura<BR>Promesa Scout  ·  Horquilla  ·  Escudo de Clan"]
        C --> D["Proyecto Personal de Vida  —  PPV<BR>Autodiagnóstico  ·  Metas SMART<BR>Dentro y fuera del Movimiento"]
        D --> E["Acciones Educativas<BR>Actividades  ·  Proyectos  ·  Eventos<BR>Metodología PER  ·  Criterio DURASLI"]
        E --> F["Progresión Personal<BR>Insignias  ·  Rutas Rover"]
        F --> G["Enlace a la Vida<BR>21.5 años  ·  Manifiesto Rover"]
        G --> H["Partida Rover<BR>Ceremonia final"]
    end

    subgraph GOB["🏛  GOBIERNO DEL CLAN"]
        direction TB
        I["Parlamento Rover<BR>Cuerpo legislativo<BR>Todos los Rovers con voz y voto<BR>Sesión mensual"]
        I --> J["Promotor Rover<BR>Dirige y coordina<BR>Electo democráticamente  ·  máx. 1 año"]
        I --> K["Equipo de Seguimiento  ES<BR>1 por cada 5 Rovers<BR>Seguimiento al PPV de cada Rover"]
        I --> L["Equipos de Apoyo a Proyecto  EAP<BR>Conformados por proyecto específico"]
        M["Consejero Rover Responsable  CRR  ≥ 27 años<BR>Consejeros  ≥ 25 años  ·  1 por 5 Rovers<BR>Asesoramiento  —  sin dirigir"]
        M -. "1 voto compartido<BR>Poder de veto solo<BR>por ordenamientos" .-> I
    end

    subgraph EJES["📌  4 EJES TEMÁTICOS DEL PPV"]
        direction LR
        N1["Salud y<BR>Bienestar"]
        N2["Habilidades<BR>para la Vida"]
        N3["Paz y<BR>Participación Comunitaria"]
        N4["Medio Ambiente<BR>y Sustentabilidad"]
    end

    subgraph RUTAS["🏅  RUTAS DE PROGRESIÓN"]
        direction LR
        O1["Aventuras en<BR>la Naturaleza"]
        O2["Especialidades<BR>para la Vida"]
        O3["Punta de Flecha<BR>Liderazgo"]
        O4["Mundo Mejor<BR>y ODS"]
        O5["Mensajeros<BR>de la Paz"]
        O6["Insignia<BR>Terminal"]
    end

    subgraph METODO["⚜️  MÉTODO SCOUT  —  8 Elementos"]
        direction LR
        P1["1 · Promesa<BR>y Ley Scout"]
        P2["2 · Aprender<BR>Haciendo"]
        P3["3 · Progresión<BR>Personal"]
        P4["4 · Sistema<BR>de Equipos"]
        P5["5 · Apoyo<BR>del Adulto"]
        P6["6 · Marco Simbólico<BR>Lema: ¡Servir!"]
        P7["7 · Naturaleza"]
        P8["8 · Participación<BR>Comunitaria"]
    end

    %% Conexiones entre subgrafos
    METODO -->|"guía educativa<BR>transversal"| VIDA
    GOB -->|"estructura,<BR>decisiones y seguimiento"| D
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