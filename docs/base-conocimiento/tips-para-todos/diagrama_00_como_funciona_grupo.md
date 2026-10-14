# ✏️ Diagrama 0:  Grupo Scout

---

## Introducción

Ésta propuesta no sustituyen la documentación oficial, no nos hacemos responsables del mal uso.

## Tecnologías usadas

- [Claude Code](https://claude.com/product/claude-code) 

## 1. Estructura Organizacional del Grupo Scout

```mermaid
graph TD
    %% Nivel externo superior
    CEP["🏛️ Comisión Ejecutiva de Provincia"]

    %% Órganos del Grupo
    AG["📢 Asamblea de Grupo<BR>(órgano informativo anual)"]
    CG["⚖️ Consejo de Grupo<BR>(máximo órgano de decisión)"]
    COM["📋 Comité de Grupo<BR>(administración y gestión)"]
    CE["🔧 Comités Especiales<BR>(temporales, máx. 3 simultáneos)"]

    %% Jefatura
    JG["👤 Jefe de Grupo<BR>(preside Consejo y Comité)"]
    SA["👤 Subjefe Administrativo<BR>(tesorería y secretaría)"]
    SME["👤 Subjefe de Métodos<BR>Educativos"]
    RJ["👥 Representantes Juveniles<BR>(2, del Clan, mayores de edad)"]
    COL["👥 Colaboradores de Grupo"]

    %% Secciones
    subgraph SECCIONES["SECCIONES (Programa de Jóvenes)"]
        MAN["🐺 Manada de Lobatos<BR>(Jefe de Manada)<BR>6–10 años"]
        TRO["⚜️ Tropa de Scouts<BR>(Jefe de Tropa)<BR>11–14 años"]
        COM2["🌄 Comunidad de Caminantes<BR>(Jefe de Comunidad)<BR>15–17 años"]
        CLA["🏕️ Clan de Rovers<BR>(Consejero Responsable)<BR>18–21 años"]
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
    S1["📄 Jefes de Sección elaboran<BR>Informe de Sección<BR>(7 días antes del Consejo)"]

    %% Comité prepara
    S2["📋 Comité de Grupo sesiona<BR>(reunión previa al Consejo)<BR>• Plan de trabajo<BR>• Informe financiero<BR>• Membresía y progresión"]

    %% Consejo de Grupo
    S3{"⚖️ Consejo de Grupo sesiona<BR>(mínimo 1 vez/mes)<BR>¿Quórum > 50%?"}
    S3NO["⚠️ Convocar nueva sesión<BR>en los 8 días siguientes"]
    S3SI["✅ Sesión válida"]

    %% Temas del Consejo
    S4["📌 Temas del Consejo:<BR>• Revisar informes de sección<BR>• Avance del Plan de Trabajo<BR>• Finanzas del grupo<BR>• Aprobación de actividades<BR>• Reconocimientos y progresiones<BR>• Acuerdos y actas"]

    %% Flujo de decisiones
    DEC{"🗳️ Votación por mayoría<BR>de presentes"}
    ACU["📝 Acuerdos asentados<BR>en acta"]

    %% Reporte a Provincia
    REP["📤 Jefe de Grupo envía<BR>a Vicepresidencia Administrativa:<BR>• Acta de sesión<BR>• Informe de Grupo<BR>(máx. 8 días después del Consejo)"]

    %% Evaluación anual
    SEP{"📅 ¿Es septiembre?"}
    EVAL["📊 Evaluación de desempeño<BR>del Jefe de Grupo<BR>(9 criterios, mínimo 6 cumplidos<BR>incl. criterios 1–3 obligatorios)"]

    %% Asamblea anual
    Q4{"📅 ¿Último trimestre?"}
    ASM["👨‍👩‍👧 Asamblea Informativa de Grupo<BR>(1 vez/año, convocada con<BR>15 días de anticipación)<BR>• Padres y tutores<BR>• Miembros mayores de 18 años<BR>• Patrono / patrocinador"]

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

##### Autora

- Yolanda Castillo
