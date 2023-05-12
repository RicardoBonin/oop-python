from classes import Cliente

cliente1 = Cliente("Luiz", 55)
cliente1.insere_enderecos("Belo Horizonte", "MG")
print(cliente1.nome)
cliente1.lista_enderecos()
print()

cliente2 = Cliente("Maria", 55)
cliente2.insere_enderecos("Salvador", "BA")
cliente2.insere_enderecos("Rio de Janeiro", "RJ")
print(cliente2.nome)
cliente2.lista_enderecos()
print()

cliente3 = Cliente("João", 55)
cliente3.insere_enderecos("São Paulo", "SP")
print(cliente3.nome)
cliente3.lista_enderecos()
print()
