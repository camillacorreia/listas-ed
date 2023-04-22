package vetor.teste;

import vetor.Vetor;

public class Aula04 {
  public static void main(String[] args) {

    Vetor vetor = new Vetor(5);

    vetor.adicionar("elemento 1");
    vetor.adicionar("elemento 2");
    vetor.adicionar("elemento 3");
    vetor.adicionar("elemento 4");

    System.out.println(vetor.tamanho());
    System.out.println(vetor.toString());
  }
}
