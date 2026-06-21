import math
import struct

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

    def floatValue(self):
        return float(self._value)

    def doubleValue(self):
        return float(self._value)

    @staticmethod
    def parseFloat(s: str) -> float:
        """
        Adaptação: Java lança NumberFormatException para entradas inválidas.
        Em Python, lançamos ValueError com mensagem equivalente, pois
        NumberFormatException não existe na linguagem.
        """
        if not isinstance(s, str):
            raise ValueError(
                f"parseFloat espera uma string, recebeu {type(s).__name__}"
            )
        s = s.strip()
        if s in ("Infinity", "+Infinity"):
            return float("inf")
        if s == "-Infinity":
            return float("-inf")
        if s == "NaN":
            return float("nan")
        try:
            return float(s)
        except ValueError:
            raise ValueError(f'parseFloat: entrada inválida: "{s}"')
 
    @staticmethod
    def valueOf(value) -> "JFloat":
        """
        Adaptação: em Java, valueOf é um método sobrecarregado — existe
        Float.valueOf(float) e Float.valueOf(String). Python não suporta
        sobrecarga de métodos, então unificamos os dois em um único método
        que detecta o tipo do argumento:
          - se receber str, converte via parseFloat antes de criar a instância;
          - se receber int ou float, cria a instância diretamente.
        """
        if isinstance(value, str):
            return JFloat(JFloat.parseFloat(value))
        if isinstance(value, (int, float)):
            return JFloat(float(value))
        raise ValueError(
            f"valueOf espera str, int ou float, recebeu {type(value).__name__}"
        )
    

    def toString(self) -> str:
        """Retorna a string correspondente ao valor do float."""
        if math.isnan(self._value):
            return "NaN"
        if self._value == float('inf'):
            return "Infinity"
        if self._value == float('-inf'):
            return "-Infinity"
        return str(self._value)

    @staticmethod
    def toString_static(f: float) -> str:
        """Equivalente a Float.toString(float) do Java."""
        return JFloat(f).toString()

    def hashCode(self) -> int:
        """Retorna o hash compatível com Float.hashCode() do Java."""
        if math.isnan(self._value):
            return 0x7fc00000
        return struct.unpack('I', struct.pack('f', self._value))[0]
    
    def equals(self, other) -> bool:
        """Compara este JFloat com outro objeto por valor."""
        if not isinstance(other, JFloat):
            return False
        if math.isnan(self._value) and math.isnan(other._value):
            return True
        if self._value == 0.0 and other._value == 0.0:
            return self.hashCode() == other.hashCode()
        return self._value == other._value

    def compareTo(self, other) -> int:
        """Compara duas instâncias de JFloat."""
        if not isinstance(other, JFloat):
            raise TypeError("compareTo expects a JFloat instance")
        return JFloat.compare(self._value, other._value)

    @staticmethod
    def compare(f1: float, f2: float) -> int:
        """Compara dois valores float brutos usando as regras do Java."""
        v1 = struct.unpack('f', struct.pack('f', float(f1)))[0]
        v2 = struct.unpack('f', struct.pack('f', float(f2)))[0]

        if math.isnan(v1):
            return 0 if math.isnan(v2) else 1
        if math.isnan(v2):
            return -1

        if v1 < v2:
            return -1
        if v1 > v2:
            return 1

        if v1 == 0.0 and v2 == 0.0:
            h1 = struct.unpack('I', struct.pack('f', v1))[0]
            h2 = struct.unpack('I', struct.pack('f', v2))[0]
            if h1 < h2:
                return 1
            if h1 > h2:
                return -1
        return 0

