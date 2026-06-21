"""Implementação inicial da classe JString."""


class JString:
    """Representa uma adaptação da classe String da API Java SE 8."""

    def __init__(self, value="", offset=None, count=None):
        has_range = offset is not None or count is not None

        if isinstance(value, JString):
            if has_range:
                raise TypeError("offset and count can only be used with character arrays")

            self._value = value._value
            return

        if isinstance(value, str):
            if has_range:
                raise TypeError("offset and count can only be used with character arrays")

            self._value = value
            return

        if isinstance(value, (list, tuple)):
            characters = list(value)

            for character in characters:
                if not isinstance(character, str) or len(character) != 1:
                    raise ValueError("character array must contain only single-character strings")

            if has_range:
                if offset is None or count is None:
                    raise ValueError("offset and count must be provided together")

                if offset < 0 or count < 0 or offset + count > len(characters):
                    raise IndexError("offset and count are outside the character array range")

                characters = characters[offset : offset + count]

            self._value = "".join(characters)
            return

        raise TypeError("value must be a string, JString, list or tuple of characters")
    
    def equals(self, other):
        if not isinstance(other, JString):
            return False
        return self._value == other._value

    def equalsIgnoreCase(self, other):
        if not isinstance(other, JString):
            return False
        return self._value.lower() == other._value.lower()
    
    def compareTo(self, other):
        if not isinstance(other, JString):
            raise TypeError("other must be a JString")

        if self._value == other._value:
            return 0

        if self._value < other._value:
            return -1

        return 1


    def compareToIgnoreCase(self, other):
        if not isinstance(other, JString):
            raise TypeError("other must be a JString")

        left = self._value.lower()
        right = other._value.lower()

        if left == right:
            return 0

        if left < right:
            return -1

        return 1