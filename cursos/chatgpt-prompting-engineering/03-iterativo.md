# Desarrollo Iterativo

Siempre que se tenga un buen proceso para mejorar iterativamente un _prompt_, uno podrá llegar a algo que funcione bien para la tarea que se desea lograr.

> Idear - Implementar - Experimentar - Analizar

Además, es importante resaltar que lo que más importa es el proceso para llegar a _prompts_ que funcionan para la aplicación de uno.

Proceso iterativo:
- Intentar algo
- Analizar porque el resultado no es el esperado
- Clarificar las instrucciones, dar más tiempo para pensar
- Refinar los _prompts_ con un lote de ejemplos

Cuando se tiene una idea de lo que se quiere hacer y la tarea a completar, entonces se puede intentar escribir un _prompt_ que con suerte sea claro y específico. Se puede dar tiempo al sistema para pensar y luego ejecutar el _prompt_ para ver el resultado obtenido.

Si esto no funciona bien la primera vez, podemos refinar la idea, refinar el _prompt_, refinar el mensaje, etc. varias veces hasta llegar a un _prompt_ que funcione (retorne un resultado esperado).

> _**IMPORTANTE**_: No dar importancia a los artículos del tipo "30 prompts que debes aprender" porque probablemente no exista el prompt perfecto para todo. Es más importante que tengas un proceso para desarrollar un buen prompt.

## Generar una descripción de marketing de un producto a partir de una ficha técnica del mismo

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

## Problema 1: El texto es demasiado largo

Limitar el número de palabras/oraciones/caracteres.

```python
prompt = f"""
Tu tarea es ayudar al equipo de marketing a crear
una descripción para un sitio web minorista de un
producto basado en una ficha técnica.

Escribe una descripción del producto basada en la
información proporcionada en las especificaciones
técnicas delimitadas por backticks triples.

Utiliza como máximo 50 palabras.

Especificaciones técnicas: ```{fact_sheet_chair}```
"""
response = get_completion(prompt)
print(response)
```

Output:
```
La silla de oficina de mediados de siglo es parte de una
hermosa familia de muebles de oficina. Con varias opciones
de color de carcasa y acabados de base, esta silla está
disponible con o sin reposabrazos y es adecuada para
entornos domésticos o comerciales. La silla está construida
con una base de aluminio plastificado de 5 ruedas y un
ajuste neumático del sillón para subir/bajar fácilmente.
Disponible en 10 opciones de tela y 6 de cuero, esta silla
es una excelente opción para cualquier espacio de trabajo.
```

Podemos verificar la cantidad de palabras con:
```python
len(response.split(" "))
```

Output:
```
88
```

No solo podemos limitar el número de palabras, también podemos hacerlo por oraciones o caracteres:

```
...
Utiliza como máximo 4 oraciones.
Utiliza como máximo 280 caracteres.
...
```

## Problema 2: El texto se enfoca en los detalles incorrectos

Solicitar que se centre en los aspectos que son relevantes para el público objetivo.

```python
prompt = f"""
Tu tarea es ayudar al equipo de marketing a crear
una descripción para un sitio web minorista de un
producto basado en una ficha técnica.

Escribe una descripción del producto basada en la
información proporcionada en las especificaciones
técnicas delimitadas por backticks triples.

La descripción está destinada a minoristas de muebles,
por lo que debe ser de naturaleza técnica y centrarse
en los materiales con los que el producto está
construido.

Utiliza como máximo 50 palabras.

Especificaciones técnicas: ```{fact_sheet_chair}```
"""
response = get_completion(prompt)
print(response)
```

Output:
```
La silla de oficina de la familia de muebles de mediados
de siglo es una opción elegante y versátil para cualquier
entorno doméstico o comercial. Con una base de aluminio
plastificado de 5 ruedas y ajuste neumático del sillón,
esta silla es fácil de ajustar y mover. Disponible en una
variedad de opciones de color y acabado de base, así como
con o sin reposabrazos, esta silla es adecuada para cualquier
necesidad. La carcasa está hecha de fundición de aluminio con 
recubrimiento de nylon PA6/PA66 modificado y el asiento
está hecho de espuma HD36. Fabricado en Italia.
```

También podemos solicitar cosas más específicas en el _prompt_:

```python
prompt = f"""
Tu tarea es ayudar al equipo de marketing a crear
una descripción para un sitio web minorista de un
producto basado en una ficha técnica.

Escribe una descripción del producto basada en la
información proporcionada en las especificaciones
técnicas delimitadas por backticks triples.

La descripción está destinada a minoristas de muebles,
por lo que debe ser de naturaleza técnica y centrarse
en los materiales con los que el producto está
construido.

Al final de la descripción, incluye cada ID de 7 caracteres
del producto en la especificación técnica.

Utiliza como máximo 50 palabras.

Especificaciones técnicas: ```{fact_sheet_chair}```
"""
response = get_completion(prompt)
print(response)
```

