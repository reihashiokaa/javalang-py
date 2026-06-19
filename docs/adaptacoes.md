# Documentação de Adaptações

## Objetivo

Este documento será utilizado para registrar diferenças entre a especificação Java SE 8 e a implementação adotada no projeto javalang-py.

Sempre que uma funcionalidade precisar ser adaptada ou não puder ser implementada exatamente como definido na API Java, a decisão deverá ser registrada neste documento.

---

## Convenção de Nomenclatura

A equipe definiu a utilização das seguintes classes:

* JString
* JInteger
* JFloat

### Justificativa

O prefixo J foi adotado para diferenciar as classes do projeto dos tipos nativos do Python (`str`, `int` e `float`).

---

## Adaptações Registradas

### JInteger

**Método:**
toBinaryString, toOctalString e toHexString

**Assinatura Java:**
Integer.toBinaryString(int i)
Integer.toOctalString(int i)
Integer.toHexString(int i)

**Decisão da equipe:**
Valores negativos são representados com sinal negativo seguido da conversão da magnitude do número.

**Justificativa:**
A API Java utiliza representação em complemento de dois para valores negativos nesses métodos. Na implementação inicial do projeto foi adotada uma abordagem simplificada e mais compatível com a representação textual utilizada em Python.

**Alternativa em Python (quando aplicável):**
JInteger.toBinaryString(-10) → "-1010"

JInteger.toOctalString(-10) → "-12"

JInteger.toHexString(-10) → "-a"

**Issue relacionada:**
#5

**Pull Request relacionado:**
Preencher após abertura do pull request.

---

## Modelo para Registro de Adaptações

### Classe

**Método:**

**Assinatura Java:**

**Decisão da equipe:**

**Justificativa:**

**Alternativa em Python (quando aplicável):**

**Issue relacionada:**

**Pull Request relacionado:**

---

## Histórico de Atualizações

| Data       | Alteração                                              | Responsável |
| ---------- | -------------------------------------------------------| ------------
| 19/06/2026 | Registro da adaptação de valores negativos em JInteger | Luciana     |
-----------  |--------------------------------------------------------|-------------
| 13/06/2026 | Criação inicial do documento                           | Luciana     |
