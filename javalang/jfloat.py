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