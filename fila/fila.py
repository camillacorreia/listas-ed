class Fila:
  def __init__(self, maxelem):
    self.fila = [0] * maxelem
    self.tamanho = 0

  def enfileirar(self, x):
    i = 0
    while i < self.tamanho and self.fila[i] != x:
      i += 1
    if i == self.tamanho:
      if self.tamanho < len(self.fila):
        self.fila[self.tamanho] = x
        self.tamanho += 1

  def desenfileirar(self):
    if self.tamanho == 0:
      return False

    elemento = self.fila[0]
    self.tamanho -= 1
    i = 0
    while i < self.tamanho:
      self.fila[i] = self.fila[i + 1]
      i += 1
    self.fila[self.tamanho] = 0
    return elemento

  def imprimir(self):
    print(self.fila[:self.tamanho])
  
fila = Fila(5)
fila.enfileirar(1)
fila.enfileirar(2)
fila.imprimir()

fila.desenfileirar()
fila.imprimir()