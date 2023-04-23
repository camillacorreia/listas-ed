package lista;

public class ListaEncadeada<T> {
  private No<T> inicio;
  private No<T> ultimo;
  private int tamanho = 0;

  public void adiciona(T elemento) {
    No<T> no = new No<T>(elemento);

    if (this.tamanho == 0) {
      this.inicio = no;
    } else {
      this.ultimo.setProximo(no);
    }
    
    this.ultimo = no;
    this.tamanho++;
  }

  @Override
  public String toString() {
    StringBuilder builder = new StringBuilder("[");
    builder.append("ListaEncadeada [inicio=").append(inicio).append("]");
    return builder.toString();
  }
}
