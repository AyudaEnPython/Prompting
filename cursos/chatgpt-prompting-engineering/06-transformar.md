# Transformar

## Traducir

_ChatGPT_ está entrenado con fuentes en muchos idiomas. Esto le da al modelo la habilidad de realizar traducciones. Aquí hay algunos ejemplos de como usar esa capacidad:

```python
prompt = f"""
Traduce el siguiente texto en español a inglés: \
```Hola, me gustaría pedir una licuadora```
"""
response = get_completion(prompt)
print(response)
```

Output:
```
Hello, I would like to order a blender.
```

```python
prompt = f"""
Dime qué idioma es:
```Combien coûte le lampadaire?```
"""
response = get_completion(prompt)
print(response)
```

Output:
```
Es francés. Significa "¿Cuánto cuesta la lámpara de pie?" en español.
```

```python
prompt = f"""
Traduce el siguiente texto a francés, inglés e inglés pirata
```Quiero pedir una pelota de baloncesto```
"""
response = get_completion(prompt)
print(response)
```

Output:
```
Francés: Je voudrais commander un ballon de basket-ball
Inglés: I want to order a basketball
Inglés pirata: Arrr, I be wantin' to order a basketball, matey!
```

```python
prompt = f"""
Traduce el siguiente texto a inglés tanto en forma \
formal e informal:
'¿Te gustaría ordenar una almohada?'
"""
response = get_completion(prompt)
print(response)
```

Output:
```
Formal: Would you like to order a pillow?
Informal: Do you wanna order a pillow?
```

## Traductor universal

Imagina que estás a cargo del departamento de IT en una gran empresa multinacional de comercio electrónico. Los usuarios te envían mensajes con problemas relacionados a IT, todos en sus idiomas nativos. Tu personal es de todo el mundo y solo hablan sus idiomas nativos. !Necesitas un traductor universal!

```python
user_messages = [
  "La performance du système est plus lente que d'habitude.", 
  # El rendimiento del sistema es más lento de lo normal
  "My monitor has pixels that are not lighting",
  # Mi monitor tiene píxeles que no se iluminan
  "Il mio mouse non funziona",
  # Mi ratón no está funcionando
  "Mój klawisz Ctrl jest zepsuty",
  # Mi teclado tiene una tecla de control rota
  "我的屏幕在闪烁",
  # Mi pantalla parpadea
] 

for issue in user_messages:
    prompt = f"Dime que idima es esto: ```{issue}```"
    lang = get_completion(prompt)
    print(f"Mensaje original ({lang}): {issue}")

    prompt = f"""
    Traduce el siguiente texto de español \
    a inglés: ```{issue}```
    """
    response = get_completion(prompt)
    print(response, "\n")
```

Output:
```
Mensaje original (Este texto está en francés.): La performance
du système est plus lente que d'habitude.
"The system performance is slower than usual." 

Mensaje original (Este texto está en inglés.): My monitor has
pixels that are not lighting
My monitor has pixels that are not lighting. 

Mensaje original (Este texto está en italiano.): Il mio mouse
non funziona
My mouse is not working. 

Mensaje original (Este texto está en polaco. Significa "Mi tecla
Ctrl está rota".): Mój klawisz Ctrl jest zepsuty
My Ctrl key is broken. 

Mensaje original (Este texto está en chino mandarín.): 我的屏幕在闪烁
"My screen is flickering" 
```

## Transformar tono

La escritura puede variar en función de la audiencia prevista. _ChatGPT_ puede producir diferentes tonos.

```python
prompt = f"""
Traduce lo siguiente de una jerga a una carta comercial:
'Amigo, soy Joe, echa un vistazo a la especificación de esta lámpara de pie.'
"""
response = get_completion(prompt)
print(response)
```

Output:
```
Estimado/a, 

Me dirijo a usted para presentarle la especificación de una
lámpara de pie. 

Atentamente, 
Joe
```

## Conversión de formato

_ChatGPT_ puede traducir entre formatos. El _prompt_ debe describir los formatos de entrada y salida.

```python
data = { "resturant employees" :[ 
    {"name":"Shyam", "email":"shyamjaiswal@gmail.com"},
    {"name":"Bob", "email":"bob32@gmail.com"},
    {"name":"Jai", "email":"jai87@gmail.com"}
]}

prompt = f"""
Traduce el siguiente diccionario de Python de JSON a \
una tabla HTML con encabezados de columna y título: {data}
"""
response = get_completion(prompt)
print(response)
```

```
<table>
  <caption>resturant employees</caption>
  <thead>
    <tr>
      <th>name</th>
      <th>email</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Shyam</td>
      <td>shyamjaiswal@gmail.com</td>
    </tr>
    <tr>
      <td>Bob</td>
      <td>bob32@gmail.com</td>
    </tr>
    <tr>
      <td>Jai</td>
      <td>jai87@gmail.com</td>
    </tr>
  </tbody>
</table>
```

Vista HTML:

<table>
  <caption>resturant employees</caption>
  <thead>
    <tr>
      <th>name</th>
      <th>email</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Shyam</td>
      <td>shyamjaiswal@gmail.com</td>
    </tr>
    <tr>
      <td>Bob</td>
      <td>bob32@gmail.com</td>
    </tr>
    <tr>
      <td>Jai</td>
      <td>jai87@gmail.com</td>
    </tr>
  </tbody>
