package vetor;

public class Vetor {
  private String[] elementos;
  private int tamanho;

  public Vetor(int capacidade){
    this.elementos = new String[capacidade];
    this.tamanho = 0;

    System.out.println("A capacidade é: " + capacidade);
  }
}
