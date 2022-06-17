import sys
from typing import TextIO
from Grafo import Grafo
from helper import mergeSortKruskal

def kruskal(grafo: Grafo):
  A = set()
  S: list[set] = []
  for i in range(grafo.qtdVertices()):
    S.append({ i })
  E = mergeSortKruskal(grafo, grafo.vetor_arestas.copy())
  for aresta in E:
    u = aresta[0] - 1
    v = aresta[1] - 1
    if S[u] != S[v]:
      A.add((u, v))
      x = S[u].union(S[v])
      for y in x:
        S[y] = x
  return A

def calculaCustoTotal(grafo: Grafo, A: 'set[tuple[int, int]]'):
  total = 0
  for aresta in A:
    u = aresta[0] + 1
    v = aresta[1] + 1
    total += grafo.peso(u, v)
  return total

def printResultado(grafo: Grafo, A: 'set[tuple[int, int]]'):
  print(calculaCustoTotal(grafo, A))
  for index, aresta in enumerate(A):
    print(f"{aresta[0]}-{aresta[1]}", end=", " if index != len(A) - 1 else "")
  print()

def main():
  grafo = Grafo()
  if (len(sys.argv) < 2):
    print("É necessário indicar um arquivo como argumento do programa\npython kruskal.py [arquivo]")
    return

  file_name = sys.argv[1]
  file: TextIO = None

  try:
    file = open(file_name, 'r')
  except:
    print("Erro ao abrir o arquivo. Verifique se o nome do arquivo informado está correto")
    return

  grafo.ler(file)
  printResultado(grafo, kruskal(grafo))
  
main()