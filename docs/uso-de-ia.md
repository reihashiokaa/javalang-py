# Uso de Inteligência Artificial no Projeto

Este documento registra os usos relevantes de ferramentas de Inteligência Artificial (IA) durante o desenvolvimento do projeto, garantindo transparência e rastreabilidade das contribuições realizadas.

---

## Registro de Uso 00EX

### Data 

**DD/MM/AAAA**

### Ferramenta Utilizada

Ex.: ChatGPT, GitHub Copilot, Gemini, Claude, etc.

### Objetivo

Descreva brevemente o motivo do uso da IA.

**Exemplo:**

* Gerar sugestão de implementação.
* Auxiliar na criação de documentação.
* Revisar código.
* Propor casos de teste.

### Trecho do Projeto Afetado

Informe os arquivos, módulos ou funcionalidades impactadas.

**Exemplo:**

* `src/services/auth.js`
* `docs/arquitetura.md`
* Módulo de autenticação

### Descrição da Contribuição da IA

Explique resumidamente o que foi gerado ou sugerido pela ferramenta.

**Exemplo:**
A IA sugeriu uma refatoração para reduzir duplicação de código na validação de usuários.

### Validação da Equipe

Descreva como a contribuição foi revisada e validada antes de ser incorporada ao projeto.

**Exemplo:**

* Código revisado por dois membros da equipe.
* Testes automatizados executados com sucesso.
* Documentação conferida e ajustada manualmente.

### Resultado

Indique se a sugestão foi aceita, adaptada ou rejeitada.

**Exemplo:**

* Aceita integralmente.
* Aceita com modificações.
* Rejeitada após revisão.

---

## Histórico

| Data       | Ferramenta | Objetivo | Arquivo/Funcionalidade | Resultado |
| ---------- | ---------- | --------- | ---------------------- | --------- |
| 13/06/2026 | ChatGPT    | Criação de documentação | docs/uso-de-ia.md | Adaptada |
| DD/MM/AAAA | ChatGPT | Criação de plano de implementação | docs/plano-implementacao.md | Aceita com modificações |
| 17/06/2026 | ChatGPT | Preparação de relatório de baseline | docs/relatorios/status-v0.1.md | Aceita com modificações |
| 18/06/2026 | ChatGPT | Apoio na implementação inicial de JInteger | javalang/jinteger.py, javalang/__init__.py, tests/test_jinteger.py | Aceita com modificações |
| 18/06/2026 | ChatGPT | Auxílio na implementação dos métodos básicos de instância da classe JInteger | javalang/jinteger.py, tests/test_jinteger.py, docs/uso-de-ia.md | Aceita com modificações |

---

## Registro de Uso 01

### Data

**13/06/2026**

### Ferramenta Utilizada

ChatGPT

### Objetivo

* Criar modelo de registro de uso de IA para trabalho de GCS

### Trecho do Projeto Afetado

* `docs/uso-de-ia.md`

### Descrição da Contribuição da IA

A IA sugeriu um modelo bem completo e útil para registro de uso de IA.

### Validação da Equipe

* Modelo revisado e adaptado em descrições e títulos.

### Resultado

* Aceita com modificações.

---

## Registro de Uso 02

### Data

17/06/2026

### Ferramenta utilizada

ChatGPT

### Objetivo

Auxiliar na criação do plano inicial de implementação das classes do projeto.

### Trecho do projeto afetado

* `docs/plano-implementacao.md`

### Prompt ou interação representativa

> Criar um plano inicial de implementação para o projeto, definindo a ordem das classes, os primeiros blocos de métodos de `JInteger` e a forma como `JFloat` e `JString` serão tratados nas próximas etapas.

### Descrição da contribuição da IA

A IA sugeriu uma estrutura inicial para o documento de plano de implementação, organizando a ordem das classes em `JInteger`, `JFloat` e `JString`, separando blocos iniciais de métodos e relacionando o plano com as próximas baselines do projeto.

