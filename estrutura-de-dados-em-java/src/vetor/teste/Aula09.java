package vetor.teste;

import vetor.Vetor;

public class Aula09 {
  public static void main(String[] args) {

    Vetor vetor = new Vetor(6);

    vetor.adicionar("elemento 1");
    vetor.adicionar("elemento 2");
    vetor.adicionar("elemento 3");
    vetor.adicionar("elemento 4");
    vetor.adicionar("elemento 5");
    vetor.adicionar("elemento 6");

    vetor.removerNaPosicao(1);
    vetor.remover("elemento 6");

    System.out.println(vetor);
  }
}
