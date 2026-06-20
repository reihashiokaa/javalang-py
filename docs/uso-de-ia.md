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
| 17/06/2026 | ChatGPT | Preparação de relatório de baseline | `docs/relatorios/status-v0.1.md` | Aceita com modificações |
| 18/06/2026 | ChatGPT | Apoio na implementação inicial de JInteger | `javalang/jinteger.py`, `javalang/__init__.py`, `tests/test_jinteger.py` | Aceita com modificações |
| 18/06/2026 | ChatGPT | axiliar na implementação dos métodos básicos de instância da classe JInteger |`javalang/jinteger.py`, `tests/test_jinteger.py` e `docs/uso-de-ia.md` | Aceita |
| 19/06/2026 | ChatGPT | Apoio na implementação de parsing e criação por valor em JInteger | `javalang/jinteger.py`, `tests/test_jinteger.py`, `docs/adaptacoes.md`, `docs/uso-de-ia.md` | Aceita com modificações |
| 19/06/2026 | ChatGPT | Auxiliar na implementação dos métodos de conversão da classe JInteger |`javalang/jinteger.py`, `tests/test_jinteger.py`, `docs/uso-de-ia.md` e `docs/adaptacoes.md` | Aceita |
| 19/06/2026 | ChatGPT | Auxiliar na implementação dos métodos operacao bit a bit classe JInteger |`javalang/jinteger.py`, `tests/test_jinteger.py`, `docs/uso-de-ia.md` e `docs/adaptacoes.md` | Aceita com modificações |
| 20/06/2026 | ChatGPT | Apoio na preparação do relatório da baseline v0.2-jinteger | `docs/relatorios/status-v0.2.md`, `docs/uso-de-ia.md` | Aceita com modificações |
| 20/06/2026 | ChatGPT | Apoio na implementação inicial de JFloat | `javalang/jfloat.py`, `javalang/__init__.py`, `tests/test_jfloat.py`, `docs/adaptacoes.md`, `docs/uso-de-ia.md` | Aceita com modificações |

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

**19/06/2026**

### Ferramenta Utilizada

ChatGPT

### Objetivo

Auxiliar na implementação das operações sem sinal da classe `JInteger`, incluindo parsing, conversão textual, comparação, divisão e resto com interpretação de 32 bits sem sinal.

### Trecho do projeto afetado

* `javalang/jinteger.py`
* `tests/test_jinteger.py`
* `docs/adaptacoes.md`
* `docs/uso-de-ia.md`

### Prompt ou interação representativa

> Ajudar a implementar a issue #30, responsável pelos métodos `parseUnsignedInt`, `toUnsignedString`, `compareUnsigned`, `divideUnsigned` e `remainderUnsigned`, respeitando a regra de até 3 métodos por commit e até 7 métodos por pull request.

### Descrição da contribuição da IA

A IA auxiliou na organização da implementação das operações sem sinal de `JInteger`, sugerindo uma estratégia baseada em máscara de 32 bits para interpretar valores negativos como inteiros sem sinal.

Também sugeriu a divisão da implementação em commits menores, separando os métodos `parseUnsignedInt` e `toUnsignedString` dos métodos `compareUnsigned`, `divideUnsigned` e `remainderUnsigned`.

Além disso, apoiou a criação de testes automatizados para parsing válido e inválido, conversão textual em diferentes bases, comparação sem sinal, divisão, resto e divisão por zero. Também auxiliou na redação do registro de adaptações técnicas em `docs/adaptacoes.md`.

### Validação da equipe

As sugestões foram revisadas antes de serem incorporadas ao projeto. A implementação foi mantida dentro do escopo da issue #30, sem adicionar métodos de outras issues.

As verificações locais foram executadas com sucesso utilizando:

* `python -m ruff check .`
* `python -m pytest`

### Resultado

Aceita com modificações.


## Registro de Uso 07

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

---

## Registro de Uso 09

### Data

19/06/2026

### Ferramenta utilizada

ChatGPT

### Objetivo

Auxiliar na implementação dos métodos de parsing e criação por valor da classe `JInteger`, incluindo `parseInt`, `valueOf` e `decode`.

### Trecho do projeto afetado

- `javalang/jinteger.py`
- `tests/test_jinteger.py`
- `docs/adaptacoes.md`
- `docs/uso-de-ia.md`

### Prompt ou interação representativa

> Ajudar a implementar a issue de parsing e criação por valor de `JInteger`, criando os métodos `parseInt`, `valueOf` e `decode`, seus testes correspondentes e os registros de adaptação necessários.

### Descrição da contribuição da IA

A IA auxiliou na organização da implementação dos métodos `parseInt`, `valueOf` e `decode`. Também sugeriu casos de teste para valores decimais, valores com radix, entradas inválidas, limites de 32 bits e formatos aceitos por `decode`, como decimal, hexadecimal e octal.

Além disso, apoiou a redação da documentação de adaptação em `docs/adaptacoes.md`, explicando a diferença entre sobrecarga de métodos em Java e o uso de parâmetros opcionais em Python.

### Validação da equipe

As sugestões foram revisadas antes de serem incorporadas ao projeto. A implementação foi mantida dentro do escopo da issue, sem adicionar operações sem sinal, formatação por base, comparação, conversões básicas ou operações bit a bit.

As verificações locais foram executadas utilizando:

- `python -m pytest`
- `python -m ruff check .`

### Resultado

Aceita com modificações.

## Registro de Uso 008

### Data 

18/06/2026

### Ferramenta Utilizada

Claude

### Objetivo

Auxiliar na adaptação da implementação de operações bit a bit da classe Jinteger e seus testes.

