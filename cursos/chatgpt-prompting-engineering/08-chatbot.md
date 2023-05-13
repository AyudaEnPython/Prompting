# Chatbot

Exploraremos como utilizar el formato de chat para extender las conversaciones con bots conversacionales (chatbots) personalizados o especializados para una tarea o comportamiento específico.


```python
messages =  [  
{'role':'system', 'content':'Eres un asistente que habla como Shakespeare.'},    
{'role':'user', 'content':'Cuéntame un chiste'},   
{'role':'assistant', 'content':'¿Por qué cruzó el pollo la carretera?'},   
{'role':'user', 'content':'No lo sé'}  ]
```

```python
response = get_completion_from_messages(messages, temperature=1)
print(response)
```

```python
messages =  [  
{'role':'system', 'content':'Eres un chatbot amigable.'},    
{'role':'user', 'content':'Hola, mi nombre es John'}  ]
response = get_completion_from_messages(messages, temperature=1)
print(response)
```


```python
messages =  [  
{'role':'system', 'content':'Eres un chatbot amigable.'},    
{'role':'user', 'content':'Si, ¿puedes recordarme cuál es mi nombre?'}  ]
response = get_completion_from_messages(messages, temperature=1)
print(response)
```

```python
messages =  [  
{'role':'system', 'content':'Eres un chatbot amigable.'},    
{'role':'user', 'content':'Hola, mi nombre es John'}  ]
{'role':'assistant', 'content': "Hola John! Encantado de conocerte. \
¿Hay algo en lo que pueda ayudarte hoy?"},
{'role':'user', 'content':'Si, ¿puedes recordarme cuál es mi nombre?'}  ]
response = get_completion_from_messages(messages, temperature=1)
print(response)
```

## Bot de órdenes

Podemos automatizar la recopilación de los _prompts_ del usuario y las respuestas del asistente para crear un `OrderBot`. El `OrderBot` tomará pedidos en un restaurante de pizza.

---

[<kbd> <br> Anterior <br> </kbd>][anterior]
[<kbd> <br> Siguiente <br> </kbd>][siguiente]

[anterior]: 07-expandir.md
[siguiente]: 09-conclusion.md
