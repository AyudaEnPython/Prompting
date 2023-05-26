from enum import Enum
from tkinter import Button, Entry, Frame, Label, Text


class Color(Enum):
    fg = "white"
    hover = "cyan"
    inner_bg = "gray8"
    footer_bg = "gray12"


class Commands(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.configure(bg=Color.inner_bg.value)
        self.setup_ui(master.CFG)

    def setup_ui(self, cfg):
        self.submit = Button(self, text="Send message", **cfg["BUTTON"])
        self.clear = Button(self, text="Clear", **cfg["BUTTON"])
        self.save = Button(self, text="Save", **cfg["BUTTON"])
        self.key = Button(self, text="Set API Key", **cfg["BUTTON"])
        self.quit = Button(self, text="Quit", **cfg["QUIT"])
        self.submit.grid(row=1, column=0, **cfg["PAD"])
        self.clear.grid(row=1, column=1, **cfg["PAD"])
        self.save.grid(row=1, column=2, **cfg["PAD"])
        self.key.grid(row=1, column=3, **cfg["PAD"]) 
        self.quit.grid(row=1, column=4, **cfg["PAD"])


class Chat(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.configure(bg=Color.inner_bg.value)
        self.setup_ui(master.CFG)

    def setup_ui(self, cfg):
        self.output = Text(self, **cfg["TEXT"])
        self.input = Entry(self, **cfg["ENTRY"])
        self.output.pack(padx=5, pady=5)
        self.input.pack(padx=5, pady=5, ipady=5)

    def clear_text(self):
        self.input.delete(0, "end")

    def set_text(self, text):
        self.output.config(state="normal")
        self.output.delete("1.0", "end")
        self.output.insert("end", text)
        self.output.config(state="disable")


class Link(Label):

    def __init__(self, master=None, link=None, func=None):
        super().__init__(master)
        self["text"] = link
        self["bg"] = Color.footer_bg.value
        self["fg"] = Color.fg.value
        self.bind("<Enter>", self._in)
        self.bind("<Leave>", self._out)
        self.bind("<Button-1>", lambda _: func(link))

    def _in(self, _):
        self["fg"] = Color.hover.value

    def _out(self, _):
        self["fg"] = Color.fg.value


class CustomBar(Frame):

    def __init__(self, master=None, callback=None):
        super().__init__(master)
        CFG = master.CFG
        self.configure(bg=Color.footer_bg.value)
        self.title = Link(self, link=CFG["INI"]["footer"], func=callback)
        self.title.pack()
