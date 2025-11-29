def calcular_media(notas):
    soma = 0
    for i in range(len(notas)):
        soma = soma + notas[i]
    media = soma / len(notas)
    return media

numeros = [10, 8, 7, 9]
print(calcular_media(numeros))
print(calcular_media([]))  # Bug: divisão por zero
