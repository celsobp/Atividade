# Rolando dados
from funcoes import *

continua = True




while (continua) == True :

    lados = 0
    totalDados = 0
    soma = 0
    pergunta = ""

    print("Vamos rolar dados!")
    while int(lados) < 6:
        lados = lado()

    print("\nTotal de lados do(s) dado(s): " + lados)
    while int(totalDados) < 1:
        totalDados = dados()

    print("\nTotal de dado(s) a rolar: " + totalDados)

    soma = rolar(totalDados, lados)

    print("\nSoma dos dados é: " + str(soma))

    while ((pergunta.upper() != "S" and pergunta.upper() != "N")) :
        pergunta = input("Deseja rolar novos dados? (S/N): ")
        if (pergunta.upper()) == "N":
            continua = False
            print("\nAté logo!!!")
        elif (pergunta.upper()) == "S":
            continua = True
            break


