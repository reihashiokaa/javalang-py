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

**Pull Request relacionado:** 42.

### Parsing e criação por valor em JInteger

**Métodos:** `parseInt`, `valueOf` e `decode`

**Assinaturas Java relacionadas:**

- `static int parseInt(String s)`
- `static int parseInt(String s, int radix)`
- `static Integer valueOf(int i)`
- `static Integer valueOf(String s)`
- `static Integer valueOf(String s, int radix)`
- `static Integer decode(String nm)`

**Decisão da equipe:**

As variações sobrecarregadas da API Java foram adaptadas para Python usando parâmetros opcionais e verificação interna de tipo.

Na implementação em Python:

- `parseInt(value, radix=10)` representa as variações de `parseInt` com e sem radix.
- `valueOf(value, radix=10)` representa as variações de `valueOf` com inteiro, string e string com radix.
- `decode(value)` interpreta prefixos numéricos para identificar decimal, hexadecimal e octal.

**Justificativa:**

Java permite sobrecarga de métodos, ou seja, vários métodos com o mesmo nome e assinaturas diferentes. Python não possui esse mesmo mecanismo. Por isso, a equipe optou por representar as variações usando parâmetros opcionais.

Além disso, a classe `JInteger` representa o `Integer` do Java, que trabalha com valores inteiros de 32 bits. Por isso, os valores convertidos por parsing são validados em relação aos limites `MIN_VALUE` e `MAX_VALUE`.

**Comportamento adotado em Python:**

- `parseInt` retorna um valor `int` do Python.
- `valueOf` retorna uma instância de `JInteger`.
- `decode` retorna uma instância de `JInteger`.
- `parseInt` aceita radix entre 2 e 36.
- `decode` suporta valores decimais, prefixos `0x`, `0X`, `#` e valores octais iniciados por `0`.
- Entradas vazias, inválidas ou com radix fora do intervalo aceito geram `ValueError`.
- Valores fora do intervalo assinado de 32 bits geram `OverflowError`.
- Tipos inválidos geram `TypeError`.

**Issue relacionada:** #N

**Pull Request relacionado:** 46.

| 19/06/2026 | Adição de adaptação métodos estáticos | Beatriz     |

### Operações bit-a-bit

**Método:**
reverse, reverseBytes, rotateLeft, rotateRight e signum

**Assinatura Java:**
public static int reverse(int i) 
public static int reverseBytes(int i) 
public static int rotateLeft(int i, int distance) 
public static int rotateRight(int i, int distance) 
public static int signum(int i)

**Decisão da equipe:**
Como Python não possui inteiros limitados a 32 bits, foram criadas funções auxiliares internas para simular inteiros de 32 bits com sinal, garantindo compatibilidade com os resultados obtidos em Java.

**Justificativa:**
Os métodos reverse, reverseBytes, rotateLeft e rotateRight dependem diretamente da representação binária fixa de 32 bits do tipo int do Java. Como os inteiros em Python possuem tamanho arbitrário, a implementação exige a limitação explícita dos valores a 32 bits para que operações de deslocamento, rotação e inversão de bits produzam os mesmos resultados da plataforma Java.

**Alternativa em Python (quando aplicável):**
    signum (valor > 0) - (valor < 0) 

    # exemplo de inversão dos 32 bits 
    int('{:032b}'.format(valor & 0xFFFFFFFF)[::-1], 2)

**Issue relacionada:**
 Issue #32

**Pull Request relacionado:**
...

## Histórico de Atualizações

| Data       | Alteração                    | Responsável |
| ---------- | ---------------------------- | ----------- |
| 13/06/2026 | Criação inicial do documento | Luciana     |
| 19/06/2026 | Implementação de conversões  | Miguel      |
| 19/06/2026 | Registro das adaptações de operações sem sinal de JInteger | Isabela |
| 19/06/2026 | Registro das adaptações de parsing e criação por valor de JInteger | Reinaldo |
| 19/06/2026 | Registro das adaptações de operações bit-a-bit| Beatriz |





