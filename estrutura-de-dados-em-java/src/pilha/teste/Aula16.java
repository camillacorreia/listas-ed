package pilha.teste;

import pilha.Pilha;

public class Aula16 {
  public static void main(String[] args) {

    Pilha pilha = new Pilha(5);

    pilha.empilhar("elemento 1");
    pilha.empilhar("elemento 2");
    pilha.empilhar("elemento 3");

    System.out.println("ANTES" + " " + pilha);
    System.out.println(pilha.desempilhar());
    System.out.println("DEPOIS" + " " + pilha);
  }
}
