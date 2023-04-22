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
}
