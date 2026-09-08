# Diagramas del Grupo Scout

---

## 1. Estructura Organizacional del Grupo Scout

```mermaid
graph TD
    %% Nivel externo superior
    CEP["🏛️ Comisión Ejecutiva de Provincia"]

    %% Órganos del Grupo
    AG["📢 Asamblea de Grupo\n(órgano informativo anual)"]
    CG["⚖️ Consejo de Grupo\n(máximo órgano de decisión)"]
    COM["📋 Comité de Grupo\n(administración y gestión)"]
    CE["🔧 Comités Especiales\n(temporales, máx. 3 simultáneos)"]

    %% Jefatura
    JG["👤 Jefe de Grupo\n(preside Consejo y Comité)"]
    SA["👤 Subjefe Administrativo\n(tesorería y secretaría)"]
    SME["👤 Subjefe de Métodos\nEducativos"]
    RJ["👥 Representantes Juveniles\n(2, del Clan, mayores de edad)"]
    COL["👥 Colaboradores de Grupo"]

    %% Secciones
    subgraph SECCIONES["SECCIONES (Programa de Jóvenes)"]
        MAN["🐺 Manada de Lobatos\n(Jefe de Manada)\n6–10 años"]
        TRO["⚜️ Tropa de Scouts\n(Jefe de Tropa)\n11–14 años"]
        COM2["🌄 Comunidad de Caminantes\n(Jefe de Comunidad)\n15–17 años"]
        CLA["🏕️ Clan de Rovers\n(Consejero Responsable)\n18–21 años"]
    end

    %% Relaciones jerárquicas
    CEP -->|"supervisa y sanciona"| CG
    AG -->|"informa a"| CG
    CG -->|"preside"| JG
    CG -->|"integra"| SA
    CG -->|"integra"| SME
    CG -->|"integra"| RJ
    CG -->|"designa"| CE
    CG -->|"supervisa"| SECCIONES

    COM -->|"responde ante"| CG
    COM -->|"integra"| JG
    COM -->|"integra"| SA
    COM -->|"integra"| SME
    COM -->|"integra"| COL

    JG -->|"coordina"| MAN
    JG -->|"coordina"| TRO
    JG -->|"coordina"| COM2
    JG -->|"coordina"| CLA
```

---

## 2. Funcionamiento del Grupo Scout

```mermaid
flowchart TD
    START(["🔔 Inicio del ciclo mensual"])

    %% Secciones reportan
    S1["📄 Jefes de Sección elaboran\nInforme de Sección\n(7 días antes del Consejo)"]

    %% Comité prepara
    S2["📋 Comité de Grupo sesiona\n(reunión previa al Consejo)\n• Plan de trabajo\n• Informe financiero\n• Membresía y progresión"]

    %% Consejo de Grupo
    S3{"⚖️ Consejo de Grupo sesiona\n(mínimo 1 vez/mes)\n¿Quórum > 50%?"}
    S3NO["⚠️ Convocar nueva sesión\nen los 8 días siguientes"]
    S3SI["✅ Sesión válida"]

    %% Temas del Consejo
    S4["📌 Temas del Consejo:\n• Revisar informes de sección\n• Avance del Plan de Trabajo\n• Finanzas del grupo\n• Aprobación de actividades\n• Reconocimientos y progresiones\n• Acuerdos y actas"]

    %% Flujo de decisiones
    DEC{"🗳️ Votación por mayoría\nde presentes"}
    ACU["📝 Acuerdos asentados\nen acta"]

    %% Reporte a Provincia
    REP["📤 Jefe de Grupo envía\na Vicepresidencia Administrativa:\n• Acta de sesión\n• Informe de Grupo\n(máx. 8 días después del Consejo)"]

    %% Evaluación anual
    SEP{"📅 ¿Es septiembre?"}
    EVAL["📊 Evaluación de desempeño\ndel Jefe de Grupo\n(9 criterios, mínimo 6 cumplidos\nincl. criterios 1–3 obligatorios)"]

    %% Asamblea anual
    Q4{"📅 ¿Último trimestre?"}
    ASM["👨‍👩‍👧 Asamblea Informativa de Grupo\n(1 vez/año, convocada con\n15 días de anticipación)\n• Padres y tutores\n• Miembros mayores de 18 años\n• Patrono / patrocinador"]

    END(["🔄 Nuevo ciclo mensual"])

    %% Flujo principal
    START --> S1
    S1 --> S2
    S2 --> S3
    S3 -->|No| S3NO
    S3NO --> S3
    S3 -->|Sí| S3SI
    S3SI --> S4
    S4 --> DEC
    DEC --> ACU
    ACU --> REP
    REP --> SEP

    SEP -->|Sí| EVAL
    SEP -->|No| Q4
    EVAL --> Q4

    Q4 -->|Sí| ASM
    Q4 -->|No| END
    ASM --> END
```

---

### Notas clave

| Órgano | Autoridad | Sesiones |
|---|---|---|
| **Consejo de Grupo** | Máxima del grupo | Mínimo 1/mes |
| **Comité de Grupo** | Administrativa (responde ante el Consejo) | Mínimo 1/mes |
| **Asamblea de Grupo** | Informativa (sin voto en decisiones del grupo) | Mínimo 1/año |
| **Comités Especiales** | Temporal, designada por el Consejo | Según necesidad (máx. 1 año) |

**Jerarquía de decisiones:** Comisión Ejecutiva de Provincia → Consejo de Grupo → Comité de Grupo → Secciones
