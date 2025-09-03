# cmt

"""

tipos de dados

int
str
flaot
bool


String nome = "Gonçalo"

"""
print("Ola Mundo")

nome = "Gonçalo" # -> str
idade = 25

print(nome)

nome = "João" # -> str
print(nome)

nome = 2014 # -> int <- !! EVITAR  MUDAR O TIPO DA VAR DINAMICAMENTE !!
print(nome)

nome2:str = "Novo Nome" # type hint
print(nome2)

nome2 = "Carlos"
print(nome2)

nome2 = 1234
print(nome2)

print("--------")

nome = "Gonçalo"
ano = 2025

# "Ola Gonçalo, estamos em 2025"

#str(ano) -> (String) ano
print("Ola " + nome + ", estamos em " + str(ano))

print("Ola", nome ,",estamos em", ano) # , -> + " " +

print("Ola {}, estamos em {}".format(nome, ano))

print(f"Ola {nome}, estamos em {ano}")

print("--------")

nome = "Gonçalo"
altura = 1.70

print(f"O {nome}, mede {altura:.2f}m")



max_cSharp = 2147483647
max64_cSharp = 9223372036854775807

"""
+ -> num + num | str + str     -> se um dos val é decimal devolve decimal, caso contrario devolve int 
- -> num - num                 -> se um dos val é decimal devolve decimal, caso contrario devolve int 
/ -> num / num                 -> devolve sempre decimal 
* -> num * num | str * str     -> se um dos val é decimal devolve decimal, caso contrario devolve int 

% -> 10 % 2 -> 0

0 1 2 3 4 5 6 7 8 9 10
0 1 0 1 0 1 0 1 0 1 0


% -> 10 % 3 <-> 10 Mod 3
0 1 2 3 4 5 6 7 8 9 10
0 1 2 0 1 2 0 1 2 0 1

// <- div int  <-> 10 // 3 = 3

"""

num1 = 10
num2 = 2

res1 = num1 / num2
res2 = num1 // num2
res3 = num1 % num2


print(res1, res2, res3)


print("--" * 10)


print(10 + 1.0)
print(10 + 1)

print(10 - 1.0)
print(10 - 1)

print(10 * 1.0)
print(10 * 1)


print("--" * 10)


max64_cSharp = 9223372036854775807

print(max64_cSharp)
print(max64_cSharp * 5)

print(max64_cSharp * max64_cSharp)
print(max64_cSharp * max64_cSharp * max64_cSharp)
print(max64_cSharp * max64_cSharp * max64_cSharp * max64_cSharp * max64_cSharp * max64_cSharp)
print(max64_cSharp * max64_cSharp * max64_cSharp * max64_cSharp * max64_cSharp * max64_cSharp * 615656346818663737291362432329573325363859439854215515892590030606645220018700810278654093633374614700204645941249)



"""
379032737378102766877218579655255646
894733941685299497278732751722208281
389295592596843602978478605938319830
800478894286982455702886976951678487
772094521525120059963757409814343188
427472525028302433942691050303481869
689159680001
"""

print("--" * 10)
max64_cSharp = 9_223_372_036_854_775_807
print(max64_cSharp)

max64_cSharp = 9_223_372_036_854_775_807
print(max64_cSharp)


print("--" * 10)

val1 = 10_000
val2 = 3

print(val1 * val2)