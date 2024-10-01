# Rolando dados
from random import randint


def lado():
    try:
        lados = input("Digite o número de lados dos dados (mínimo 6): ")
    except EOFError:
        lados = 6
    return lados

def dados():
    try:
        dado = input("\nDigite o total de dados a rolar (mínimo 1): ")
    except EOFError:
        dado = 2
    return dado

def rolar(totalDados, lados):
    soma = 0
    for x in range(0, int(totalDados)):
        valor = randint(1, int(lados))
        print("\nValor do dado nº " + str(x + 1) + " é " + str(valor))
        soma = soma + valor
    return soma

lados = 0
totalDados = 0
soma = 0

print("Vamos rolar dados!")
while int(lados) < 6:
    lados = lado()

print("\nTotal de lados do(s) dado(s): " + str(lados))

while int(totalDados) < 1:
    totalDados = dados()

print("\nTotal de dado(s) a rolar: " + str(totalDados))

soma = rolar(totalDados, lados)

print("\nSoma dos dados é: " + str(soma))

