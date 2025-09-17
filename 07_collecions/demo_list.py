
fruta = ["Pera", "Maçã", "Banana"]
print(fruta)

print(fruta[1])

fruta[1] = "Kiwi"
print(fruta)

print(fruta[1])

print("---"*10)
nomes = [
    "Ana", "Bruno", "Carla", "Diogo", "Eduarda",
    "Filipe", "Gabriela", "Henrique", "Inês", "João",
    "Kátia", "Luís", "Marta", "Nuno", "Olívia",
    "Paulo", "Rita", "Sérgio", "Teresa", "Urbano",
    "Vera", "Wilson", "Xavier", "Yara", "Zé"
]

print(nomes[1])
print(nomes[-1])
print(nomes[-5])

print("--"*5)

print(nomes[5:8]) # sub list com os val do idx 5 a 8-1 ->nomes[n:m] sub list com os val do idx n a m-1

print("--"*5)

print(nomes[:8]) # ->  print(nomes[0:8])

print("--"*5)

print(nomes[20:-1])


print("--"*5)
print(nomes[20:-1: 2]) # o que esta dentro [] é do genero do range

print("--"*5)

print(nomes[20:: 2])

print("--"*5)

print(nomes[20:-1: 2])

nomes[20:-1: 2] = ["novo nome 1", "novo nome 2"]

print(nomes[20:-1: 2])

print("--"*5)

print(nomes[20:-1: 2])

nomes[20:-1: 2] = ["novo nome 1", "novo nome 2"]

print(nomes[20:-1: 2])


print("--"*10)

print(nomes[-1])

nomes.append("Maria") # add um valor no final
print(nomes[-1])

print("--"*10)
print(nomes[0])

nomes.insert(0, "Joana") # add um valor na pos indicada
print(nomes[0])