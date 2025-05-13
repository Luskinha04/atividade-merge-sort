# Questão 1.- Escreva uma versão recursiva do algoritmo Merge Sort que ordene um vetor v[incio..fim]
# em ordem decrescente. Sua função deve conter o código da intercalação, considerando que os sub
# vetores v[incio..meio] e v[meio+1..fim] já estejam ordenados de forma decrescente. O resultado final
# também deve ser um vetor decrescente.


def merge_sort_decrescente(v, inicio, fim):
    if inicio < fim:
        meio = (inicio + fim) // 2
        merge_sort_decrescente(v, inicio, meio)
        merge_sort_decrescente(v, meio + 1, fim)
        intercalar_decrescente(v, inicio, meio, fim)


def intercalar_decrescente(v, inicio, meio, fim):
    esquerda = v[inicio : meio + 1]
    direita = v[meio + 1 : fim + 1]

    i = 0  # ponteiro para esquerda
    j = 0  # ponteiro para direita
    k = inicio  # ponteiro para vetor principal

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] > direita[j]:  # Aqui inverte o sinal para decrescente
            v[k] = esquerda[i]
            i += 1
        else:
            v[k] = direita[j]
            j += 1
        k += 1

    while i < len(esquerda):
        v[k] = esquerda[i]
        i += 1
        k += 1

    while j < len(direita):
        v[k] = direita[j]
        j += 1
        k += 1


vetor = [7, 3, 9, 1, 4, 8]
merge_sort_decrescente(vetor, 0, len(vetor) - 1)
print(vetor)
# Saída esperada: [9, 8, 7, 4, 3, 1]
