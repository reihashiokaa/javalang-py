
import pytest

from javalang import JInteger


def test_jinteger_max_value_matches_java_integer_limit():
    assert JInteger.MAX_VALUE == (2**31) - 1


def test_jinteger_min_value_matches_java_integer_limit():
    assert JInteger.MIN_VALUE == -(2**31)


def test_jinteger_size_and_bytes_match_java_integer():
    assert JInteger.SIZE == 32
    assert JInteger.BYTES == 4
    assert JInteger.SIZE == JInteger.BYTES * 8


def test_jinteger_type_uses_python_int_as_adaptation():
    assert JInteger.TYPE is int

def test_jinteger_constructor_rejects_invalid_values():
    with pytest.raises(TypeError):
        JInteger("10")

    with pytest.raises(OverflowError):
        JInteger(JInteger.MAX_VALUE + 1)

    with pytest.raises(OverflowError):
        JInteger(JInteger.MIN_VALUE - 1)


def test_to_string_returns_decimal_representation():
    assert JInteger(10).toString() == "10"
    assert JInteger(-10).toString() == "-10"
    assert JInteger(0).toString() == "0"


def test_hash_code_returns_stored_integer_value():
    assert JInteger(10).hashCode() == 10
    assert JInteger(-10).hashCode() == -10
    assert JInteger(0).hashCode() == 0

def test_equals_compares_jinteger_by_value():
    assert JInteger(10).equals(JInteger(10)) is True
    assert JInteger(10).equals(JInteger(5)) is False
    assert JInteger(-1).equals(JInteger(-1)) is True
    assert JInteger(0).equals(0) is False


def test_compare_to_orders_jinteger_values():
    assert JInteger(10).compareTo(JInteger(5)) == 1
    assert JInteger(5).compareTo(JInteger(10)) == -1
    assert JInteger(10).compareTo(JInteger(10)) == 0
    assert JInteger(-5).compareTo(JInteger(0)) == -1


def test_compare_to_rejects_non_jinteger():
    with pytest.raises(TypeError):
        JInteger(10).compareTo(10)



def test_compare_less():
    assert JInteger.compare(5, 10) == -1

def test_compare_greater():
    assert JInteger.compare(10, 5) == 1

def test_compare_equal():
    assert JInteger.compare(5, 5) == 0

def test_compare_zero():
    assert JInteger.compare(0, 0) == 0

def test_reverse_zero():
    assert JInteger.reverse(0) == 0
 
 
def test_reverse_one():
    assert JInteger.reverse(1) == -2147483648
 
 
def test_reverse_minus_one():
    assert JInteger.reverse(-1) == -1
 
 
def test_reverse_bytes_zero():
    assert JInteger.reverseBytes(0) == 0
 
 
def test_reverse_bytes_hex():
    assert JInteger.reverseBytes(0x01020304) == 0x04030201

def test_rotate_left_distance_1():
    assert JInteger.rotateLeft(1, 1) == 2
 
 
def test_rotate_left_distance_32():
    assert JInteger.rotateLeft(1, 32) == 1
 
 
def test_rotate_left_distance_33():
    assert JInteger.rotateLeft(1, 33) == JInteger.rotateLeft(1, 1)

def test_rotate_right_distance_1():
    assert JInteger.rotateRight(1, 1) == -2147483648
 
 
def test_rotate_right_distance_32():
    assert JInteger.rotateRight(1, 32) == 1
 
 
def test_rotate_right_distance_33():
    assert JInteger.rotateRight(1, 33) == JInteger.rotateRight(1, 1)
 
def test_signum_negative():
    assert JInteger.signum(-10) == -1
 
 
def test_signum_zero():
    assert JInteger.signum(0) == 0
 
 
def test_signum_positive():
    assert JInteger.signum(10) == 1
 
def test_int_value_returns_stored_integer():
    assert JInteger(10).intValue() == 10

def test_int_value_negative():
    assert JInteger(-10).intValue() == -10

def test_int_value_zero():
    assert JInteger(0).intValue() == 0

def test_long_value_returns_stored_integer():
    assert JInteger(10).longValue() == 10

def test_float_value_returns_float():
    assert JInteger(10).floatValue() == 10.0

