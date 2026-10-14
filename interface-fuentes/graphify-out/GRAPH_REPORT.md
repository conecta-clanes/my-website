# Graph Report - .  (2026-10-14)

## Corpus Check
- Large corpus: 59 files · ~911,087 words. Semantic extraction will be expensive (many Claude tokens). Consider running on a subfolder.

## Summary
- 208 nodes · 368 edges · 23 communities (14 shown, 9 thin omitted)
- Extraction: 89% EXTRACTED · 10% INFERRED · 0% AMBIGUOUS · INFERRED: 38 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Marco Simbólico Rover
- Actividades y Proyectos
- Misión Scout y Uniforme
- Formación y Secciones
- Liderazgo del Clan
- Formación de Adultos
- Programas Mundiales
- Estructura Institucional
- Chatbot Scout IA
- Conversión PDF
- Aventuras en la Naturaleza
- Recursos Visuales
- Extracción de PDFs
- Avatar Popeye JPEG
- Personaje Popeye JPG
- Ilustración Popeye PNG
- Asociado Rover
- Bandera del Clan
- COP y CEP
- Foros Nacionales
- Individuo Asociado
- Insignia ASMAC
- Community 22

## God Nodes (most connected - your core abstractions)
1. `Clan de Rovers` - 18 edges
2. `Manual del Uniforme ASMAC 2026 (Markdown)` - 15 edges
3. `Programa de Jóvenes` - 13 edges
4. `Método Scout` - 13 edges
5. `Declaración de Principios de la Asociación de Scouts de México 2020` - 12 edges
6. `Guia de Scouter de Tropa de Scouts 2024` - 12 edges
7. `Estructura del Clan de Rovers (diagrama v1)` - 11 edges
8. `Marco Simbólico del Clan de Rovers` - 11 edges
9. `Manual de Operación Nivel Provincia` - 11 edges
10. `Manual de Operación Nivel Grupo 2018` - 11 edges

## Surprising Connections (you probably didn't know these)
- `Playwright MCP Session` --conceptually_related_to--> `Gradio Application Session`  [AMBIGUOUS]
  .playwright-mcp/page-2026-10-05T17-47-32-385Z.yml → gradio_out.txt
- `Consejo de Grupo` --references--> `Comité de Grupo`  [EXTRACTED]
  .playwright-mcp/page-2026-10-05T17-49-43-466Z.yml → md/02 Manual de Operación Nivel Grupo 2018.md
- `Anexo 8 - Procedimiento de Captación y Selección de Adultos` --references--> `Consejo de Grupo`  [EXTRACTED]
  md/Anexo 8 Captación y Selección de Adultos.md → .playwright-mcp/page-2026-10-05T17-49-43-466Z.yml
- `Punta de Flecha (curso de liderazgo)` --references--> `Clan de Rovers`  [EXTRACTED]
  .playwright-mcp/page-2026-10-13T17-38-38-662Z.yml → md/01 Manual del Uniforme Actualizado Junio 2026.md
- `Transferencia de Liderazgo Adulto-Juvenil` --rationale_for--> `Clan de Rovers`  [EXTRACTED]
  .playwright-mcp/page-2026-10-13T21-54-09-422Z.yml → md/01 Manual del Uniforme Actualizado Junio 2026.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Gobierno del Clan: Parlamento + Promotor + CRR** — concept_parlamento_rover, concept_promotor_rover, concept_consejero_rover_responsable, concept_consejeros_rover [EXTRACTED 0.95]
