# 🔨 Framework 5W + 2H — Preguntas Orientadoras

## Introducción

Esta propuesta no sustituye la documentación oficial, no nos hacemos responsables del mal uso.

> En gestión de proyectos y mejora continua se conoce como **5W + 2H**.
> En el Movimiento Scout se aplica como **Preguntas Orientadoras** para planear, ejecutar y evaluar proyectos y actividades.



## Diagrama Preguntas Orientadoras

---

```mermaid
mindmap
  root(("❓ 5W + 2H<BR>Preguntas<BR>Orientadoras"))
    WHO("👤 WHO<BR>¿QUIÉN?")
      ::icon(fa fa-user)
      académico("Académico:<BR>Autor · Audiencia<BR>Partes interesadas<BR>¿Quién investiga?<BR>¿A quién va dirigido?")
      scout("Scout:<BR>¿Quiénes participan?<BR>¿Quién coordina?<BR>¿Quiénes son los<BR>beneficiarios?<BR>¿Quién evalúa?")
    WHAT("📦 WHAT<BR>¿QUÉ?")
      académico2("Académico:<BR>Tema · Problema<BR>Hipótesis · Argumento<BR>¿Qué se investiga?<BR>¿Qué se demuestra?")
      scout2("Scout:<BR>¿Qué problema<BR>queremos resolver?<BR>¿Qué actividad<BR>o proyecto?<BR>¿Qué ODS impactamos?")
    WHEN("📅 WHEN<BR>¿CUÁNDO?")
      académico3("Académico:<BR>Contexto temporal<BR>Período de estudio<BR>¿Cuándo ocurrió?<BR>¿Cuándo es relevante?")
      scout3("Scout:<BR>¿Cuándo se realiza?<BR>Cronograma<BR>Fechas clave<BR>Duración del proyecto")
    WHERE("📍 WHERE<BR>¿DÓNDE?")
      académico4("Académico:<BR>Contexto geográfico<BR>Ámbito de la investigación<BR>¿Dónde aplica?<BR>¿Dónde se desarrolla?")
      scout4("Scout:<BR>¿Dónde se realiza?<BR>Comunidad · Barrio<BR>Escuela · Parque<BR>Área de impacto")
    WHY("💡 WHY<BR>¿POR QUÉ?")
      académico5("Académico:<BR>Justificación<BR>Relevancia · Propósito<BR>¿Por qué es importante?<BR>¿Qué vacío llena?")
      scout5("Scout:<BR>¿Por qué este proyecto?<BR>Necesidad identificada<BR>Vinculación con ODS<BR>Impacto esperado")
    HOW("⚙️ HOW<BR>¿CÓMO?")
      académico6("Académico:<BR>Metodología · Proceso<BR>Estrategia · Método<BR>¿Cómo se investiga?<BR>¿Cómo se argumenta?")
      scout6("Scout:<BR>¿Cómo lo haremos?<BR>Plan de acción<BR>Recursos · Etapas<BR>Monitoreo y evaluación")
    HOWMUCH("💰 HOW MUCH<BR>¿CUÁNTO?")
      académico7("Académico:<BR>Presupuesto · Muestra<BR>Cantidad de datos<BR>¿Cuánto cuesta?<BR>¿Cuántos casos?")
      scout7("Scout:<BR>¿Cuánto presupuesto?<BR>¿Cuántas horas de servicio?<BR>¿Cuántos beneficiarios?<BR>Indicadores de impacto")
```

---

