class Pilha:
  def __init__(self, max_itens=100):
    self.tamanho = 0
    self.max_itens = max_itens
    self.estrutura = [None] * self.max_itens

  def __del__(self):
    del self.estrutura

  def estacheia(self):
    return self.tamanho == self.max_itens

  def estavazia(self):
    return self.tamanho == 0

  def inserir(self, item):
    if self.estacheia():
      print("A pilha está cheia!\nNão é possível inserir este elemento!")
    else:
      self.estrutura[self.tamanho] = item
      self.tamanho += 1

  def remover(self):
    if self.estavazia():
      print("A pilha está vazia!\nNão tem elemento para ser removido!")
      return 0
    else:
      self.tamanho -= 1
      item = self.estrutura[self.tamanho]
      self.estrutura[self.tamanho] = None
      return item

  def imprimir(self):
    print("Pilha: [ ", end="")
    i = 0
    while i < self.tamanho:
      print(self.estrutura[i], end=" ")
      i += 1
    print("]")

  def qualtamanho(self):
    return self.tamanho