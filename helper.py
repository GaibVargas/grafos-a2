import math

from Grafo import Grafo


def formataEstruturaAuxiliar(F: 'list[int]'):
  resposta: list[dict] = []
  for index, valor in enumerate(F):
    resposta.append({
      'vertice': index,
      'f': valor
    })
  return resposta

# Adaptado de https://pt.wikipedia.org/wiki/Merge_sort
def mergeSort(lista: 'list[dict]'):
  if (len(lista) > 1):

    meio = math.floor(len(lista)/2)
    esquerda = lista[:meio]
    direita = lista[meio:]

    mergeSort(esquerda)
    mergeSort(direita)

    i = 0
    j = 0
    k = 0

    while i < len(esquerda) and j < len(direita):
      if esquerda[i]['f'] < direita[j]['f']:
        lista[k] = direita[j]
        j += 1
      else:
        lista[k] = esquerda[i]
        i += 1
      k += 1

    while i < len(esquerda):
      lista[k] = esquerda[i]
      i += 1
      k += 1

    while j < len(direita):
      lista[k] = direita[j]
      j += 1
      k += 1

  return lista

# Adaptado de https://pt.wikipedia.org/wiki/Merge_sort
def mergeSortKruskal(grafo: Grafo, lista: 'list[tuple[int, int]]'):
  if (len(lista) > 1):

    meio = math.floor(len(lista)/2)
    esquerda = lista[:meio]
    direita = lista[meio:]

    mergeSortKruskal(grafo, esquerda)
    mergeSortKruskal(grafo, direita)

    i = 0
    j = 0
    k = 0

    while i < len(esquerda) and j < len(direita):
      if grafo.peso(esquerda[i][0], esquerda[i][1]) < grafo.peso(direita[j][0], direita[j][1]):
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

  return lista