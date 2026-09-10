# Graph Report - C:/Users/user21/Documents/formatos-scouts/libros  (2026-09-10)

## Corpus Check
- Large corpus: 45 files · ~786,774 words. Semantic extraction will be expensive (many Claude tokens). Consider running on a subfolder.

## Summary
- 138 nodes · 274 edges · 12 communities (9 shown, 3 thin omitted)
- Extraction: 90% EXTRACTED · 10% INFERRED · 0% AMBIGUOUS · INFERRED: 27 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Principios y Adultos Scout
- Proyectos y Actividades Educativas
- Ramas y Progresion Juvenil
- Formacion de Adultos
- Iniciativas Mundiales y Sostenibilidad
- Estructura Organizacional ASMAC
- Chatbot ASMAC (Codigo)
- Medio Ambiente y Mundo Mejor
- Avatar AvatarMaker
- Avatar D-ID JPEG
- Ilustracion Popeye JPG
- Ilustracion Popeye PNG

## God Nodes (most connected - your core abstractions)
1. `Programa de Jóvenes` - 13 edges
2. `Método Scout` - 13 edges
3. `Declaración de Principios de la Asociación de Scouts de México 2020` - 12 edges
4. `Guia de Scouter de Tropa de Scouts 2024` - 12 edges
5. `Manual de Operación Nivel Provincia` - 11 edges
6. `Manual de Operación Nivel Grupo 2018` - 11 edges
7. `Políticas y Procedimientos de la Comisión Nacional de Formación` - 10 edges
8. `Comunidad de Caminantes (14-18 años)` - 10 edges
9. `Clan de Rovers (18-21 años)` - 10 edges
10. `Guia Punta de Flecha 2025 - Tropa de Scouts` - 10 edges

## Surprising Connections (you probably didn't know these)
- `Comunidad de Caminantes (14-18 años)` --covered_by--> `Guías de Scouter por Rama (Manada, Tropa, Comunidad, Clan)`  [INFERRED]
  md/ProyectosActividades.md → README.md
- `Comunidad Rover / Clan de Rovers (18-21 años)` --covered_by--> `Guías de Scouter por Rama (Manada, Tropa, Comunidad, Clan)`  [INFERRED]
  md/ProyectosActividades.md → README.md
- `Guía Nacional para la Obtención de la Insignia Mensajeros de la Paz` --semantically_similar_to--> `Guía Nacional para la Obtención de la Insignia Reconocimiento Scouts del Mundo`  [INFERRED] [semantically similar]
  md/05 Guía Insignia Mensajeros de la Paz.md → md/07 Guía Insignia Reconocimiento Scouts del Mundo.md
- `Guía Nacional para la Obtención de la Insignia Mensajeros de la Paz` --semantically_similar_to--> `Guía Nacional para la Obtención de la Insignia Scouts Go Solar`  [INFERRED] [semantically similar]
  md/05 Guía Insignia Mensajeros de la Paz.md → md/08 Guia Insignia Go Solar.md
- `Guía Nacional para la Obtención de la Insignia Mensajeros de la Paz` --semantically_similar_to--> `Guía Champions For Nature México`  [INFERRED] [semantically similar]
  md/05 Guía Insignia Mensajeros de la Paz.md → md/Guia Champions for nature.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
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

## Communities (12 total, 3 thin omitted)

### Community 0 - "Principios y Adultos Scout"
Cohesion: 0.17
Nodes (26): Adultos en el Movimiento Scout (AMS), Asociación de Scouts de México, A.C. (ASMAC), Robert Baden-Powell - Fundador del Escultismo, Ciclo de Vida del Adulto en el Movimiento Scout, Comunidad Digital de Conocimiento (CDC) - ASMAC, Insignia de Madera - Formacion de Dirigentes, Ley Scout y Promesa Scout, Manada de Lobatos y Lobeznas (6-10 años) (+18 more)

### Community 1 - "Proyectos y Actividades Educativas"
Cohesion: 0.10
Nodes (25): Actividades Centrales y Conexas de Proyectos Scout, Actividades Educativas (Radioteatro, Safari Fotográfico, Debate Político, etc.), Proyectos y Actividades Educativas para Jóvenes de 15 a 21 Años (REME/OMMS), Comunidad de Caminantes (14-18 años), Comunidad Rover / Clan de Rovers (18-21 años), Proyecto: Excursión en Bicicleta, Oportunidades de Aprendizaje y Desarrollo de Competencias Scout, Otros Proyectos Scout (Parque Recreativo, Sendero Ecológico, Programa de Radio, etc.) (+17 more)

### Community 2 - "Ramas y Progresion Juvenil"
Cohesion: 0.29
Nodes (17): Aventuras en la Naturaleza (programa de vida al aire libre), Clan de Rovers (18-21 años), Comunidad de Caminantes (14-18 años), Participacion Juvenil Scout, Proyecto Personal de Vida (PPV) - Clan de Rovers, Curso de Liderazgo Juvenil Punta de Flecha, Safe from Harm (A Salvo del Peligro), Tropa de Scouts (10-14 años) (+9 more)

