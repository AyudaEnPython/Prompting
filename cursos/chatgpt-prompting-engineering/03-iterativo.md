# Desarrollo Iterativo

Siempre que se tenga un buen proceso para mejorar iterativamente un _prompt_, uno podrá llegar a algo que funcione bien para la tarea que se desea lograr.

Además, es importante resaltar que lo que más importa es el proceso para llegar a _prompts_ que funcionan para la aplicación de uno.

Proceso iterativo
- Intentar algo
- Analizar porque el resultado no es el esperado
- Clarificar las instrucciones, dar más tiempo para pensar
- Refinar los _prompts_ con un lote de ejemplos

Cuando se tiene una idea de lo que se quiere hacer y la tarea a completar, entonces se puede intentar escribir un _prompt_ que con suerte sea claro y específico. Se puede dar tiempo al sistema para pensar y luego ejecutar el _prompt_ para ver el resultado obtenido.

Si esto no funciona bien la primera vez, podemos refinar la idea, refinar el _prompt_, refinar el mensaje, etc. varias veces hasta llegar a un _prompt_ que funcione (retorne un resultado esperado).

> _**IMPORTANTE**_: No dar importancia a los artículos del tipo "30 prompts que debes aprender" porque probablemente no exista el prompt perfecto para todo. Es más importante que tengas un proceso para desarrollar un buen prompt.

### Generar una descripción de marketing de un producto a partir de una ficha técnica del mismo

```python
fact_sheet_chair = """
DESCRIPCIÓN GENERAL
- Parte de una hermosa familia de muebles de oficina inspirados
en mediados de siglo, incluyendo archivadores, escritorios,
estanterías, mesas de reuniones y más.
- Varias opciones de color de carcasa y acabados de base.
- Disponible con respaldo de plástico y tapizado frontal (SWC-100)
o tapizado completo (SWC-110) en 10 opciones de tela y 6 de cuero.
- Las opciones de acabado de la base son: acero inoxidable, negro mate,
blanco brillo o cromo.
- La silla está disponible con o sin reposabrazos.
- Adecuado para entornos domésticos o comerciales.
- Cualificado para uso por contrato.

CONSTRUCCIÓN
- Base de aluminio plastificado de 5 ruedas.
- Ajuste neumático del sillón para subir/bajar fácilmente.

DIMENSIONES
- ANCHO 53 CM | 20.87”
- PROFUNDIDAD 51 CM | 20.08”
- ALTURA 80 CM | 31.50”
- ALTURA DEL ASIENTO 44 CM | 17,32”
- PROFUNDIDAD DEL ASIENTO 41 CM | 16,14”

OPCIONES
- Opciones de ruedas para piso blando o duro.
- Dos opciones de densidades de espuma de asiento:
 medio (1,8 lb/ft3) o alto (2,8 lb/ft3)
- Reposabrazos sin brazos o de PU de 8 posiciones

MATERIALES
PLANEADOR CON BASE DE CARCASA
- Fundición de aluminio con recubrimiento de nylon PA6/PA66 modificado.
- Grosor de la carcasa: 10 mm.
ASIENTO
- espuma HD36

PAÍS DE ORIGEN
- Italia
"""
```

```python
prompt = f"""
Tu tarea es ayudar al equipo de marketing a crear
una descripción para un sitio web minorista de un
producto basado en una ficha técnica.

Escribe una descripción del producto basada en la
información proporcionada en las especificaciones
técnicas delimitadas por backticks triples.

Especificaciones técnicas: ```{fact_sheet_chair}```
"""
response = get_completion(prompt)
print(response)
```

Output:
```
Introduciendo nuestra silla de oficina inspirada en mediados
de siglo, parte de una hermosa familia de muebles de oficina
que incluye archivadores, escritorios, estanterías, mesas de
reuniones y más. Con varias opciones de color de carcasa y
acabados de base, esta silla está disponible con respaldo de
plástico y tapizado frontal o tapizado completo en una amplia
variedad de opciones de tela y cuero. La base de aluminio
plastificado de 5 ruedas y el ajuste neumático del sillón
hacen que subir y bajar sea fácil. La silla está disponible
con o sin reposabrazos y es adecuada para entornos domésticos
o comerciales. Además, está cualificada para uso por contrato.
Con una construcción de alta calidad, la carcasa está hecha de
fundición de aluminio con recubrimiento de nylon PA6/PA66
modificado y un grosor de 10 mm. El asiento está hecho de espuma
HD36 y viene con opciones de ruedas para piso blando o duro, dos
opciones de densidades de espuma de asiento y reposabrazos sin
brazos o de PU de 8 posiciones. Con dimensiones de 53 cm de ancho,
51 cm de profundidad y 80 cm de altura, esta silla tiene una
altura de asiento de 44 cm y una profundidad de asiento de 41 cm.
Fabricada en Italia, esta silla es una adición elegante y
funcional a cualquier espacio de oficina.
```

---

Para aplicaciones más sofisticadas, puede resultar útil evaluar los _prompts_ con un conjunto más grande de ejemplos, probar diferentes _prompts_ en docenas de fichas técnicas para ver el desempeño promedio o el peor en varias fichas técnicas. Por lo general terminarás haciendo esto solo cuando la aplicación es lo suficientemente madura y tengas las métricas necesarias para impulsar los últimos pasos incrementales de mejorar en el _prompt_.

---

[<kbd> <br> Anterior <br> </kbd>][anterior]
[<kbd> <br> Siguiente <br> </kbd>][siguiente]

[anterior]: 02-pautas.md
[siguiente]: 04-resumir.md
