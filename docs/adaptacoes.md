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
## Adaptações da JInteger

### Operações sem sinal de 32 bits

**Métodos:** `parseUnsignedInt`, `toUnsignedString`, `compareUnsigned`, `divideUnsigned` e `remainderUnsigned`

**Assinaturas Java:**
- `static int parseUnsignedInt(String s)`
- `static int parseUnsignedInt(String s, int radix)`
- `static String toUnsignedString(int i)`
- `static String toUnsignedString(int i, int radix)`
- `static int compareUnsigned(int x, int y)`
- `static int divideUnsigned(int dividend, int divisor)`
- `static int remainderUnsigned(int dividend, int divisor)`

**Decisão da equipe:**
As operações sem sinal foram implementadas usando interpretação de 32 bits por meio de máscara `0xFFFFFFFF`.

**Justificativa:**
Em Java, a classe `Integer` trabalha com `int` de 32 bits. Já em Python, o tipo `int` possui precisão arbitrária e não possui uma separação nativa entre inteiro assinado e inteiro sem sinal. Por isso, valores negativos são convertidos para sua representação sem sinal de 32 bits antes das operações.

**Comportamento adotado em Python:**
- `parseUnsignedInt` retorna um valor inteiro positivo quando a entrada está dentro do intervalo de 0 a 4294967295.
- Valores negativos em `parseUnsignedInt` são rejeitados.
- `toUnsignedString`, `compareUnsigned`, `divideUnsigned` e `remainderUnsigned` interpretam valores negativos usando máscara de 32 bits.
- Divisão e resto usam divisão inteira do Python após a conversão para a representação sem sinal.
- Divisão por zero gera `ZeroDivisionError`.

**Alternativa em Python:**
Usar `value & 0xFFFFFFFF` para interpretar um inteiro como valor sem sinal de 32 bits.

**Issue relacionada:** #30

**Pull Request relacionado:** A definir.

## Histórico de Atualizações

| Data       | Alteração                    | Responsável |
| ---------- | ---------------------------- | ----------- |
| 13/06/2026 | Criação inicial do documento | Luciana     |
| 19/06/2026 | Registro das adaptações de operações sem sinal de JInteger | Isabela |