- **Ciclo de Vida Rover: Inducción → Compromiso → Vida en Clan → Partida** — concept_periodo_induccion, concept_compromiso_rover, concept_ppv, concept_partida_rover [EXTRACTED 0.95]
- **Progresión Personal Rover: Rutas + Especialidades + Aventuras + Insignias Terminales** — concept_rutas_progresion_rover, concept_especialidades_rover, concept_aventuras_naturaleza_rover, concept_insignias_terminales_rover [EXTRACTED 0.95]
- **Estructura Organizacional ASMAC (Nacional - Provincia - Grupo)** — concept_direccion_ejecutiva_nacional, concept_provincia_scout, concept_grupo_scout, concept_asmac [EXTRACTED 1.00]
- **Progresión de Formación de Adultos Voluntarios** — concept_curso_induccion, concept_insignia_de_madera, concept_ttt1, concept_ttt2, concept_formacion_basica, concept_comision_nacional_de_formacion [EXTRACTED 1.00]
- **Secciones del Programa de Jóvenes ASMAC** — concept_manada_de_lobatos, concept_tropa_de_scouts, concept_comunidad_de_caminantes, concept_clan_de_rovers, concept_programa_de_jovenes [EXTRACTED 1.00]
- **Colección Carnets Aventuras en la Naturaleza 2024 (todas las secciones)** — md_carnet_aventuras_en_la_naturaleza_para_manada_2024, md_carnet_aventuras_en_la_naturaleza_para_tropa_2024, md_carnet_aventuras_en_la_naturaleza_para_comunidad_2024, md_carnet_aventuras_en_la_naturaleza_para_rovers_2024, concept_aventuras_en_la_naturaleza [INFERRED 0.95]
- **Insignias y Reconocimientos Mundiales del Programa de Jóvenes** — md_05_guia_insignia_mensajeros_de_la_paz, md_07_guia_insignia_reconocimiento_scouts_del_mundo, md_08_guia_insignia_go_solar, md_guia_champions_for_nature, concept_insignia_mensajeros_de_la_paz, concept_reconocimiento_scouts_del_mundo, concept_insignia_go_solar, concept_champions_for_nature [INFERRED 0.95]
- **Colección Guías de Scouter por Sección 2024** — md_guia_de_scouter_de_manada_de_lobatos_2024, md_guia_de_scouter_de_comunidad_2024, md_guia_de_scouter_de_clan_de_rovers_2024, concept_metodo_scout [INFERRED 0.95]
- **Cuatro Secciones del Programa de Jovenes ASMAC** — concept_manada_de_lobatos, concept_tropa_de_scouts, concept_comunidad_de_caminantes, concept_clan_de_rovers [EXTRACTED 1.00]
- **Materiales Educativos para Tropa de Scouts** — md_guia_de_scouter_de_tropa_de_scouts_2024, md_pistas_de_la_aventura_2024, md_guia_punta_de_flecha_2025_ts, concept_tropa_de_scouts [INFERRED 0.95]
- **Punta de Flecha aplicado en las tres secciones mayores** — md_guia_punta_de_flecha_2025_ts, md_guia_punta_de_flecha_2025_comunidad, md_guia_punta_de_flecha_2025_clan, concept_punta_de_flecha [EXTRACTED 1.00]
- **Iniciativas del Marco Mundo Mejor** — concept_tribu_de_la_tierra, concept_plastic_tide_turners, concept_mundo_mejor, concept_agenda_2030_ods [EXTRACTED 1.00]
- **Marco documental de Adultos en el Movimiento Scout** — md_politica_nacional_ams_2024, md_modelo_de_gestion_de_adultos_2025_b, md_modelo_de_actualizacion_continua_para_adultos, concept_adultos_en_el_movimiento_scout [INFERRED 0.95]
- **Politicas Nacionales ASMAC** — md_politica_nacional_ams_2024, md_politica_nacional_programa_de_jovenes_2025, md_pn_nineces_adolescencias_y_juventudes, concept_asmac [INFERRED 0.95]

## Communities (23 total, 9 thin omitted)

### Community 0 - "Marco Simbólico Rover"
Cohesion: 0.21
Nodes (26): Agenda 2030 - Objetivos de Desarrollo Sostenible, Robert Baden-Powell - Fundador del Escultismo, Comunidad de Caminantes (14-18 años), Marco Mundo Mejor - Iniciativas Scouts Globales, NNAJ - Ninos Ninas Adolescentes y Jovenes, Participacion Juvenil Scout, Plastic Tide Turners - Desafio Ambiental Scout, Programa de las Naciones Unidas para el Medio Ambiente (PNUMA/UNEP) (+18 more)

### Community 1 - "Actividades y Proyectos"
Cohesion: 0.11
Nodes (26): Aventuras en la Naturaleza — Rover (Art. 61), Cintas de Liderazgo Clan de Rovers (Art. 58), Compromiso Rover (ceremonia), Comunidad de Caminantes (Sección 14-17 años), Distintivo de Viaje Rover (Art. 64), Elementos Físicos del Marco Simbólico, Elementos Intangibles del Marco Simbólico, Escudo de Clan (Art. 64) (+18 more)

### Community 2 - "Misión Scout y Uniforme"
Cohesion: 0.10
Nodes (25): Actividades Centrales y Conexas de Proyectos Scout, Actividades Educativas (Radioteatro, Safari Fotográfico, Debate Político, etc.), Proyectos y Actividades Educativas para Jóvenes de 15 a 21 Años (REME/OMMS), Comunidad de Caminantes (14-18 años), Comunidad Rover / Clan de Rovers (18-21 años), Proyecto: Excursión en Bicicleta, Oportunidades de Aprendizaje y Desarrollo de Competencias Scout, Otros Proyectos Scout (Parque Recreativo, Sendero Ecológico, Programa de Radio, etc.) (+17 more)

### Community 3 - "Formación y Secciones"
Cohesion: 0.16
Nodes (24): Champions For Nature / Tribu de la Tierra, Cultura de Paz, Insignia Scouts Go Solar, Insignia Mensajeros de la Paz, Ley Scout y Promesa Scout, Manada de Lobatos y Lobeznas (6-10 años), Método Scout, Objetivos de Desarrollo Sostenible (ODS / Agenda 2030) (+16 more)

