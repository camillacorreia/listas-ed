class Pilha:
  def __init__(self, maxelem):
    self.pilha = [0] * maxelem
    self.tamanho = 0

  def empilhar(self, x):
    i = 0
    while i < self.tamanho and self.pilha[i] != x:
      i += 1
    if i == self.tamanho:
      if self.tamanho < len(self.pilha):
        self.pilha[self.tamanho] = x
        self.tamanho += 1
        return True
      else:
        return False
    else:
      return False

  def desempilhar(self):
    if self.tamanho == 0:
      return False
    
    elemento = self.pilha[self.tamanho-1]
    self.tamanho -= 1
    return elemento

  def imprimir(self):
    print(self.pilha[:self.tamanho])
  
pilha = Pilha(5)
pilha.empilhar(1)
pilha.empilhar(2)
pilha.imprimir()

pilha.desempilhar()
pilha.imprimir()
    