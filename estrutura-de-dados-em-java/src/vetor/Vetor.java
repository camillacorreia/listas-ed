package vetor;

public class Vetor {
  private String[] elementos;
  private int tamanho;

  public Vetor(int capacidade){
    this.elementos = new String[capacidade];
    this.tamanho = 0;

    System.out.println("A capacidade é: " + capacidade);
  }

  public void adicionar(String elemento) {
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

    System.out.println("Foi adicionado o: " + elemento);
  }

  // 0 1 2 3 4 5 6 = tamanho é 5
  // B C E F G + +
  // Colocar D na posicao 2
  public boolean adicionarNaPosicao(int posicao, String elemento){
    if (!(posicao >= 0 && posicao < tamanho)){
      throw new IllegalArgumentException("Posição inválida");
    }

    this.aumentarCapacidade();

    //mover todos os elementos
    int i = this.tamanho - 1;
    while (i >= posicao) {
      this.elementos[i + 1] = this.elementos[i];
      i--;
    }

    //colocar o elemento na posicao
    this.elementos[posicao] = elemento;
    this.tamanho++;

    return true;
  }

  public String buscarPosicao(int posicao){
    if (!(posicao >= 0 && posicao < tamanho)){
      throw new IllegalArgumentException("Posição inválida");
    }
    return this.elementos[posicao];
  }

  public int buscar(String elemento){
    int i = 0;
    while (i < this.tamanho && this.elementos[i] != elemento) {
      i++;
    }
    if (i == this.tamanho) {
      return -1;
    } else {
      return i;
    }
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

  public int tamanho(){
    return this.tamanho;
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
