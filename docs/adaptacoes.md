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

### JInteger

**Método:** bitCount, highestOneBit, lowestOneBit, numberOfLeadingZeros e numberOfTrailingZeros

**Assinatura Java:**

public static int bitCount(int i) 
public static int highestOneBit(int i) 
public static int lowestOneBit(int i)
public static int numberOfLeadingZeros(int i) 
public static int numberOfTrailingZeros(int i)

**Decisão da equipe:**

As operações bit a bit foram implementadas considerando uma representação fixa de 32 bits. Antes dos cálculos, os valores são convertidos para uma representação sem sinal de 32 bits utilizando função auxiliar interna. Quando necessário, o resultado é convertido novamente para inteiro assinado de 32 bits.

**Justificativa:**

Diferentemente do Java, que utiliza inteiros de 32 bits com sinal, o Python possui inteiros de precisão arbitrária. Sem essa adaptação, operações envolvendo números negativos ou limites de 32 bits produziriam resultados diferentes dos definidos pela API Java.

**Alternativa em Python (quando aplicável):**

Foi utilizada uma estratégia baseada em máscaras de bits e funções auxiliares internas para simular o comportamento de inteiros de 32 bits:

_to_uint32(value)
_to_int32(value)

Essa abordagem permite reproduzir o comportamento da classe Integer do Java para operações bit a bit.

**Issue relacionada: #<31>**

**Pull Request relacionado:**

--- 

### Estrutura inicial e constantes de JFloat

**Classe:** `JFloat`

**Elementos relacionados da API Java:**

- `Float.POSITIVE_INFINITY`
- `Float.NEGATIVE_INFINITY`
- `Float.NaN`
- `Float.MAX_VALUE`
- `Float.MIN_VALUE`
- `Float.MIN_NORMAL`
- `Float.MAX_EXPONENT`
- `Float.MIN_EXPONENT`
- `Float.SIZE`
- `Float.BYTES`
- `Float.TYPE`

**Decisão da equipe:**

A classe `JFloat` foi criada como adaptação da classe `Float` da API Java SE 8. A implementação inicial utiliza o tipo `float` do Python para armazenar internamente os valores.

**Justificativa:**

No Java, o tipo `float` representa valores de ponto flutuante de 32 bits. Em Python, o tipo `float` normalmente utiliza precisão dupla. Por isso, a implementação inicial de `JFloat` registra os valores principais da classe `Float`, mas usa `float` do Python como base para armazenamento interno.

Diferenças mais específicas de precisão, arredondamento, representação binária e tratamento de valores especiais serão documentadas conforme os métodos forem implementados nas próximas issues da milestone `v0.3-jfloat`.

**Comportamento adotado em Python:**

- `POSITIVE_INFINITY` foi representado com `float("inf")`.
- `NEGATIVE_INFINITY` foi representado com `float("-inf")`.
- `NaN` foi representado com `float("nan")`.
- `TYPE` foi adaptado para `float`.
- O valor interno da instância foi armazenado em `_value` como `float` do Python.

**Issue relacionada:** #49

**Pull Request relacionado:** 57.

### JFloat

**Métodos:**
byteValue, shortValue, intValue, longValue, floatValue e doubleValue

**Assinatura Java:**
Float.byteValue()

Float.shortValue()

Float.intValue()

Float.longValue()

Float.floatValue()

Float.doubleValue()

**Decisão da equipe:**
As conversões foram adaptadas para os tipos nativos do Python. Os métodos intValue e longValue retornam `int`; os métodos floatValue e doubleValue retornam `float`. Os métodos byteValue e shortValue simulam o comportamento dos tipos assinados de 8 e 16 bits do Java por meio de mascaramento de bits e ajuste de sinal.

**Justificativa:**
Python não possui tipos primitivos equivalentes a `byte`, `short`, `long` e `double` com o mesmo comportamento da plataforma Java. Para manter compatibilidade com a API Java, foram simuladas as conversões de `byte` e `short`, enquanto `longValue` e `doubleValue` utilizam os tipos nativos mais próximos disponíveis em Python.

Além disso, as conversões para tipos inteiros utilizam `int()`, que realiza truncamento em direção ao zero, comportamento compatível com as conversões primitivas de estreitamento da API Java.

**Alternativa em Python (quando aplicável):**
JFloat(10.8).intValue() → 10

JFloat(-10.8).intValue() → -10

JFloat(130.0).byteValue() → -126

JFloat(32768.0).shortValue() → -32768

