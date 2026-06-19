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

## Histórico de Atualizações

| Data       | Alteração                    | Responsável |
| ---------- | ---------------------------- | ----------- |
| 13/06/2026 | Criação inicial do documento | Luciana     |
| 19/06/2026 | Adição de adaptação métodos estáticos | Beatriz     |



### Classe
Jinteger

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