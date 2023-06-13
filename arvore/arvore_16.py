class NoArvore:
  def __init__(self, chave):
    self.chave = chave
    self.esquerda = None
    self.direita = None

def somaChaves(arv):
  if arv is None:
    return 0

  return arv.chave + somaChaves(arv.esquerda) + somaChaves(arv.direita)

arvore = NoArvore(10)
arvore.esquerda = NoArvore(5)
arvore.direita = NoArvore(15)
arvore.esquerda.esquerda = NoArvore(3)
arvore.esquerda.direita = NoArvore(7)
arvore.direita.esquerda = NoArvore(12)
arvore.direita.direita = NoArvore(17)

# Calculando a soma das chaves
resultado = somaChaves(arvore)

print(resultado)  # Saída: 69 (10 + 5 + 15 + 3 + 7 + 12 + 17)
