#              0      1        2       3
my_tuple = ("Val1", "Val2", "Val3", "Val4")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[3])

# print(my_tuple[12]) # -> IndexError: tuple index out of range

print("---" * 10)
my_tuple = ("usr", "pwd", "token")

usr = my_tuple[0]
pwd = my_tuple[1]
token = my_tuple[2]

print(usr)
print(pwd)
print(token)

print("---" * 10)
my_tuple = ("usr 2", "pwd 2", "token 2", )


usr2, pwd2, token2 = my_tuple
print(usr2)
print(pwd2)
print(token2)

print("---" * 10)


for elm in my_tuple:
    print(f"for: {elm}")


print("---" * 10)

def func1():
    #codigo e mais codigo
    return "nome", "email"

resp = func1()
print(type(resp))

abc, xyz = func1()

print(abc)
print(xyz)


print("---" * 10)
my_tuple = ("usr 2", "pwd 2", "token 2", "usr 2")


print(my_tuple)
print(type(my_tuple))

print(len(my_tuple))
print(my_tuple.__len__())

print("-" * 3)
print(my_tuple.count("usr 2")) # conta o num de vezes que o param indicado se repete


print("-" * 3)

print(my_tuple.index("usr 2")) # o 1º idx onde aparece o valor indicado
print(my_tuple.index("pwd 2"))

# print(my_tuple.index("outro valor")) # se não existe -> ValueError: tuple.index(x): x not in tuple



print("-" * 3)

print(my_tuple[-1])


print("# mudar o um valor dentro de um tuplo ?")

my_tuple = ("usr 2", "pwd 2", "token 2")

# mudar o um valor dentro de um tuplo ?

# 1 - converter para lista
lista_temp = list(my_tuple)

# 2 - mudar o valor
lista_temp[0] = "cool username"

# 3 - converter para tuplo

my_tuple = tuple(lista_temp)

print(my_tuple)


# adicinar um valor dentro de um tuplo ?

# 1 - converter para lista
lista_temp = list(my_tuple)

# 2 - adicionar o valor

lista_temp.append("Novo valor")

# 3 - converter para tuplo

my_tuple = tuple(lista_temp)

print(my_tuple)