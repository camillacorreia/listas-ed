from no import No

class FilaEncadeada:
    def __init__(self):
      self.inicio = None
      self.fim = None
      self.tamanho = 0

    def enfileirar(self, elemento):
      if self.consultar(elemento):
        return False

      no = No(elemento)

      if self.tamanho == 0:
        self.inicio = no
        self.fim = no
      else:
        self.fim.set_proximo(no)
        self.fim = no
      
      self.tamanho += 1
      return True

    def desenfileirar(self):
      if self.tamanho == 0:
        return None

      elemento = self.inicio.get_elemento()
      self.inicio = self.inicio.get_proximo()
      self.tamanho -= 1

      if self.tamanho == 0:
        self.fim = None

      return elemento

    def consultar(self, elemento):
      atual = self.inicio
      while atual is not None:
        if atual.get_elemento() == elemento:
          return True
        atual = atual.get_proximo()

      return False

    def get_tamanho(self):
      return self.tamanho