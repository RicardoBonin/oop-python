from pessoa import Pessoa

p1 = Pessoa("Luiz", 29)
p2 = Pessoa("João", 32)


p1 = Pessoa("Luiz", 29)
p2 = Pessoa("João", 32)

print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()

print(Pessoa.gera_id())
