# Expandir

Expandir es la tarea de tomar un texto corto, como un conjunto de instrucciones o una lista de temas, y hacer que el modelo (_LLM_) genere un texto más largo, como un correo electrónico o un ensayo sobre algún tema.

Generar correos electrónicos de servicio al cliente que se adapten a la reseña de cada cliente.

> _**NOTA**_: Un problemático uso de caso sería un usuario irresponsable que genera grandes cantidades de spam.

## Personalizar la respuesta automática a un correo electrónico del cliente

```python
# dado un sentimiento,
# y el mensaje original del cliente, personalizar el correo
# electrónico
sentimient = "negativo"

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
```

## Recordarle al modelo que use los detalles del correo electrónico del cliente

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
```

> _**NOTA**_: Para tareas que requieran confiabilidad y/o previsibilidad usar una temperatura de `0` (`temperature = 0`), para tareas que requieran variedad usar una temperatura más alta (`temperature = 0.7`)

---

[<kbd> <br> Anterior <br> </kbd>][anterior]
[<kbd> <br> Siguiente <br> </kbd>][siguiente]

[anterior]: 06-transformar.md
[siguiente]: 08-chatbot.md
