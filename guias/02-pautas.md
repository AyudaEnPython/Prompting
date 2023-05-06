# Pautas para Prompting

## Setup

Bibliotecas necesarias:
- [openai](https://pypi.org/project/openai/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)


## Principios

- Principio 1: Escribir instrucciones claras y específicas
- Principio 2: Darle al modelo tiempo para "pensar"

### Principio 1: Escribir instrucciones claras y específicas

Debes expresar lo que quieres que el modelo haga, entregando instrucciones tan claras y específicas como puedas. 

No confundir escribir un "_prompt_ claro" con un "_prompt_ corto", porque en muchos casos _prompts_ mas largos en realidad brindan más claridad y contexto, conduciendo a resultados más detallados y relvantes.

#### Táctica 1: Usar delimitadores para indicar claramente distintas partes de la entrada

#### Táctica 2: Pedir una salida estructurada

#### Táctica 3: Pedir al modelo que revise si las condiciones fueron satisfactorias

#### Táctica 4: "Few-shot" prompting

### Principio 2: Darle al modelo timpo para pensar

#### Táctica 1: Especificar los pasos requeridos para completar una tarea

#### Táctica 2: Instruir al modelo para que trabaje en su propia solución antes de precipitarse a una conclusión
