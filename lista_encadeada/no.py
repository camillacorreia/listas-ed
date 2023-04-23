class No:
  def __init__(self, elemento):
    self.elemento = elemento
    self.proximo = None

  def get_elemento(self):
    return self.elemento

  def set_elemento(self, elemento):
    self.elemento = elemento

  def get_proximo(self):
    return self.proximo

  def set_proximo(self, proximo):
    self.proximo = proximo