from no import No

class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        self.ultimo = None
        self.tamanho = 0

    def adicionar(self, elemento):
        no = No(elemento)

        if self.tamanho == 0:
            self.inicio = no
        else:
            self.ultimo.set_proximo(no)
        
        self.ultimo = no
        self.tamanho += 1

    def get_tamanho(self):
        return self.tamanho

    def limpar(self):
      atual = self.inicio
      while atual is not None:
        proximo = atual.get_proximo()
        atual.set_elemento(None)
        atual.set_proximo(None)
        atual = proximo
      self.inicio = None
      self.ultimo = None
      self.tamanho = 0

    def __str__(self):
      if self.tamanho == 0:
        return "[]"

      builder = "["
      atual = self.inicio
      i = 0
      while i < self.tamanho - 1:
        builder += str(atual.get_elemento()) + ","
        atual = atual.get_proximo()
        i += 1
      builder += str(atual.get_elemento()) + "]"
      return builder
    
lista = ListaEncadeada()
lista.adicionar(1)
lista.adicionar(2)
lista.adicionar(3)
print(lista)