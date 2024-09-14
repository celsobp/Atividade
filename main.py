# Rolando dados
from random import randint

print("Vamos rolar dados!")
lados = input("Digite o número de lados dos dados (mínimo 6): ")
print("\nTotal de lados do(s) dado(s): " + lados)
totalDados = input("\nDigite o total de dados a rolar: ")
print("\nTotal de dado(s) a rolar: " + totalDados)

for x in range(0, int(totalDados)):
    print("\n Valor do dado nº " + str(x+1) + " é " + str(randint(1, int(lados))))
