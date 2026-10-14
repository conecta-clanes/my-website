# Ciclo de Programa — Clan de Rovers

## Introducción

Ésta propuesta no sustituyen la documentación oficial, no nos hacemos responsables del mal uso.

## Tecnologías usadas

- [Claude Code](https://claude.com/product/claude-code) 

## Diagrama Ciclo de Programa en el Clan de Rovers

```mermaid
flowchart TD
    TITLE(["🏕️ CICLOS DE PROGRAMA<BR>Clan de Rovers · 18–21 años<BR>Dos ciclos paralelos: Colectivo + Personal"])

    subgraph COL["CICLO COLECTIVO DEL CLAN · 3–4 meses"]
        direction LR
        COL1["📌 PLANEAR colectivo<BR>Parlamento selecciona<BR>y calendariza actividades del Clan"]
        COL2["⚡ EJECUTAR colectivo<BR>Clan realiza actividades<BR>comunes calendarizadas"]
        COL3["🔍 REVISAR colectivo<BR>Parlamento evalúa actividades<BR>Equipo de Seguimiento rinde informe<BR>Promotor Rover reporta situación financiera"]
        COL1 --> COL2 --> COL3
        COL3 -->|"Nuevo ciclo colectivo"| COL1
    end

    subgraph PER["CICLO PERSONAL DE PROGRAMA (PPV) · Duración individual: 3–6 meses"]

        subgraph PP["🗺️ PLANEAR — Preparo mi propia aventura"]
            PP1["Reflexiona sobre Planos de Relación<BR>y Ejes Temáticos (Horquillas)"]
            PP2["Elige la Ruta de progresión<BR>y competencias a desarrollar"]
            PP3["Establece metas SMART"]
            PP4["Elabora cronograma de<BR>Acciones Educativas en su Agenda Rover"]
            PP5["Comparte su plan<BR>en el Parlamento Rover"]
            PP1 --> PP2 --> PP3 --> PP4 --> PP5
        end

        subgraph EP["⚡ EJECUTAR — Vive tu propia aventura"]
            EP1["Realiza Acciones Educativas (AEs)<BR>dentro y fuera del Movimiento"]
            EP2["Participa en eventos y desarrolla proyectos"]
            EP3["Viaje Rover · Gran Aventura<BR>Actividad de larga duración dentro del PPV<BR>• Gran Aventura en la Naturaleza<BR>• Gran Aventura Intercultural"]
            EP1 --> EP2 --> EP3
        end

        subgraph RP["🔍 REVISAR"]
            RP1["Autoevaluación de las<BR>Acciones Educativas realizadas"]
            RP2["Evaluación con Consejero Rover<BR>mediante entrevistas periódicas"]
            RP3["Registra el avance<BR>en su Agenda Rover"]
            RP4["Reporta al Parlamento<BR>Comparte y celebra"]
            RP1 --> RP2 --> RP3 --> RP4
        end

        PP --> EP
        EP --> RP
        RP -->|"Nuevo Ciclo Personal"| PP
    end

    subgraph RUTA["4 RUTAS DE PROGRESIÓN (Horquillas)"]
        direction LR
        R1["🧘 Kikapú<BR>Salud y Bienestar"]
        R2["🛠️ Otomí<BR>Habilidades para la Vida"]
        R3["🕊️ Wixárika<BR>Paz y Participación Comunitaria"]
        R4["🌿 Maya<BR>Medio Ambiente y Sustentabilidad"]
    end

    subgraph ORG["ÓRGANOS DE GOBIERNO"]
        direction TB
        PARL["Parlamento Rover<BR>Todos los Rovers<BR>Toma de decisiones colectivas<BR>Recibe reportes · Fija fechas de celebración"]
        PROM["Promotor Rover<BR>Presidenta/e del Parlamento<BR>Dirige operación del Clan · máx. 1 año"]
        CRR["Consejero Responsable Rover<BR>Acompañamiento individual del PPV"]
        ES["Equipo de Seguimiento<BR>Da seguimiento a los PPV<BR>Rinde informe al Parlamento"]
        PARL --- PROM
        CRR --- ES
    end

    TITLE --> COL
    TITLE --> PER
    RUTA -.-> PER
    ORG -.-> COL
    ORG -.-> PER
    COL <-->|"Se integran<BR>mutualmente"| PER
```

##### Autora

    - Yolanda Castillo