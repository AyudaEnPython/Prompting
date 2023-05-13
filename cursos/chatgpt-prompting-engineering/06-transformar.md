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

Imagina que estás a cargo de IT en una gran empresa multinacional de comercio electrónico. Los usuarios te envían mensajes con problemas relacionados a IT, todos en sus idiomas nativos. Tu personal es de todo el mundo y solo hablan sus idiomas nativos. !Necesitas un traductor universal!

```python
user_messages = [
  # El rendimiento del sistema es más lento de lo normal
  "La performance du système est plus lente que d'habitude.", 
  # Mi monitor tiene píxeles que no se iluminan
  "My monitor has pixels that are not lighting",
  # Mi ratón no está funcionando
  "Il mio mouse non funziona",
  # Mi teclado tiene una tecla de control rota
  "Mój klawisz Ctrl jest zepsuty",
  # Mi pantalla parpadea
  "我的屏幕在闪烁",
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
  # The girl has a ball.
  "The girl with the black and white puppies have a ball.",
  # ok
  "Yolanda has her notebook.",
  # Homonyms
  "Its going to be a long day. Does the car need it’s oil changed?",
  # Homonyms
  "Their goes my freedom. There going to bring they’re suitcases.",
  # Homonyms
  "Your going to need you’re notebook.",
  # Homonyms
  "That medicine effects my ability to sleep. Have you heard of the butterfly affect?",
  # spelling
  "This phrase is to cherck chatGPT for speling abilitty"
]
for t in text:
    prompt = f"""Proofread and correct the following text
    and rewrite the corrected version. If you don't find
    and errors, just say "No errors found". Don't use 
    any punctuation around the text:
    ```{t}```"""
    response = get_completion(prompt)
    print(response)
```

Output:
```
The girl with the black and white puppies has a ball.
No errors found.
It's going to be a long day. Does the car need its oil changed?
Their goes my freedom. There going to bring they're suitcases.

Corrected version: 
There goes my freedom. They're going to bring their suitcases.
You're going to need your notebook.
That medicine affects my ability to sleep. Have you heard of the
butterfly effect?
This phrase is to check ChatGPT for spelling ability.
```

```python
text = f"""
Got this for my daughter for her birthday cuz she keeps taking \
mine from my room.  Yes, adults also like pandas too.  She takes \
it everywhere with her, and it's super soft and cute.  One of the \
ears is a bit lower than the other, and I don't think that was \
designed to be asymmetrical. It's a bit small for what I paid for it \
though. I think there might be other options that are bigger for \
the same price.  It arrived a day earlier than expected, so I got \
to play with it myself before I gave it to my daughter.
"""
prompt = f"proofread and correct this review: ```{text}```"
response = get_completion(prompt)
print(response)
```

Output:
```
I got this for my daughter's birthday because she keeps taking mine
from my room. Yes, adults also like pandas too. She takes it everywhere 
with her, and it's super soft and cute. However, one of the ears is a
bit lower than the other, and I don't think that was designed to be 
asymmetrical. Additionally, it's a bit small for what I paid for it.
I think there might be other options that are bigger for the same price. 
On the positive side, it arrived a day earlier than expected, so I got
to play with it myself before I gave it to my daughter.
```

```python
from redlines import Redlines

diff = Redlines(text,response)
display(Markdown(diff.output_markdown))
```

Output:
```
~~Got~~ I got this for my ~~daughter~~ for her daughter's birthday ~~cuz~~ 
because she keeps taking mine from my ~~room.~~ room. Yes, adults also 
like pandas ~~too.~~ too. She takes it everywhere with her, and it's super 
soft and ~~cute. One~~ cute. However, one of the ears is a bit lower than
the other, and I don't think that was designed to be asymmetrical.
~~It's~~ Additionally, it's a bit small for what I paid for ~~it though.~~
it. I think there might be other options that are bigger for the same
~~price. It~~ price. On the positive side, it arrived a day earlier than
expected, so I got to play with it myself before I gave it to my
~~daughter.~~ daughter.

```

```python
prompt = f"""
proofread and correct this review. Make it more compelling. 
Ensure it follows APA style guide and targets an advanced reader. 
Output in markdown format.
Text: ```{text}```
"""
response = get_completion(prompt)
display(Markdown(response))
```

```
Title: A Soft and Cute Panda Plushie for All Ages

As an adult, I can attest that pandas are not just for kids. That's
why I got this adorable panda plushie for my daughter's birthday,
after she kept taking mine from my room. And let me tell you, it
was a hit!

The plushie is super soft and cuddly, making it the perfect
companion for my daughter. She takes it everywhere with her, and
it has quickly become her favorite toy. However, I did notice that
one of the ears is a bit lower than the other, which I don't think
was designed to be asymmetrical. But that doesn't take away from
its cuteness.

The only downside is that it's a bit small for the price I paid.
I think there might be other options that are bigger for the same
price. But overall, I'm happy with my purchase.

One thing that surprised me was that it arrived a day earlier than 
expected. This gave me the chance to play with it myself before
giving it to my daughter. And let me tell you, it's just as fun for
adults as it is for kids.

In conclusion, if you're looking for a soft and cute panda plushie
that's perfect for all ages, this is definitely a great option.
Just be aware that it might be a bit small for the price. But trust
me, the cuteness factor makes up for it.

```

---

[<kbd> <br> Anterior <br> </kbd>][anterior]
[<kbd> <br> Siguiente <br> </kbd>][siguiente]

[anterior]: 05-inferir.md
[siguiente]: 07-expandir.md