JFloat(10.5).doubleValue() → 10.5

**Limitações conhecidas:**
Casos especiais envolvendo NaN, POSITIVE_INFINITY e NEGATIVE_INFINITY não são tratados especificamente nesta implementação e serão abordados em issue própria relacionada aos valores especiais de JFloat.

**Issue relacionada:**
#50

**Pull Request relacionado:**
Preencher após abertura do pull request.

---

### JFloat

**Método:**
parseFloat
valueOf(float f)
valueOf(String s)

**Assinatura Java:**
public static float parseFloat(String s)
public static Float valueOf(float f) 
public static Float valueOf(String s)

**Decisão da equipe:**
Implementado. Strings especiais "Infinity", "-Infinity" e "NaN" são verificadas explicitamente antes de chamar float() do Python, pois o Python nativo não reconhece esse formato com letra maiúscula (usado pelo Java). Entradas inválidas lançam ValueError no lugar de NumberFormatException, que não existe em Python, ValueError é a exceção idiomática equivalente para erros de conversão de valor.
As duas sobrecargas foram unificadas em um único método estático valueOf(value). O método detecta o tipo do argumento em tempo de execução: se receber str, chama parseFloat internamente antes de criar a instância; se receber int ou float, cria a instância diretamente; qualquer outro tipo lança ValueError.
**Justificativa:**
Sem o tratamento das strings especiais, parseFloat("Infinity") lançaria ValueError em vez de retornar float("inf"), quebrando o contrato Java.
A troca de exceção foi necessária porque NumberFormatException não faz parte da linguagem Python.
Python não suporta sobrecarga de métodos. Definir dois métodos com o mesmo nome na mesma classe faz o segundo substituir o primeiro silenciosamente, sem erro. A detecção por tipo em tempo de execução preserva o contrato público das duas assinaturas Java em um único ponto de entrada, que é a abordagem idiomática em Python para esse caso.
**Alternativa em Python (quando aplicável):**
float("inf"), float("-inf"), float("nan") e float("3.14") para conversões diretas sem passar pela classe.
Chamar JFloat(float(valor)) ou JFloat(JFloat.parseFloat(string)) diretamente, sem passar por valueOf.

**Issue relacionada:**
#51

**Pull Request relacionado:**
Preencher após o pull request

---

### JFloat

**Métodos:**
`isNaN`, `isInfinite` e `isFinite`

**Assinatura Java:**
`public boolean isNaN()`

`public static boolean isNaN(float v)`

`public boolean isInfinite()`

`public static boolean isInfinite(float v)`

`public static boolean isFinite(float f)`

**Decisão da equipe:**
Os métodos de verificação de valores especiais foram implementados utilizando a biblioteca `math` do Python. A implementação permite verificar tanto o valor armazenado em uma instância de `JFloat` quanto um valor numérico recebido diretamente pela chamada da classe.

**Justificativa:**
A classe `Float` do Java possui métodos para identificar valores especiais de ponto flutuante, como `NaN`, infinito positivo, infinito negativo e valores finitos. Em Python, esses valores podem ser representados por `float("nan")`, `float("inf")` e `float("-inf")`, e verificados com `math.isnan`, `math.isinf` e `math.isfinite`.

Como Python não possui sobrecarga de métodos como Java, a implementação foi adaptada para identificar se o argumento recebido é uma instância de `JFloat` ou um valor numérico direto. Dessa forma, o mesmo método atende ao uso por instância e ao uso pela classe.

**Comportamento adotado em Python:**

* `isNaN` retorna `True` quando o valor é `NaN`.
* `isInfinite` retorna `True` para infinito positivo ou negativo.
* `isFinite` retorna `True` para valores finitos e `False` para `NaN` ou infinito.
* Os métodos podem ser chamados por instância, como `JFloat(float("nan")).isNaN()`.
* Os métodos também podem ser chamados pela classe, como `JFloat.isNaN(float("nan"))`.

**Alternativa em Python (quando aplicável):**
`math.isnan(value)`

`math.isinf(value)`

`math.isfinite(value)`

**Issue relacionada:**
#53

**Pull Request relacionado:**
A definir.

---

### Conversões de bits e representação hexadecimal de JFloat

**Método:**
toHexString, floatToIntBits, floatToRawIntBits e intBitsToFloat

**Assinatura Java:**
public static String toHexString(float f)
public static int floatToIntBits(float value)
public static int floatToRawIntBits(float value)
public static float intBitsToFloat(int bits)

