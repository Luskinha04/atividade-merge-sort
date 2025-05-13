# Questão 4.– Implemente o algoritmo Merge Sort para listas encadeadas simples (estrutura de nó
# com campo de valor e ponteiro para o próximo). A função deve ordenar a lista em ordem crescente
# sem alocar novas células, apenas manipulando os ponteiros existentes.


class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


def imprimir_lista(head):
    atual = head
    while atual:
        print(atual.valor, end=" -> ")
        atual = atual.proximo
    print("None")


def encontrar_meio(head):
    if not head or not head.proximo:
        return head, None

    lento = head
    rapido = head.proximo

    while rapido and rapido.proximo:
        lento = lento.proximo
        rapido = rapido.proximo.proximo

    meio = lento.proximo
    lento.proximo = None
    return head, meio


def intercalar_listas(esq, dir):
    if not esq:
        return dir
    if not dir:
        return esq

    if esq.valor < dir.valor:
        resultado = esq
        resultado.proximo = intercalar_listas(esq.proximo, dir)
    else:
        resultado = dir
        resultado.proximo = intercalar_listas(esq, dir.proximo)

    return resultado


def merge_sort_lista(head, nivel=0):
    if not head or not head.proximo:
        return head

    esquerda, direita = encontrar_meio(head)

    print("  " * nivel + f"Dividindo no nível {nivel}:")
    print("  " * nivel + "Esquerda: ", end="")
    imprimir_lista(esquerda)
    print("  " * nivel + "Direita:  ", end="")
    imprimir_lista(direita)

    esquerda = merge_sort_lista(esquerda, nivel + 1)
    direita = merge_sort_lista(direita, nivel + 1)

    resultado = intercalar_listas(esquerda, direita)

    print("  " * nivel + f"Intercalação no nível {nivel}: ", end="")
    imprimir_lista(resultado)

    return resultado


valores = [4, 2, 7, 1]
head = No(valores[0])
atual = head
for val in valores[1:]:
    atual.proximo = No(val)
    atual = atual.proximo

print("Lista original:")
imprimir_lista(head)

# Ordenando com rastreamento
head = merge_sort_lista(head)

print("Lista ordenada:")
imprimir_lista(head)
