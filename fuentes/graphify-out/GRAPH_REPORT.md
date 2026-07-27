# Graph Report - C:\Users\user21\Documents\formatos-scouts\libros  (2026-07-27)

## Corpus Check
- Large corpus: 37 files · ~690,797 words. Semantic extraction will be expensive (many Claude tokens). Consider running on a subfolder.

## Summary
- 98 nodes · 229 edges · 9 communities
- Extraction: 91% EXTRACTED · 9% INFERRED · 0% AMBIGUOUS · INFERRED: 21 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Gestión y Políticas de Adultos
- Secciones Scouts y Liderazgo Juvenil
- Formación y Capacitación de Adultos
- Insignias Mundiales y ODS
- Estructura Organizacional ASMAC
- Método Scout y Principios
- Sostenibilidad y Medio Ambiente
- Chat Scouts App (Python)
- Carnets Aventuras en la Naturaleza

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
- `Guía Nacional para la Obtención de la Insignia Mensajeros de la Paz` --semantically_similar_to--> `Guía Nacional para la Obtención de la Insignia Reconocimiento Scouts del Mundo`  [INFERRED] [semantically similar]
  md/05 Guía Insignia Mensajeros de la Paz.md → md/07 Guía Insignia Reconocimiento Scouts del Mundo.md
- `Guía Nacional para la Obtención de la Insignia Mensajeros de la Paz` --semantically_similar_to--> `Guía Nacional para la Obtención de la Insignia Scouts Go Solar`  [INFERRED] [semantically similar]
  md/05 Guía Insignia Mensajeros de la Paz.md → md/08 Guia Insignia Go Solar.md
- `Guía Nacional para la Obtención de la Insignia Mensajeros de la Paz` --semantically_similar_to--> `Guía Champions For Nature México`  [INFERRED] [semantically similar]
  md/05 Guía Insignia Mensajeros de la Paz.md → md/Guia Champions for nature.md
- `Carnet de Aventuras en la Naturaleza para Caminantes 2024` --semantically_similar_to--> `Carnet de Aventuras en la Naturaleza para Lobatos y Lobeznas 2024`  [INFERRED] [semantically similar]
  md/Carnet Aventuras en la Naturaleza para Comunidad 2024.md → md/Carnet Aventuras en la Naturaleza para Manada 2024.md
- `Carnet de Aventuras en la Naturaleza para Caminantes 2024` --semantically_similar_to--> `Carnet de Aventuras en la Naturaleza para Rovers 2024`  [INFERRED] [semantically similar]
  md/Carnet Aventuras en la Naturaleza para Comunidad 2024.md → md/Carnet Aventuras en la Naturaleza para Rovers 2024.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Insignias y Reconocimientos Mundiales del Programa de Jóvenes** — md_05_guia_insignia_mensajeros_de_la_paz, md_07_guia_insignia_reconocimiento_scouts_del_mundo, md_08_guia_insignia_go_solar, md_guia_champions_for_nature, concept_insignia_mensajeros_de_la_paz, concept_reconocimiento_scouts_del_mundo, concept_insignia_go_solar, concept_champions_for_nature [INFERRED 0.95]
