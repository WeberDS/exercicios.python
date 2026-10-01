q_positivos = 0

numero = int(input("Digite um número (ou 0 para sair): "))
while numero != 0:
    if numero > 0:
        q_positivos += 1
    numero = int(input("Digite um número (ou 0 para sair): "))

print(f"Quantidade de números positivos: {q_positivos}")3
