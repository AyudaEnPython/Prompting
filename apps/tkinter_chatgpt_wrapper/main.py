from tkinter import Tk

from frames import Commands, Chat, CustomBar
from utils import get_cfg, get_completion, Message


class App(Tk):

    def __init__(self):
        super().__init__()
        self.CFG = get_cfg()
        self.api_key = None
        self.response = ""
        self.configure(bg="gray8")
        self.title(self.CFG["INI"]["title"])
        self.iconbitmap(self.CFG["INI"]["path"])
        self.setup_ui()

    def setup_ui(self):
        self.footer = CustomBar(self, callback=Message.callback)
        self.chat = Chat(self)
        self.cmds = Commands(self)
        self.chat.pack(padx=25, pady=15)
        self.cmds.pack(padx=25, ipady=5)
        self.footer.pack(expand=1, fill="x")
        self.bind("<Return>", self.get_completion)
        self.cmds.submit.config(command=self.get_completion)
        self.cmds.clear.config(command=self.chat.clear_text)
        self.cmds.save.config(command=self.save_file)
        self.cmds.key.config(command=self.set_api_key)
        self.cmds.quit.config(command=self.destroy)

    def set_api_key(self):
        self.api_key = Message.ask_api()

    def get_completion(self, _=None):
        if not self.api_key:
            Message.api_error()
            return None
        try:
            response = get_completion(
                prompt=self.chat.input.get(),
                api_key=self.api_key,
            )
        except Exception:
            Message.show_error()
        else:
            self.chat.set_text(response)

    def save_file(self):
        print(self.chat.output.get(1.0, "end"))
        Message.save(self.chat.output.get(1.0, "end"))


if __name__ == "__main__":
    app = App()
    app.mainloop()
