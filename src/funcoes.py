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