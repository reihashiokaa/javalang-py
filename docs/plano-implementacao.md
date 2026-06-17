\# Plano inicial de implementação



Este documento organiza a ordem inicial de implementação das classes do projeto e os principais blocos de trabalho previstos para cada etapa.



O plano poderá ser ajustado conforme a equipe avance nas milestones, encontre diferenças relevantes entre Java e Python ou identifique métodos que precisem de adaptação documentada.



\## Ordem de implementação



A equipe adotará a seguinte ordem de implementação:



1\. `JInteger`

2\. `JFloat`

3\. `JString`



A ordem foi escolhida para iniciar por uma classe menor e mais controlável, avançar depois para os detalhes de ponto flutuante e deixar a classe mais extensa para uma etapa em que o fluxo de issues, branches, pull requests e revisões já esteja mais consolidado.



\## Relação com as baselines



| Baseline          | Foco principal                                                                          |

| ----------------- | --------------------------------------------------------------------------------------- |

| `v0.1-functional` | Estrutura inicial, decisões, configuração do repositório e plano de implementação       |

| `v0.2-jinteger`   | Implementação inicial da classe `JInteger` e seus testes                                |

| `v0.3-jfloat`     | Implementação inicial da classe `JFloat`, incluindo casos de NaN, infinito e conversões |

| `v0.4-jstring`    | Implementação inicial da classe `JString` e seus principais grupos de métodos           |

| `v1.0.0`          | Consolidação final, documentação, auditorias e release final                            |



\## Diretrizes gerais



As implementações serão organizadas em issues pequenas. Cada issue deve tratar um conjunto limitado de métodos relacionados, evitando mudanças grandes demais em um único pull request.



Cada bloco de implementação deve considerar:



\* comportamento esperado segundo a especificação Java SE 8;

\* diferenças relevantes entre Java e Python;

\* testes associados;

\* documentação de adaptações, quando necessário.



Métodos que não forem implementados ou que exigirem adaptação devem ser registrados em `docs/adaptacoes.md`.



\## Plano para `JInteger`



A classe `JInteger` será a primeira classe implementada. Ela será usada para consolidar o fluxo inicial de implementação, testes e revisão.



Blocos iniciais previstos:



| Bloco                         | Métodos ou elementos relacionados                                                                                                                              | Observações                                                                       |

| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |

| Constantes e estrutura básica | `MAX\_VALUE`, `MIN\_VALUE`, `SIZE`, `BYTES`, `TYPE`, construtor inicial                                                                                          | Definir a representação interna do valor inteiro e os limites de 32 bits          |

| Conversões básicas            | `byteValue`, `shortValue`, `intValue`, `longValue`, `floatValue`, `doubleValue`                                                                                | Registrar diferenças entre os tipos primitivos do Java e o `int` do Python        |

| Representação e comparação    | `toString`, `hashCode`, `equals`, `compareTo`                                                                                                                  | Garantir comportamento previsível para comparação entre instâncias                |

| Parsing                       | `parseInt`, `parseInt` com radix, `valueOf`, `decode`                                                                                                          | Criar testes para entradas válidas, inválidas e bases numéricas diferentes        |

| Formatação por base           | `toBinaryString`, `toOctalString`, `toHexString`, `toUnsignedString`                                                                                           | Avaliar comportamento de inteiros negativos considerando representação de 32 bits |

| Operações bit a bit           | `bitCount`, `highestOneBit`, `lowestOneBit`, `numberOfLeadingZeros`, `numberOfTrailingZeros`, `reverse`, `reverseBytes`, `rotateLeft`, `rotateRight`, `signum` | Dividir em mais de uma issue caso o bloco fique grande                            |

| Operações estáticas           | `sum`, `max`, `min`, `compare`, `compareUnsigned`, `divideUnsigned`, `remainderUnsigned`                                                                       | Separar operações simples das operações sem sinal                                 |



A implementação de `JInteger` deve priorizar métodos com comportamento claro e testável, para que a equipe consiga validar rapidamente o fluxo de contribuição.



\## Plano para `JFloat`



A classe `JFloat` será tratada após `JInteger`, aproveitando decisões já tomadas sobre estrutura de classes, testes e documentação.



Blocos previstos:



| Bloco                            | Métodos ou elementos relacionados                                                                        | Observações                                                              |

| -------------------------------- | -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |

| Constantes e estrutura básica    | `MAX\_VALUE`, `MIN\_VALUE`, `MIN\_NORMAL`, `POSITIVE\_INFINITY`, `NEGATIVE\_INFINITY`, `NaN`, `SIZE`, `BYTES` | Registrar diferenças entre o `Float` do Java e o `float` do Python       |

| Conversões básicas               | `byteValue`, `shortValue`, `intValue`, `longValue`, `floatValue`, `doubleValue`                          | Definir comportamento esperado para truncamento e valores especiais      |

| Verificações IEEE 754            | `isNaN`, `isInfinite`, `isFinite`                                                                        | Criar testes específicos para NaN, infinito positivo e infinito negativo |

| Parsing e formatação             | `parseFloat`, `valueOf`, `toString`, `toHexString`                                                       | Avaliar diferenças de representação textual entre Java e Python          |

| Conversão binária                | `floatToIntBits`, `floatToRawIntBits`, `intBitsToFloat`                                                  | Documentar decisões caso a representação de 32 bits precise ser simulada |

| Comparação e operações estáticas | `compare`, `max`, `min`, `sum`                                                                           | Considerar comportamento com NaN e infinitos                             |



\## Plano para `JString`



A classe `JString` será implementada após as classes numéricas, por ter maior quantidade de métodos e mais diferenças potenciais entre Java e Python.



Blocos previstos:



| Bloco                           | Métodos ou elementos relacionados                                            | Observações                                                         |

| ------------------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------- |

| Estrutura básica e construtores | Construtores simples e representação interna da string                       | Definir imutabilidade e comportamento básico da classe              |

| Acesso e tamanho                | `length`, `isEmpty`, `charAt`, `toCharArray`, `getBytes`                     | Criar testes para string vazia, índices válidos e índices inválidos |

| Comparação                      | `equals`, `equalsIgnoreCase`, `compareTo`, `compareToIgnoreCase`, `hashCode` | Verificar diferenças de comparação entre Java e Python              |

| Busca                           | `indexOf`, `lastIndexOf`, `contains`, `startsWith`, `endsWith`               | Dividir por grupos de métodos para manter PRs pequenos              |

| Transformação                   | `substring`, `concat`, `replace`, `toLowerCase`, `toUpperCase`, `trim`       | Garantir que métodos de transformação não alterem o valor original  |

| Expressões regulares            | `matches`, `replaceFirst`, `replaceAll`, `split`                             | Registrar diferenças entre regex de Java e Python quando necessário |

| Métodos estáticos               | `valueOf`, `copyValueOf`, `format`, `join`                                   | Priorizar métodos com comportamento mais direto em Python           |



\## Critérios para avanço entre etapas



Uma classe pode avançar para a baseline correspondente quando:



\* os blocos definidos para a etapa tiverem sido tratados por issues;

\* os pull requests principais tiverem sido revisados;

\* os testes existentes estiverem passando;

\* as adaptações conhecidas estiverem registradas;

\* as pendências relevantes estiverem descritas na release da baseline.



\## Observações finais



Este plano representa uma organização inicial. A equipe poderá revisar a divisão dos blocos conforme o projeto evoluir, desde que as mudanças sejam registradas nas issues e refletidas na documentação quando necessário.



