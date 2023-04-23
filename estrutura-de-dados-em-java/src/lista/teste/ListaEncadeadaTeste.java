package lista.teste;

import lista.ListaEncadeada;

public class ListaEncadeadaTeste {
  public static void main(String[] args) {
    ListaEncadeada<Integer> lista = new ListaEncadeada<>();
    lista.adicionar(1);

    System.out.println(lista);

    lista.adicionar(2);
    System.out.println(lista);

    lista.adicionar(3);
    System.out.println(lista);

    System.out.println("Tamanho = " + lista.getTamanho());

    lista.limpar();
    System.out.println(lista);
  }
}