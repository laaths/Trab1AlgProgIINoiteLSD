from tkinter import *
import tkinter

class cadCidade:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.Container1 = Frame( master )
        self.Container1["pady"] = 10
        self.Container1.pack()

        self.Container2 = Frame( master )
        self.Container2["padx"] = 20
        self.Container2.pack()

        self.Container3 = Frame( master )
        self.Container3["padx"] = 20
        self.Container3.pack()

        self.Container4 = Frame( master )
        self.Container4["pady"] = 20
        self.Container4.pack()

        self.titulo = Label( self.Container1, text="Cadastrar Cidade" )
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabel = Label( self.Container2, text="Nome: ", font=self.fontePadrao )
        self.nomeLabel.pack( side=LEFT )
        self.nome = Entry(self.Container2)
        self.nome["width"] = 20
        self.nome.pack(side=RIGHT)

        self.codigoLabel = Label( self.Container3, text="Código Cidade:", font=self.fontePadrao )
        self.codigoLabel.pack( side=LEFT )
        self.codigo = Label( self.Container3, text=self.gerCodigoCidade(), font=self.fontePadrao )
        self.codigo.pack( side=RIGHT )

        self.enviar = Button( self.Container4 )
        self.enviar["text"] = "Enviar"
        self.enviar["font"] = ("Calibri", "11")
        self.enviar["width"] = 15
        self.enviar["command"] = self.sendCidade()
        self.enviar.pack()

    def sendCidade(self):
        pass

    def gerCodigoCidade(self):
        return "0000"



root = Tk()
cadCidade(root)
root.geometry( '300x200' )
root.configure()
root.mainloop()