class Heap:
  def __init__(self):
    self.heap = []
  
  def pai(self, i):
    return (i - 1) // 2
  
  def filho_esquerda(self, i):
    return 2 * i + 1
  
  def filho_direita(self, i):
    return 2 * i + 2
  
  def trocar_elementos(self, i, j):
    self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
  
  def subir(self, i):
    pai = self.pai(i)
    if i > 0 and self.heap[i] < self.heap[pai]:
      self.trocar_elementos(i, pai)
      self.subir(pai)
  
  def descer(self, i):
    esquerda = self.filho_esquerda(i)
    direita = self.filho_direita(i)
    menor = i
    
    if esquerda < len(self.heap) and self.heap[esquerda] < self.heap[menor]:
      menor = esquerda
    
    if direita < len(self.heap) and self.heap[direita] < self.heap[menor]:
      menor = direita
    
    if menor != i:
      self.trocar_elementos(i, menor)
      self.descer(menor)
  
  def inserir(self, valor):
    self.heap.append(valor)
    indice = len(self.heap) - 1
    self.subir(indice)
  
  def remover(self):
    if not self.heap:
      return None
    
    raiz = self.heap[0]
    ultimo = self.heap.pop()
    
    if self.heap:
      self.heap[0] = ultimo
      self.descer(0)
    
    return raiz

  def heapify(self, lista):
    self.heap = lista.copy()
    indice = len(self.heap) // 2 - 1
    for i in range(indice, -1, -1):
      self.descer(i)
