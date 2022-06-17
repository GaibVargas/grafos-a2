class ListItem:
  def __init__(self, valor: int, proximo: 'ListItem' = None):
    self.valor = valor
    self.proximo: 'ListItem' = proximo

class LinkedList:
  def __init__(self):
    self.cabeca: ListItem = None
  
  def insert(self, valor: int):
    item = ListItem(valor, self.cabeca)
    self.cabeca = item
