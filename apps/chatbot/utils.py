import os
import openai

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")


def get_completion(prompt, model="gpt-3.5-turbo", temperature=0):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]


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


def collect_messages(_, user_input, context, panels, panel):
    prompt = user_input.value_input
    user_input.value = ''
    context.append({'role':'user', 'content':f"{prompt}"})
    response = get_completion_from_messages(context) 
    context.append({'role':'assistant', 'content':f"{response}"})
    panels.append(
        panel.Row('Usuario:', panel.pane.Markdown(prompt, width=600)))
    panels.append(
        panel.Row('Asistente:', panel.pane.Markdown(
            response, width=600,
        )))
    return panel.Column(*panels)



def read_content(filename="content.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()
