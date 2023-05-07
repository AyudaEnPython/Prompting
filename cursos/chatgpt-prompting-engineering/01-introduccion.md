# Introducción

Existe una gran cantidad de material en internet para _prompting_ con artículos como "30 prompts que todos deben conocer". Mucho de eso se ha centrado en la interfaz de usuario web de _ChatGPT_, que muchas personas usan para realizar tareas específicas y, a menudo, únicas.

Pero, como desarrollador, el poder de un _modelo lingüístico de gran tamaño_ es usar llamadas _API_ para crear rápidamente aplicaciones de software.

En este curso, se compartirá algunas de las posibilidades de lo que se puede hacer, así como las mejores práticas sobre como hacerlo. Se cubrirá algunos casos de uso comunes como resumir, inferir, transformar, y expandir. Luego, se creará un _chatbot_ utilizando un _LLM_.

Al finalizar el curso se espera que esto despierte la imaginación sobre las nuevas aplicaciones que se pueden crear.

> _**NOTA**_: Varias partes de este repositorio han sido creadas usando AI, ¿Puedes adivinar cuáles?

## Tipos de LLMs

- [LLM base](#llm-base)
- [LLM afinado para instrucciones](#llm-afinado-para-instrucciones)

### LLM base

Entrenados para predecir la siguiente palabra en función de los datos de entrenamiento.

Si por ejemplo, como _prompt_ ingresamos:
```
Había una vez un unicornio
```

Sería completado (prediciendo las siguientes palabras) de esta forma:
```
que vivía en un bosque mágico
con todo sus amigos
```

Pero, si el _prompt_ fuése:
```
¿Cuál es la capital de Francia?
```

Basado en los artículos de internet, es muy probable que el _LLM base_ lo complete de esta forma:
```
¿Cuál es la ciudad más grande de Francia?
¿Cuál es la población de Francia?
¿Cuál es la moneda de Francia?
```

### LLM afinado para instrucciones (Instruction Tuned LLM)

Entrenados para seguir instrucciones.

Si el _prompt_ fuése:
```
¿Cuál es la capital de Francia?
```

Es mucho más probable que sea completado de la siguiente forma:
```
La capital de Francia es París.
```

Un LLM afinado para instrucciones típicamente empieza como un LLM base que ha sido entrenado con una gran cantidad de datos y entrenado aún más para afinarlo con instrucciones e intentos para seguir esas instrucciones, siendo refinados a menudo con una técnica llamada _RLHF_ para hacer que el sistema sea capaz de ser útil y seguir las instrucciones.

---

Cuando se usa un _LLM afinado para instrucciones_, se debe pensar como darle instrucciones a otra persona que es inteligente pero que no conoce las especificaciones de la tarea.

Cuando un _LLMs_ no funciona, algunas veces es porque las instrucciones no fueron lo suficientemente claras. Por ejemplo, si pidieras: "escribe algo sobre Alan Turing", además de eso, puede ser útil tener claro si se desea que el texto se centre en su trabajo científico, en su vida personal, en su papel en la historia o en otra cosa. Y si se especifíca el tono, ¿debería adoptar el tono que escribiría un periodista profesional? ¿O es más una nota casual que será enviada a un amigo?

En las siguientes lecciones se verán ejemplos de como ser claro y específico, lo cual es un principio importante del _prompting_ y también sobre el segundo principio del _prompting_ que es darle al _LLM_ tiempo para pensar.

---

[<kbd> <br> Inicio <br> </kbd>][inicio]
[<kbd> <br> Siguiente <br> </kbd>][siguiente]

[inicio]: README.md
[siguiente]: 02-pautas.md
