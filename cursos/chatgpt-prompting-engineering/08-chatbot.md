# Chatbot

Exploraremos como utilizar el formato de chat para extender las conversaciones con bots conversacionales (chatbots) personalizados o especializados para una tarea o comportamiento específico.

## Configuración adicional

Función _helper_:
```python
def get_completion_from_messages(
        messages,
        model="gpt-3.5-turbo",
        temperature=0,
):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]
```

---

Roles:
- user: el usuario que interactúa con el modelo
- assistant: el modelo
- system: establece el comportamiento del modelo

Si alguna vez has usado _ChatGPT_ (la interfaz web), entonces tus mensajes son los mensajes de **usuario** (`user`), los mensajes de _ChatGPT_ son los mensajes del **asistente** (`assistant`), y el **sistema** (`system`) ayuda a establecer el comportamiento y personalidad del asistente (actúa como una instrucción de alto nivel para la conversación). Por lo tanto, se puede considerar al sistema como un susurro al oído del asistente y una forma de guiar sus respuestas sin que el usuario se dé cuenta del mensaje del sistema.

```python
messages =  [  
{'role':'system', 'content':'Eres un asistente que habla como Shakespeare.'},    
{'role':'user', 'content':'Cuéntame un chiste'},   
{'role':'assistant', 'content':'¿Por qué cruzó el pollo la carretera?'},   
{'role':'user', 'content':'No lo sé'}  ]
response = get_completion_from_messages(messages, temperature=1)
print(response)
```

Output:
```
Para llegar al otro lado, por supuesto. ¡Eso es lo que hacen los pollos!
```

```python
messages =  [  
{'role':'system', 'content':'Eres un chatbot amigable.'},    
{'role':'user', 'content':'Hola, mi nombre es John'}  ]
response = get_completion_from_messages(messages, temperature=1)
print(response)
```

Output:
```
¡Hola John! ¡Bienvenido! ¿En qué puedo ayudarte hoy?
```

```python
messages =  [  
{'role':'system', 'content':'Eres un chatbot amigable.'},    
{'role':'user', 'content':'Si, ¿puedes recordarme cuál es mi nombre?'}  ]
response = get_completion_from_messages(messages, temperature=1)
print(response)
```

Output:
```
Lo siento, pero como soy un chatbot, no tengo la capacidad de
recordar tu nombre, pero siempre puedes decírmelo y yo lo
utilizaré en nuestra conversación. ¿Cómo te llamas?
```

```python
messages =  [  
{'role':'system', 'content':'Eres un chatbot amigable.'},    
{'role':'user', 'content':'Hola, mi nombre es John'},
{'role':'assistant', 'content': "Hola John! Encantado de conocerte. \
¿Hay algo en lo que pueda ayudarte hoy?"},
{'role':'user', 'content':'Si, ¿puedes recordarme cuál es mi nombre?'}  ]
response = get_completion_from_messages(messages, temperature=1)
print(response)
```

Output:
```
¡Por supuesto! Tu nombre es John, ¿estoy en lo cierto?
```

## Bot de órdenes

Podemos automatizar la recopilación de los _prompts_ del usuario y las respuestas del asistente para crear un `OrderBot`. El `OrderBot` tomará pedidos en un restaurante de pizza.

> _**NOTA**_: los siguientes códigos son para usarlos en un _notebook_, si no los usas puedes revisar nuestra alternativa [aquí](chatbot/README.md)

```python
def collect_messages(_):
    prompt = inp.value_input
    inp.value = ''
    context.append({'role':'user', 'content':f"{prompt}"})
    response = get_completion_from_messages(context) 
    context.append({'role':'assistant', 'content':f"{response}"})
    panels.append(
        pn.Row('Usuario:', pn.pane.Markdown(prompt, width=600)))
    panels.append(
        pn.Row('Asistente:', pn.pane.Markdown(response, width=600, style={'background-color': '#F6F6F6'})))
    return pn.Column(*panels)
```

```python
import panel as pn

pn.extension()
panels = [] 

context = [ {'role':'system', 'content':"""
Eres OrderBot, un servicio automatizado para recolectar ordenes para \
una pizzería.
Primero saludas al cliente, luego recolectas el pedido, \
y luego preguntas si se trata de recoger el pedido o llevarlo.
Espera hasta recolectar todo el pedido, luego resúmelo y comprueba por \
última vez si el cliente quiere añadir algo más. \ 
Si es una entrega, pregunta la dirección. \
Finalmente cobra el pago.
Asegúrate de aclarar todas las opciones, extras y tamaños para \
identificar los elementos del menú. \
Responde en estilo corto, amigable y muy conversacional. \
El menú incluye \
pizza de pepperoni 12.95, 10.00, 7.00 \
pizza de queso   10.95, 9.25, 6.50 \
pizza de berenjena   11.95, 9.75, 6.75 \
papas fritas 4.50, 3.50 \
ensalada griega 7.25 \
Coberturas: \
queso extra 2.00, \
champiñones 1.50 \
salchicha 3.00 \
tocino canadiense 3.50 \
AI salsa 1.50 \
pimientos 1.00 \
Bebidas: \
coca cola 3.00, 2.00, 1.00 \
sprite 3.00, 2.00, 1.00 \
agua embotellada 5.00 \
"""} ]

inp = pn.widgets.TextInput(value="Hola", placeholder='Ingresar texto aquí...')
button_conversation = pn.widgets.Button(name="Chat!")
interactive_conversation = pn.bind(collect_messages, button_conversation)
dashboard = pn.Column(
    inp,
    pn.Row(button_conversation),
    pn.panel(interactive_conversation, loading_indicator=True, height=300),
)
dashboard
```

```python
messages =  context.copy()
messages.append({'role':'system', 'content':"""
Crea un resumen en json del pedido de comida anterior. \
Detalla el precio de cada artículo. \
Los campos deben ser \
1) pizza, incluir el tamaño \
2) lista de ingredientes \
3) lista de bebidas, incluir tamaño \
4) lista de acompañamientos, incluir tamaño \
5) precio total """
})

response = get_completion_from_messages(messages, temperature=0)
print(response)
```

> _**NOTA**: revisa nuestros repositorios para la integración de un chatbot en CLI, GUI, WebApp.

---

[<kbd> <br> Anterior <br> </kbd>][anterior]
[<kbd> <br> Siguiente <br> </kbd>][siguiente]

[anterior]: 07-expandir.md
[siguiente]: 09-conclusion.md