**Decisão da equipe:**
Como Python não possui um tipo `float` limitado diretamente a 32 bits como o `float` do Java, os métodos foram adaptados utilizando o módulo `struct` para converter valores de ponto flutuante para a representação IEEE 754 de 32 bits e também para reconstruir valores `float` a partir de inteiros de 32 bits.

O método `floatToIntBits` normaliza valores `NaN` para o padrão canônico esperado pela API Java. Já o método `floatToRawIntBits` preserva o padrão bruto de bits sempre que possível, considerando as limitações do tipo `float` do Python. O método `intBitsToFloat` realiza o caminho inverso, interpretando um inteiro como uma sequência de 32 bits de ponto flutuante. O método `toHexString` gera uma representação textual hexadecimal baseada nessa representação binária.

**Justificativa:**
Os métodos desta issue dependem diretamente da representação binária de valores `float` em 32 bits. Em Java, o tipo `float` segue esse tamanho fixo, enquanto em Python o tipo `float` normalmente possui precisão equivalente ao `double`. Por isso, foi necessário forçar a conversão para 32 bits antes de manipular os bits, garantindo uma adaptação mais próxima do comportamento da classe `Float` da API Java SE 8.

Além disso, existe uma diferença entre `floatToIntBits` e `floatToRawIntBits` no tratamento de `NaN`. A versão `floatToIntBits` usa uma representação canônica para `NaN`, enquanto `floatToRawIntBits` tenta preservar a representação bruta. Essa diferença foi mantida na adaptação sempre que possível.

**Alternativa em Python (quando aplicável):**
struct.pack("!f", valor)
struct.unpack("!I", bytes_do_float)

```
# exemplo de conversão de float para bits
struct.unpack("!I", struct.pack("!f", float(valor)))[0]

# exemplo de conversão de bits para float
struct.unpack("!f", struct.pack("!I", bits & 0xFFFFFFFF))[0]
```

**Issue relacionada:**
Issue #54

**Pull Request relacionado:**
A definir

### JFloat

**Métodos:**
`sum`, `max` e `min`

**Assinatura Java:**
`public static float sum(float a, float b)`

`public static float max(float a, float b)`

`public static float min(float a, float b)`

**Decisão da equipe:**
Os métodos aritméticos estáticos foram implementados utilizando as operações nativas de ponto flutuante do Python. Os argumentos recebidos são convertidos para `float` antes da execução da operação, buscando reproduzir o comportamento da classe `Float` da API Java.

**Justificativa:**
A classe `Float` do Java disponibiliza métodos estáticos para realizar operações simples de soma, obtenção do maior valor e obtenção do menor valor entre dois números de ponto flutuante.

Em Python, essas operações podem ser realizadas diretamente com os operadores e comparações nativas da linguagem. Para manter compatibilidade com o contrato da API Java, os métodos recebem dois valores, convertem os argumentos para `float` e retornam o resultado correspondente.

Nos métodos `max` e `min`, foi adotado tratamento explícito para valores `NaN`. Quando qualquer um dos argumentos é `NaN`, o método retorna `JFloat.NaN`, aproximando o comportamento esperado para operações envolvendo valores especiais de ponto flutuante.

**Comportamento adotado em Python:**

* `sum` retorna a soma de dois valores convertidos para `float`.
* `max` retorna o maior entre dois valores.
* `min` retorna o menor entre dois valores.
* Quando algum argumento é `NaN`, os métodos `max` e `min` retornam `JFloat.NaN`.
* Valores infinitos são tratados pelo próprio comportamento do tipo `float` do Python.

**Alternativa em Python (quando aplicável):**
`float(a) + float(b)`

`max(a, b)`

`min(a, b)`

**Issue relacionada:**
#55

**Pull Request relacionado:**
A definir.

### Estrutura inicial e construtores de JString

**Classe:** `JString`

**Elementos Java relacionados:**

- `String()`
- `String(String original)`
- `String(char[] value)`
- `String(char[], int, int)`

**Decisão da equipe:**

A classe `JString` foi implementada como adaptação da classe `String` da API Java SE 8. O valor interno é armazenado como `str` do Python, aproveitando a imutabilidade natural desse tipo.

As sobrecargas de construtores da API Java foram adaptadas para um único construtor Python, usando verificação de tipo e parâmetros opcionais `offset` e `count`.

**Justificativa:**

Python não possui sobrecarga de construtores da mesma forma que Java. Por isso, a equipe optou por concentrar os construtores básicos em `__init__`, preservando o comportamento principal esperado.

