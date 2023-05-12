# Resumir

Hay demasiado texto en el mundo de hoy, casi ninguno de nosotros tiene suficiente tiempo para leer todas las cosas que desearíamos.

Una de las aplicaciones más emocionantes de los _LLM_ es usarlos para resumir texto, algo que muchos equipos de desarrolladores construyen en múltiples aplicaciones de software. La interfaz web de _ChatGPT_ puede resumir artículos de modo que podamos leer el contenido de mucho más artículos de los que antes podíamos.

Si estás creando un sitio web de comercio electrónico y hay un gran volumen de reseñas, tener una herramienta para resumir reseñas extensas podría darte una forma de revisar rápidamente más reseñas para tener una mejor idea de lo que todos tus clientes están pensando.

## Texto a resumir

```python
prod_review = """
Recibí este peluche de panda por el cumpleaños de mi hija, \
que lo ama y lo lleva a todas partes. Es suave y \
super lindo, y su cara tiene una mirada amistosa. Es \
un poco pequeño para lo que pagué. Creo que \
podrían haber otras opciones que son más grandes por el \
mismo precio. Llegó un día antes de lo esperado, \
así que pude jugar con él antes de dárselo a ella.
"""
```

## Resumir con un límite de palabras/oraciones/caracteres

```python
prompt = f"""
Tu tarea es generar un breve resumen de la reseña \
del producto de un sitio de comercio electrónico.

Resume la reseña a continuación, delimitada por
triple backticks, en un máximo de 30 palabras.

Reseña: ```{prod_review}```
"""

response = get_completion(prompt)
print(response)
```

Output:
```
Peluche de panda suave y lindo, pero un poco pequeño 
para el precio. Entrega rápida. Ideal para regalar a niños.
```

## Resumir con un enfoque en el envío y la entrega

```python
prompt = f"""
Tu tarea es generar un breve resumen de la reseña \
del producto de un sitio de comercio electrónico para
dar retroalimentación al departamento de envíos.

Resume la reseña a continuación, delimitada por
triple backticks, en un máximo de 30 palabras, y 
centrándote en cualquier aspecto que menciona el 
envío o la entrega del producto.

Reseña: ```{prod_review}```
"""

response = get_completion(prompt)
print(response)
```

Output:
```
El peluche de panda es suave y lindo, pero un poco
pequeño para el precio. Llegó un día antes de lo esperado.
```

## Resumir con un enfoque en el precio y valor

```python
prompt = f"""
Tu tarea es generar un breve resumen de la reseña \
del producto de un sitio de comercio electrónico para \
dar retroalimentación al departamento de precios.

Resume la reseña a continuación, delimitada por \
triple backticks, en un máximo de 30 palabras, y \
centrándote en cualquier aspecto que sea relevante \
para el precio y el valor percibido.

Reseña: ```{prod_review}```
"""

response = get_completion(prompt)
print(response)
```

Output:
```
Peluche de panda suave y lindo, pero un poco pequeño
para el precio. Entrega rápida. Se sugiere buscar
opciones más grandes por el mismo precio.
```

## Intenta "extraer" en lugar de "resumir"

```python
prompt = f"""
Tu tarea es extraer información relevante de la \
reseña de un producto de un sitio de comercio \
electrónico para dar retroalimentación al \
departamento de envíos.

Para la reseña a continuación, delimitada por \
triple quotes, extrae la información relevante para \
la entrega y el envío. Limitar a 30 palabras.

Reseña: ```{prod_review}```
"""

response = get_completion(prompt)
print(response)
```

Output:
```
El peluche llegó un día antes de lo esperado. Podrían
haber opciones más grandes por el mismo precio.
```

## Resumir múltiples reseñas de un producto

