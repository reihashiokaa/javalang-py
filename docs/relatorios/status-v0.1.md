# Status da baseline v0.1-functional

## Resumo

A baseline `v0.1-functional` consolida a organização inicial do projeto. Nesta etapa, o repositório foi estruturado, os papéis da equipe foram registrados, as primeiras decisões foram documentadas e os arquivos de apoio para as próximas etapas foram preparados.

Esta baseline não tem como foco a implementação completa das classes, mas sim a criação de uma base organizada para o desenvolvimento de `JInteger`, `JFloat` e `JString` nas próximas milestones.

## Escopo consolidado

Foram considerados parte desta baseline:

* estrutura inicial do repositório;
* definição dos papéis da equipe;
* convenção de nomenclatura das classes;
* modelo de branches, commits, pull requests e revisões;
* documento inicial de itens de configuração;
* configuração inicial do projeto Python;
* integração contínua inicial;
* templates de issues e pull requests;
* documentação inicial de adaptações;
* documentação inicial de uso de IA;
* plano inicial de implementação.

## Decisões registradas

| Decisão                               | Registro                      |
| ------------------------------------- | ----------------------------- |
| Convenção de nomenclatura das classes | ADR de nomenclatura           |
| Modelo de branches e pull requests    | ADR de fluxo de contribuição  |
| Ordem inicial de implementação        | `docs/plano-implementacao.md` |

## Artefatos adicionados ou atualizados

| Artefato                           | Finalidade                                                      |
| ---------------------------------- | --------------------------------------------------------------- |
| `README.md`                        | Apresentação inicial do projeto e papéis da equipe              |
| `CONTRIBUTING.md`                  | Orientações para branches, commits, PRs e revisões              |
| `docs/itens-de-configuracao.md`    | Registro dos principais artefatos controlados                   |
| `docs/adaptacoes.md`               | Estrutura inicial para registrar adaptações entre Java e Python |
| `docs/uso-de-ia.md`                | Registro do uso de ferramentas de IA no projeto                 |
| `docs/plano-implementacao.md`      | Organização inicial das próximas etapas de implementação        |
| `docs/adr/`                        | Registro das decisões técnicas e organizacionais                |
| `.github/workflows/ci.yml`         | Workflow inicial de integração contínua                         |
| `.github/ISSUE_TEMPLATE/`          | Templates para abertura de issues                               |
| `.github/pull_request_template.md` | Template para pull requests                                     |
| `pyproject.toml`                   | Configuração inicial do projeto Python                          |
| `.gitignore`                       | Arquivos e diretórios ignorados pelo Git                        |

## Issues relacionadas

* #1 — Configurar estrutura inicial do projeto
* #3 — Definir papéis da equipe
* #4 — Definir convenção de nomenclatura das classes
* #5 — Definir modelo de branches e pull requests
* #6 — Criar documento de itens de configuração
* #7 — Configurar arquivos base do projeto Python
* #8 — Configurar integração contínua inicial
* #9 — Criar templates de issues e pull request
* #10 — Criar documentação inicial de adaptações
* #11 — Criar documentação inicial de uso de IA
* #12 — Criar plano inicial de implementação
* #13 — Preparar baseline v0.1-functional

## Pull requests relacionados

* #2 — Configurar estrutura inicial do projeto
* #15 — Registrar papéis da equipe
* #21 — Registrar convenção de nomenclatura das classes
* #16 — Definir modelo de branches e pull requests
* #17— Criar documento de itens de configuração
* #20 — Configurar arquivos base do projeto Python
* #22 — Configurar integração contínua inicial
* #19 — Criar templates de issues e pull request
* #18 — Criar documentação inicial de adaptações
* #14 — Criar documentação inicial de uso de IA
* #23 — Criar plano inicial de implementação

## Integração contínua

A integração contínua inicial foi configurada para executar verificações automáticas no repositório.

Nesta baseline, a CI contempla:

* execução em eventos de `push`;
* execução em eventos de `pull_request`;
* instalação do Python;
* instalação das dependências iniciais de teste e qualidade;
* execução do `ruff`;
* execução do `pytest` quando houver arquivos de teste disponíveis.

Como a implementação das classes ainda não é o foco desta baseline, a suíte de testes será ampliada nas próximas milestones.

## Adaptações documentadas

Nesta baseline, foi criada a estrutura inicial para registrar adaptações técnicas entre a especificação Java SE 8 e a implementação em Python.

As adaptações específicas de métodos serão registradas conforme as classes forem implementadas.

## Pendências conhecidas para a próxima baseline

Para a baseline `v0.2-jinteger`, as principais pendências são:

* criar o módulo da classe `JInteger`;
* criar a suíte inicial de testes de `JInteger`;
* implementar constantes e estrutura básica da classe;
* implementar os primeiros métodos de conversão;
* implementar os primeiros métodos de parsing;
* registrar adaptações relacionadas ao tipo `int` do Python e ao `int` de 32 bits do Java;
* garantir que a CI execute os testes adicionados.

## Observações finais

A baseline `v0.1-functional` estabelece a base de organização do projeto. As próximas baselines devem evoluir a implementação técnica mantendo o fluxo de issues, branches, pull requests, revisões e documentação.
