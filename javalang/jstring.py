"""Implementação inicial da classe JString."""


class JString:
    """Representa uma adaptação da classe String da API Java SE 8."""

    def length(self):
        """Retorna o tamanho da string."""
        return len(self._value)
    
    def isEmpty(self):
        """Verifica se a string esta vazia."""
        return self.length() == 0
    
    def charAt(self, index):
        """Retorna o caractere na posicao informada."""
        if not isinstance(index, int):
            raise TypeError("index must be an int")
        if index < 0 or index >= self.length():
            raise IndexError("index out of range")
    
        return self._value[index]
    
    def toCharArray(self):
        """Retorna uma lista com os caracteres da string."""
        return list(self._value)
    
    def getChars(self, srcBegin, srcEnd, dst, dstBegin):
        """Copia caracteres da string para uma lista de destino."""
        if not all(isinstance(value, int) for value in [srcBegin, srcEnd, dstBegin]):
            raise TypeError("srcBegin, srcEnd and dstBegin must be integers")
        
        if not isinstance(dst, list):
            raise TypeError("dst must be a list")
        
        if srcBegin < 0 or srcEnd < srcBegin or srcEnd > self.length():
            raise IndexError("source range is invalid")
        
        characters_to_copy = self._value[srcBegin:srcEnd]

        if dstBegin < 0 or dstBegin + len(characters_to_copy) > len(dst):
            raise IndexError("destination range is invalid")
        
        for index, character in enumerate(characters_to_copy):
            dst[dstBegin + index] = character

    def getBytes(self, charset="utf-8"):
        """Retorna os bytes da string usando o charset informado."""
        if not isinstance(charset, str):
            raise TypeError("charset must be a string")
        
        try:
            return self._value.encode(charset)
        except LookupError as error:
            raise LookupError("unsupported charset") from error

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
    
    def contentEquals(self, other):
        if isinstance(other, JString):
            return self._value == other._value

        if isinstance(other, str):
            return self._value == other

        return False


    def hashCode(self):
        return hash(self._value)
    
    def substring(self, beginIndex, endIndex=None):
        """Retorna uma nova JString com parte do conteudo."""
        if not isinstance(beginIndex, int):
            raise TypeError("beginIndex must be an int")
        
        if endIndex is None:
            endIndex = self.length()
        elif not isinstance(endIndex, int):
            raise TypeError("endIndex must be an int")
        
        if beginIndex < 0 or endIndex < beginIndex or endIndex > self.length():
            raise IndexError("substring range is invalid")
        
        return JString(self._value[beginIndex:endIndex])
    
    def subSequence(self, beginIndex, endIndex):
        """Retorna uma subsequencia da string."""

        return self.substring(beginIndex, endIndex)
    
    def concat(self, other):
        """Concatena esta string com outra string."""
        if isinstance(other, JString):
            other_value = other._value
        elif isinstance(other, str):
            other_value = other
        else:
            raise TypeError("other must be a string or JString")
        return JString(self._value + other_value)

    def trim(self):
        """Remove espacos das extremidades da string."""
        return JString(self._value.strip())

    def intern(self):
        """Retorna a propria instancia como adaptacao de String.intern."""
        return self
    
    def contains(self, sequence):
        """Verifica se a string contem a sequencia informada."""
        if isinstance(sequence, JString):
            sequence_value = sequence._value
        elif isinstance(sequence, str):
            sequence_value = sequence
        else:
            raise TypeError("sequence must be a string or JString")
        return sequence_value in self._value
    
    def startsWith(self, prefix, toffset=0):
        """Verifica se a string começa com o prefixo informado."""
        if isinstance(prefix, JString):
            prefix = prefix._value
        elif not isinstance(prefix, str):
            raise TypeError("prefix must be a string or JString")

        if not isinstance(toffset, int):
            raise TypeError("toffset must be an int")

        if toffset < 0 or toffset > self.length():
            return False

        return self._value.startswith(prefix, toffset)
    
    def endsWith(self, suffix):
        """Verifica se a string termina com o sufixo informado."""
        if isinstance(suffix, JString):
            suffix = suffix._value
        elif not isinstance(suffix, str):
            raise TypeError("suffix must be a string or JString")

        return self._value.endswith(suffix)