**Comportamento adotado em Python:**

- `JString()` cria uma string vazia.
- `JString("abc")` cria uma instância a partir de `str`.
- `JString(outra_jstring)` copia o valor interno de outra instância.
- `JString(["a", "b", "c"])` cria uma string a partir de caracteres.
- `JString(["a", "b", "c"], 1, 2)` cria uma string usando intervalo.

**Issue relacionada:** #65

**Pull Request relacionado:** #79

### Igualdade, hash e comparação de JString

**Classe:** `JString`

**Métodos:** `equals`, `equalsIgnoreCase`, `compareTo`, `compareToIgnoreCase`, `contentEquals` e `hashCode`

**Assinaturas Java:**
* `public boolean equals(Object anObject)`
* `public boolean equalsIgnoreCase(String anotherString)`
* `public int compareTo(String anotherString)`
* `public int compareToIgnoreCase(String str)`
* `public boolean contentEquals(CharSequence cs)`
* `public int hashCode()`

**Decisão da equipe:**
Os métodos de igualdade e comparação lexicográfica foram implementados utilizando as operações nativas de strings do Python (`==`, `<`, `>`). O método `contentEquals` foi adaptado para aceitar tanto `JString` quanto o tipo primitivo `str`. O método `hashCode` delega a geração do valor para a função embutida `hash()` do Python.

**Justificativa:**
Em Java, a comparação de strings com operadores relacionais checa a referência de memória, exigindo o uso explícito de `equals` e `compareTo`. Em Python, os operadores relacionais nativos já realizam a comparação estrutural e lexicográfica de strings de forma idiomática.

Para o `hashCode`, o algoritmo oficial do Java SE 8 baseia-se na fórmula s[0]*31^(n-1) + s[1]*31^(n-2) + ... gerando um inteiro de 32 bits fixo. Visando simplicidade e performance em ambiente Python, a equipe optou por utilizar a função `hash()` nativa, que garante a consistência (objetos iguais geram hashes iguais) necessária para o projeto, embora o valor final divirja do cálculo exato do Java.

**Alternativa em Python (quando aplicável):**
python
# equals nativo
string1 == string2

# hashCode nativo do Python
hash(string_value)

### Métodos de tamanho e acesso de JString

**Classe:** ‘JString‘

**Métodos relacionados:**
- ‘length‘
- ‘isEmpty‘
- ‘charAt‘
- ‘toCharArray‘
- ‘getChars‘
- ‘getBytes‘

**Decisão da equipe:**
Os métodos básicos de acesso de ‘JString‘ foram adaptados usando operações nativas de ‘str‘ do Python. O método ‘getBytes()‘ usa ‘utf-8‘ como charset padrão. A variação ‘getBytes(String charset)‘ foi adaptada por meio de um parâmetro opcional chamado ‘charset‘.

**Justificativa:**
Java pode usar o charset padrão da plataforma em ‘getBytes()‘. Para evitar comportamento dependente do ambiente, a implementação em Python usa ‘utf-8‘ como padrão.

**Comportamento adotado em Python:**

- ‘length()‘ retorna ‘len(self._value)‘.
- ‘isEmpty()‘ verifica se o tamanho é zero.
- ‘charAt(index)‘ retorna o caractere no índice informado.
- ‘toCharArray()‘ retorna uma nova lista de caracteres.
- ‘getChars()‘ copia caracteres para uma lista de destino.
- ‘getBytes()‘ retorna bytes usando ‘utf-8‘ por padrão.

**Issue relacionada:** #66

**Pull Request relacionado:** A definir.

---

### Transformações básicas de JString

**Classe:** ‘JString‘

**Métodos relacionados:**

- ‘substring‘
- ‘subSequence‘
- ‘concat‘
- ‘trim‘
- ‘intern‘

**Decisão da equipe:**

Os métodos de recorte e transformação de ‘JString‘ retornam novas instâncias de ‘JString‘, preservando a ideia de imutabilidade da classe ‘String‘ do Java. O método ‘substring‘ foi adaptado para aceitar ‘endIndex‘ opcional, representando as duas variações da API Java. O método ‘intern‘ foi tratado como adaptação e retorna a própria instância.

**Justificativa:**

Python não possui sobrecarga de métodos como Java, por isso as variações de ‘substring‘ foram reunidas em um único método. O pool interno de strings do Java não é reproduzido diretamente no runtime Python. Por isso, ‘intern‘ foi mantido apenas como método de compatibilidade.

