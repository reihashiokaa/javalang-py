# ADR 0002 — Convenção de nomenclatura das classes

## Status

Aprovado

## Data

16/06/2026

## Contexto

O projeto tem como objetivo implementar em Python versões adaptadas de classes da API Java SE 8. Antes do início da implementação, a equipe precisou definir uma convenção de nomenclatura para as classes principais do projeto.

A decisão precisava evitar confusão com os tipos nativos do Python e manter uma associação clara com as classes originais da plataforma Java.

## Decisão

A equipe adotará a seguinte nomenclatura para as classes principais do projeto:

* `JString`
* `JInteger`
* `JFloat`

As opções consideradas foram:

* `JString`, `JInteger` e `JFloat`;
* `JavaString`, `JavaInteger` e `JavaFloat`;
* utilização de um pacote dedicado contendo classes chamadas `String`, `Integer` e `Float`.

Após discussão, a equipe escolheu utilizar o prefixo `J`.

A nomenclatura adotada deverá ser utilizada em toda a documentação, código-fonte, testes, issues e pull requests relacionados ao projeto.

## Consequências

O uso do prefixo `J` diferencia claramente as classes do projeto dos tipos nativos do Python (`str`, `int` e `float`).

Além disso, os nomes permanecem curtos, fáceis de identificar e próximos da nomenclatura utilizada pela API Java original.

Como consequência, todas as implementações futuras deverão seguir essa convenção para manter a consistência do projeto.
