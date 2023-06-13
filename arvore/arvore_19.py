class NoArvore:
  def __init__(self, chave):
    self.chave = chave
    self.esquerda = None
    self.direita = None

def altura(arv):
  if arv is None:
    return 0

  altura_esquerda = altura(arv.esquerda)
  altura_direita = altura(arv.direita)

  if altura_esquerda > altura_direita:
    return altura_esquerda + 1
  else:
    return altura_direita + 1
  
# Criando uma árvore com vários nós
arvore = NoArvore(10)
arvore.esquerda = NoArvore(5)
arvore.direita = NoArvore(15)
arvore.esquerda.esquerda = NoArvore(3)
arvore.esquerda.direita = NoArvore(7)
arvore.direita.esquerda = NoArvore(12)
arvore.direita.direita = NoArvore(17)

# Calculando a altura da árvore
resultado = altura(arvore)

print(resultado)  # Saída: 3

