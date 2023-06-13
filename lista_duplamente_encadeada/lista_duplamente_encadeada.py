class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def esta_vazia(self):
        return self.primeiro is None

    def inserir_inicio(self, dado):
        novo_no = No(dado)
        if self.esta_vazia():
            self.primeiro = novo_no
            self.ultimo = novo_no
        else:
            novo_no.proximo = self.primeiro
            self.primeiro.anterior = novo_no
            self.primeiro = novo_no

    def inserir_fim(self, dado):
        novo_no = No(dado)
        if self.esta_vazia():
            self.primeiro = novo_no
            self.ultimo = novo_no
        else:
            novo_no.anterior = self.ultimo
            self.ultimo.proximo = novo_no
            self.ultimo = novo_no

    def remover_inicio(self):
        if self.esta_vazia():
            raise Exception("A lista está vazia.")
        else:
            no_removido = self.primeiro
            if self.primeiro == self.ultimo:
                self.primeiro = None
                self.ultimo = None
            else:
                self.primeiro = self.primeiro.proximo
                self.primeiro.anterior = None
            return no_removido.dado

    def remover_fim(self):
        if self.esta_vazia():
            raise Exception("A lista está vazia.")
        else:
            no_removido = self.ultimo
            if self.primeiro == self.ultimo:
                self.primeiro = None
                self.ultimo = None
            else:
                self.ultimo = self.ultimo.anterior
                self.ultimo.proximo = None
            return no_removido.dado

    def imprimir_lista(self):
        if self.esta_vazia():
            print("A lista está vazia.")
        else:
            no_atual = self.primeiro
            while no_atual is not None:
                print(no_atual.dado)
                no_atual = no_atual.proximo
                
    def remover_ultimo_elemento(self):
      if self.esta_vazia():
          raise Exception("A lista está vazia.")
      else:
          no_removido = self.ultimo
          if self.primeiro == self.ultimo:
              self.primeiro = None
              self.ultimo = None
          else:
              self.ultimo = self.ultimo.anterior
              self.ultimo.proximo = None
          return no_removido.dado
      
    def contar_elementos_maiores(self, x):
      contador = 0
      no_atual = self.primeiro
      while no_atual is not None:
          if no_atual.dado > x:
              contador += 1
          no_atual = no_atual.proximo
      return contador

# Criando a lista
lista = ListaDuplamenteEncadeada()

# Inserindo elementos no início da lista
lista.inserir_inicio(3)
lista.inserir_inicio(2)
lista.inserir_inicio(1)

# Inserindo elementos no fim da lista
lista.inserir_fim(4)
lista.inserir_fim(5)

# Imprimindo a lista
lista.imprimir_lista()  # Output: 1 2 3 4 5

# Removendo elementos do início e fim da lista
lista.remover_inicio()  # Remove o 1
lista.remover_fim()     # Remove o 5

# Imprimindo a lista após as remoções
lista.imprimir_lista()  # Output: 2 3 4