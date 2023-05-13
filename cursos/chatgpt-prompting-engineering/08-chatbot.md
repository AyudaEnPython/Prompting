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

> _**NOTA**_: los siguientes códigos son para usarlos en un _notebook_.

```python
def collect_messages(_):
    prompt = inp.value_input
    inp.value = ''
    context.append({'role':'user', 'content':f"{prompt}"})
    response = get_completion_from_messages(context) 
    context.append({'role':'assistant', 'content':f"{response}"})
    panels.append(
        pn.Row('User:', pn.pane.Markdown(prompt, width=600)))
    panels.append(
        pn.Row('Assistant:', pn.pane.Markdown(response, width=600, style={'background-color': '#F6F6F6'})))
 
    return pn.Column(*panels)

```

```python
import panel as pn  # GUI
pn.extension()

panels = [] # collect display 

context = [ {'role':'system', 'content':"""
You are OrderBot, an automated service to collect orders for a pizza restaurant. \
You first greet the customer, then collects the order, \
and then asks if it's a pickup or delivery. \
You wait to collect the entire order, then summarize it and check for a final \
time if the customer wants to add anything else. \
If it's a delivery, you ask for an address. \
Finally you collect the payment.\
Make sure to clarify all options, extras and sizes to uniquely \
identify the item from the menu.\
You respond in a short, very conversational friendly style. \
The menu includes \
pepperoni pizza  12.95, 10.00, 7.00 \
cheese pizza   10.95, 9.25, 6.50 \
eggplant pizza   11.95, 9.75, 6.75 \
fries 4.50, 3.50 \
greek salad 7.25 \
Toppings: \
extra cheese 2.00, \
mushrooms 1.50 \
sausage 3.00 \
canadian bacon 3.50 \
AI sauce 1.50 \
peppers 1.00 \
Drinks: \
coke 3.00, 2.00, 1.00 \
sprite 3.00, 2.00, 1.00 \
bottled water 5.00 \
"""} ]  # accumulate messages


inp = pn.widgets.TextInput(value="Hi", placeholder='Enter text here…')
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
messages.append(
{'role':'system', 'content':'create a json summary of the previous food order. Itemize the price for each item\
 The fields should be 1) pizza, include size 2) list of toppings 3) list of drinks, include size   4) list of sides include size  5)total price '},    
)
 #The fields should be 1) pizza, price 2) list of toppings 3) list of drinks, include size include price  4) list of sides include size include price, 5)total price '},    

response = get_completion_from_messages(messages, temperature=0)
print(response)
```

---

[<kbd> <br> Anterior <br> </kbd>][anterior]
[<kbd> <br> Siguiente <br> </kbd>][siguiente]

[anterior]: 07-expandir.md
[siguiente]: 09-conclusion.md
