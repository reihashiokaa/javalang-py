"""Implementação inicial da classe JInteger."""

"""Funções auxiliares"""
     
def _to_uint32(value: int) -> int:
        return value & 0xFFFFFFFF
    
    
def _to_int32(value: int) -> int:
        value = _to_uint32(value)
        if value >= 0x80000000:
            value -= 0x100000000
        return value


class JInteger:
    """Representa a classe Integer da API Java SE 8."""

    MAX_VALUE = (2**31) - 1
    MIN_VALUE = -(2**31)
    SIZE = 32
    BYTES = 4
    TYPE = int


    """Métodos estáticos"""
    @staticmethod
    def reverse(i: int) -> int:
        """
        Inverte a ordem dos 32 bits do valor.
        Equivalente a Integer.reverse(int) do Java SE 8.
        Diferença em relação ao Python: int nativo não tem tamanho fixo,
        por isso a operação é forçada em 32 bits e o resultado é convertido
        para inteiro assinado (igual ao Java).
        """
        bits = _to_uint32(i)
        result = 0
        for _ in range(32):
            result = (result << 1) | (bits & 1)
            bits >>= 1
        return _to_int32(result)
    

    @staticmethod
    def reverseBytes(i: int) -> int:
        """
        Inverte a ordem dos quatro bytes do inteiro de 32 bits.
        Diferença: resultado convertido para inteiro assinado de 32 bits.
        """
        bits = _to_uint32(i)
        b0 = (bits >> 24) & 0xFF
        b1 = (bits >> 16) & 0xFF
        b2 = (bits >> 8) & 0xFF
        b3 = bits & 0xFF
        result = (b3 << 24) | (b2 << 16) | (b1 << 8) | b0
        return _to_int32(result)
 
    @staticmethod
    def rotateLeft(i: int, distance: int) -> int:
        """
        Rotaciona os bits do valor para a esquerda.
        Distâncias >= 32 ou negativas são normalizadas com módulo 32.
        Bits que saem pela esquerda retornam pela direita.
        """
        distance = distance % 32
        if distance == 0:
            return _to_int32(i)
        bits = _to_uint32(i)
        result = ((bits << distance) | (bits >> (32 - distance)))
        return _to_int32(result)
 
    @staticmethod
    def rotateRight(i: int, distance: int) -> int:
        """
        Rotaciona os bits do valor para a direita.
        Distâncias >= 32 ou negativas são normalizadas com módulo 32.
        Bits que saem pela direita retornam pela esquerda.
        """
        distance = distance % 32
        if distance == 0:
            return _to_int32(i)
        bits = _to_uint32(i)
        result = ((bits >> distance) | (bits << (32 - distance)))
        return _to_int32(result)
 
    @staticmethod
    def signum(i: int) -> int:
        """
        Retorna o sinal do valor: -1 se negativo, 0 se zero, 1 se positivo.
        Não há diferença de comportamento em relação ao Python.
        """
        if i < 0:
            return -1
        if i > 0:
            return 1
        return 0 

    def __init__(self, value: int):
        """Inicializa um JInteger a partir de um valor inteiro."""
        if not isinstance(value, int):
            raise TypeError("JInteger value must be an int")

        if value < self.MIN_VALUE or value > self.MAX_VALUE:
            raise OverflowError("JInteger value must be within 32-bit signed integer range")

        self._value = value

    def toString(self):
        """Retorna a representação textual do valor inteiro."""
        return str(self._value)

    def hashCode(self):
        """Retorna o hash compatível com o valor inteiro armazenado."""
        return self._value
    def equals(self, other):
        """Compara este JInteger com outro objeto por valor."""
        return isinstance(other, JInteger) and self._value == other._value

    def compareTo(self, other):
        """Compara este JInteger com outro JInteger."""
        if not isinstance(other, JInteger):
            raise TypeError("compareTo expects a JInteger instance")

        if self._value < other._value:
            return -1

        if self._value > other._value:
            return 1

        return 0