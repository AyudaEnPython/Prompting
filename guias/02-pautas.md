# Pautas para Prompting

## Setup

Bibliotecas necesarias:
- [openai](https://pypi.org/project/openai/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)


## Principios

- [Principio 1](#principio-1-escribir-instrucciones-claras-y-específicas): Escribir instrucciones claras y específicas
- [Principio 2](#principio-2-darle-al-modelo-timpo-para-pensar): Darle al modelo tiempo para "pensar"

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
AyudaEnPython es una comunidad que ofrece ayuda y soporte en cualquier nivel de conocimiento sobre Python, además de compartir información y experiencias relacionadas con este lenguaje de programación.
```

#### Táctica 2: Pedir una salida estructurada

#### Táctica 3: Pedir al modelo que revise si las condiciones fueron satisfactorias

#### Táctica 4: "Few-shot" prompting

### Principio 2: Darle al modelo timpo para pensar

#### Táctica 1: Especificar los pasos requeridos para completar una tarea

#### Táctica 2: Instruir al modelo para que trabaje en su propia solución antes de precipitarse a una conclusión
