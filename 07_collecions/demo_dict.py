#criar dict

my_dict = {
            "nome":"Gonçalo",
            "ano":2024,
            "ativo":True,
           }

#lst = [("nome","Gonçalo"),
#        ("ano",2024),
#        ("ativo",True)]

print(my_dict)

#aceder a val
print(my_dict["nome"])

print(my_dict["ativo"])

# print(my_dict["aTiVo"]) se a key não existe -> erro KeyError: 'aTiVo'

# print(my_dict["key invalida"]) se a key não existe -> erro KeyError: 'key invalida'

print("--" * 3)
print(my_dict.get("ativo"))
print(my_dict.get("aTiVo")) # se a key não existe -> devolve None

print("--" * 3)
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

# modificar elm
print("--" * 3)

print(my_dict)
my_dict["ativo"] = False
print(my_dict)

my_dict.update({"ativo":True})
print(my_dict)

print("--" * 3)
#add elm

print(my_dict)
my_dict["anoNasc"] = 1990
print(my_dict)

my_dict.update({"anoNasc 2":1986})
print(my_dict)


# remover elm
print("--" * 3)
print(my_dict)

print(my_dict.pop("anoNasc 2"))
# print(my_dict.pop("anoNasc 2")) # -> se a key nao existe -> KeyError: 'anoNasc'
print(my_dict)

print(my_dict.popitem())

print(my_dict)

# del my_dict["anoNasc"] # -> se a key nao existe -> KeyError: 'anoNasc'
del my_dict["ano"]


# ver um ele eixste como key
print(my_dict)

print("ano" in my_dict)

my_dict["ano"] = 1990
print(my_dict)
print("ano" in my_dict)

print(my_dict.__contains__("ano"))

# loops
print("--" * 3)

for dict_key in my_dict:
    print(dict_key, end=" | ")


print("")

for dict_key in my_dict.keys():
    print(dict_key, end=" | ")


print("")

for dict_key in my_dict.values():
    print(dict_key, end=" | ")


print("")

for dict_key in my_dict.items():
    print(dict_key, end=" | ")


print("")

for dict_key in my_dict:
    print(my_dict[dict_key], end=" | ")


print("")

for key, value in my_dict.items():
    print(f"key: {key}, value: {value}")