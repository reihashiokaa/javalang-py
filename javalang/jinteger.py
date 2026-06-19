"""Implementação inicial da classe JInteger."""


class JInteger:
    MAX_VALUE = (2**31) - 1
    MIN_VALUE = -(2**31)
    SIZE = 32
    BYTES = 4
    TYPE = int

    @staticmethod
    def toString(value, radix=10):
        if radix < 2 or radix > 36:
            raise ValueError("radix deve estar entre 2 e 36")

        if radix == 10:
            return str(value)

        digits = "0123456789abcdefghijklmnopqrstuvwxyz"

        if value == 0:
            return "0"

        negative = value < 0
        value = abs(value)

        result = ""

        while value > 0:
            result = digits[value % radix] + result
            value //= radix

        return "-" + result if negative else result

    @staticmethod
    def toBinaryString(value):
        return JInteger.toString(value, 2)

    @staticmethod
    def toOctalString(value):
        return JInteger.toString(value, 8)

    @staticmethod
    def toHexString(value):
        return JInteger.toString(value, 16)