### Community 3 - "Formacion de Adultos"
Cohesion: 0.27
Nodes (13): Captación y Selección de Adultos Voluntarios, Clave de Autorización de Curso (CLAC), Comisión Nacional de Formación (CNF), Curso de Inducción al Escultismo, Formación Básica (Inducción + CIM), Formación de Adultos en el Movimiento Scout, Curso Insignia de Madera (CIM), Curso TTT1 (Formación de Formadores Nivel 1) (+5 more)

### Community 4 - "Iniciativas Mundiales y Sostenibilidad"
Cohesion: 0.26
Nodes (13): Champions For Nature / Tribu de la Tierra, Cultura de Paz, Insignia Scouts Go Solar, Insignia Mensajeros de la Paz, Objetivos de Desarrollo Sostenible (ODS / Agenda 2030), Organización Mundial del Movimiento Scout (OMMS), Reconocimiento Scouts del Mundo (RSDM), WWF (World Wide Fund for Nature) (+5 more)

### Community 5 - "Estructura Organizacional ASMAC"
Cohesion: 0.22
Nodes (13): Comisión Ejecutiva de Provincia, Comité de Grupo, Consejo de Grupo, Consejo de Provincia, Dirección Ejecutiva Nacional (DEN), Grupo Scout, Jefe de Grupo, Presidente de Provincia (+5 more)

### Community 6 - "Chatbot ASMAC (Codigo)"
Cohesion: 0.26
Nodes (8): chat(), _env(), _generar_video_hablante(), _llamar_llm(), Chat con documentos ASMAC — multi-backend LLM_BACKEND: claude | openai | gemini, Retorna los TOP_K documentos más relevantes para la consulta., responder(), _seleccionar_docs()

### Community 7 - "Medio Ambiente y Mundo Mejor"
Cohesion: 0.44
Nodes (9): Agenda 2030 - Objetivos de Desarrollo Sostenible, Marco Mundo Mejor - Iniciativas Scouts Globales, Plastic Tide Turners - Desafio Ambiental Scout, Programa de las Naciones Unidas para el Medio Ambiente (PNUMA/UNEP), Tribu de la Tierra - Iniciativa Ambiental Scout, Guia para la implementacion de la iniciativa Tribu de la Tierra 2021, Manual Plastic Tide Turners Mexico, Mis Rastros en la Selva 2024 - Manada de Lobatos y Lobeznas (+1 more)

### Community 8 - "Avatar AvatarMaker"
Cohesion: 0.50
Nodes (4): AvatarMaker Avatar Image, Scout Educational Material Avatar Asset, Illustrated Female Character, Flat Vector Illustration Style

## Knowledge Gaps
- **35 isolated node(s):** `Dirección Ejecutiva Nacional (DEN)`, `Presidente de Provincia`, `Vicepresidente Administrativo de Provincia`, `Vicepresidente de Métodos Educativos de Provincia`, `Formación de Adultos en el Movimiento Scout` (+30 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **3 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Programa de Jóvenes` connect `Principios y Adultos Scout` to `Formacion de Adultos`, `Iniciativas Mundiales y Sostenibilidad`, `Estructura Organizacional ASMAC`?**
  _High betweenness centrality (0.079) - this node is a cross-community bridge._
- **Why does `Asociación de Scouts de México, A.C. (ASMAC)` connect `Principios y Adultos Scout` to `Formacion de Adultos`, `Iniciativas Mundiales y Sostenibilidad`, `Estructura Organizacional ASMAC`?**
  _High betweenness centrality (0.073) - this node is a cross-community bridge._
- **Why does `Manual de Operación Nivel Provincia` connect `Estructura Organizacional ASMAC` to `Principios y Adultos Scout`, `Formacion de Adultos`?**
  _High betweenness centrality (0.071) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Declaración de Principios de la Asociación de Scouts de México 2020` (e.g. with `Código de Ética de la Asociación de Scouts de México` and `Guía de Aplicación del Método Scout en Jóvenes de 18 a 21 años (Clan de Rovers) 2024`) actually correct?**
  _`Declaración de Principios de la Asociación de Scouts de México 2020` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `Guia de Scouter de Tropa de Scouts 2024` (e.g. with `Guia Punta de Flecha 2025 - Tropa de Scouts` and `Pistas de la Aventura 2024 - Tropa Scout`) actually correct?**
  _`Guia de Scouter de Tropa de Scouts 2024` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Dirección Ejecutiva Nacional (DEN)`, `Presidente de Provincia`, `Vicepresidente Administrativo de Provincia` to the rest of the system?**
  _35 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Proyectos y Actividades Educativas` be split into smaller, more focused modules?**
  _Cohesion score 0.09666666666666666 - nodes in this community are weakly interconnected._