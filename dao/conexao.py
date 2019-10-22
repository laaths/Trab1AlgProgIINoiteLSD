import sqlite3

class connBanco():
    def __init__(self):
        self.conexao = sqlite3.connect('bancoAlgProgII.db')
        self.createTables()

    def createTables(self):
        c = self.conexao.cursor()
        c.execute("""create table if not exists clientes (
                 idusuario integer primary key autoincrement ,
                 nome text,
                 email text,
                 cpf_cnpj text,
                 receberEmail text,
                 tipo text,
                 codCidade int)                 
                 """)
        c.execute("""create table if not exists cidades (
                  nome text)
                  """)
        self.conexao.commit()
        c.close()