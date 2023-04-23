### Exercício 1 - Lista

Uma lista é um tipo de dados que representa um conjunto de elementos dispostos em uma sequência.
Cada elemento da lista possui uma posição (na lista) associada a ele: o primeiro elemento, o segundo, etc.
E definida, portanto, uma ordem total sobre as posições dos elementos na lista.
Considere uma estrutura em Python, definida da seguinte forma:
```lista = [0] * maxelem```

Onde lista será a estrutura de armazenamento de dados de uma `lista` e `maxelem` é o número máximo de elementos na lista. Consideraremos essa estrutura como sendo estática, pois o número máximo de elementos é fixo e definido inicialmente.

Observe que a estrutura que irá armazenar a lista possui maxelem elementos, todos inicialmente contendo o valor zero. Sobre a estrutura lista, queremos armazenar uma lista tal que:

- a lista conterá apenas números inteiros;
- a lista pode ter de zero a maxelem elementos;
- a lista conterá operações para:

(a) inserir um novo elemento na lista com valor x, ou seja, inserir um novo valor inteiro x na lista: a lista não poderá conter elementos repetidos (elementos com mesmo valor);

(b) remover um elemento da lista com valor x, caso exista;

(c) consultar se existe ou não um elemento de valor x na lista. Se sim, deve-se indicar em que posição da lista ele se encontra;

(d) imprimir os elementos que estão atualmente na lista.

Escreva uma classe Lista em Python para implementar essa lista, sobre uma estrutura estática, como definida acima.