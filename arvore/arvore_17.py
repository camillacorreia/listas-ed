class NoArvore:
  def __init__(self, chave):
    self.chave = chave
    self.esquerda = None
    self.direita = None

def numeroNos(arv):
  if arv is None:
    return 0

  return 1 + numeroNos(arv.esquerda) + numeroNos(arv.direita)

# Criando uma árvore com um único nó (chave = 5)
arvore = NoArvore(5)

# Calculando o número de nós
resultado = numeroNos(arvore)

print(resultado)  # Saída: 1

# Criando uma árvore com vários nós
arvore = NoArvore(10)
arvore.esquerda = NoArvore(5)
arvore.direita = NoArvore(15)
arvore.esquerda.esquerda = NoArvore(3)
arvore.esquerda.direita = NoArvore(7)
arvore.direita.esquerda = NoArvore(12)
arvore.direita.direita = NoArvore(17)

# Calculando o número de nós
resultado = numeroNos(arvore)

print(resultado)  # Saída: 7
