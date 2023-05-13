# Expandir

Expandir es la tarea de tomar un texto corto, como un conjunto de instrucciones o una lista de temas, y hacer que el modelo (_LLM_) genere un texto más largo, como un correo electrónico o un ensayo sobre algún tema.

Hay algunos excelentes casos de uso, como usar al _LLM_ como un compañero de lluvia de ideas. Pero también debemos reconocer que existen algunos casos de uso problemáticos, como por ejemplo un usuario irresponsable que genera grandes cantidades de spam.

> _**NOTA**_: Utilizar el _LLM_ de manera responsable y de una forma que ayude a las personas.

## Personalizar la respuesta automática a un correo electrónico del cliente

Podemos generar correos electrónicos de servicio al cliente que se adapten a la reseña de cada cliente.

```python
# dado un sentimiento,
# y el mensaje original del cliente, personalizar el correo
# electrónico
sentiment = "negativo"

# reseña de batidora
review = f"""
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
```

```python
prompt = f"""
Eres un asistente de IA de servicio al cliente.
Tu tarea es enviar una respuesta por correo electrónico \
a un cliente valioso.
Dado el correo electrónico del cliente delimitado por ```, \
genera una respuesta para agradecer al cliente por su \
reseña.
Si el sentimiento es positivo o neutral, agradécele por \
su reseña.
Si el sentimiento es negativo, pide disculpas y sugiere \
que puede ponerse en contacto con el servicio de atención \
al cliente.
Asegúrate de usar detalles específicos de la reseña.
Escribe en un tono conciso y profesional.
Firma el correo electrónico como `Agente AI de clientes`.
Reseña del cliente: ```{review}```
Sentimiento de la reseña: {sentiment}
"""
response = get_completion(prompt)
print(response)
```

Output:
```
Estimado cliente,

Gracias por tomarse el tiempo de dejarnos una reseña. Lamentamos
mucho que su experiencia con nuestro producto no haya sido
satisfactoria. Nos disculpamos por cualquier inconveniente que
esto haya causado.

Nos gustaría asegurarnos de que nuestros clientes estén completamente 
satisfechos con nuestros productos y servicios. Si desea ponerse en
contacto con nuestro servicio de atención al cliente, estaremos
encantados de ayudarlo a resolver cualquier problema que pueda tener.

Agradecemos sus comentarios sobre la calidad de nuestros productos
y los tendremos en cuenta para mejorar en el futuro.

Gracias de nuevo por su reseña y esperamos tener la oportunidad de 
servirle mejor en el futuro.

Atentamente,
Agente AI de clientes
```

## Recordarle al modelo que use los detalles del correo electrónico del cliente

A continuación, vamos a utilizar un parámetro del _LLM_ llamado `temperature` (temperatura) que nos permitirá cambiar el tipo de variedad de las respuestas del modelo.

Podemos pensar en la _temperatura_ como un grado de exploración o el tipo de aleatoridad del modelo.

En general, al crear aplicaciones en las que se desea un tipo de respuesta confiable y predecible, se recomienda usar una temperatura baja (`temperature = 0`); de lo contrario, si se desea una variedad más amplia de respuestas diferentes, lo mejor es optar por una temperatura más alta (`temperature = 0.7` por ejemplo).

```python
prompt = f"""
Eres un asistente de IA de servicio al cliente.
Tu tarea es enviar una respuesta por correo electrónico \
a un cliente valioso.
Dado el correo electrónico del cliente delimitado por ```, \
genera una respuesta para agradecer al cliente por su \
reseña.
Si el sentimiento es positivo o neutral, agradécele por \
su reseña.
Si el sentimiento es negativo, pide disculpas y sugiere \
que puede ponerse en contacto con el servicio de atención \
al cliente.
Asegúrate de usar detalles específicos de la reseña.
Escribe en un tono conciso y profesional.
Firma el correo electrónico como `Agente AI de clientes`.
Reseña del cliente: ```{review}```
Sentimiento de la reseña: {sentiment}
"""
response = get_completion(prompt, temperature=0.7)
print(response)
```

Output (diferente al anterior por tener una temperatura más alta):
```
Estimado cliente,

Gracias por tomarse el tiempo de dejarnos su reseña sobre nuestro
sistema de 17 piezas. Lamentamos mucho que haya experimentado un
aumento de precio en diciembre y que haya tenido problemas con el
sistema después de aproximadamente un año de uso. Sentimos mucho
que haya tenido que comprar otro sistema después de que expirara
la garantía.

Nos disculpamos por cualquier inconveniente que haya causado esto
y le agradecemos su comentario. Si tiene algún problema con su
nuevo sistema, no dude en ponerse en contacto con nuestro servicio
de atención al cliente para que podamos ayudarlo.

Gracias de nuevo por su reseña y esperamos que disfrute de su
nuevo sistema.

Atentamente,
Agente AI de clientes
```

> _**NOTA**_: A menor temperatura, las respuestas son más confiables y predecibles; a mayor temperatura, las respuestas las respuestas son más variadas.

---

[<kbd> <br> Anterior <br> </kbd>][anterior]
[<kbd> <br> Siguiente <br> </kbd>][siguiente]

[anterior]: 06-transformar.md
[siguiente]: 08-chatbot.md
