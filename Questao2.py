# Questão 2.– Implemente um programa que utilize a função merge_sort(array) e realize testes experimentais
# para verificar sua correção. Gere vetores de inteiros aleatórios de vários tamanhos (por
# exemplo, 10, 100, 1000 elementos). Após a ordenação, verifique automaticamente se o vetor está, de
# fato, em ordem crescente. Exiba o resultado de cada teste.

import random
import time

# Garante 20 números únicos entre 0 e 100
vetor = random.sample(range(101), 20)


def merge_sort(array, nivel=0):
    if len(array) > 1:
        meio = len(array) // 2
        esquerda = array[:meio]
        direita = array[meio:]

        merge_sort(esquerda, nivel + 1)
        merge_sort(direita, nivel + 1)

        i = j = k = 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                array[k] = esquerda[i]
                i += 1
            else:
                array[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            array[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            array[k] = direita[j]
            j += 1
            k += 1

        print(f"{'  ' * nivel}Intercalação no nível {nivel}: {array}")


def esta_ordenado(array):
    return all(array[i] <= array[i + 1] for i in range(len(array) - 1))


# Exibe o vetor original
print(" Vetor gerado aleatoriamente:")
print(vetor)

# Inicia ordenação com rastreamento
print("\nIniciando Merge Sort com rastreamento de intercalações...\n")
inicio = time.time()
merge_sort(vetor)
fim = time.time()

# Resultado
print("\nVetor ordenado:")
print(vetor)
print(f"\nTempo de execução: {fim - inicio:.6f} segundos")
print("Verificação:", "ORDENADO " if esta_ordenado(vetor) else "NÃO ordenado")
