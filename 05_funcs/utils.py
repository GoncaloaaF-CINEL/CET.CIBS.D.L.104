"""

saida

nome

entrada

corpo


___ nome entrada [saida] corpo


"""

def ola_mundo():
    print('ola mundo')

ola_mundo()
ola_mundo()
ola_mundo()

print("---" * 10)
def ola_mundo2(nome):
        print(f"ola mundo, {nome}")

ola_mundo2("Gonçalo")
ola_mundo2("Rita")
ola_mundo2("Joana")


"""
Nivel 0
    Nivel 1
        Nivel 2
        
Nivel 0


"""

print("---" * 10)
def ola_mundo3(nome, ano):
    print(f"ola mundo, {nome} em {ano}")

ola_mundo3("Gonçalo", 2025)
ola_mundo3("Rita", 2026)

print("---" * 2)
ola_mundo3(nome="Gonçalo", ano=2025)

ola_mundo3("Rita", ano=2025)

# ola_mundo3(nome="Gonçalo", 2025)

ola_mundo3(ano=2030, nome="Joao")


print("---" * 10)

# hint
def nome(nome:str, aplido:str, idade:int):
    print(f"Nome: {nome.capitalize()} {aplido.capitalize()}")
    print(f"Idade: {idade}")

nome("goncalo","feliciano", 39)

print("---" * 10)
def nome(nome:str, idade:int):

    print(f"Nome: {nome.title()}")
    print(f"Idade: {idade}")

nome("goncalo feliciano", 39)

nome("goncalo feliciano", "dez")


print("---" * 10)


"""

func sem param
func cem param
type hint
ordem dos param 


"""

print("---" * 10)

def soma(valor1:int, valor2:int): # tipo de return implicito
    return valor1 + valor2

soma(1, 2)

print("---" * 2)

print(soma(1, 2))

print("---" * 2)

res = soma(1, 2)
print(res)

print("---" * 10)

def div(valor1:int, valor2:int) -> float:
    print(valor1 / valor2)


div(1, 2)

print("---" * 2)
def div2(valor1:int, valor2:int) -> float:
    return valor1 / valor2


print(div2(1, 2))


print("---" * 10)


def soma2(valor1:int, valor2:int = 20) -> int:
    return valor1 + valor2

print(soma2(1, 2))

print(soma2(1))


print("---" * 2)

"""
o(s) Valor(s) default  tem de estar no final 

def soma2(valor1:int = 10, valor2:int) -> int:
    return valor1 + valor2
"""