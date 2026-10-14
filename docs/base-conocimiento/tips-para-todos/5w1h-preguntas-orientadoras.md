# 🔨 Framework 5W + 1H — Preguntas Orientadoras

## Introducción

Ésta propuesta no sustituyen la documentación oficial, no nos hacemos responsables del mal uso.

> En escritura académica se conoce como **5W + 1H**.
> En el Movimiento Scout se aplica como **Preguntas Orientadoras** para planear, ejecutar y evaluar proyectos y actividades.

## Diagrama Preguntas Orientadoras

---

```mermaid
mindmap
  root(("❓ 5W + 1H<BR>Preguntas<BR>Orientadoras"))
    WHO("👤 WHO<BR>¿QUIÉN?")
      ::icon(fa fa-user)
      académico("Académico:<BR>Autor · Audiencia<BR>Partes interesadas<BR>¿Quién investiga?<BR>¿A quién va dirigido?")
      scout("Scout:<BR>¿Quiénes participan?<BR>¿Quién coordina?<BR>¿Quiénes son los<BR>benefiiciarios?<BR>¿Quién evalúa?")
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
        WHEN --- WHERE --- HOW
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
        E1 --- E2 --- E3 --- E4 --- E5 --- E6
    end

    EVAL --> MOP

    subgraph MOP["🕊️ APLICACIÓN EN MENSAJEROS DE LA PAZ"]
        M1["¿QUIÉN?<BR>→ Máx. 5 coordinadores Rovers<BR>Beneficiarios activos en el proyecto"]
        M2["¿QUÉ?<BR>→ Proyecto de servicio comunitario<BR>alineado a un ODS"]
        M3["¿POR QUÉ?<BR>→ Construir una Cultura de Paz<BR>Contribuir a la Agenda 2030"]
        M4["¿CUÁNDO?<BR>→ Inicio conteo de horas al informar<BR>al Jefe de Sección · 800 h mínimo"]
        M5["¿DÓNDE?<BR>→ Comunidad local · scout.org<BR>sdgs.scout.org → mapa global"]
        M6["¿CÓMO?<BR>→ 4 Pasos: Inspira · Aprende<BR>Actúa · Comparte"]
    end

    style TITLE fill:#1a1a2e,color:#f0c040,stroke:#c8a92b
    style PLAN fill:#0a1628,stroke:#1e40af
    style EXEC fill:#0a1a0a,stroke:#15803d
    style EVAL fill:#1a0a0a,stroke:#991b1b
    style MOP fill:#1a120a,stroke:#92400e
    style WHO fill:#1e3a8a,color:#93c5fd,stroke:#1e40af
    style WHAT fill:#1e3a8a,color:#93c5fd,stroke:#1e40af
    style WHY fill:#1e3a8a,color:#93c5fd,stroke:#1e40af
    style WHEN fill:#14532d,color:#86efac,stroke:#15803d
    style WHERE fill:#14532d,color:#86efac,stroke:#15803d
    style HOW fill:#14532d,color:#86efac,stroke:#15803d
    style M1 fill:#431407,color:#fed7aa,stroke:#92400e
    style M2 fill:#431407,color:#fed7aa,stroke:#92400e
    style M3 fill:#431407,color:#fed7aa,stroke:#92400e
    style M4 fill:#431407,color:#fed7aa,stroke:#92400e
    style M5 fill:#431407,color:#fed7aa,stroke:#92400e
    style M6 fill:#431407,color:#fed7aa,stroke:#92400e
```

---

## Las 6 Preguntas Orientadoras — Referencia rápida

| Pregunta | Inglés | En escritura académica | En Scouts (planeación) |
|---|---|---|---|
| **¿Quién?** | Who | Autor, audiencia, actores | Coordinadores, beneficiarios, scouters |
| **¿Qué?** | What | Tema, problema, hipótesis | Proyecto, actividad, ODS a impactar |
| **¿Cuándo?** | When | Período, contexto temporal | Cronograma, duración, horas de servicio |
| **¿Dónde?** | Where | Ámbito geográfico o conceptual | Comunidad, espacio físico, alcance |
| **¿Por qué?** | Why | Justificación, relevancia, propósito | Necesidad detectada, conexión con valores scout |
| **¿Cómo?** | How | Metodología, proceso, estrategia | Plan de acción, etapas, recursos, evaluación |

---


## Fuentes

- [Las Rutas del Rover — ASMAC 2024](https://drive.scouts.org.mx/s/qnisYDHz4TNbDpi?dir=/&editing=false&openfile=true)
- [Guía de Scouter de Clan de Rovers — ASMAC 2024](https://drive.scouts.org.mx/s/nPfaxYwRB4Ryiyw?dir=/&editing=false&openfile=true)
- [Framework 5W+1H — Center for Teaching & Learning, UAF](https://ctl.uaf.edu/2025/07/24/the-5w-and-1h-framework-in-academic-writing/)


#### Autora

- Yolanda Castillo 