- **Secciones del Programa de Jóvenes ASMAC** — concept_manada_de_lobatos, concept_tropa_de_scouts, concept_comunidad_de_caminantes, concept_clan_de_rovers, concept_programa_de_jovenes [EXTRACTED 1.00]
- **Colección Carnets Aventuras en la Naturaleza 2024 (todas las secciones)** — md_carnet_aventuras_en_la_naturaleza_para_manada_2024, md_carnet_aventuras_en_la_naturaleza_para_tropa_2024, md_carnet_aventuras_en_la_naturaleza_para_comunidad_2024, md_carnet_aventuras_en_la_naturaleza_para_rovers_2024, concept_aventuras_en_la_naturaleza [INFERRED 0.95]
- **Colección Guías de Scouter por Sección 2024** — md_guia_de_scouter_de_manada_de_lobatos_2024, md_guia_de_scouter_de_comunidad_2024, md_guia_de_scouter_de_clan_de_rovers_2024, concept_metodo_scout [INFERRED 0.95]
- **Progresión de Formación de Adultos Voluntarios** — concept_curso_induccion, concept_insignia_de_madera, concept_ttt1, concept_ttt2, concept_formacion_basica, concept_comision_nacional_de_formacion [EXTRACTED 1.00]
- **Estructura Organizacional ASMAC (Nacional - Provincia - Grupo)** — concept_direccion_ejecutiva_nacional, concept_provincia_scout, concept_grupo_scout, concept_asmac [EXTRACTED 1.00]
- **Cuatro Secciones del Programa de Jovenes ASMAC** — concept_manada_de_lobatos, concept_tropa_de_scouts, concept_comunidad_de_caminantes, concept_clan_de_rovers [EXTRACTED 1.00]
- **Punta de Flecha aplicado en las tres secciones mayores** — md_guia_punta_de_flecha_2025_ts, md_guia_punta_de_flecha_2025_comunidad, md_guia_punta_de_flecha_2025_clan, concept_punta_de_flecha [EXTRACTED 1.00]
- **Iniciativas del Marco Mundo Mejor** — concept_tribu_de_la_tierra, concept_plastic_tide_turners, concept_mundo_mejor, concept_agenda_2030_ods [EXTRACTED 1.00]
- **Marco documental de Adultos en el Movimiento Scout** — md_politica_nacional_ams_2024, md_modelo_de_gestion_de_adultos_2025_b, md_modelo_de_actualizacion_continua_para_adultos, concept_adultos_en_el_movimiento_scout [INFERRED 0.95]
- **Politicas Nacionales ASMAC** — md_politica_nacional_ams_2024, md_politica_nacional_programa_de_jovenes_2025, md_pn_nineces_adolescencias_y_juventudes, concept_asmac [INFERRED 0.95]
- **Materiales Educativos para Tropa de Scouts** — md_guia_de_scouter_de_tropa_de_scouts_2024, md_pistas_de_la_aventura_2024, md_guia_punta_de_flecha_2025_ts, concept_tropa_de_scouts [INFERRED 0.95]

## Communities (9 total, 0 thin omitted)

### Community 0 - "Gestión y Políticas de Adultos"
Cohesion: 0.24
Nodes (14): Adultos en el Movimiento Scout (AMS), Asociación de Scouts de México, A.C. (ASMAC), Ciclo de Vida del Adulto en el Movimiento Scout, Comunidad Digital de Conocimiento (CDC) - ASMAC, Insignia de Madera - Formacion de Dirigentes, NNAJ - Ninos Ninas Adolescentes y Jovenes, Proyecto Educativo ASMAC 2020-2030 Orientado a la Sustentabilidad, Organizacion Mundial del Movimiento Scout (OMMS/WOSM) (+6 more)

### Community 1 - "Secciones Scouts y Liderazgo Juvenil"
Cohesion: 0.40
Nodes (14): Robert Baden-Powell - Fundador del Escultismo, Clan de Rovers (18-21 años), Comunidad de Caminantes (14-18 años), Participacion Juvenil Scout, Proyecto Personal de Vida (PPV) - Clan de Rovers, Curso de Liderazgo Juvenil Punta de Flecha, Safe from Harm (A Salvo del Peligro), Tropa de Scouts (10-14 años) (+6 more)

### Community 2 - "Formación y Capacitación de Adultos"
Cohesion: 0.27
Nodes (13): Captación y Selección de Adultos Voluntarios, Clave de Autorización de Curso (CLAC), Comisión Nacional de Formación (CNF), Curso de Inducción al Escultismo, Formación Básica (Inducción + CIM), Formación de Adultos en el Movimiento Scout, Curso Insignia de Madera (CIM), Curso TTT1 (Formación de Formadores Nivel 1) (+5 more)

### Community 3 - "Insignias Mundiales y ODS"
Cohesion: 0.26
Nodes (13): Champions For Nature / Tribu de la Tierra, Cultura de Paz, Insignia Scouts Go Solar, Insignia Mensajeros de la Paz, Objetivos de Desarrollo Sostenible (ODS / Agenda 2030), Organización Mundial del Movimiento Scout (OMMS), Reconocimiento Scouts del Mundo (RSDM), WWF (World Wide Fund for Nature) (+5 more)

### Community 4 - "Estructura Organizacional ASMAC"
Cohesion: 0.22
Nodes (13): Comisión Ejecutiva de Provincia, Comité de Grupo, Consejo de Grupo, Consejo de Provincia, Dirección Ejecutiva Nacional (DEN), Grupo Scout, Jefe de Grupo, Presidente de Provincia (+5 more)

