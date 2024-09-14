# Rolando dados
from random import randint

lados = 0
totalDados = 0

print("Vamos rolar dados!")
while int(lados) < 6:
    lados = input("Digite o número de lados dos dados (mínimo 6): ")

print("\nTotal de lados do(s) dado(s): " + lados)
while int(totalDados) < 1:
    totalDados = input("\nDigite o total de dados a rolar (mínimo 1): ")

print("\nTotal de dado(s) a rolar: " + totalDados)

for x in range(0, int(totalDados)):
    print("\nValor do dado nº " + str(x+1) + " é " + str(randint(1, int(lados))))
