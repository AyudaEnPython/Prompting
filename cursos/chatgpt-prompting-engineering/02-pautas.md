# Pautas para Prompting

## Configuración 

Bibliotecas necesarias:
- [openai](https://pypi.org/project/openai/)
- [python-dotenv](https://pypi.org/project/python-dotenv/) (opcional)

Para instalarlas, abrir un terminal escribir:
```terminal
> pip install openai
```

> _**NOTA**_: Si se trabaja con _notebooks_, anteponer `!`, por ejemplo `!pip install openai` 

La biblioteca `openai` necesita se configurada con la clave secreta de tu cuenta, la cual esta disponible en su [página](https://platform.openai.com/account/api-keys)

Se puede establecer como variable de entorno:

```
!export OPENAI_API_KEY='sk-...'
```

O, establecerla con su valor:
```python
import openai

openai.api_key = 'sk-...'
```

Para esta ultima forma, no es necesario `python_dotenv` (no recomendable).

Importar las bibliotecas y cargar la clave API:
```python
import os
import openai

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())
openai.api_key  = os.getenv('OPENAI_API_KEY')
```

Función _helper_:

```python
def get_completion(prompt, model="gpt-3.5-turbo", temperature=0):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]
```

Para más información consultar la [documentación](https://platform.openai.com/docs/guides/chat) de `openai`.

---

## Principios

- [Principio 1](#principio-1-escribir-instrucciones-claras-y-específicas): Escribir instrucciones claras y específicas
- [Principio 2](#principio-2-darle-al-modelo-timpo-para-pensar): Darle al modelo tiempo para "pensar"

---

### Principio 1: Escribir instrucciones claras y específicas

Debes expresar lo que quieres que el modelo haga, proporcionando instrucciones tan claras y específicas como puedas. Esto guiará al modelo hacia la salida esperada y reducirá las posibilidades de recibir respuestas irrelevantes o incorrectas.

No confundir escribir un "_prompt_ claro" con un "_prompt_ corto". En muchos casos, _prompts_ mas largos en realidad brindan más claridad y contexto, conduciendo a resultados más detallados y relvantes.

#### Táctica 1: Usar delimitadores para indicar claramente distintas partes de la entrada

Los delimitadores pueden ser:
- Triple quotes: """
- Triple backticks: ```
- Triple dashes: ---
- Angle brackets: <>
- XML tags: `<tag> </tag>`

```python
text = f"""
AyudaEnPython es una comunidad dedicada a brindar apoyo \
a cualquier problema sobre Python (principiante, intermedio \
avanzado), compartir información, conocimientos y experiencias \
relacionadas.
"""

prompt = f"""
Resume el texto delimitado backticks triples
```{text}```
"""
response = get_completion(prompt)
print(response)
```

Output:

```
AyudaEnPython es una comunidad que ofrece ayuda y soporte en cualquier
nivel de conocimiento sobre Python, además de compartir información y
experiencias relacionadas con este lenguaje de programación.
```

#### Táctica 2: Pedir una salida estructurada
- JSON
- HTML

```python
prompt = f"""
Generar una lista de tres títulos de libros inventados con \
sus autores y géneros. \
Proporcionarlos en formato JSON con las siguientes claves: book_id, \
title, author, genre.
"""
response = get_completion(prompt)
print(response)
```

Output:
```
{
    "books": [
        {
            "book_id": 1,
            "title": "El jardín de las mariposas",
            "author": "Ana García",
            "genre": "Drama"
        },
        {
            "book_id": 2,
            "title": "La ciudad de los sueños",
            "author": "Carlos Pérez",
            "genre": "Ciencia ficción"
        },
        {
            "book_id": 3,
            "title": "El secreto de la montaña",
            "author": "María López",
            "genre": "Misterio"
        }
    ]
}
```

#### Táctica 3: Pedir al modelo que revise si las condiciones fueron satisfactorias

#### Táctica 4: "Few-shot" prompting

---

### Principio 2: Darle al modelo timpo para pensar

#### Táctica 1: Especificar los pasos requeridos para completar una tarea

#### Táctica 2: Instruir al modelo para que trabaje en su propia solución antes de precipitarse a una conclusión

---

[<kbd> <br> Anterior <br> </kbd>][anterior]
[<kbd> <br> Siguiente <br> </kbd>][siguiente]

[anterior]: 01-introduccion.md
[siguiente]: 03-iterativo.md
