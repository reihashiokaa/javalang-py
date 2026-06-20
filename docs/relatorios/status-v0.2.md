# Relatório de Status da Baseline v0.2-jinteger

## Identificação da baseline

**Baseline:** `v0.2-jinteger`
**Data:** 20/06/2026
**Milestone relacionada:** `v0.2-jinteger`
**Issue de fechamento:** #36
**Responsável:** Reinaldo

## Objetivo

Esta baseline consolida a implementação inicial da classe `JInteger`, reunindo os métodos, testes, adaptações documentadas e registros de apoio produzidos durante a milestone `v0.2-jinteger`.

O objetivo desta etapa foi aproximar a classe `JInteger` da API Java SE 8, respeitando as adaptações necessárias para Python e mantendo o processo de Gerência de Configuração de Software definido pelo projeto.

## Escopo consolidado

A baseline `v0.2-jinteger` inclui:

* estrutura inicial da classe `JInteger`;
* constantes básicas da classe;
* construtor e armazenamento interno do valor inteiro;
* métodos de representação, igualdade, hash e comparação;
* métodos de conversão básica;
* métodos de parsing e criação por valor;
* métodos de formatação por bases numéricas;
* operações sem sinal;
* operações aritméticas estáticas;
* operações bit a bit;
* testes automatizados relacionados aos métodos implementados;
* registros de adaptação entre Java e Python;
* registros de uso de IA relacionados à milestone.

## Itens de configuração envolvidos

Os principais itens de configuração afetados nesta baseline foram:

* `javalang/jinteger.py`;
* `javalang/__init__.py`;
* `tests/test_jinteger.py`;
* `docs/adaptacoes.md`;
* `docs/uso-de-ia.md`;
* `docs/relatorios/status-v0.2.md`.

## Issues e pull requests

As issues da milestone `v0.2-jinteger` foram trabalhadas por meio de branches próprias e pull requests revisados antes da integração na branch `main`.

Foram concluídas as issues relacionadas à implementação, testes, documentação de adaptações e fechamento da baseline.

## Verificação da integração contínua

Antes do fechamento da baseline, foram executadas as verificações locais:

* `python -m pytest`
* `python -m ruff check .`

Resultado:

- Testes automatizados: aprovados.
- Verificação de estilo/lint: aprovada.
- Situação da CI no GitHub: a conferir após abertura do PR.

## Adaptações documentadas

As principais adaptações documentadas envolveram diferenças entre a API Java SE 8 e a implementação em Python, incluindo:

* ausência de sobrecarga de métodos em Python;
* uso de parâmetros opcionais em métodos como `parseInt` e `valueOf`;
* representação de inteiros de 32 bits;
* tratamento de valores sem sinal;
* representação de valores negativos em bases numéricas;
* diferenças entre tipos primitivos Java e o tipo `int` do Python.

As decisões foram registradas em `docs/adaptacoes.md`.

## Uso de IA

O uso de IA durante a milestone foi registrado em `docs/uso-de-ia.md`.

Os registros incluem apoio em:

* organização de implementação;
* criação de testes;
* documentação de adaptações;
* preparação de textos de apoio;
* resolução orientada de etapas da milestone.

As sugestões foram revisadas e adaptadas antes de serem incorporadas ao projeto.

## Conflitos de merge

Durante a milestone, ocorreram conflitos reais em arquivos compartilhados, principalmente em:

* `javalang/jinteger.py`;
* `tests/test_jinteger.py`;
* `docs/adaptacoes.md`;
* `docs/uso-de-ia.md`.

Os conflitos foram resolvidos nas próprias branches dos pull requests e registrados no histórico do Git.

## Estado da baseline

A baseline `v0.2-jinteger` está pronta para publicação após:

* confirmação de que todos os pull requests da milestone foram revisados e mergeados;
* confirmação de que a CI está passando;
* publicação da release `v0.2-jinteger` no GitHub.

## Texto sugerido para a release v0.2-jinteger

### Título

`v0.2-jinteger`

### Descrição

Esta release consolida a baseline `v0.2-jinteger`, referente à implementação inicial da classe `JInteger` do projeto `javalang-py`.

### Principais entregas

* Implementação da classe `JInteger`.
* Definição das constantes principais da classe.
* Implementação de métodos de representação, comparação e conversão.
* Implementação de parsing e criação por valor.
* Implementação de formatação em diferentes bases numéricas.
* Implementação de operações sem sinal.
* Implementação de operações aritméticas estáticas.
* Implementação de operações bit a bit.
* Criação e revisão de testes automatizados.
* Registro das adaptações entre Java e Python.
* Registro do uso de IA durante a milestone.

### Verificações

* `python -m pytest`
* `python -m ruff check .`

### Observações

Esta release representa uma baseline intermediária do projeto, focada na classe `JInteger`. As próximas baselines devem avançar para as demais classes previstas no escopo do projeto.
