class Lista:
  def __init__(self, maxelem):
    self.lista = [0] * maxelem
    self.tamanho = 0

  def inserir(self, x):
    encontrado = False
    i = 0
    while i < self.tamanho:
      if self.lista[i] == x:
        encontrado = True
        break
      i += 1
    if encontrado == False:
      if self.tamanho < len(self.lista):
        self.lista[self.tamanho] = x
        self.tamanho += 1
       
  def remover(self, x):
    posicao = -1
    i = 0
    while i < self.tamanho:
      if self.lista[i] == x:
        posicao = i
        break
      i += 1
    if posicao != -1:
      j = posicao
      while j < self.tamanho-1:
        self.lista[j] = self.lista[j+1]
        j += 1
      self.tamanho -= 1
       
  def consultar(self, x):
    posicao = -1
    i = 0
    while i < self.tamanho:
      if self.lista[i] == x:
        posicao = i
        break
      i += 1
    if posicao != -1:
      print(f"O elemento {x} está na posição {posicao}")
       
  def imprimir(self):
    print(self.lista[:self.tamanho])

lista = Lista(5)
lista.inserir(2)
lista.inserir(3)
lista.remover(2)
lista.consultar(3)

# Explicação do código:

# O método init inicializa a lista com uma lista de tamanho fixo com valores 0 e define o atributo tamanho como 0.

# O método inserir itera sobre a lista utilizando um loop while, incrementando i em cada iteração, buscando por um
#   valor x igual ao valor de algum elemento da lista. Se o valor x não for encontrado, o método insere o valor na
#   posição self.tamanho da lista e incrementa o atributo tamanho.

# O método remover também utiliza um loop while para encontrar a posição do elemento a ser removido. Se o elemento
#   é encontrado, um segundo loop while é usado para reorganizar a lista, movendo todos os elementos após a posição
#   do elemento removido uma posição para trás. Por fim, o atributo tamanho é decrementado.

# O método consultar também utiliza um loop while para encontrar a posição do elemento consultado, e se o elemento
#   é encontrado, o método imprime uma mensagem indicando a posição do elemento na lista.

# O método imprimir simplesmente imprime a lista até a posição self.tamanho.