**Comportamento adotado em Python:**

- ‘substring(beginIndex)‘ retorna do índice informado até o fim.
- ‘substring(beginIndex, endIndex)‘ retorna o intervalo informado.
- ‘subSequence(beginIndex, endIndex)‘ reutiliza ‘substring‘.
- ‘concat‘ retorna uma nova ‘JString‘.
- ‘trim‘ usa ‘strip()‘ do Python.
- ‘intern‘ retorna a própria instância.

**Issue relacionada:** #72

**Pull Request relacionado:** A definir.

---
### JString

**Métodos:**
`codePointAt`, `codePointBefore`, `codePointCount` e `offsetByCodePoints`

**Assinatura Java:**
`public int codePointAt(int index)`

`public int codePointBefore(int index)`

`public int codePointCount(int beginIndex, int endIndex)`

`public int offsetByCodePoints(int index, int codePointOffset)`

**Decisão da equipe:**
Os métodos de code points da classe `JString` foram implementados utilizando o comportamento nativo de strings do Python.

O método `codePointAt` retorna o código Unicode do caractere na posição informada usando `ord`. O método `codePointBefore` retorna o código Unicode do caractere anterior ao índice informado. O método `codePointCount` conta a quantidade de code points/caracteres Unicode no intervalo, e `offsetByCodePoints` calcula um novo índice a partir de um deslocamento informado.

**Justificativa:**
Na classe `String` do Java, os métodos de code points existem para lidar com caracteres Unicode, inclusive casos em que determinados caracteres podem ocupar mais de uma unidade `char`.

Em Python, a `str` trabalha de forma mais direta com caracteres Unicode, permitindo acessar caracteres por índice e obter seu código Unicode com `ord`. Por isso, a implementação foi adaptada para usar os recursos nativos da linguagem, mantendo uma interface semelhante à API Java.

**Comportamento adotado em Python:**

* `codePointAt(index)` retorna `ord(self._value[index])`.
* `codePointBefore(index)` retorna `ord(self._value[index - 1])`.
* `codePointCount(beginIndex, endIndex)` retorna o tamanho do intervalo da string.
* `offsetByCodePoints(index, codePointOffset)` retorna o índice deslocado pela quantidade informada.
* Índices inválidos geram `IndexError`.
* Índices ou deslocamentos com tipo inválido geram `TypeError`.

**Diferença em relação ao Java:**
A implementação não simula manualmente pares substitutos (`surrogate pairs`) da representação interna do Java. Para esta adaptação inicial, foi adotado o tratamento direto de caracteres Unicode do Python.

**Alternativa em Python (quando aplicável):**
`ord(character)`

`len(text[beginIndex:endIndex])`

**Issue relacionada:**
#67

**Pull Request relacionado:**
A definir.

---
### JString

**Métodos:**
`valueOf`, `copyValueOf`, `format` e `join`

**Assinatura Java:**
`public static String valueOf(Object obj)`

`public static String copyValueOf(char[] data)`

`public static String format(String format, Object... args)`

`public static String join(CharSequence delimiter, CharSequence... elements)`

**Decisão da equipe:**
Os métodos estáticos auxiliares da classe `JString` foram adaptados para Python utilizando verificação de tipos e recursos nativos da linguagem.

O método `valueOf` foi expandido para aceitar objetos genéricos, retornando uma `JString` baseada na representação textual do objeto. O valor `None` foi tratado como equivalente ao texto `"null"`, aproximando o comportamento esperado para `null` em Java.

O método `copyValueOf` cria uma nova `JString` a partir de uma lista ou tupla de caracteres, reutilizando as validações já existentes no construtor da classe.

O método `format` foi adaptado usando formatação textual do Python com o operador `%`. O método `join` foi implementado usando o método nativo `join` de strings do Python, aceitando delimitador e elementos do tipo `str` ou `JString`.

**Justificativa:**
Java possui sobrecarga de métodos e métodos estáticos específicos para conversão, cópia, formatação e junção de strings. Python não possui sobrecarga de métodos da mesma forma, então a implementação foi adaptada para concentrar os comportamentos em métodos com verificação de tipo em tempo de execução.

Além disso, a formatação de strings em Java e Python possui diferenças de sintaxe e funcionamento. Para esta adaptação inicial, foi adotada uma abordagem simplificada com o operador `%`, suficiente para os cenários básicos previstos na issue.

