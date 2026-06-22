# Auditoria interna do projeto

## Identificação

* Projeto: `javalang-py`
* Repositório: `reihashiokaa/javalang-py`
* Versão auditada: `v1.0.0`
* Responsável pela consolidação: Reinaldo Andrade Hashioka
* Data da auditoria: 21/06/2026

## Objetivo da auditoria

Esta auditoria interna tem como objetivo verificar se o projeto seguiu o processo de Gerência de Configuração de Software definido para o trabalho.

Foram analisadas as evidências de controle de versão, rastreabilidade, organização das baselines, uso de branches, commits semânticos, pull requests, revisão por pares, integração contínua, documentação de adaptações e registro do uso de ferramentas de IA.

## Escopo auditado

A auditoria considerou os seguintes itens do projeto:

* Estrutura do repositório.
* Issues e milestones.
* Branches de desenvolvimento.
* Commits semânticos.
* Pull requests.
* Revisões por pares.
* Execução da integração contínua.
* Baselines e releases.
* Documentação técnica.
* Registros de adaptação entre Java e Python.
* Registros de uso de IA.
* Evidências de conflitos de merge.
* Estado final da release `v1.0.0`.

## Itens de configuração auditados

Os principais itens de configuração acompanhados durante o projeto foram:

* `javalang/jinteger.py`
* `javalang/jfloat.py`
* `javalang/jstring.py`
* `javalang/__init__.py`
* `tests/test_jinteger.py`
* `tests/test_jfloat.py`
* `tests/test_jstring.py`
* `README.md`
* `CONTRIBUTING.md`
* `pyproject.toml`
* `.github/workflows/ci.yml`
* `.github/ISSUE_TEMPLATE/`
* `.github/pull_request_template.md`
* `docs/adaptacoes.md`
* `docs/uso-de-ia.md`
* `docs/itens-de-configuracao.md`
* `docs/plano-implementacao.md`
* `docs/relatorios/`
* `docs/auditoria.md`

## Verificação de issues e milestones

O projeto foi organizado por issues associadas às baselines e às classes implementadas.

As principais milestones utilizadas foram:

* `v0.1-functional`
* `v0.2-jinteger`
* `v0.3-jfloat`
* `v0.4-jstring`
* `v1.0.0`

Cada milestone agrupou issues relacionadas a uma etapa do projeto. As issues foram usadas para definir o escopo das alterações, distribuir responsabilidades entre os integrantes e manter rastreabilidade entre requisitos, branches, commits e pull requests.

Durante a auditoria, foi verificado que as principais alterações do projeto possuem issue associada.

## Verificação de branches

O desenvolvimento foi realizado por meio de branches específicas para cada issue ou conjunto pequeno de alterações.

Foram utilizadas branches com nomes relacionados ao escopo da alteração, como:

* branches de implementação de `JInteger`;
* branches de implementação de `JFloat`;
* branches de implementação de `JString`;
* branches de documentação;
* branches de preparação de baseline.

Essa organização ajudou a separar as alterações, evitar commits diretos na branch principal e facilitar a revisão por pull request.

## Verificação de commits

Os commits foram organizados de forma semântica, utilizando prefixos como:

* `feat:`
* `test:`
* `docs:`
* `fix:`
* `ci:`

Também foi adotada a prática de referenciar a issue relacionada nos commits por meio de `refs #N`.

A auditoria verificou que as alterações foram divididas em commits menores, separando implementação, testes e documentação sempre que possível.

## Verificação de pull requests

As alterações principais foram integradas à branch principal por meio de pull requests.

Os pull requests foram utilizados para:

* descrever o escopo da alteração;
* relacionar a issue correspondente;
* apresentar os arquivos modificados;
* registrar os testes executados;
* permitir revisão por outro integrante;
* aguardar a execução da CI antes do merge.

Foi verificado que os pull requests seguiram o fluxo:

```text
issue → branch → commits → pull request → revisão → CI → merge
```

## Verificação de revisão por pares

A equipe adotou revisão por pares nos pull requests.

A aprovação foi realizada por integrante diferente do autor da alteração, evitando autoaprovação e reforçando o controle de qualidade.

As revisões consideraram:

* aderência ao escopo da issue;
* organização dos commits;
* presença de testes;
* atualização da documentação;
* resultado da CI;
* impacto da alteração na baseline.

## Verificação da integração contínua

O projeto utilizou integração contínua por meio do GitHub Actions.

A CI foi configurada para executar verificações como:

* instalação do ambiente Python;
* execução dos testes automatizados;
* verificação de estilo com Ruff.

Os principais comandos utilizados localmente e pela equipe foram:

```bat
python -m pytest
python -m ruff check .
```

A auditoria considerou a CI como parte das evidências de validação das alterações antes da consolidação das baselines.

## Verificação de testes

Foram criados testes automatizados para as classes implementadas:

* `JInteger`
* `JFloat`
* `JString`

Os testes foram organizados em arquivos específicos dentro do diretório `tests/`.

A auditoria verificou que os testes acompanham os principais grupos de métodos implementados e foram utilizados como critério de validação antes dos merges e releases.

## Verificação das baselines

O projeto foi consolidado em baselines intermediárias e uma release final.

As baselines utilizadas foram:

### Baseline `v0.1-functional`

Consolidou a estrutura inicial do projeto, arquivos de configuração, documentação inicial, templates, CI e plano de implementação.

### Baseline `v0.2-jinteger`

Consolidou a implementação da classe `JInteger`, seus testes, adaptações e documentação relacionada.

### Baseline `v0.3-jfloat`

Consolidou a implementação da classe `JFloat`, seus testes, adaptações e documentação relacionada.

### Baseline `v0.4-jstring`

Consolidou a implementação da classe `JString`, seus testes, adaptações e documentação relacionada.

### Release `v1.0.0`

Consolida a entrega final do projeto, reunindo as classes implementadas, documentação, auditoria interna, registros de IA, baselines anteriores e evidências do processo de Gerência de Configuração.

## Verificação das adaptações

As adaptações entre a API Java SE 8 e a implementação em Python foram registradas em `docs/adaptacoes.md`.

A auditoria verificou que o documento registra decisões relacionadas a:

* diferenças entre tipos Java e Python;
* ausência de sobrecarga tradicional em Python;
* tratamento de inteiros de 32 bits;
* tratamento de ponto flutuante;
* uso de `str` para representar strings;
* métodos adaptados;
* métodos simplificados;
* decisões técnicas específicas de cada classe.

## Verificação do uso de IA

O uso de ferramentas de IA foi registrado em `docs/uso-de-ia.md`.

Os registros indicam:

* data de uso;
* ferramenta utilizada;
* objetivo;
* arquivos afetados;
* contribuição sugerida;
* validação pela equipe;
* resultado da sugestão.

A auditoria verificou que o uso de IA foi documentado como apoio ao desenvolvimento e à documentação, mantendo revisão humana antes da incorporação ao projeto.

## Verificação de conflitos de merge

Durante o desenvolvimento, ocorreram conflitos de merge em integrações entre branches.

Esses conflitos foram resolvidos manualmente pela equipe antes da conclusão dos merges.

As evidências de conflitos podem ser observadas no histórico de commits e merges do repositório, especialmente nas integrações entre branches de implementação e a branch principal.

## Verificação do README

O `README.md` foi revisado para apresentar:

* objetivo do projeto;
* classes implementadas;
* instruções de instalação;
* instruções de execução dos testes;
* informações sobre baselines;
* informações sobre adaptações;
* informações sobre uso de IA;
* link para a apresentação final;
* limitações conhecidas, quando aplicável.

## Resultado da auditoria

A auditoria interna concluiu que o projeto apresenta evidências suficientes do processo de Gerência de Configuração de Software.

Foram observadas evidências de:

* controle de versão com Git;
* organização por issues e milestones;
* uso de branches;
* commits semânticos;
* pull requests revisados;
* integração contínua;
* testes automatizados;
* documentação das baselines;
* registros de adaptação;
* registros de uso de IA;
* preparação da release final.

## Conclusão

O projeto `javalang-py` foi conduzido com uso de práticas de Gerência de Configuração de Software, incluindo controle de versões, rastreabilidade, revisão por pares, integração contínua, baselines, releases e documentação das decisões técnicas.

A release `v1.0.0` representa a consolidação final do trabalho.
