package pilha.teste;

import pilha.Pilha;

public class Aula13 {
  public static void main(String[] args) {

    Pilha pilha = new Pilha(5);

    pilha.empilhar("elemento 1");
    pilha.empilhar("elemento 2");
    pilha.empilhar("elemento 3");

    System.out.println(pilha);
  }
}