</table>

Si estas usando un _notebook_, para visualizar el output:

```python
from IPython.display import display, Markdown, Latex, HTML, JSON

display(HTML(response))
```

## Revisión de ortografía/gramática

Estos son algunos ejemplos de problemas comunes de gramática/ortografía y la respuesta del _LLM_.

Para indicarle al _LLM_ corrija el texto, indicar al modelo que "revise" o "revise y corrija".

```python
text = [ 
  "La niña con los cachorros blancos y negros tienen una pelota.",
  # La niña tiene una pelota.
  "Yolanda tiene su libreta.",
  # ok
  "El barco emprendió un viaje asia el continente de Hacia.",
  # Homónima
  "Tu papel es muy vello, pero si sales así podrías cortarte el bello.",
  # Homónima
  "Esta fraze ez para berifikar la kapazidad de hortografia de chatGPT "
  # ortografía
]
for t in text:
    prompt = f"""Revisa y corrige el siguiente texto y 
    reescribe la versión corregida. Si no encuentras
    ningun error, solo di "No se encontraron errores". No
    uses ninguna puntuación alrededor del texto:
    ```{t}```"""
    response = get_completion(prompt)
    print(response)
```

Output:
```
La niña con los cachorros blancos y negros tiene una pelota.
No se encontraron errores.
El barco emprendió un viaje hacia el continente de Asia.
Tu papel es muy bello, pero si sales así podrías cortarte el pelo.
Esta frase es para verificar la capacidad de ortografía de ChatGPT.
```

```python
text = f"""
Tengo esto para mi hija por el cumpleaños de mi hija pq sigue \
tomando el mío de mi habitación.  Sí, a los adultos también \
les gustan los pandas.  Ella lo lleva a todas partes, y es \
super suave y lindo.  Una de las orejas está un poco más \
baja que la otra, y no creo que fuera diseñado para ser \
asimétrico. Es un poco pequeño para lo que pagué por el. \
Creo que podrían haber otras opciones más grandes \
por el mismo precio. LLegó un día antes de lo esperado, así \
que pude jugar con él antes de dárselo a mi hija,
"""
prompt = f"revisa y corrige esta reseña: ```{text}```"
response = get_completion(prompt)
print(response)
```

Output:
```
Tengo esto para mi hija por su cumpleaños, porque sigue tomando
el mío de mi habitación. Sí, a los adultos también les gustan
los pandas. Ella lo lleva a todas partes y es súper suave y lindo.
Una de las orejas está un poco más baja que la otra, y no creo
que haya sido diseñado para ser asimétrico. Es un poco pequeño
para lo que pagué por él. Creo que podría haber otras opciones
más grandes por el mismo precio. Llegó un día antes de lo
esperado, así que pude jugar con él antes de dárselo a mi hija.
```

Si estas usando un _notebook_:
```python
from redlines import Redlines

diff = Redlines(text,response)
display(Markdown(diff.output_markdown))
```

Output:

Tengo esto para mi hija por **~~el cumpleaños de mi hija pq~~ su cumpleaños,
porque** sigue tomando el mío de mi **~~habitación.~~ habitación**. Sí, a los
adultos también les gustan los **~~pandas. pandas.~~** Ella lo lleva a todas
**~~partes,~~ partes** y es **~~super~~ súper** suave y **~~lindo.~~ lindo.**
Una de las orejas está un poco más baja que la otra, y no creo que
**~~fuera~~ haya** sido diseñado para ser asimétrico. Es un poco pequeño para
lo que pagué por **~~el.~~ él.** Creo que **~~podrían~~ podría** haber otras
opciones más grandes por el mismo precio. **~~LLegó~~ Llegó** un día antes de
lo esperado, así que pude jugar con él antes de dárselo a mi **~~hija,~~ hija.**

```python
prompt = f"""
revisar y corregir esta reseña. Hazlo más convincente.
Asegúrate que siga la guía de estilo APA y esté \
dirigido a un lector avanzado.
Salido de formato markdown.
Texto: ```{text}```
"""
response = get_completion(prompt)
display(Markdown(response))
```

```
La elección de un regalo para el cumpleaños de mi hija fue fácil
gracias a este adorable panda de peluche. Aunque es común pensar
que los peluches son solo para niños, este panda ha demostrado
ser un éxito entre adultos también. Su suavidad y ternura lo
hacen irresistible para llevarlo a todas partes.

Sin embargo, debo mencionar que una de las orejas del panda está
un poco más baja que la otra, lo que lo hace asimétrico. No creo
que esto haya sido intencional en el diseño, pero no afecta su
encanto. Además, el tamaño del peluche es un poco pequeño para
el precio que pagué. Creo que podría haber opciones más grandes
disponibles por el mismo precio.

A pesar de estos pequeños detalles, el panda llegó un día antes
de lo esperado, lo que me permitió jugar con él antes de
entregárselo a mi hija. En general, estoy satisfecho con mi
compra y recomendaría este peluche a cualquier persona que busque
un regalo lindo y suave para un ser querido.
```

---

[<kbd> <br> Anterior <br> </kbd>][anterior]
[<kbd> <br> Siguiente <br> </kbd>][siguiente]

[anterior]: 05-inferir.md
[siguiente]: 07-expandir.md
