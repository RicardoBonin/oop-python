from pessoa import Pessoa
#  https://www.youtube.com/watch?v=RLVbB91A5-8&list=PLbIBj8vQhvm34qAAEEH_PdL2tMG9rz-P7&index=1

p1 = Pessoa("Luiz", 29)
p2 = Pessoa('João', 32)



p1 = Pessoa('Luiz', 29)
p2 = Pessoa('João', 32)

print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()

print(Pessoa.gera_id())