package pilha;

public class Pilha {
  private String[] elementos;
  private int tamanho;

  public Pilha(int capacidade){
    this.elementos = new String[capacidade];
    this.tamanho = 0;
  }

  public void empilhar(String elemento){
    this.aumentarCapacidade();

    int i = 0;
    while (i < this.tamanho && this.elementos[i] != elemento) {
      i++;
    }
    if (i == this.tamanho) {
      if (this.tamanho < this.elementos.length) {
        this.elementos[this.tamanho] = elemento;
        this.tamanho++;
      }
    }
  }

  public boolean estaVazia(){
    return this.tamanho == 0;
  }

  public String topo(){
    return this.elementos[this.tamanho - 1];
  }

  public String desempilhar(){
   if(this.estaVazia()){
     return null;
   }

   return this.elementos[--tamanho];
  }

  private void aumentarCapacidade(){
    if (this.tamanho == this.elementos.length) {
      String[] elementosNovos = new String[this.elementos.length * 2];
      int i = 0;
      while (i < this.elementos.length) {
        elementosNovos[i] = this.elementos[i];
        i++;
      }
      this.elementos = elementosNovos;

      System.out.println("Aumentou a capacidade para " + this.elementos.length);
    }
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("[");
    int i = 0;

    while (i < this.tamanho - 1) {
      s.append(this.elementos[i]);
      s.append(", ");
      i++;
    }

    if (this.tamanho > 0) {
      s.append(this.elementos[this.tamanho - 1]);
    }

    s.append("]");
    return s.toString();
  }
}
