# Manejo de conflictos, problema o inquietud que no es de vida o muerte

Ésta es un propuesta sobre de como manejar algún conflicto, problema o inquitud de un Rover


```mermaid
stateDiagram-v2
    state "Un Rover tiene una inquitud" as s0
    state "Expresarlo en el Parlamento" as s1

    state "El tema se da por cerrado" as tc

    state "Buscar directamente a los consejeros" as bdc
    state "Pedir que se asiente en el actua del parlamento" as pap

    state "Buscar a los representantes juveniles" as rj

    state "Buscar al consejo de grupo" as cg

    state "Buscar instancias superiores" as is
    
    state es_tercera_vez <<choice>>    
    state expresarlo_parlamento <<choice>>

    state buscar_representantes_juveniles <<choice>>

    state tema_resuelto <<choice>>

    state tema_resueltoIS <<choice>>
    
    [*] --> s0
    s0 --> s1
    s1 --> expresarlo_parlamento
    expresarlo_parlamento --> es_tercera_vez : no se resolvió
    expresarlo_parlamento --> tc : se resolvió
    tc --> [*]
    es_tercera_vez --> bdc : es la tecera vez?
    es_tercera_vez --> pap : no es la tecera vez?

    pap --> s1 : volver a llevarlo al parlamento

    bdc-->buscar_representantes_juveniles
    buscar_representantes_juveniles--> rj : no se resolvió
    buscar_representantes_juveniles--> tc: se resolvió
    
    rj --> tema_resuelto
    tema_resuelto --> tc: se resolvió

    tema_resuelto --> cg : no resolvió
    
    cg --> tema_resueltoIS

    tema_resueltoIS --> tc: se resolvió
    tema_resueltoIS --> is: no se resolvió
    
    
```


Por **Instancias superiores** nos referimos a Provincia o Nacional