### Trecho do Projeto Afetado

javalang/test_jinteger.py
tests/jinteger.py
docs/adaptacoes.md

### Descrição da Contribuição da IA

O agente explicou como funcionava a lógica bit abit de Java e como adapta-lá para python. Auxiliou também na documentação dessas adaptações.

### Validação da Equipe

O conteúdo sugerido foi revisado antes de ser incorporado ao repositório. A implementação foi mantida dentro do escopo da issue, sem adicionar métodos fora do escopo.

### Resultado
Aceito com modificações

## Registro de Uso IA-08

### Data

19/06/2026

### Ferramenta Utilizada

ChatGPT

### Objetivo

Auxiliar na implementação e validação das operações bit a bit iniciais da classe JInteger, bem como na criação dos testes automatizados e na documentação das adaptações necessárias para compatibilidade com o comportamento da classe Integer do Java.

### Trecho do Projeto Afetado

* `javalang/jinteger.py`
* `tests/test_jinteger.py`
* `docs/adaptacoes.md`
* `docs/uso-de-ia.md`

Funcionalidades afetadas:

* `bitCount`
* `highestOneBit`
* `lowestOneBit`
* `numberOfLeadingZeros`
* `numberOfTrailingZeros`

### Descrição da Contribuição da IA

A IA foi utilizada para:

* Explicar o comportamento esperado dos métodos da API Java.
* Sugerir estratégias para simulação de inteiros de 32 bits em Python.
* Auxiliar na implementação dos métodos utilizando as funções auxiliares já existentes no projeto.
* Propor casos de teste para valores zero, positivos, negativos e limites de 32 bits.
* Auxiliar na elaboração da documentação de adaptação referente ao tratamento de inteiros de 32 bits e operações bit a bit.

### Validação da Equipe

* As implementações sugeridas foram comparadas com os requisitos da issue e com o guia da milestone.
* O código foi revisado manualmente antes da incorporação ao projeto.
* Os testes automatizados foram executados localmente utilizando `python -m pytest`.
* As verificações de qualidade foram executadas utilizando `python -m ruff check .`.
* As adaptações documentadas foram revisadas pela equipe para garantir consistência com as decisões já adotadas no projeto.

### Resultado

Aceita com modificações.

As sugestões fornecidas pela IA foram analisadas, adaptadas ao padrão já existente no projeto e integradas utilizando as funções auxiliares de manipulação de inteiros de 32 bits previamente implementadas pela equipe.

---

## Registro de Uso IA-09

### Data

20/06/2026

### Ferramenta utilizada

ChatGPT

### Objetivo

Auxiliar na preparação do fechamento da baseline `v0.2-jinteger`, incluindo a estrutura do relatório de status e o texto sugerido para a release.

### Trecho do projeto afetado

* `docs/relatorios/status-v0.2.md`
* `docs/uso-de-ia.md`

### Prompt ou interação representativa

> Ajudar a fazer a issue de preparação da baseline `v0.2-jinteger`, criando o relatório de status da baseline e o texto da release.

### Descrição da contribuição da IA

A IA auxiliou na organização do relatório de status da baseline `v0.2-jinteger`, incluindo identificação da baseline, objetivo, escopo consolidado, itens de configuração envolvidos, verificações realizadas, adaptações documentadas, uso de IA, conflitos de merge e estado final da baseline.

Também foi sugerido um texto inicial para a release `v0.2-jinteger`, destacando as principais entregas relacionadas à classe `JInteger`.

### Validação da equipe

O conteúdo foi revisado antes de ser incorporado ao repositório. As informações foram ajustadas de acordo com o estado real das issues, pull requests, testes, documentação e CI do projeto.

As verificações locais foram executadas utilizando:

* `python -m pytest`
* `python -m ruff check .`

### Resultado

Aceita com modificações.

## Registro de Uso IA-10

### Data

20/06/2026

### Ferramenta utilizada

ChatGPT

### Objetivo

Auxiliar na implementação inicial da classe `JFloat`, incluindo a criação da estrutura da classe, definição das constantes principais, criação dos testes iniciais e registro da adaptação entre `Float` do Java e `float` do Python.

### Trecho do projeto afetado

- `javalang/jfloat.py`
- `javalang/__init__.py`
- `tests/test_jfloat.py`
- `docs/adaptacoes.md`
- `docs/uso-de-ia.md`

### Prompt ou interação representativa

> Ajudar a implementar a primeira issue da milestone `v0.3-jfloat`, criando a estrutura inicial da classe `JFloat`, suas constantes principais, os testes iniciais e a documentação de adaptação necessária.

### Descrição da contribuição da IA

A IA auxiliou na organização da implementação inicial da classe `JFloat`, sugerindo a criação do arquivo `javalang/jfloat.py`, a definição das constantes principais inspiradas na classe `Float` da API Java SE 8 e o armazenamento interno do valor como `float` do Python.

Também foram sugeridos testes iniciais para validar a criação da classe, constantes de infinito, `NaN`, tamanho em bits, quantidade de bytes e adaptação do tipo base para `float`.

Além disso, a IA apoiou a redação do registro em `docs/adaptacoes.md`, explicando a diferença entre o `float` de 32 bits do Java e o `float` utilizado em Python.

### Validação da equipe

O conteúdo foi revisado antes de ser incorporado ao projeto. A implementação foi mantida dentro do escopo da issue, sem adicionar métodos de conversão, parsing, comparação, operações de bits ou operações estáticas.

As verificações locais foram executadas utilizando:

- `python -m pytest`
- `python -m ruff check .`

### Resultado

Aceita com modificações.

