numero = input("Digite um número: ")
fator = 1 

for i in range(1, int(numero) + 1):
    fator *= i
print(f"O fatorial de {numero} é {fator}")