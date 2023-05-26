import openai
import webbrowser
from configparser import ConfigParser
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter.filedialog import asksaveasfile


class Message:

    @staticmethod
    def ask_api():
        return askstring("API KEY", "Set your API_KEY")

    @staticmethod
    def api_error():
        messagebox.showerror("Error", "Error: Set API KEY first!")

    @staticmethod
    def show_error():
        messagebox.showerror(
            "Error",
            "\n".join((
                "Something went wrong!",
                "Check your API_KEY again!"
            )),
        )

    @staticmethod
    def save(content):
        file = asksaveasfile(
            title="Save as",
            filetypes= (
                ("All files", "*.*"),
                ("Python file", "*.py"),
                ("Markdown document", "*.md"),
                ("Text document", "*.txt"),
            ),
        )
        try:
            file.write(str(content))
        except:
            pass
        else:
            file.close()

    @staticmethod
    def callback(url):
        webbrowser.open_new_tab(url)


def get_cfg(filename="config.ini"):
    config = ConfigParser()
    config.read(filename)
    return config


def get_completion(
    prompt,
    api_key=None,
    model="gpt-3.5-turbo",
    temperature=0,
):
    openai.api_key = api_key
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]
