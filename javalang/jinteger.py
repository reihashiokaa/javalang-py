"""Implementação inicial da classe JInteger."""


class JInteger:
    """Representa a classe Integer da API Java SE 8."""

    MAX_VALUE = (2**31) - 1
    MIN_VALUE = -(2**31)
    SIZE = 32
    BYTES = 4
    TYPE = int

    """Funções auxiliares"""
     
    def _to_uint32(value: int) -> int:
        """Interpreta o valor como inteiro sem sinal de 32 bits."""
        return value & 0xFFFFFFFF
    
    
    def _to_int32(value: int) -> int:
        """Converte um inteiro de 32 bits sem sinal para inteiro assinado."""
        value = _to_uint32(value)
        if value >= 0x80000000:
            value -= 0x100000000
        return value


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