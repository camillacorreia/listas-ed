# Listas de Exercícios

| Disciplina      | MATD04 - ESTRUTURAS DE DADOS                                      |
| --------------- | ----------------------------------------------------------------- |
| **Professor**   | Flávio Assis                                                      |
| **Semestre**    | 2023.1                                                            |

## Assuntos
- [x] Listas
- [x] Filas
- [x] Pilhas
- [x] Listas com alocação dinâmica
- [x] Filas e Pilhas com alocação dinâmica
- [x] Listas encadeadas
- [x] Listas duplamente encadeadas

#### Lista
São estrutura de dados que permitem armazenar e organizar um conjunto de elementos em uma determinada ordem. Em geral, as listas são implementadas como um conjunto de nós ou elementos que contêm informações sobre o próprio elemento e um ponteiro para o próximo elemento na lista.

#### Filas
São estruturas de dados lineares que seguem o princípio "primeiro a entrar, primeiro a sair" (FIFO) e são comumente usadas em algoritmos de processamento de dados que exigem que as operações sejam executadas na ordem em que foram recebidas. As operações principais de uma fila são "enfileirar" (adicionar um elemento ao final) e "desenfileirar" (remover o primeiro elemento).

#### Pilas
Pilhas são estruturas de dados lineares que seguem o princípio "último a entrar, primeiro a sair" (LIFO - Last-In, First-Out) e são comumente usadas em algoritmos que envolvem a reversão de ordem, como por exemplo, a inversão de uma string. As principais operações de uma pilha são "empilhar" (adicionar um elemento no topo) e "desempilhar" (remover o elemento do topo).

#### Listas, Filas e Pilhas com alocação dinâmica
Quando usadas com alocação dinâmica, essas estruturas permitem que seus tamanhos sejam ajustados durante a execução do programa. Podendo crescer ou encolher em tamanho à medida que elementos são adicionados ou removidos.

#### Listas encadeadas
São estruturas de dados que permitem armazenar um conjunto de elementos em uma ordem específica e que permitem que novos elementos sejam adicionados ou removidos dinamicamente durante a execução do programa. Essas listas são implementadas utilizando ponteiros para criar uma sequência de elementos que estão vinculados entre si, formando uma cadeia de ponteiros. Cada elemento da lista contém um ponteiro que aponta para o próximo elemento da lista. Isso permite que as listas encadeadas tenham tamanho variável e sejam facilmente modificadas durante a execução do programa. As principais operações de uma lista encadeada são a adição e remoção de elementos em posições específicas da lista.

#### Diferença entre listas com alocação dinâmica e listas encadeadas
A principal diferença entre as listas com alocação dinâmica e as listas encadeadas é a forma como elas alocam e gerenciam a memória para armazenar seus elementos.

Em uma lista com alocação dinâmica, os elementos são armazenados em um bloco contíguo de memória alocado dinamicamente durante a execução do programa. A lista tem um tamanho fixo, determinado no momento da alocação de memória, e pode ser aumentada ou diminuída mediante realocação de memória.

Já em uma lista encadeada, cada elemento é armazenado em um nó independente, que contém um ponteiro para o próximo elemento da lista. Dessa forma, não há necessidade de alocar uma grande quantidade de memória de uma vez só, o que torna as listas encadeadas mais flexíveis e eficientes em termos de uso de memória, principalmente em casos onde não se sabe previamente a quantidade de elementos que serão armazenados.

Em resumo, a principal diferença entre as duas estruturas de dados está na forma como elas gerenciam a memória para armazenar seus elementos: a lista com alocação dinâmica usa um bloco contíguo de memória enquanto a lista encadeada usa vários nós independentes com ponteiros entre eles.

##### Exemplo
Uma lista com alocação dinâmica seria como uma fila onde todas as pessoas têm que ficar em uma mesma área limitada, onde a fila tem um tamanho fixo. Se você quiser adicionar mais pessoas na fila, precisará aumentar essa área para acomodá-las. E se algumas pessoas saírem da fila, você pode diminuir essa área.

Já uma lista encadeada seria como uma fila onde cada pessoa pode ficar em qualquer lugar, sem precisar se preocupar com o espaço que a fila ocupa como um todo. Cada pessoa tem um papel com o nome da pessoa seguinte na fila, e assim a fila é formada por uma série de papéis ligados uns aos outros. Se você quiser adicionar ou remover pessoas da fila, basta ajustar os papéis de cada pessoa para indicar a pessoa seguinte correta.

Essa é a diferença entre as listas com alocação dinâmica e as listas encadeadas: uma usa uma área limitada para armazenar todos os elementos da lista, enquanto a outra usa uma série de elementos independentes ligados uns aos outros.

#### Listas duplamente encadeadas
Essas listas são semelhantes às listas encadeadas simples, mas cada elemento da lista contém dois ponteiros, um que aponta para o próximo elemento e outro que aponta para o elemento anterior da lista. Isso permite que as operações de adição e remoção de elementos sejam realizadas com mais eficiência, pois não é necessário percorrer toda a lista para encontrar o elemento anterior ou posterior a um determinado elemento. As principais operações de uma lista duplamente encadeada são a adição e remoção de elementos em posições específicas da lista, bem como a navegação para frente e para trás na lista.

### [Anotações - notion](https://study-camilla.notion.site/Estruturas-de-Dados-df346772a99b4d0fbc6fb0d329112e23)