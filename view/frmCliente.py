from tkinter import *
from tkinter import ttk
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

        #self.tipo = Label( self.container5, text="Tipo: ", font=self.fontePadrao )
        #self.tipo["width"] = 20
        #self.tipo.pack(side=LEFT)
        self.var = StringVar
        self.tipoPF = Radiobutton(self.container5, text="Pessoa Física",  value="PF", variable=self.var)
        self.tipoPJ = Radiobutton(self.container5, text="Pessoa Jurídica", value="PJ", variable=self.var)
        self.tipoPF.pack()
        self.tipoPJ.pack()

        self.cpf = Label( self.container6, text="CPF: ", font=self.fontePadrao )
        self.cpf.pack( side=LEFT )
        self.cpf = Entry( self.container6 )
        self.cpf["width"] = 20
        self.cpf.pack( side=LEFT )

        self.cnpj = Label( self.container7, text="CNPJ: ", font=self.fontePadrao )
        self.cnpj.pack( side=LEFT )
        self.cnpj = Entry( self.container7 )
        self.cnpj["width"] = 20
        self.cnpj.pack( side=LEFT )

        self.cidade = Label( self.container8, text="Cidade: ", font=self.fontePadrao )
        self.cidade.pack( side=LEFT )
        self.cidade = ttk.Combobox(self.container8, values=self.GetCidades())
        self.cidade["width"] = 20
        self.cidade.pack( side=LEFT )

        self.receberemail = Checkbutton(self.container9, text="Aceiro receber e-mail", font=self.fontePadrao)
        self.receberemail["width"] = 20
        self.receberemail.pack( side=LEFT )

        self.save = Button( self.container10, text="Salvar", font=self.fontePadrao )
        self.save.pack( side=LEFT )
        self.reset = Button( self.container10, text="Limpar", font=self.fontePadrao )
        self.reset.pack( side=RIGHT )

    def geraCodigoCliente(self):
        return "0000"

    def GetCidades(self):
        return ["", "Porto Alegre", "Cachoeirinha", "Canoas", "Gravatai"]

    def rButt(self):
        PfPj = [("Pessoa Física", "PF"), ("Pessoa Jurídica", "PJ")]
        v = StringVar()
        v.set("L")
        for t, md in PfPj:
            b = Radiobutton(text=t, variable=v, value=md)
            b.pack(anchor=W)


root = Tk()
Application(root)
root.geometry( '300x450' )
root.mainloop()
