from no import No

class PilhaEncadeada:
  def __init__(self):
      self.topo = None
      self.tamanho = 0

  def empilhar(self, elemento):
    if self.consultar(elemento):
      return False

    no = No(elemento)
    no.set_proximo(self.topo)
    self.topo = no
    self.tamanho += 1
    return True

  def desempilhar(self):
    if self.esta_vazia():
      return None

    elemento = self.topo.get_elemento()
    self.topo = self.topo.get_proximo()
    self.tamanho -= 1
    return elemento

  def consultar(self, elemento):
    atual = self.topo
    while atual is not None:
      if atual.get_elemento() == elemento:
        return True
      atual = atual.get_proximo()
    return False

  def esta_vazia(self):
    return self.tamanho == 0

  def get_tamanho(self):
    return self.tamanho