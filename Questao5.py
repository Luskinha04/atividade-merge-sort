# Questão 5.– Utilize a versão iterativa do Merge Sort e compare-a com a versão recursiva. Faça testes
# com vetores de tamanhos variados, meça o tempo de execução de ambas as versões e apresente os
# resultados em uma tabela. Em seguida, discuta as vantagens e desvantagens observadas entre as duas
# abordagens

import random
import time


# --------- Função de Mesclagem Compartilhada ---------
def merge(lista, inicio, meio, fim):
    esquerda = lista[inicio : meio + 1]
    direita = lista[meio + 1 : fim + 1]
    i = j = 0
    k = inicio

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            lista[k] = esquerda[i]
            i += 1
        else:
            lista[k] = direita[j]
            j += 1
        k += 1

    while i < len(esquerda):
        lista[k] = esquerda[i]
        i += 1
        k += 1

    while j < len(direita):
        lista[k] = direita[j]
        j += 1
        k += 1


# --------- Versão Iterativa ---------
def merge_sort_iterativo(lista):
    n = len(lista)
    tamanho = 1
    while tamanho < n:
        for inicio in range(0, n, 2 * tamanho):
            meio = min(inicio + tamanho - 1, n - 1)
            fim = min(inicio + 2 * tamanho - 1, n - 1)
            if meio < fim:
                merge(lista, inicio, meio, fim)
        tamanho *= 2


# --------- Versão Recursiva ---------
def merge_sort_recursivo(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]

        merge_sort_recursivo(esquerda)
        merge_sort_recursivo(direita)

        i = j = k = 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] <= direita[j]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1


# --------- Comparação das duas versões ---------
def comparar_tempos():
    tamanhos = [100, 1000, 5000]
    print(f"{'Tamanho':<10} | {'Iterativo (s)':<15} | {'Recursivo (s)':<15}")
    print("-" * 45)

    for tam in tamanhos:
        lista = random.sample(range(10000), tam)
        lista_iterativa = lista[:]
        lista_recursiva = lista[:]

        inicio = time.time()
        merge_sort_iterativo(lista_iterativa)
        fim = time.time()
        tempo_iter = fim - inicio

        inicio = time.time()
        merge_sort_recursivo(lista_recursiva)
        fim = time.time()
        tempo_rec = fim - inicio

        print(f"{tam:<10} | {tempo_iter:<15.6f} | {tempo_rec:<15.6f}")


# --------- Execução principal ---------
if __name__ == "__main__":
    comparar_tempos()
