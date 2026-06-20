"""Implementação inicial da classe JFloat."""


class JFloat:
    """Representa uma adaptação da classe Float da API Java SE 8."""

    POSITIVE_INFINITY = float("inf")
    NEGATIVE_INFINITY = float("-inf")
    NaN = float("nan")
    MAX_VALUE = 3.4028235e38
    MIN_VALUE = 1.4e-45
    MIN_NORMAL = 1.17549435e-38
    MAX_EXPONENT = 127
    MIN_EXPONENT = -126
    SIZE = 32
    BYTES = 4
    TYPE = float

    def __init__(self, value=0.0):
        self._value = float(value)

    def byteValue(self):
        value = int(self._value) & 0xFF
        return value - 256 if value >= 128 else value

    def shortValue(self):
        value = int(self._value) & 0xFFFF
        return value - 65536 if value >= 32768 else value
    
    def intValue(self):
        return int(self._value)

    def longValue(self):
        return int(self._value)
