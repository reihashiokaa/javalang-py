# Guia de contribuição

Este documento descreve o fluxo básico para contribuir com o projeto.

## 1. Antes de iniciar uma mudança

Antes de iniciar qualquer alteração, verifique se existe uma issue correspondente. A issue deve ter responsável, milestone e labels adequadas.

Se a mudança ainda não tiver issue, crie uma antes de começar.

## 2. Criando uma branch

Sempre crie a branch a partir da `main` atualizada:

```bash
git checkout main
git pull origin main
git checkout -b tipo/nome-da-tarefa
```

Use nomes curtos e descritivos. Exemplos:

```text
feature/jinteger-parseint
docs/adaptacoes-iniciais
fix/jstring-charat-indice
test/jfloat-nan
```

## 3. Mensagens de commit

As mensagens de commit devem usar um prefixo semântico:

```text
feat: adiciona método parseInt - refs #10
fix: corrige validação de índice em charAt - refs #18
docs: registra adaptação de StringBuilder - refs #22
test: adiciona casos para toHexString - refs #15
refactor: reorganiza validações de JInteger - refs #19
chore: ajusta configuração do projeto - refs #7
```

Commits devem ser pequenos e relacionados à issue em andamento.

## 4. Pull requests

Todo pull request deve partir de uma branch específica para a `main`.

A descrição do PR deve conter:

* issue relacionada;
* resumo das alterações;
* arquivos principais modificados;
* testes adicionados ou executados;
* observações sobre impacto, se houver.

Quando o PR resolver uma issue, use:

```text
Closes #N
```

## 5. Revisão

Cada pull request deve ser revisado por pelo menos uma pessoa diferente do autor.

O revisor deve verificar se a alteração está clara, se os testes fazem sentido e se a documentação foi atualizada quando necessário.

Comentários de revisão devem ser respondidos antes do merge.

## 6. Merge

O merge só deve ser feito após aprovação e, quando aplicável, verificações automáticas concluídas com sucesso.

Depois do merge, a branch utilizada deve ser removida.

## 7. Tamanho das mudanças

As mudanças devem ser mantidas pequenas. Um commit não deve concentrar muitos métodos, e um pull request não deve reunir blocos grandes demais de implementação ou testes.

Quando uma tarefa ficar grande, ela deve ser dividida em issues menores.
