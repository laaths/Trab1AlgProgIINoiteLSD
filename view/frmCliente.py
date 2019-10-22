from tkinter import *
class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.container1 = Frame( master )
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame( master )
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame( master )
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame( master )
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame( master )
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame( master )
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = Frame( master )
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        self.container8 = Frame( master )
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()
        self.container9 = Frame( master )
        self.container9["pady"] = 15
        self.container9.pack()
        self.container10 = Frame( master )
        self.container10["pady"] = 15
        self.container10.pack()

        self.titulo = Label( self.container1, text="Cadastrar Cliente", font=self.fontePadrao )
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.codigo = Label( self.container2, text="Código Cliente: ", font=self.fontePadrao )
        self.codigo.pack(side=LEFT)
        self.codigo = Label( self.container2, text=self.geraCodigoCliente(), font=self.fontePadrao )
        self.codigo.pack(side=RIGHT)

        self.nome = Label(self.container3, text="Nome: ", font=self.fontePadrao)
        self.nome.pack(side=LEFT)
        self.nome = Entry(self.container3)
        self.nome["width"] = 20
        self.nome.pack(side=LEFT)

        self.email = Label( self.container4, text="E-mail: ", font=self.fontePadrao )
        self.email.pack( side=LEFT )
        self.email = Entry( self.container4 )
        self.email["width"] = 20
        self.email.pack( side=LEFT )

        self.tipo = Label( self.container5, text="Tipo: ", font=self.fontePadrao )
        self.tipo.pack( side=LEFT )
        self.tipo = Entry( self.container5 )
        self.tipo["width"] = 20
        self.tipo.pack( side=LEFT )

    def geraCodigoCliente(self):
        return "0000"

root = Tk()
Application(root)
root.geometry( '300x300' )
root.mainloop()
