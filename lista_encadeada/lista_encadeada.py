from no import No

class ListaEncadeada:
  def __init__(self):
    self.primeiro = None

  def inserir(self, elemento):
    if self.consultar(elemento) is not None:
      return False

    no = No(elemento)
    no.set_proximo(self.primeiro)
    self.primeiro = no
    return True

  def consultar(self, elemento):
    atual = self.primeiro
    while atual is not None:
      if atual.get_elemento() == elemento:
        return True
      atual = atual.get_proximo()

    return False

  def remover(self, elemento):
    atual = self.primeiro
    anterior = None

    while atual is not None:
      if atual.get_elemento() == elemento:
        if anterior is None:
          self.primeiro = atual.get_proximo()
        else:
          anterior.set_proximo(atual.get_proximo())
        return True

      anterior = atual
      atual = atual.get_proximo()

    return False
    
lista = ListaEncadeada()
lista.adicionar(1)
lista.adicionar(2)
lista.adicionar(3)
print(lista)