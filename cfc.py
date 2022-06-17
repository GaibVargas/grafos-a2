import math
import sys
from typing import TextIO
from Grafo import Grafo
from helper import formataEstruturaAuxiliar, mergeSort

def dfsVisit(
  grafo: Grafo,
  origem: int,
  C: 'list[int]',
  A: 'list[int]',
  F: 'list[int]',
  tempo: dict
):
  C[origem] = True
  tempo['valor'] += 1
  for u in grafo.vizinhos(origem + 1):
    u -= 1
    if not C[u]:
      A[u] = origem
      dfsVisit(grafo, u, C, A, F, tempo)
  tempo['valor'] += 1
  F[origem] = tempo['valor']

def dfs(grafo: Grafo):
  C = []
  A = []
  F = []
  tempo = { 'valor': 0 }

  for i in range(grafo.qtdVertices()):
    C.append(False)
    A.append(None)
    F.append(math.inf)
  
  for u in range(grafo.qtdVertices()):
    if not C[u]:
      dfsVisit(grafo, u, C, A, F, tempo)
  return [C, A, F]

def dfsAdaptado(grafo: Grafo, F: 'list[int]'):
  C = []
  A = []
  F2 = []
  tempo = { 'valor': 0 }

  for i in range(grafo.qtdVertices()):
    C.append(False)
    A.append(None)
    F2.append(math.inf)
  
  aux = formataEstruturaAuxiliar(F)
  auxSorted = mergeSort(aux)
  for obj in auxSorted:
    u = obj['vertice']
    if not C[u]:
      dfsVisit(grafo, u, C, A, F2, tempo)
  return [C, A, F2]

def cfc(grafo: Grafo):
  [C, A, F] = dfs(grafo)
  At = []
  for vertice in grafo.vetor_arestas:
    At.append((vertice[1], vertice[0]))
  Gt = Grafo()
  Gt.iniciar(grafo, At)
  [Ct, At2, Ft] = dfsAdaptado(Gt, F)
  return At2

def montarComponentes(origem: int, componente: 'list[int]', A: 'list[int]'):
  componente.append(origem)
  for vertice, ancestral in enumerate(A):
    if (ancestral == origem):
      montarComponentes(vertice, componente, A)
  return componente

def printResposta(A: 'list[int]'):
  raizes = []
  for index, valor in enumerate(A):
    if (valor == None):
      raizes.append(index)
  
  componentes = []
  for vertice in raizes:
    componentes.append(montarComponentes(vertice, [], A))
  
  for cfc in componentes:
    for index, vertice in enumerate(cfc):
      print(vertice + 1, end=", " if index != len(cfc) - 1 else "")
    print()

def main():
  grafo = Grafo()
  if (len(sys.argv) < 2):
    print("É necessário indicar um arquivo como argumento do programa\npython cfc.py [arquivo]")
    return

  file_name = sys.argv[1]
  file: TextIO = None

  try:
    file = open(file_name, 'r')
  except:
    print("Erro ao abrir o arquivo. Verifique se o nome do arquivo informado está correto")
    return
  
  grafo.ler(file)
  printResposta(cfc(grafo))
  
main()