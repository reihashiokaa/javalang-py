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