# range

range(5) # devolve todos os val int de 0 a 4, range(m) -> 0 a m-1
range(8) # 0 a 7

range(3, 8) # devolve todos os val int de 3 a 7, range(n, m) -> n a m-1

range(5)
range(0, 5)


range(0, 10, 2) # devolve todos os val int de 0 a 10 com um step de 2
                # 0 2 4 8


# for

# for(int i = 0; i < 10; i++)

for i in range(5):
    print(i, end=" ")

print("")

for i in range(0, 5):
    print(i, end=" ")

print("")



for i in range(4, 20):
    print(i, end=" ")

print("")


for i in range(4, 20,2):
    print(i, end=" ")

print("")



for i in range(-4, -20, -1):
    print(i, end=" ")


print("")
print("----" * 10)
#testar o range


# print("foo", end=" <--> ")
# print("bar")
for i in range(50):
    if i == 35:
        break

    print(i, end=" ")


print("")

for i in range(50):
    if i == 35:
        break

    if i % 2 == 0:
        continue

    print(i, end=" ")


print("")
print("----" * 10)



num1 = 10
num2 = 20

soma = num1 + num2

print(soma)


soma2 = num1 + num2 + 5

print(soma2)

# while




"""

var
in/out 
if 
match
for 
while

"""

"""
proxima aula

funcs 
collections -list, set, dict, tuplos 

"""

"""
17 e 19 - classes 

"""


"""
24 e 26 - pandas - Analise de logs 

"""