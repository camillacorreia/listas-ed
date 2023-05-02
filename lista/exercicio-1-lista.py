class Lista:
  def __init__(self, maxelem):
    self.lista = [0] * maxelem
    self.tamanho = 0

  def inserir(self, x):
    i = 0
    while i < self.tamanho and self.lista[i] != x:
      i += 1
    if i == self.tamanho:
      if self.tamanho < len(self.lista):
        self.lista[self.tamanho] = x
        self.tamanho += 1
        return True
      else:
        return False
    else:
        return False

  def remover(self, x):
    i = 0
    while i < self.tamanho and self.lista[i] != x:
      i += 1
    if i != self.tamanho:
      j = i
      while j < self.tamanho - 1:
        self.lista[j] = self.lista[j + 1]
        j += 1
      self.tamanho -= 1

  def consultar(self, x):
    i = 0
    while i < self.tamanho and self.lista[i] != x:
      i += 1
    if i != self.tamanho:
      return True
    else:
      return False

  def imprimir(self):
    print(self.lista[:self.tamanho])


lista = Lista(5)
lista.inserir(2)
lista.inserir(3)
lista.remover(2)
lista.consultar(3)

# Explicação do código:

# O método __init__ é o construtor da classe e recebe um parâmetro maxelem que define o tamanho máximo da lista.
#   Nesse método, a lista é inicializada com maxelem elementos nulos (zeros) e o tamanho é definido como zero.

# O método inserir recebe um parâmetro x e insere esse valor na lista, caso ele ainda não exista nela. Para isso,
#   o método percorre a lista procurando o valor x e, caso ele não seja encontrado, o valor é adicionado na primeira
#   posição livre (onde o valor é nulo) e o tamanho da lista é incrementado em uma unidade.

# O método remover recebe um parâmetro x e remove esse valor da lista, caso ele exista nela. Para isso, o método
#   percorre a lista procurando o valor x e, caso ele seja encontrado, os elementos à direita dele são deslocados
#   uma posição para a esquerda (para sobrescrever o elemento a ser removido) e o tamanho da lista é decrementado
#   em uma unidade.

# O método consultar recebe um parâmetro x e retorna a posição do valor x na lista, caso ele exista nela. Para isso,
#   o método percorre a lista procurando o valor x e, caso ele seja encontrado, a posição é retornada. Caso contrário,
#   é retornado o valor -1.

# O método imprimir simplesmente imprime na tela os elementos da lista até a posição tamanho.