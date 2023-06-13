class NoArvore:
  def __init__(self, chave):
    self.chave = chave
    self.esquerda = None
    self.direita = None

def menorChave(arv):
  if arv is None:
    return 0

  while arv.esquerda is not None:
    arv = arv.esquerda

  return arv.chave