Output:
```
La silla de oficina SWC es parte de una hermosa familia
de muebles de mediados de siglo. Con varias opciones de
color de carcasa y acabados de base, esta silla está
disponible con o sin reposabrazos y en 10 opciones de
tela y 6 de cuero. La base de aluminio plastificado de
5 ruedas y el ajuste neumático del sillón hacen que sea
fácil de subir y bajar. La silla es adecuada para entornos
domésticos o comerciales y está calificada para uso por
contrato. ID del producto: SWC-100, SWC-110.
```

## Problema 3: La descripción necesita una tabla de dimensiones

Solicitar que extraiga información y la organice en una tabla.

```python
prompt = f"""
Tu tarea es ayudar al equipo de marketing a crear
una descripción para un sitio web minorista de un
producto basado en una ficha técnica.

Escribe una descripción del producto basada en la
información proporcionada en las especificaciones
técnicas delimitadas por backticks triples.

La descripción está destinada a minoristas de muebles,
por lo que debe ser de naturaleza técnica y centrarse
en los materiales con los que el producto está
construido.

Al final de la descripción, incluye cada ID de 7 caracteres
del producto en la especificación técnica.

Después de la descripción, incluye una tabla sobre las
dimensiones del producto. La tabla debe tener dos columnas.
En la primera, incluye el nombre de la dimensión.
En la segunda, incluye las medidas.

Dale el título "Dimensiones del producto" a la tabla.

Formatea todo como HTML que pueda ser usado en una página.
Coloca la descripción en un elemnto <div>.

Especificaciones técnicas: ```{fact_sheet_chair}```
"""
response = get_completion(prompt)
print(response)
```

Output:
```
<div>
  <p>La silla de oficina SWC es parte de una hermosa familia de muebles de oficina inspirados en mediados de siglo. Esta silla está disponible en varias opciones de color de carcasa y acabados de base, lo que la hace perfecta para cualquier entorno doméstico o comercial. Además, la silla está disponible con o sin reposabrazos y es adecuada para uso por contrato.</p>
  <p>La base de la silla está hecha de aluminio plastificado de 5 ruedas y cuenta con un ajuste neumático del sillón para subir/bajar fácilmente. El asiento está hecho de espuma HD36 y está disponible en dos opciones de densidades de espuma de asiento: medio (1,8 lb/ft3) o alto (2,8 lb/ft3). La silla también está disponible con respaldo de plástico y tapizado frontal (SWC-100) o tapizado completo (SWC-110) en 10 opciones de tela y 6 de cuero.</p>
  <p>La silla SWC está construida con materiales de alta calidad. La carcasa está hecha de fundición de aluminio con recubrimiento de nylon PA6/PA66 modificado y tiene un grosor de 10 mm. La silla también está disponible con opciones de ruedas para piso blando o duro y reposabrazos sin brazos o de PU de 8 posiciones.</p>
  <p>ID del producto: SWC-1001</p>
</div>

<table>
  <caption>Dimensiones del producto</caption>
  <tr>
    <th>Dimensión</th>
    <th>Medida</th>
  </tr>
  <tr>
    <td>Ancho</td>
    <td>53 cm | 20.87"</td>
  </tr>
  <tr>
    <td>Profundidad</td>
    <td>51 cm | 20.08"</td>
  </tr>
  <tr>
    <td>Altura</td>
    <td>80 cm | 31.50"</td>
  </tr>
  <tr>
    <td>Altura del asiento</td>
    <td>44 cm | 17,32"</td>
  </tr>
  <tr>
    <td>Profundidad del asiento</td>
    <td>41 cm | 16,14"</td>
  </tr>
</table>
```


Si estas usando un _notebook_, para visualizar el output:
```python
from IPython.display import display, HTML
```

```python
display(HTML(response))
```


---

Para aplicaciones más sofisticadas, puede resultar útil evaluar los _prompts_ con un conjunto más grande de ejemplos, probar diferentes _prompts_ en docenas de fichas técnicas para ver el desempeño promedio o el peor en varias fichas técnicas. Por lo general terminarás haciendo esto solo cuando la aplicación es lo suficientemente madura y tengas las métricas necesarias para impulsar los últimos pasos incrementales de mejorar en el _prompt_.

---

[<kbd> <br> Anterior <br> </kbd>][anterior]
[<kbd> <br> Siguiente <br> </kbd>][siguiente]

[anterior]: 02-pautas.md
[siguiente]: 04-resumir.md
