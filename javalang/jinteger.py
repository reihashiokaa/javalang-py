"""Implementação inicial da classe JInteger."""

_DIGITS = "0123456789abcdefghijklmnopqrstuvwxyz"
_UNSIGNED_MASK = (2**32) - 1
_UNSIGNED_MAX_VALUE = (2**32) - 1


def _validate_radix(radix: int):
    """Valida se a base numérica está dentro do intervalo permitido."""
    if not isinstance(radix, int):
        raise TypeError("radix must be an int")

    if radix < 2 or radix > 36:
        raise ValueError("radix must be between 2 and 36")


def _to_unsigned_32(value: int):
    """Interpreta um inteiro como valor sem sinal de 32 bits."""
    if not isinstance(value, int):
        raise TypeError("value must be an int")

    return value & _UNSIGNED_MASK


def _format_unsigned(value: int, radix: int):
    """Formata um inteiro positivo em uma base entre 2 e 36."""
    if value == 0:
        return "0"

    digits = []

    while value > 0:
        digits.append(_DIGITS[value % radix])
        value //= radix

    return "".join(reversed(digits))


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

        return 0

    @staticmethod
    def parseInt(value: str, radix: int = 10):
        """Converte uma string em inteiro com sinal de 32 bits."""
        _validate_radix(radix)

        if not isinstance(value, str):
            raise TypeError("value must be a string")

        if value == "":
            raise ValueError("value must not be empty")

        if value.strip() != value:
            raise ValueError("value must not contain whitespace")

        parsed_value = int(value, radix)

        if parsed_value < JInteger.MIN_VALUE or parsed_value > JInteger.MAX_VALUE:
            raise OverflowError("integer value must be within signed 32-bit range")

        return parsed_value
    
    @staticmethod
    def valueOf(value, radix: int = 10):
        """Cria uma instância de JInteger a partir de inteiro ou string."""
        if isinstance(value, int):
            if value < JInteger.MIN_VALUE or value > JInteger.MAX_VALUE:
                raise OverflowError("integer value must be within signed 32-bit range")

            return JInteger(value)

        if isinstance(value, str):
            return JInteger(JInteger.parseInt(value, radix))

        raise TypeError("value must be an int or a string")
    
    @staticmethod
    def decode(value: str):
        """Decodifica uma string numérica em uma instância de JInteger."""
        if not isinstance(value, str):
            raise TypeError("value must be a string")

        if value == "":
            raise ValueError("value must not be empty")

        if value.strip() != value:
            raise ValueError("value must not contain whitespace")

        sign = 1
        number = value

        if number[0] in "+-":
            if number[0] == "-":
                sign = -1

            number = number[1:]

            if number == "":
                raise ValueError("value must contain digits")

        radix = 10

        if number.startswith(("0x", "0X")):
            radix = 16
            number = number[2:]
        elif number.startswith("#"):
            radix = 16
            number = number[1:]
        elif len(number) > 1 and number.startswith("0"):
            radix = 8
            number = number[1:]

        if number == "":
            raise ValueError("value must contain digits")

        parsed_value = int(number, radix) * sign

        if parsed_value < JInteger.MIN_VALUE or parsed_value > JInteger.MAX_VALUE:
            raise OverflowError("integer value must be within signed 32-bit range")

        return JInteger(parsed_value)

    @staticmethod
    def parseUnsignedInt(value: str, radix: int = 10):
        """Converte uma string em inteiro sem sinal de 32 bits."""
        _validate_radix(radix)

        if not isinstance(value, str):
            raise TypeError("value must be a string")

        if value == "":
            raise ValueError("value must not be empty")

        if value.startswith("-"):
            raise ValueError("unsigned integer must not be negative")

        parsed_value = int(value, radix)

        if parsed_value > _UNSIGNED_MAX_VALUE:
            raise OverflowError("unsigned integer value must be within 32-bit range")

        return parsed_value

    @staticmethod
    def toUnsignedString(value: int, radix: int = 10):
        """Retorna a representação textual sem sinal de um inteiro de 32 bits."""
        _validate_radix(radix)
        unsigned_value = _to_unsigned_32(value)

        return _format_unsigned(unsigned_value, radix)
    
    @staticmethod
    def compareUnsigned(first: int, second: int):
        """Compara dois inteiros usando interpretação sem sinal de 32 bits."""
        first_unsigned = _to_unsigned_32(first)
        second_unsigned = _to_unsigned_32(second)

        if first_unsigned < second_unsigned:
            return -1

        if first_unsigned > second_unsigned:
            return 1

        return 0

    @staticmethod
    def divideUnsigned(dividend: int, divisor: int):
        """Divide dois inteiros interpretados como sem sinal de 32 bits."""
        unsigned_dividend = _to_unsigned_32(dividend)
        unsigned_divisor = _to_unsigned_32(divisor)

        if unsigned_divisor == 0:
            raise ZeroDivisionError("division by zero")

        return unsigned_dividend // unsigned_divisor

    @staticmethod
    def remainderUnsigned(dividend: int, divisor: int):
        """Retorna o resto da divisão sem sinal de 32 bits."""
        unsigned_dividend = _to_unsigned_32(dividend)
        unsigned_divisor = _to_unsigned_32(divisor)

        if unsigned_divisor == 0:
            raise ZeroDivisionError("division by zero")

        return unsigned_dividend % unsigned_divisor