def test_double_value_returns_float():
    assert JInteger(10).doubleValue() == 10.0

def test_byte_value_positive():
    assert JInteger(127).byteValue() == 127

def test_byte_value_overflow():
    assert JInteger(128).byteValue() == -128

def test_byte_value_negative():
    assert JInteger(-1).byteValue() == -1

def test_short_value_positive():
    assert JInteger(32767).shortValue() == 32767

def test_short_value_overflow():
    assert JInteger(32768).shortValue() == -32768

def test_short_value_negative():
    assert JInteger(-1).shortValue() == -1

def test_parse_unsigned_int_accepts_valid_values():
    assert JInteger.parseUnsignedInt("0") == 0
    assert JInteger.parseUnsignedInt("10") == 10
    assert JInteger.parseUnsignedInt("4294967295") == 4294967295
    assert JInteger.parseUnsignedInt("11111111", 2) == 255
    assert JInteger.parseUnsignedInt("ff", 16) == 255
    assert JInteger.parseUnsignedInt("377", 8) == 255


def test_parse_unsigned_int_rejects_invalid_values():
    with pytest.raises(ValueError):
        JInteger.parseUnsignedInt("-1")

    with pytest.raises(ValueError):
        JInteger.parseUnsignedInt("")

    with pytest.raises(ValueError):
        JInteger.parseUnsignedInt("10", 1)

    with pytest.raises(ValueError):
        JInteger.parseUnsignedInt("10", 37)

    with pytest.raises(OverflowError):
        JInteger.parseUnsignedInt("4294967296")


def test_to_unsigned_string_formats_values():
    assert JInteger.toUnsignedString(0) == "0"
    assert JInteger.toUnsignedString(10) == "10"
    assert JInteger.toUnsignedString(-1) == "4294967295"
    assert JInteger.toUnsignedString(255, 2) == "11111111"
    assert JInteger.toUnsignedString(255, 8) == "377"
    assert JInteger.toUnsignedString(255, 16) == "ff"
    assert JInteger.toUnsignedString(-1, 16) == "ffffffff"

def test_compare_unsigned_orders_values_as_unsigned_32_bits():
    assert JInteger.compareUnsigned(1, 2) == -1
    assert JInteger.compareUnsigned(2, 1) == 1
    assert JInteger.compareUnsigned(2, 2) == 0
    assert JInteger.compareUnsigned(-1, 1) == 1


def test_divide_unsigned_uses_unsigned_32_bit_interpretation():
    assert JInteger.divideUnsigned(10, 2) == 5
    assert JInteger.divideUnsigned(-1, 2) == 2147483647
    assert JInteger.divideUnsigned(-1, -1) == 1


def test_remainder_unsigned_uses_unsigned_32_bit_interpretation():
    assert JInteger.remainderUnsigned(10, 3) == 1
    assert JInteger.remainderUnsigned(-1, 2) == 1
    assert JInteger.remainderUnsigned(-1, -1) == 0


def test_unsigned_division_operations_reject_zero_divisor():
    with pytest.raises(ZeroDivisionError):
        JInteger.divideUnsigned(10, 0)

    with pytest.raises(ZeroDivisionError):
        JInteger.remainderUnsigned(10, 0)


def test_parse_int_accepts_decimal_values():
    assert JInteger.parseInt("0") == 0
    assert JInteger.parseInt("10") == 10
    assert JInteger.parseInt("-10") == -10


def test_parse_int_accepts_radix_values():
    assert JInteger.parseInt("1010", 2) == 10
    assert JInteger.parseInt("12", 8) == 10
    assert JInteger.parseInt("A", 16) == 10


def test_parse_int_rejects_invalid_values():
    with pytest.raises(ValueError):
        JInteger.parseInt("")

    with pytest.raises(ValueError):
        JInteger.parseInt("abc")

    with pytest.raises(ValueError):
        JInteger.parseInt("102", 2)

    with pytest.raises(ValueError):
        JInteger.parseInt("10", 1)

    with pytest.raises(ValueError):
        JInteger.parseInt("10", 37)


