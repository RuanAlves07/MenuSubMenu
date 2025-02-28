# EXERCICIO 2

from tkinter import *

class janela:
    def __init__(self, instancia_de_tk):
        self.menu = Menu(instancia_de_tk, tearoff = 0)
        self.menu.add_command(label = "Ola 1", command = self.ola)
        self.menu.add_command(label = "Ola 2", command = self.ola)

        frame = Frame(instancia_de_tk, width = 200, height = 200)
        frame.pack()
        frame.bind("<Button-3>", self.popup)

        mainloop()

    def ola(self):

        print("Olá!")
    
    def popup(self, e): self.menu.post(e.x_root, e.y_root)

raiz = Tk()
janela(raiz)
raiz.mainloop()
