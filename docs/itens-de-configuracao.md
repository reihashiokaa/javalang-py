# Itens de configuração

Este documento lista os principais artefatos acompanhados no projeto. A lista será atualizada conforme novas decisões, módulos, testes e documentos forem adicionados ao repositório.

## Critérios usados

Um artefato é tratado como item de configuração quando influencia diretamente a implementação, os testes, a documentação, o fluxo de contribuição ou a consolidação das baselines do projeto.

## Itens de código

| Item             | Caminho previsto       | Responsável inicial                               | Formato       | Frequência de alteração      | Dependências principais                                             |
| ---------------- | ---------------------- | ------------------------------------------------- | ------------- | ---------------------------- | ------------------------------------------------------------------- |
| Classe Integer   | `javalang/jinteger.py` | A definir nas issues da milestone `v0.2-jinteger` | Código Python | Alta durante `v0.2-jinteger` | Especificação Java SE 8, ADR de nomenclatura, testes de Integer     |
| Classe Float     | `javalang/jfloat.py`   | A definir nas issues da milestone `v0.3-jfloat`   | Código Python | Alta durante `v0.3-jfloat`   | Especificação Java SE 8, decisões sobre IEEE 754, testes de Float   |
| Classe String    | `javalang/jstring.py`  | A definir nas issues da milestone `v0.4-jstring`  | Código Python | Alta durante `v0.4-jstring`  | Especificação Java SE 8, decisões sobre Unicode, regex e adaptações |
| Pacote principal | `javalang/__init__.py` | Beatriz                                           | Código Python | Média                        | Módulos das classes implementadas                                   |

## Itens de teste

| Item                         | Caminho previsto         | Responsável inicial                               | Formato                  | Frequência de alteração      | Dependências principais                           |
| ---------------------------- | ------------------------ | ------------------------------------------------- | ------------------------ | ---------------------------- | ------------------------------------------------- |
| Testes de Integer            | `tests/test_jinteger.py` | A definir nas issues da milestone `v0.2-jinteger` | Testes Python com pytest | Alta durante `v0.2-jinteger` | Implementação de `JInteger`                       |
| Testes de Float              | `tests/test_jfloat.py`   | A definir nas issues da milestone `v0.3-jfloat`   | Testes Python com pytest | Alta durante `v0.3-jfloat`   | Implementação de `JFloat`                         |
| Testes de String             | `tests/test_jstring.py`  | A definir nas issues da milestone `v0.4-jstring`  | Testes Python com pytest | Alta durante `v0.4-jstring`  | Implementação de `JString`                        |
| Testes de interoperabilidade | `tests/test_interop.py`  | Isabela                                           | Testes Python com pytest | Média                        | Interações entre `JInteger`, `JFloat` e `JString` |

## Itens de documentação

| Item                  | Caminho                         | Responsável inicial      | Formato  | Frequência de alteração                | Dependências principais                                                       |
| --------------------- | ------------------------------- | ------------------------ | -------- | -------------------------------------- | ----------------------------------------------------------------------------- |
| README                | `README.md`                     | Reinaldo e Maria Eduarda | Markdown | Média                                  | Papéis da equipe, visão geral do projeto, decisões consolidadas               |
| Guia de contribuição  | `CONTRIBUTING.md`               | Reinaldo e Miguel        | Markdown | Média                                  | Modelo de branches, commits, pull requests e revisões                         |
| Itens de configuração | `docs/itens-de-configuracao.md` | Reinaldo                 | Markdown | Média                                  | Estrutura do projeto, baselines e responsáveis                                |
| Adaptações            | `docs/adaptacoes.md`            | Luciana                  | Markdown | Alta durante implementação das classes | Diferenças entre Java e Python, decisões técnicas e métodos não implementados |
| Uso de IA             | `docs/uso-de-ia.md`             | Maria Eduarda            | Markdown | Média                                  | Registros de uso de ferramentas de apoio no projeto                           |
| ADRs                  | `docs/adr/`                     | Luciana                  | Markdown | Média                                  | Decisões arquiteturais e técnicas                                             |
| Relatórios de status  | `docs/relatorios/`              | Maria Eduarda            | Markdown | A cada baseline                        | Issues resolvidas, PRs mesclados, pendências e métricas                       |
| Auditoria interna     | `docs/auditoria.md`             | Luciana                  | Markdown | Final do projeto                       | Issues, PRs, commits, tags e releases                                         |
| Auditoria cruzada     | `docs/auditoria-cruzada.md`     | A definir                | Markdown | Final do projeto                       | Repositório da equipe auditada                                                |

## Itens de configuração do repositório

| Item                           | Caminho ou local                   | Responsável inicial | Formato                     | Frequência de alteração | Dependências principais                                  |
| ------------------------------ | ---------------------------------- | ------------------- | --------------------------- | ----------------------- | -------------------------------------------------------- |
| Workflow de CI                 | `.github/workflows/ci.yml`         | Isabela             | YAML                        | Média                   | pytest, ruff, coverage e configuração do projeto         |
| Templates de issue             | `.github/ISSUE_TEMPLATE/`          | Miguel              | Markdown/YAML               | Baixa                   | Labels, milestones e tipos de tarefa                     |
| Template de pull request       | `.github/pull_request_template.md` | Miguel              | Markdown                    | Baixa                   | Fluxo de revisão e informações esperadas no PR           |
| Configuração do projeto Python | `pyproject.toml`                   | Beatriz             | TOML                        | Média                   | Ferramentas de teste, lint e empacotamento               |
| Arquivos ignorados pelo Git    | `.gitignore`                       | Beatriz             | Texto                       | Baixa                   | Ambiente Python, arquivos temporários e artefatos locais |
| Proteção da branch principal   | Configurações do GitHub            | Reinaldo            | Configuração do repositório | Baixa                   | Fluxo de pull requests e revisões                        |
| Milestones                     | GitHub Issues                      | Reinaldo            | Configuração do GitHub      | Média                   | Baselines do projeto                                     |
| Labels                         | GitHub Issues                      | Reinaldo            | Configuração do GitHub      | Baixa                   | Classificação das issues                                 |

## Baselines relacionadas

| Baseline          | Conteúdo principal                                                                                    |
| ----------------- | ----------------------------------------------------------------------------------------------------- |
| `v0.1-functional` | Estrutura inicial, decisões arquiteturais, itens de configuração, CI inicial e plano de implementação |
| `v0.2-jinteger`   | Implementação e testes da classe Integer                                                              |
| `v0.3-jfloat`     | Implementação e testes da classe Float                                                                |
| `v0.4-jstring`    | Implementação e testes da classe String                                                               |
| `v1.0.0`          | Release final, documentação completa, auditorias e apresentação                                       |

## Observações

Este documento representa a versão inicial dos itens de configuração. Novos itens podem ser adicionados conforme o projeto evoluir, especialmente durante a implementação das classes e a preparação das releases.