```python
review_1 = prod_review 

# reseña para un soporte de lampara
review_2 = """
Necesitaba una linda lámpara para mi dormitorio, y \
esta tenía almacenamiento adicional y un precio no tan \
alto. Lo tuve rápido - llegó en 2 días. La cuerda \
a la lámpara se rompió durante el tránsito y la empresa \
felizmente envió uno nuevo. Llegó a los pocos días \
también. Fue fácil de armar. Luego tuve un \
parte faltante, así que me puse en contacto con su \
soporte y ellos muy rápidamente me consigieron la pieza \
que faltaba! Me parece ser una gran empresa que se preocupa \
por sus clientes y productos.
"""

# reseña para un cepillo eléctrico
review_3 = """
Mi higienista dental me recomendó un cepillo de dientes \
eléctrico, por eso tengo este. La duración de la batería \
parece ser bastante impresionante hasta ahora. Después de \
la carga inicial y dejando el cargador enchufado durante \
la primera semana para acondicionar la bateria, he \
desenchufado el cargador y lo he estado usando para el \
cepillarme dos veces al día durante el último \
3 semanas todo con la misma carga. Pero el cabezal del \
cepillo de dientes es demasiado pequeño. He visto cepillos de\
dientes para bebés más grandes que este. Desearía que la\
cabeza fuera más grande con diferentes cerdas largas para \
meterse mejor entre los dientes porque este no lo hace. En \
general, si puedes conseguir este alrededor de los $ 50, es \
una buena oferta. Los cabezales de repuesto del fabricante \
son bastante caros, pero puedes obtener los genéricos que \
tienen un precio más razonable. Este cepillo de dientes me \
hace sentir como si hubiera ido al dentista \
cada día. ¡Mis dientes se sienten limpios y relucientes!
"""

# reseña para una batidora
review_4 = """
Entonces, todavía tenían el sistema de 17 piezas en \
temporada de venta por alrededor de $ 49 en el mes de \
noviembre, alrededor de la mitad de descuento, pero por \
alguna razón (llámase aumento de precios) alrededor de la \
segunda semana de diciembre todos los precios subieron \
hasta alrededor de $70-$89 por el mismo sistema. Y el \
sistema de 11 piezas subió alrededor de $10 mas o menos \
también desde el precio de venta anterior de $29. \
Se ve bien, pero si miras la base, la parte \
donde la hoja se traba en su lugar no se ve tan bien \
como en ediciones anteriores de hace unos años, pero yo \
planeo ser muy gentil con él (ejemplo, aplasto \
artículos muy duros como frijoles, hielo, arroz, etc. en \
la licuadora primero y luego los pulverizo en el tamaño de \
la porción que quiero en la licuadora luego cambio a la batida \
hoja para una harina más fina, y uso la hoja de corte \
transversal primero cuando haga batidos, luego use la cuchilla \
plana si los necesito más finos/menos pulposos). Consejo \
especial al hacer batidos, corte finamente y congele las \
frutas y verduras (si usa espinacas, estofado ligeramente, \
ablande la espinaca luego congélela hasta que esté lista para \
usar, y si está haciendo sorbete, use un procesador de \
alimentos de tamaño pequeño a mediano) que planea usar de esa \
manera puede evitar agregar mucho hielo, si es que lo hay, al \
hacer su batido. Después de aproximadamente un año, el motor \
estaba haciendo un ruido raro. Llamé al servicio de atención \
al cliente pero la garantía ya expiró, así que tuve que comprar \
otro. FYI: En general la calidad se ha ido en este tipo de \
productos, por lo que en cierto modo estan contando en el \
reconocimiento de la marca y fidelización del consumidor para \
mantener las ventas. Lo tengo alrededor de dos días.
"""

reviews = [review_1, review_2, review_3, review_4]
```

```python
for i, review in enumerate(reviews, 1):
    prompt = f"""
    Tu tarea es generar un breve resumen de la reseña de un \
    producto de un comercio electrónico.
    
    Resume la reseña, delimitada por triple backticks en un \
    máximo de 20 palabras.

    Reseña: ```{review}```
    """

    response = get_completion(prompt)
    print(f"{i}. {response}\n")
```

Output:
```
1. Peluche de panda suave y lindo, pero un poco pequeño
para el precio. Entrega rápida. Ideal para regalar a niños.

2. Lámpara con almacenamiento adicional, envío rápido,
excelente servicio al cliente y fácil de armar. Gran empresa.

3. Cepillo de dientes eléctrico con buena duración de
batería, pero cabezal pequeño. Buena relación calidad-precio.

4. Reseña de un sistema de licuadora con aumento de precios
en diciembre, calidad inferior a ediciones anteriores y motor
ruidoso después de un año de uso.
```

---

[<kbd> <br> Anterior <br> </kbd>][anterior]
[<kbd> <br> Siguiente <br> </kbd>][siguiente]

[anterior]: 03-iterativo.md
[siguiente]: 05-inferir.md