### Validação da equipe

O conteúdo foi revisado e adaptado antes de ser incorporado ao repositório.

### Resultado

Aceita com modificações.

---

## Registro de Uso 03

### Data

17/06/2026

### Ferramenta utilizada

ChatGPT

### Objetivo

Auxiliar na preparação do relatório de status da baseline `v0.1-functional`.

### Trecho do projeto afetado

* `docs/relatorios/status-v0.1.md`
* `docs/uso-de-ia.md`

### Prompt ou interação representativa

> Preparar o conteúdo da issue de baseline `v0.1-functional`, incluindo relatório de status, escopo consolidado, artefatos adicionados, estado da CI, pendências conhecidas e texto de pull request.

### Descrição da contribuição da IA

A IA sugeriu uma estrutura inicial para o relatório de status da baseline, incluindo resumo da etapa, escopo consolidado, decisões registradas, artefatos adicionados, estado da integração contínua e pendências previstas para a próxima milestone.

### Validação da equipe

O conteúdo foi revisado e ajustado antes de ser incorporado ao repositório.

### Resultado

Aceita com modificações.

---

## Registro de Uso 04

### Data

18/06/2026

### Ferramenta utilizada

ChatGPT

### Objetivo

Auxiliar na implementação inicial da classe `JInteger`, incluindo constantes básicas e estrutura inicial de testes.

### Trecho do projeto afetado

- `javalang/jinteger.py`
- `javalang/__init__.py`
- `tests/test_jinteger.py`

### Prompt ou interação representativa

> Ajudar a implementar a primeira issue da milestone v0.2-jinteger.

### Descrição da contribuição da IA

A IA sugeriu a estrutura inicial da classe `JInteger`, com constantes como `MAX_VALUE`, `MIN_VALUE`, `SIZE`, `BYTES` e `TYPE`, além de orientar a criação de testes básicos.

### Validação da equipe

O código foi revisado antes de ser incorporado ao repositório.

### Resultado

Aceito com modificações.

---

## Registro de Uso 05

### Data

18/06/2026

### Ferramenta utilizada

ChatGPT

### Objetivo

Auxiliar na implementação dos métodos de instância da classe `JInteger` (`toString`, `hashCode`, `equals`, `compareTo`).

### Trecho do projeto afetado

- `javalang/jinteger.py`
- `tests/test_jinteger.py`
- `docs/uso-de-ia.md`

### Prompt ou interação representativa

> Implementar métodos de instância de JInteger respeitando rastreabilidade e divisão de commits.

### Descrição da contribuição da IA

A IA auxiliou na organização da implementação em pequenas etapas e sugeriu testes para validar comportamento dos métodos de instância.

### Validação da equipe

O código foi revisado manualmente e testado com pytest.

### Resultado

Aceita com modificações.

---

## Registro de Uso 06

### Data

19/06/2026

### Ferramenta utilizada

ChatGPT

### Objetivo

Auxiliar na implementação dos métodos estáticos de aritmética da classe `JInteger`, incluindo `sum`, `max`, `min` e `compare`.

### Trecho do projeto afetado

- `javalang/jinteger.py`
- `tests/test_jinteger.py`

### Prompt ou interação representativa

> Ajudar a implementar métodos estáticos da classe JInteger (sum, max, min, compare), respeitando limites de commits.

### Descrição da contribuição da IA

A IA auxiliou na implementação dos métodos estáticos da classe `JInteger`, garantindo aderência à especificação da API Java SE 8.

Foram sugeridos:
- implementação dos métodos `sum`, `max`, `min` e `compare` como métodos estáticos;
- criação de testes unitários cobrindo casos positivos, negativos, zero e igualdade.

### Validação da equipe

O código foi revisado manualmente antes do commit final e validado com execução dos testes automatizados (`pytest`).

### Resultado

Aceita com modificações.