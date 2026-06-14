# ADR 0001 — Modelo de branches e pull requests

## Status

Aprovado

## Data

14/06/2026

## Contexto

O projeto será desenvolvido por uma equipe de seis integrantes, com alterações frequentes em código, testes e documentação. Para manter o histórico organizado e facilitar a revisão das mudanças, a equipe precisa seguir um fluxo comum de trabalho.

## Decisão

A equipe adotará um fluxo baseado em branches curtas, pull requests e revisão por pares.

A branch `main` será mantida como linha principal estável do projeto. Alterações não devem ser feitas diretamente nela. Cada mudança deve ser desenvolvida em uma branch própria, criada a partir da `main` atualizada.

Os nomes das branches seguirão o formato:

* `feature/nome-da-tarefa` para novas funcionalidades ou métodos;
* `fix/nome-da-correcao` para correções;
* `docs/nome-da-documentacao` para documentação;
* `test/nome-dos-testes` para testes;
* `refactor/nome-do-ajuste` para reorganizações internas.

As mensagens de commit devem usar um prefixo semântico, como:

* `feat:` para implementação de funcionalidade;
* `fix:` para correção;
* `docs:` para documentação;
* `test:` para testes;
* `refactor:` para reorganização de código;
* `chore:` para ajustes de configuração ou manutenção.

Sempre que possível, o commit deve referenciar a issue relacionada com `refs #N`.

Pull requests devem ser pequenos e associados a uma issue. A descrição do PR deve indicar a issue fechada, resumir as alterações feitas e informar se houve impacto em código, testes ou documentação.

Cada pull request deve ser revisado por pelo menos uma pessoa diferente do autor. Comentários de revisão devem ser respondidos ou resolvidos antes do merge.

Após o merge, a branch usada no desenvolvimento deve ser removida para manter o repositório organizado.

## Consequências

Esse modelo mantém o histórico do projeto mais claro e facilita acompanhar por que cada mudança foi feita. Também reduz o risco de alterações grandes demais entrarem na `main` sem revisão adequada.

Como consequência, a equipe precisa dividir o trabalho em tarefas pequenas e manter as issues atualizadas ao longo das milestones.