def test_parse_int_rejects_values_outside_signed_32_bit_range():
    with pytest.raises(OverflowError):
        JInteger.parseInt(str(JInteger.MAX_VALUE + 1))

    with pytest.raises(OverflowError):
        JInteger.parseInt(str(JInteger.MIN_VALUE - 1))
        
        
def test_value_of_creates_jinteger_from_integer():
    result = JInteger.valueOf(10)

    assert isinstance(result, JInteger)
    assert result.toString() == "10"


def test_value_of_creates_jinteger_from_string():
    result = JInteger.valueOf("10")

    assert isinstance(result, JInteger)
    assert result.toString() == "10"


def test_value_of_creates_jinteger_from_string_with_radix():
    result = JInteger.valueOf("1010", 2)

    assert isinstance(result, JInteger)
    assert result.toString() == "10"


def test_value_of_rejects_invalid_type():
    with pytest.raises(TypeError):
        JInteger.valueOf(10.5)


def test_value_of_rejects_integer_outside_signed_32_bit_range():
    with pytest.raises(OverflowError):
        JInteger.valueOf(JInteger.MAX_VALUE + 1)

    with pytest.raises(OverflowError):
        JInteger.valueOf(JInteger.MIN_VALUE - 1)
        
def test_decode_interprets_decimal_values():
    assert JInteger.decode("10").toString() == "10"
    assert JInteger.decode("-10").toString() == "-10"
    assert JInteger.decode("0").toString() == "0"


def test_decode_interprets_hexadecimal_prefixes():
    assert JInteger.decode("0x10").toString() == "16"
    assert JInteger.decode("0X10").toString() == "16"
    assert JInteger.decode("#10").toString() == "16"
    assert JInteger.decode("-0x10").toString() == "-16"


def test_decode_interprets_octal_prefix():
    assert JInteger.decode("010").toString() == "8"


def test_decode_rejects_invalid_values():
    with pytest.raises(TypeError):
        JInteger.decode(10)

    with pytest.raises(ValueError):
        JInteger.decode("")

    with pytest.raises(ValueError):
        JInteger.decode("0x")

    with pytest.raises(ValueError):
        JInteger.decode("abc")


def test_decode_rejects_values_outside_signed_32_bit_range():
    with pytest.raises(OverflowError):
        JInteger.decode("0x80000000")

    assert JInteger.decode("-0x80000000").toString() == str(JInteger.MIN_VALUE)

def test_bit_count_zero():
    assert JInteger.bitCount(0) == 0


def test_bit_count_positive():
    assert JInteger.bitCount(10) == 2


def test_bit_count_all_bits_set():
    assert JInteger.bitCount(-1) == 32

def test_highest_one_bit_zero():
    assert JInteger.highestOneBit(0) == 0


def test_highest_one_bit_positive():
    assert JInteger.highestOneBit(10) == 8


def test_highest_one_bit_power_of_two():
    assert JInteger.highestOneBit(16) == 16


def test_highest_one_bit_negative():
    assert JInteger.highestOneBit(-1) == -2147483648

def test_lowest_one_bit_zero():
    assert JInteger.lowestOneBit(0) == 0


def test_lowest_one_bit_positive():
    assert JInteger.lowestOneBit(10) == 2


def test_lowest_one_bit_power_of_two():
    assert JInteger.lowestOneBit(16) == 16


def test_lowest_one_bit_negative():
    assert JInteger.lowestOneBit(-1) == 1

def test_number_of_leading_zeros_zero():
    assert JInteger.numberOfLeadingZeros(0) == 32


def test_number_of_leading_zeros_one():
    assert JInteger.numberOfLeadingZeros(1) == 31


def test_number_of_leading_zeros_eight():
    assert JInteger.numberOfLeadingZeros(8) == 28


def test_number_of_leading_zeros_highest_bit_set():
    assert JInteger.numberOfLeadingZeros(-2147483648) == 0

def test_number_of_trailing_zeros_zero():
    assert JInteger.numberOfTrailingZeros(0) == 32


def test_number_of_trailing_zeros_one():
    assert JInteger.numberOfTrailingZeros(1) == 0


def test_number_of_trailing_zeros_two():
    assert JInteger.numberOfTrailingZeros(2) == 1


def test_number_of_trailing_zeros_eight():
    assert JInteger.numberOfTrailingZeros(8) == 3
