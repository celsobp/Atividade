# Rolando dados
from random import randint


def lado():
    lados = input("Digite o número de lados dos dados (mínimo 6): ")
    return lados

def dados():
    dado = input("\nDigite o total de dados a rolar (mínimo 1): ")
    return dado

def rolar(totalDados, lados):
    soma = 0
    for x in range(0, int(totalDados)):
        valor = randint(1, int(lados))
        print("\nValor do dado nº " + str(x + 1) + " é " + str(valor))
        soma = soma + valor
    return soma
continua = True




while (continua) == True :

    lados = 0
    totalDados = 0
    soma = 0
    pergunta = ""

    print("Vamos rolar dados!")
    while int(lados) < 6:
        try:
            lados = lado()
        except EOFError:
            lados = 6
            break

    print("\nTotal de lados do(s) dado(s): " + str(lados))
    while int(totalDados) < 1:
        try:
            totalDados = dados()
        except EOFError:
            totalDados = 2
            break

    print("\nTotal de dado(s) a rolar: " + str(totalDados))

    soma = rolar(totalDados, lados)

    print("\nSoma dos dados é: " + str(soma))

    while ((pergunta.upper() != "S" and pergunta.upper() != "N")) :
        try:
            pergunta = input("Deseja rolar novos dados? (S/N): ")
        except EOFError:
            pergunta = "N"
            break

        if (pergunta.upper()) == "N":
            continua = False
            print("\nAté logo!!!")
        elif (pergunta.upper()) == "S":
            continua = True
            break


