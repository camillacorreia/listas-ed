package fila.teste;

import fila.Fila;

public class Aula21 {
  public static void main(String[] args) {

    Fila fila = new Fila(5);

    fila.enfileirar("elemento 1");
    fila.enfileirar("elemento 2");
    fila.enfileirar("elemento 3");

    System.out.println(fila.primeiro());
    System.out.println(fila);
  }
}