**Comportamento adotado em Python:**

* `valueOf(value)` retorna uma nova `JString` com a representação textual do valor recebido.
* `valueOf(None)` retorna `JString("null")`.
* `copyValueOf(value)` cria uma `JString` a partir de lista ou tupla de caracteres.
* `format(format_string, *args)` retorna uma `JString` com o texto formatado.
* `join(delimiter, *elements)` une strings usando o delimitador informado.
* `join` aceita delimitador e elementos do tipo `str` ou `JString`.
* Tipos inválidos geram `TypeError`.
* Argumentos inválidos de formatação geram `ValueError`.

**Diferença em relação ao Java:**
A implementação não reproduz todas as variações sobrecarregadas da API Java. As variações foram adaptadas para métodos Python com parâmetros flexíveis e validação interna.

O método `format` também não implementa toda a sintaxe de formatação da classe `String` do Java, adotando a formatação nativa do Python como alternativa simplificada.

**Alternativa em Python (quando aplicável):**
`str(value)`

`"".join(characters)`

`format_string % args`

`delimiter.join(elements)`

**Issue relacionada:**
#76

**Pull Request relacionado:**
A definir.


### Busca e correspondência de conteúdo em JString

**Classe:** `JString`

**Métodos relacionados:**

* `contains`
* `startsWith`
* `startsWith` com offset
* `endsWith`
* `regionMatches`
* `regionMatches` com `ignoreCase`

**Decisão da equipe:**

Os métodos de busca e correspondência de conteúdo foram implementados utilizando as operações equivalentes disponíveis na classe `str` do Python. As sobrecargas existentes na API Java foram adaptadas para uma única implementação quando necessário, preservando o comportamento esperado da especificação.

**Justificativa:**

Python não possui suporte nativo à sobrecarga de métodos baseada em assinatura, como ocorre em Java. Por esse motivo, as variações de `startsWith` e `regionMatches` foram unificadas em uma única implementação capaz de tratar diferentes conjuntos de parâmetros. A funcionalidade original foi mantida sem perda de comportamento observável.

**Comportamento adotado em Python:**

* `contains(sequence)` verifica se uma sequência está presente na string.
* `startsWith(prefix)` verifica se a string começa com o prefixo informado.
* `startsWith(prefix, toffset)` verifica se a string começa com o prefixo a partir da posição indicada.
* `endsWith(suffix)` verifica se a string termina com o sufixo informado.
* `regionMatches(toffset, other, ooffset, length)` compara regiões específicas de duas strings.
* `regionMatches(ignoreCase, toffset, other, ooffset, length)` compara regiões específicas ignorando diferenças entre maiúsculas e minúsculas quando solicitado.
* Comparações de região que ultrapassem os limites das strings retornam `False`, seguindo o comportamento da API Java.

**Issue relacionada:** #69


---

## Histórico de Atualizações

| Data       | Alteração                    | Responsável |
| ---------- | ---------------------------- | ----------- |
| 13/06/2026 | Criação inicial do documento | Luciana     |
| 19/06/2026 | Registro das adaptações de operações sem sinal de JInteger | Isabela |
| 19/06/2026 | Implementação de conversões  | Miguel      |
| 19/06/2026 | Registro das adaptações de parsing e criação por valor de JInteger | Reinaldo |
| 19/06/2026 | Registro das adaptações de operações bit-a-bit| Beatriz |
| 19/06/2026 | Registro das adaptações de operações bit-a-bit| Miguel |
| 20/06/2026 | Registro das adaptações de operações de conversões em JFloat| Miguel |
| 20/06/2026 | Registro das adaptações de  parsing value em JFloat| Beatriz |
| 21/06/2026 | Registro das adaptações de valores especiais em JFloat | Isabela |
| 21/06/2026 | Registro das adaptações de conversões de bits e representação hexadecimal em JFloat | Luciana |
| 21/06/2026 | Registro das adaptações dos metodos estaticos min, max e sum em JFloat | Miguel |
| 21/06/2026 | Registro das adaptações de igualdade, hash e comparação em JString | Maria Eduarda |
| 21/06/2026 | Registro das adaptações de de acesso, tamanho, conversão, da classe JString. em JString | BEatriz |
| 21/06/2026 | Registro das adaptações de recorte e transformação em JString | Beatriz |
| 21/06/2026 | Registro das adaptações de code points em JString | Isabela |
| 21/06/2026 | Registro das adaptações de métodos estáticos auxiliares em JString | Isabela |