### Community 5 - "Método Scout y Principios"
Cohesion: 0.40
Nodes (10): Ley Scout y Promesa Scout, Manada de Lobatos y Lobeznas (6-10 años), Método Scout, Programa de Jóvenes, Proyecto Educativo ASMAC 2020-2030 orientado a la Sustentabilidad, Código de Ética de la Asociación de Scouts de México, Declaración de Principios de la Asociación de Scouts de México 2020, Guía de Aplicación del Método Scout en Jóvenes de 18 a 21 años (Clan de Rovers) 2024 (+2 more)

### Community 6 - "Sostenibilidad y Medio Ambiente"
Cohesion: 0.44
Nodes (9): Agenda 2030 - Objetivos de Desarrollo Sostenible, Marco Mundo Mejor - Iniciativas Scouts Globales, Plastic Tide Turners - Desafio Ambiental Scout, Programa de las Naciones Unidas para el Medio Ambiente (PNUMA/UNEP), Tribu de la Tierra - Iniciativa Ambiental Scout, Guia para la implementacion de la iniciativa Tribu de la Tierra 2021, Manual Plastic Tide Turners Mexico, Mis Rastros en la Selva 2024 - Manada de Lobatos y Lobeznas (+1 more)

### Community 7 - "Chat Scouts App (Python)"
Cohesion: 0.33
Nodes (4): chat(), Chat con los documentos del Clan de Rovers — compatible con Gradio 6 Responde pr, Historial en formato Gradio: lista de tuplas (user, assistant)., responder()

### Community 8 - "Carnets Aventuras en la Naturaleza"
Cohesion: 0.70
Nodes (5): Aventuras en la Naturaleza (programa de vida al aire libre), Carnet de Aventuras en la Naturaleza para Caminantes 2024, Carnet de Aventuras en la Naturaleza para Lobatos y Lobeznas 2024, Carnet de Aventuras en la Naturaleza para Rovers 2024, Carnet de Aventuras en la Naturaleza para Scouts 2024

## Knowledge Gaps
- **14 isolated node(s):** `Formación de Adultos en el Movimiento Scout`, `Clave de Autorización de Curso (CLAC)`, `Comisión Nacional de Formación (CNF)`, `Dirección Ejecutiva Nacional (DEN)`, `Presidente de Provincia` (+9 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Programa de Jóvenes` connect `Método Scout y Principios` to `Gestión y Políticas de Adultos`, `Secciones Scouts y Liderazgo Juvenil`, `Formación y Capacitación de Adultos`, `Insignias Mundiales y ODS`, `Estructura Organizacional ASMAC`?**
  _High betweenness centrality (0.159) - this node is a cross-community bridge._
- **Why does `Asociación de Scouts de México, A.C. (ASMAC)` connect `Gestión y Políticas de Adultos` to `Secciones Scouts y Liderazgo Juvenil`, `Formación y Capacitación de Adultos`, `Insignias Mundiales y ODS`, `Estructura Organizacional ASMAC`, `Método Scout y Principios`?**
  _High betweenness centrality (0.146) - this node is a cross-community bridge._
- **Why does `Manual de Operación Nivel Provincia` connect `Estructura Organizacional ASMAC` to `Gestión y Políticas de Adultos`, `Formación y Capacitación de Adultos`, `Método Scout y Principios`?**
  _High betweenness centrality (0.141) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Declaración de Principios de la Asociación de Scouts de México 2020` (e.g. with `Código de Ética de la Asociación de Scouts de México` and `Guía de Aplicación del Método Scout en Jóvenes de 18 a 21 años (Clan de Rovers) 2024`) actually correct?**
  _`Declaración de Principios de la Asociación de Scouts de México 2020` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `Guia de Scouter de Tropa de Scouts 2024` (e.g. with `Guia Punta de Flecha 2025 - Tropa de Scouts` and `Pistas de la Aventura 2024 - Tropa Scout`) actually correct?**
  _`Guia de Scouter de Tropa de Scouts 2024` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Formación de Adultos en el Movimiento Scout`, `Clave de Autorización de Curso (CLAC)`, `Comisión Nacional de Formación (CNF)` to the rest of the system?**
  _14 weakly-connected nodes found - possible documentation gaps or missing edges._