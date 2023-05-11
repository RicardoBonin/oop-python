from classes import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor("Joãozinho")
caneta = Caneta("Bic")
maquina = MaquinaDeEscrever()

print(escritor.nome)
print(caneta.marca)
print(maquina)

escritor.ferramenta = maquina
escritor.ferramenta.escrever()
