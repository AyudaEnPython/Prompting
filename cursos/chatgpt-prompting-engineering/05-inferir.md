# Inferir

Si se requiere extraer un sentimiento, positivo o negativo, de un fragmento de texto para realizar algún tipo de análisis, en un flujo de trabajo de _ML_ tradicional se debería recopilar el conjunto de datos de la etiqueta, entrenar el modelo, implementar el modelo en la nube y hacer inferencias. Esto puede funcionar bien pero realizar todo ese proceso es muy laborioso, además para cada tarea, como sentimientos y extracción de nombres, se debe entrenar e implementar un modelo separado.

Una de las cosas realmente buenas de un _LLM_ es que en tareas como las mencionadas anteriormente, basta con escribir un _prompt_ y obtener resultados prácticamente de inmediato, acelerando de esta forma el desarrollo de aplicaciones. Basta con usar un modelo, una _API_, para llevar a cabo varias tareas en lugar de averiguar cómo entrenar e implementar muchos modelos diferentes.

## Reseña del producto

```python
lamp_review = """
Necesitaba una linda lámpara para mi dormitorio, y \
esta tenía almacenamiento adicional y un precio no tan \
elevado. La obtuve enseguida. La cuerda de la lámpara \
se rompió durante el trayecto y la compañia felizmente\
envió una nueva. Llegó a los pocos días también. Fue \
fácil de armar. Me faltaba una pieza, así que me puse \
en contacto con su soporte y ellos rápidamente me \
consigieron la pieza faltante! Lumina me parece ser \
una gran compañía que se preocupa por sus clientes y \
productos!!
"""
```

## Sentimiento (positivo/negativo)

```python
prompt = f"""
¿Cuál es el sentimiento de la siguiente reseña de producto,
que está delimitado con triple backticks?

Texto de reseña: '''{lamp_review}'''
"""
response = get_completion(prompt)
print(response)
```

Output:
```
El sentimiento de la reseña es positivo y satisfecho con
el producto y la atención al cliente de la compañía.
```

Podemos también añadir otra instrucción para obtener un resultado más conciso:

```python
prompt = f"""
¿Cuál es el sentimiento de la siguiente reseña de producto,
que está delimitado con triple backticks?

Entrega tu respuesta como una sola palabra, ya sea \
"positiva" o "negativa".

Texto de reseña: '''{lamp_review}'''
"""
response = get_completion(prompt)
print(response)
```

Output:
```
positiva
```

## Identificar tipos de emociones

```python
prompt = f"""

Identifica una lista de emociones que el escritor de la \
siguiente reseña está expresando. No incluyas más de \
cinco elementos en la lista. Formatea tu respuesta como \
una lista de palabras en minúsculas separadas por comas.

Texto de reseña: '''{lamp_review}'''
"""
response = get_completion(prompt)
print(response)
```

Output:
```
contento, satisfecho, agradecido, impresionado, confiado
```

## Identifica ira


```python
prompt = f"""

¿El escritor de la siguiente reseña está expresando enojo? \
La reseña está delimitada con triples comillas invertidas. \
Dé su respuesta como sí o no.

Texto de reseña:'''{lamp_review}'''
"""
response = get_completion(prompt)
print(response)
```

Output:
```
No.
```

## Extraer productos y nombres de compañias desde reseñas de clientes

```python
prompt = f"""
Identifica los siguientes elementos del texto de reseña:
- Artículo comprado por el reseñador
- Empresa que fabricó el artículo.

La reseña está delimitada con triples comillas invertidas. \
Formata tu respuesta como un objeto JSON con \
"Artículo" y "Marca" como claves.
Si la información no está presente, usa "desconocido" \
como valor.
Haz tu respuesta lo más breve posible.
  
Texto de reseña:'''{lamp_review}'''
"""
response = get_completion(prompt)
print(response)
```

Output:
```
{
  "Artículo": "lámpara con almacenamiento adicional",
  "Marca": "Lumina"
}   
```

## Realizando múltiples tareas al mismo tiempo

```python
prompt = f"""
Identifica los siguientes elementos del texto de reseña:
- Sentimiento (positivo o negativo)
- ¿El reseñador está expresando enojo? (verdadero o falso)
- Artículo comprado por el reseñador
- Empresa que fabricó el artículo.

La reseña está delimitada con triples comillas invertidas. \
Formatea tu respuesta como un objeto JSON con \
"Sentimiento", "Ira", "Artículo" y "Marca" como claves.
Si la información no está presente, usa "desconocido" \
como valor.
Haz tu respuesta lo más breve posible.
Formatea el valor de Ira como un valor booleano.

Texto de reseña: '''{lamp_review}'''
"""
response = get_completion(prompt)
print(response)
```

