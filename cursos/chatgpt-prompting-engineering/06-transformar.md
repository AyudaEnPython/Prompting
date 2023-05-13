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

```python
```

```
```

## Transformar tono

```python
```

```
```

## Conversión de formato

```python
```

```
```

## Revisión de ortografía/gramática

```python
```

```
```

---

[<kbd> <br> Anterior <br> </kbd>][anterior]
[<kbd> <br> Siguiente <br> </kbd>][siguiente]

[anterior]: 05-inferir.md
[siguiente]: 07-expandir.md