```mermaid
flowchart TD
    TITLE["🧭 PREGUNTAS ORIENTADORAS EN EL ESCULTISMO<BR>Aplicación en Proyectos y Actividades Scout"]

    TITLE --> PLAN

    subgraph PLAN["📋 FASE DE PLANEACIÓN"]
        direction LR
        WHO["👤 ¿QUIÉN?<BR>Coordinadores · Colaboradores<BR>Beneficiarios · Scouters"]
        WHAT["📦 ¿QUÉ?<BR>Problema a resolver<BR>Tipo de proyecto o actividad<BR>ODS a impactar"]
        WHY["💡 ¿POR QUÉ?<BR>Necesidad detectada<BR>Justificación del proyecto<BR>Conexión con la Promesa y Ley"]
        WHO --- WHAT --- WHY
    end

    PLAN --> EXEC

    subgraph EXEC["⚡ FASE DE EJECUCIÓN"]
        direction LR
        WHEN["📅 ¿CUÁNDO?<BR>Cronograma · Fechas clave<BR>Duración · Horas de servicio"]
        WHERE["📍 ¿DÓNDE?<BR>Comunidad · Espacio físico<BR>Área de impacto"]
        HOW["⚙️ ¿CÓMO?<BR>Plan de acción · Etapas<BR>Recursos · Método de trabajo"]
        HOWMUCH["💰 ¿CUÁNTO?<BR>Presupuesto · Costo total<BR>Nº beneficiarios · Indicadores"]
        WHEN --- WHERE --- HOW --- HOWMUCH
    end

    EXEC --> EVAL

    subgraph EVAL["🔍 FASE DE EVALUACIÓN"]
        direction LR
        E1["¿Quién participó<BR>realmente?"]
        E2["¿Qué se logró<BR>vs. lo planeado?"]
        E3["¿Por qué se<BR>lograron o no<BR>los objetivos?"]
        E4["¿Cuándo se<BR>alcanzaron los<BR>hitos clave?"]
        E5["¿Dónde fue<BR>el mayor<BR>impacto?"]
        E6["¿Cómo se puede<BR>mejorar para la<BR>próxima vez?"]
        E7["¿Cuánto costó<BR>vs. presupuesto?<BR>¿Cuántos<BR>beneficiados?"]
        E1 --- E2 --- E3 --- E4 --- E5 --- E6 --- E7
    end

    EVAL --> MOP

    subgraph MOP["🕊️ APLICACIÓN EN MENSAJEROS DE LA PAZ"]
        M1["¿QUIÉN?<BR>→ Máx. 5 coordinadores Rovers<BR>Beneficiarios activos en el proyecto"]
        M2["¿QUÉ?<BR>→ Proyecto de servicio comunitario<BR>alineado a un ODS"]
        M3["¿POR QUÉ?<BR>→ Construir una Cultura de Paz<BR>Contribuir a la Agenda 2030"]
        M4["¿CUÁNDO?<BR>→ Inicio conteo de horas al informar<BR>al Jefe de Sección · 800 h mínimo"]
        M5["¿DÓNDE?<BR>→ Comunidad local · scout.org<BR>sdgs.scout.org → mapa global"]
        M6["¿CÓMO?<BR>→ 4 Pasos: Inspira · Aprende<BR>Actúa · Comparte"]
        M7["¿CUÁNTO?<BR>→ 800 h de servicio mínimo<BR>Presupuesto del proyecto<BR>Nº de personas beneficiadas"]
    end

    style TITLE fill:#8e44ad,stroke:#6c3483,color:#fff
    style PLAN fill:#d6eaf8,stroke:#2980b9
    style EXEC fill:#d5f5e3,stroke:#27ae60
    style EVAL fill:#fadbd8,stroke:#e74c3c
    style MOP fill:#fde8d8,stroke:#d35400
    style WHO fill:#2980b9,stroke:#1a5276,color:#fff
    style WHAT fill:#2980b9,stroke:#1a5276,color:#fff
    style WHY fill:#2980b9,stroke:#1a5276,color:#fff
    style WHEN fill:#27ae60,stroke:#1e8449,color:#fff
    style WHERE fill:#27ae60,stroke:#1e8449,color:#fff
    style HOW fill:#27ae60,stroke:#1e8449,color:#fff
    style HOWMUCH fill:#1a5276,stroke:#154360,color:#fff
    style M1 fill:#d35400,stroke:#a04000,color:#fff
    style M2 fill:#d35400,stroke:#a04000,color:#fff
    style M3 fill:#d35400,stroke:#a04000,color:#fff
    style M4 fill:#d35400,stroke:#a04000,color:#fff
    style M5 fill:#d35400,stroke:#a04000,color:#fff
    style M6 fill:#d35400,stroke:#a04000,color:#fff
    style M7 fill:#d35400,stroke:#a04000,color:#fff
```

---

## Las 7 Preguntas Orientadoras — Referencia rápida

| Pregunta | Inglés | En gestión de proyectos | En Scouts (planeación) |
|---|---|---|---|
| **¿Quién?** | Who | Responsable, equipo, partes interesadas | Coordinadores, beneficiarios, scouters |
| **¿Qué?** | What | Objetivo, entregable, problema a resolver | Proyecto, actividad, ODS a impactar |
| **¿Cuándo?** | When | Fecha inicio/fin, cronograma, hitos | Cronograma, duración, horas de servicio |
| **¿Dónde?** | Where | Ubicación, ámbito geográfico o digital | Comunidad, espacio físico, alcance |
| **¿Por qué?** | Why | Justificación, causa raíz, propósito | Necesidad detectada, conexión con valores scout |
| **¿Cómo?** | How | Metodología, proceso, pasos de ejecución | Plan de acción, etapas, recursos, evaluación |
| **¿Cuánto?** | How Much | Presupuesto, costo, cantidad de recursos | Presupuesto, horas de servicio, beneficiarios |

---


## Fuentes

- [Las Rutas del Rover — ASMAC 2024](https://drive.scouts.org.mx/s/qnisYDHz4TNbDpi?dir=/&editing=false&openfile=true)
- [Guía de Scouter de Clan de Rovers — ASMAC 2024](https://drive.scouts.org.mx/s/nPfaxYwRB4Ryiyw?dir=/&editing=false&openfile=true)
- Moen, R. D., & Norman, C. L. (2010). *Circling Back: Clearing up myths about the Deming cycle and seeing how it keeps evolving.* Quality Progress, 43(11), 22–28. — Origen del 5W2H en la gestión de calidad (ciclo PDCA/PDSA).
- Ohno, T. (1988). *Toyota Production System: Beyond Large-Scale Production.* Productivity Press. — Fundamento del análisis de causa raíz con preguntas orientadoras.
- [5W2H](https://www.leanconstructionmexico.com.mx/post/5w2h-qu%C3%A9-significa-para-qu%C3%A9-sirve-c%C3%B3mo-aplicarla-y-algunos-ejemplos) qué significa, para qué sirve, cómo aplicarla y algunos ejemplos


#### Autora

- Yolanda Castillo
