"""Implementação inicial da classe JInteger."""


class JInteger:
    """Representa a classe Integer da API Java SE 8."""

    MAX_VALUE = (2**31) - 1
    MIN_VALUE = -(2**31)
    SIZE = 32
    BYTES = 4
    TYPE = int

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
    
    def intValue(self):
        """Retorna o valor armazenado como int"""
        return self._value

    def logValue(self):
        """Retorna o valor armazenado como long"""
        return self._value
    

        return 0