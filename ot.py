import sys
from typing import TextIO
from Grafo import Grafo
from LinkedList import LinkedList

def dfsVisit(grafo: Grafo, origem: int, C: 'list[int]', O: LinkedList):
  C[origem] = True
  for u in grafo.vizinhos(origem + 1):
    u -= 1
    if not C[u]:
      dfsVisit(grafo, u, C, O)
  O.insert(origem)

def ot(grafo: Grafo):
  C = []
  O = LinkedList()
  for i in range(grafo.qtdVertices()):
    C.append(False)
  
  for u in range(grafo.qtdVertices()):
    if not C[u]:
      dfsVisit(grafo, u, C, O)
  
  return O

def printResultado(grafo: Grafo, O: LinkedList):
  vertice = O.cabeca
  while (True):
    print(grafo.rotulo(vertice.valor + 1), end=" -> " if vertice.proximo != None else "")
    vertice = vertice.proximo
    if (vertice == None):
      break
  print()

def main():
  grafo = Grafo()
  if (len(sys.argv) < 2):
    print("É necessário indicar um arquivo como argumento do programa\npython ot.py [arquivo]")
    return

  file_name = sys.argv[1]
  file: TextIO = None

  try:
    file = open(file_name, 'r')
  except:
    print("Erro ao abrir o arquivo. Verifique se o nome do arquivo informado está correto")
    return

  grafo.ler(file)
  printResultado(grafo, ot(grafo))
  
main()