### Community 4 - "Liderazgo del Clan"
Cohesion: 0.17
Nodes (20): Camisola Roja — Rovers, Clan de Rovers, Consejero Rover Responsable (CRR), Consejeros Rover (CR), Equipo de Apoyo a Proyecto (EAP), Equipo de Seguimiento (ES), Liderazgo de Proyecto, Liderazgo Formativo (+12 more)

### Community 5 - "Formación de Adultos"
Cohesion: 0.27
Nodes (13): Captación y Selección de Adultos Voluntarios, Clave de Autorización de Curso (CLAC), Comisión Nacional de Formación (CNF), Curso de Inducción al Escultismo, Formación Básica (Inducción + CIM), Formación de Adultos en el Movimiento Scout, Curso Insignia de Madera (CIM), Curso TTT1 (Formación de Formadores Nivel 1) (+5 more)

### Community 6 - "Programas Mundiales"
Cohesion: 0.22
Nodes (13): Comisión Ejecutiva de Provincia, Comité de Grupo, Consejo de Grupo, Consejo de Provincia, Dirección Ejecutiva Nacional (DEN), Grupo Scout, Jefe de Grupo, Presidente de Provincia (+5 more)

### Community 7 - "Estructura Institucional"
Cohesion: 0.26
Nodes (8): chat(), _env(), _generar_video_hablante(), _llamar_llm(), Chat con documentos ASMAC — multi-backend LLM_BACKEND: claude | openai | gemini, Retorna los TOP_K documentos más relevantes para la consulta., responder(), _seleccionar_docs()

### Community 8 - "Chatbot Scout IA"
Cohesion: 0.20
Nodes (8): fs, lines, lines2, md, out, pages, raw, text

### Community 9 - "Conversión PDF"
Cohesion: 0.39
Nodes (8): Adultos en el Movimiento Scout (AMS), Asociación de Scouts de México (ASMAC), Ciclo de Vida del Adulto en el Movimiento Scout, Comunidad Digital de Conocimiento (CDC) - ASMAC, Modelo de Actualizacion Continua para Adultos, Modelo de Gestion de Adultos en el Movimiento Scout 2025, Politica Nacional de Adultos en el Movimiento Scout 2024, Reglamento Asociacion de Scouts de Mexico 2023

### Community 10 - "Aventuras en la Naturaleza"
Cohesion: 0.47
Nodes (6): Playwright MCP Page Snapshot 2026-10-05, Playwright MCP Page Snapshot 2026-10-13, Gradio Application Session, Gradio Error Log, Gradio Output Log, Playwright MCP Session

### Community 11 - "Recursos Visuales"
Cohesion: 0.70
Nodes (5): Aventuras en la Naturaleza (programa de vida al aire libre), Carnet de Aventuras en la Naturaleza para Caminantes 2024, Carnet de Aventuras en la Naturaleza para Lobatos y Lobeznas 2024, Carnet de Aventuras en la Naturaleza para Rovers 2024, Carnet de Aventuras en la Naturaleza para Scouts 2024

### Community 12 - "Extracción de PDFs"
Cohesion: 0.50
Nodes (4): AvatarMaker Avatar Image, Scout Educational Material Avatar Asset, Illustrated Female Character, Flat Vector Illustration Style

### Community 13 - "Avatar Popeye JPEG"
Cohesion: 0.50
Nodes (3): fs, p, PDFParser

## Ambiguous Edges - Review These
- `Playwright MCP Session` → `Gradio Application Session`  [AMBIGUOUS]
  gradio_out.txt · relation: conceptually_related_to

## Knowledge Gaps
- **67 isolated node(s):** `fs`, `raw`, `pages`, `text`, `lines` (+62 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **9 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Playwright MCP Session` and `Gradio Application Session`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `Clan de Rovers` connect `Liderazgo del Clan` to `Marco Simbólico Rover`, `Actividades y Proyectos`, `Formación y Secciones`, `Programas Mundiales`, `Recursos Visuales`?**
  _High betweenness centrality (0.157) - this node is a cross-community bridge._
- **Why does `Manual del Uniforme ASMAC 2026 (Markdown)` connect `Actividades y Proyectos` to `Conversión PDF`, `Liderazgo del Clan`, `Programas Mundiales`?**
  _High betweenness centrality (0.078) - this node is a cross-community bridge._
- **Why does `Asociación de Scouts de México (ASMAC)` connect `Conversión PDF` to `Marco Simbólico Rover`, `Actividades y Proyectos`, `Formación y Secciones`, `Formación de Adultos`, `Programas Mundiales`?**
  _High betweenness centrality (0.072) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Declaración de Principios de la Asociación de Scouts de México 2020` (e.g. with `Código de Ética de la Asociación de Scouts de México` and `Guía de Aplicación del Método Scout en Jóvenes de 18 a 21 años (Clan de Rovers) 2024`) actually correct?**
  _`Declaración de Principios de la Asociación de Scouts de México 2020` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `fs`, `raw`, `pages` to the rest of the system?**
  _67 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Actividades y Proyectos` be split into smaller, more focused modules?**
  _Cohesion score 0.11076923076923077 - nodes in this community are weakly interconnected._