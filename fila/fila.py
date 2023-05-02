class Fila:
  def __init__(self, maxelem):
    self.fila = [0] * maxelem
    self.tamanho = 0

  def enfileirar(self, x):
    if self.tamanho < len(self.fila):
      self.fila[self.tamanho] = x
      self.tamanho += 1
      return True
    else:
      return False

  def desenfileirar(self):
    if self.tamanho == 0:
      return False

    elemento = self.fila[self.inicio]
    self.fila[self.inicio] = 0
    self.inicio = (self.inicio + 1) % len(self.fila)
    self.tamanho -= 1

    return elemento

  def imprimir(self):
    print(self.fila[:self.tamanho])
  
fila = Fila(5)
fila.enfileirar(1)
fila.enfileirar(2)
fila.imprimir()

fila.desenfileirar()
fila.imprimir()