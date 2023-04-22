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

  public String buscarPosicao(int posicao){
    if (!(posicao >= 0 && posicao < tamanho)){
      throw new IllegalArgumentException("Posição inválida");
    }
    return this.elementos[posicao];
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
