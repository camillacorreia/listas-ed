package lista;

public class ListaEncadeada<T> {
  private No<T> inicio;
  private No<T> ultimo;
  private int tamanho = 0;

  public void adicionar(T elemento) {
    No<T> no = new No<T>(elemento);

    if (this.tamanho == 0) {
      this.inicio = no;
    } else {
      this.ultimo.setProximo(no);
    }
    
    this.ultimo = no;
    this.tamanho++;
  }

  public int getTamanho() {                                                                                                                                                                                                         
    return this.tamanho;
  }

  @Override
  public String toString() {
    if (this.tamanho == 0) {
      return "[]";
    }

    StringBuilder builder = new StringBuilder("[");
    // builder.append("ListaEncadeada [inicio=").append(inicio).append("]");

    No<T> atual = this.inicio;
    int i = 0;
    while (i < this.tamanho - 1) {
      builder.append(atual.getElemento()).append(",");
      atual = atual.getProximo();
      i++;
    }
    builder.append(atual.getElemento()).append("]");
    return builder.toString();
  }
}