Output:
```
{
  "Sentimiento": "positivo",
  "Ira": false,
  "Artículo": "lámpara",
  "Marca": "Lumina"
}
```

## Infiriendo temas

Una de las más geniales aplicaciones de los _LLM_ es inferir temas. Dado un texto largo, ¿sabes de que se trata en el texto?, ¿cuáles son los temas? Aquí tenemos un artículo de un periódico fictiocio sobre cómo se sienten los trabajadores del gobierno acerca de la agencia para la que trabajan.

```python
story = """
En una encuesta reciente realizada por el gobierno,
Se pidió a los empleados del sector público que calificaran su nivel
de satisfacción con el departamento en el que trabajan.
Los resultados revelaron que la NASA fue el departamento más
popular con un índice de satisfacción del 95%.

Un empleado de la NASA, John Smith, comentó sobre los hallazgos,
diciendo: "No me sorprende que la NASA esté en la cima.
Es un gran lugar para trabajar con gente increíble e
increíbles oportunidades. Estoy orgulloso de ser parte de
una organización tan innovadora".

Los resultados también fueron bien recibidos por el equipo
directivo de la NASA, con el director Tom Johnson afirmando:
"Estamos encantados de escuchar que nuestros empleados están
satisfechos con su trabajo en la NASA. Contamos con un equipo
talentoso y dedicado que trabaja incansablemente para lograr
nuestras metas, y es fantástico ver que el arduo trabajo está
dando frutos".

La encuesta también reveló que la La Administración del Seguro
Social tuvo la satisfacción más baja calificación, con solo el
45% de los empleados indicando que estaban satisfechos con su
trabajo. El gobierno se ha comprometido a abordar las inquietudes
planteadas por los empleados en la encuesta y trabajar para mejorar
la satisfacción laboral en todos los departamentos.
"""
```

## Inferir 5 temas

```python
prompt = f"""
Determina cinco temas que se están discutiendo en el \
siguiente texto, que está delimitado por triples acentos graves.

Haz que cada artículo tenga una o dos palabras.

Formatea tu respuesta como una lista de elementos separados \
por comas.

Ejemplo de texto:'''{story}'''
"""
response = get_completion(prompt)
print(response)
```

Output:
```
Departamentos del sector público, Satisfacción laboral, NASA, Administración del Seguro Social, Encuesta gubernamental.
```

Nota: en español aún indicando al modelo que no agrégue un punto "." al final de la respuesta, lo hace.
```python
response[:-1].split(sep=",")
```

Output:
```
['Departamentos del sector público',
 ' Satisfacción laboral',
 ' NASA',
 ' Administración del Seguro Social',
 ' Encuesta gubernamental']
```

## Crear alertas para ciertos temas

Si queremos averiguar, dado un artículo de periódico, cuales de los siguientes temas se tratan en ese artículo:

```python
topics = [
    "nasa", "gobierno local", "ingeniería", 
    "satisfacción de los empleados", "gobierno federal"
]
```

Podemos utilizar el siguiente _prompt_:

```python
prompt = f"""
Determine si cada elemento de la siguiente lista de \
temas es un tema en el texto a continuación, que
está delimitado con tres comillas graves.

Da tu respuesta como una lista con 0 o 1 para cada tema.\

Lista de temas: {", ".join(topics)}

Ejemplo de texto:'''{story}'''
"""
response = get_completion(prompt)
print(response)
```

Output:
```
nasa: 1
gobierno local: 0
ingeniería: 1
satisfacción de los empleados: 1
gobierno federal: 1
```

En _ML_ esto a veces se denomina _aprendizaje de tiro cero_ porque no le dimos ningún dato de entrenamiento que estuviera etiquetado.

Si queremos generar una alerta de noticias, podriamos hacer lo siguiente:

```python
topics = {
    k: int(v) for k, v in
    (s.split(": ") for s in response.split("\n"))
}
if topics["nasa"] == 1:
    print("Alerta: Nueva noticia sobre la NASA")
```

Output:
```
Alerta: Nueva noticia sobre la NASA
```

---

[<kbd> <br> Anterior <br> </kbd>][anterior]
[<kbd> <br> Siguiente <br> </kbd>][siguiente]

[anterior]: 04-resumir.md
[siguiente]: 06-transformar.md
