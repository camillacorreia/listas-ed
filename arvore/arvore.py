class No:
  def __init__(self, valor):
    self.valor = valor
    self.esquerda = None
    self.direita = None

class ArvoreBinaria:
  def __init__(self):
    self.raiz = None

  def inserir(self, valor):
    if self.raiz is None:
      self.raiz = No(valor)
    else:
      self._inserir_recursivo(valor, self.raiz)

  def _inserir_recursivo(self, valor, no_atual):
    if valor < no_atual.valor:
      if no_atual.esquerda is None:
        no_atual.esquerda = No(valor)
      else:
        self._inserir_recursivo(valor, no_atual.esquerda)
    else:
      if no_atual.direita is None:
        no_atual.direita = No(valor)
      else:
        self._inserir_recursivo(valor, no_atual.direita)

  def buscar(self, valor):
    return self._buscar_recursivo(valor, self.raiz)

  def _buscar_recursivo(self, valor, no_atual):
    if no_atual is None or no_atual.valor == valor:
      return no_atual
    if valor < no_atual.valor:
      return self._buscar_recursivo(valor, no_atual.esquerda)
    return self._buscar_recursivo(valor, no_atual.direita)

  def contar_nos(self):
    return self._contar_nos_recursivo(self.raiz)

  def _contar_nos_recursivo(self, no_atual):
    if no_atual is None:
      return 0
    return 1 + self._contar_nos_recursivo(no_atual.esquerda) + self._contar_nos_recursivo(no_atual.direita)

  def imprimir_em_ordem(self):
    self._imprimir_em_ordem_recursivo(self.raiz)

  def _imprimir_em_ordem_recursivo(self, no_atual):
    if no_atual:
      self._imprimir_em_ordem_recursivo(no_atual.esquerda)
      print(no_atual.valor, end=" ")
      self._imprimir_em_ordem_recursivo(no_atual.direita)

  def remover(self, valor):
    self.raiz = self._remover_recursivo(valor, self.raiz)

  def _remover_recursivo(self, valor, no_atual):
    if no_atual is None:
      return no_atual
    if valor < no_atual.valor:
      no_atual.esquerda = self._remover_recursivo(valor, no_atual.esquerda)
    elif valor > no_atual.valor:
      no_atual.direita = self._remover_recursivo(valor, no_atual.direita)
    else:
      if no_atual.esquerda is None:
        return no_atual.direita
      elif no_atual.direita is None:
        return no_atual.esquerda
      no_atual.valor = self._valor_minimo(no_atual.direita)
      no_atual.direita = self._remover_recursivo(no_atual.valor, no_atual.direita)
    return no_atual

  def _valor_minimo(self, no_atual):
    while no_atual.esquerda is not None:
      no_atual = no_atual.esquerda
    return no_atual.valor


# Exemplo de uso
arvore = ArvoreBinaria()

arvore.inserir(50)
arvore.inserir(30)
arvore.inserir(20)
arvore.inserir(40)
arvore.inserir(70)
arvore.inserir(60)
arvore.inserir(80)

print("Árvore em ordem:")
arvore.imprimir_em_ordem()
print("\n")

elemento = 40
if arvore.buscar(elemento):
  print(f"Elemento {elemento} encontrado na árvore.")
else:
  print(f"Elemento {elemento} não encontrado na árvore.")

print("Número de nós na árvore:", arvore.contar_nos())

elemento = 30
arvore.remover(elemento)
print(f"Elemento {elemento} removido.")

print("Árvore em ordem após a remoção:")
arvore.imprimir_em_ordem()
