
# if





"""

if (num > num2){ 

}

: -> inicia um bloco

{ -> :


"""
from turtledemo.paint import switchupdown

num  = 110
num2 = 20

if num > num2:
    #cmt

    """
    cmt 
    multi 
    linha
    
    tem de estar identado 
    """
    print("dentro do if")
    print(f"o maior e {num}")
    print("ainda dentro do if")

print("fora do if 2")



"""
nivel 0
    nivel 1
        nivel 2
            nivel 3
        nivel 2
    nivel 1
nivel 0


"""

print("---" * 10)

num1 = 210
num2 = 20

if num1 > num2:
    print("o maior é num1")
else:
    print("o maior é num2")

print("---" * 10)

num1 = 20
num2 = 20

if num1 > num2:
    print("o maior é num1")
elif num2 > num1: # else if num2 > num1
    print("o maior é num2")
else:
    print("são iguais")

"""
 
 = <- atr
 == <- eq


"""
# switch
print("---" * 10)
print("---" * 10)

mes = "jan"

match mes: # switch
    case 1:
        print("jan")
    case 2:
        print("feb")
    case "jan":
        print("Janeiro")
    case _: # default
        print("Outro mes")


if mes == "jan":
    print("Janeiro")
elif mes == 1:
    print("Jan")
elif mes == 2:
    print("Feb")
else:
    print("Outro mes")



