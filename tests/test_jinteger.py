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
