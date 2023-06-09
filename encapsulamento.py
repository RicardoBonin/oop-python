"""
public, protected, private
_ protected
__ private
"""


class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    def inserir_cliente(self, id, nome):
        if "clientes" not in self.__dados:
            self.__dados["clientes"] = {id: nome}
        else:
            self.__dados["clientes"].update({id: nome})

    def lista_client(self):
        list(map(lambda client: print(client), self.__dados["clientes"].items()))
        return

    def apaga_cliente(self, id):
        del self.__dados["clientes"][id]


bd = BaseDeDados()
bd.inserir_cliente(1, "Otávio")
bd.inserir_cliente(2, "Miranda")
bd.inserir_cliente(3, "Rose")
bd.apaga_cliente(2)
bd.lista_client()
