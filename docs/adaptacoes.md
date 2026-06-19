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

## Adaptações

### longValue

**Método:** `longValue`

**Assinatura Java:** `public long longValue()`

**Decisão da equipe:** Retornar um objeto do tipo `int` do Python.

**Justificativa:** Em Java, `int` e `long` são tipos distintos, com 32 e 64 bits respectivamente. Em Python não existe distinção entre esses tipos, sendo utilizado apenas `int` para representar números inteiros.

**Alternativa em Python (quando aplicável):** `return self._value`

**Issue relacionada:** #<26>

**Pull Request relacionado:** #<5>

### doubleValue

**Método:** `doubleValue`

**Assinatura Java:** `public double doubleValue()`

**Decisão da equipe:** Retornar um objeto do tipo `float` do Python.

**Justificativa:** Em Java existem os tipos `float` (32 bits) e `double` (64 bits). Em Python existe apenas o tipo `float`, que internamente já utiliza precisão equivalente ao `double` da maioria das implementações.

**Alternativa em Python (quando aplicável):** `return float(self._value)`

**Issue relacionada:** #<26>

**Pull Request relacionado:** #<5>

### byteValue

**Método:** `byteValue`

**Assinatura Java:** `public byte byteValue()`

**Decisão da equipe:** Simular o comportamento de conversão para inteiro com sinal de 8 bits utilizando operações bit a bit.

**Justificativa:** Python não possui um tipo primitivo equivalente ao `byte` assinado do Java. Para manter compatibilidade com a API Java, a implementação preserva apenas os 8 bits menos significativos e interpreta o resultado como um valor com sinal.

**Alternativa em Python (quando aplicável):** Conversão utilizando máscara `0xFF` e ajuste de sinal.

**Issue relacionada:** #<26>

**Pull Request relacionado:** #<5>

### shortValue

**Método:** `shortValue`

**Assinatura Java:** `public short shortValue()`

**Decisão da equipe:** Simular o comportamento de conversão para inteiro com sinal de 16 bits utilizando operações bit a bit.

**Justificativa:** Python não possui um tipo primitivo equivalente ao `short` do Java. Para manter compatibilidade com a API Java, a implementação preserva apenas os 16 bits menos significativos e interpreta o resultado como um valor com sinal.

**Alternativa em Python (quando aplicável):** Conversão utilizando máscara `0xFFFF` e ajuste de sinal.

**Issue relacionada:** #<26>

**Pull Request relacionado:** #<5>



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

| Data       | Alteração                    | Responsável |
| ---------- | ---------------------------- | ----------- |
| 13/06/2026 | Criação inicial do documento | Luciana     |
| 19/06/2026 | Implementação de conversões  | Miguel      |
