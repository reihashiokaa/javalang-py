import math

import pytest

from javalang import JFloat


def test_jfloat_can_be_created_with_default_value():
    value = JFloat()

    assert value._value == 0.0


def test_jfloat_can_store_float_value():
    value = JFloat(10.5)

    assert value._value == 10.5


def test_jfloat_infinity_constants():
    assert math.isinf(JFloat.POSITIVE_INFINITY)
    assert JFloat.POSITIVE_INFINITY > 0
    assert math.isinf(JFloat.NEGATIVE_INFINITY)
    assert JFloat.NEGATIVE_INFINITY < 0


def test_jfloat_nan_constant():
    assert math.isnan(JFloat.NaN)


def test_jfloat_size_and_bytes_match_java_float():
    assert JFloat.SIZE == 32
    assert JFloat.BYTES == 4
    assert JFloat.SIZE == JFloat.BYTES * 8


def test_jfloat_type_uses_python_float_as_adaptation():
    assert JFloat.TYPE is float

def test_jfloat_int_value_truncates_decimal_part():
    value = JFloat(10.8)
    assert value.intValue() == 10


def test_jfloat_int_value_truncates_negative_decimal_part():
    value = JFloat(-10.8)
    assert value.intValue() == -10


def test_jfloat_long_value_returns_integer_value():
    value = JFloat(20.5)
    assert value.longValue() == 20

def test_jfloat_float_value_returns_float():
    value = JFloat(10.5)
    assert value.floatValue() == 10.5


def test_jfloat_double_value_returns_float_adaptation():
    value = JFloat(10.5)
    assert value.doubleValue() == 10.5

def test_jfloat_byte_value_with_value_inside_range():
    value = JFloat(10.5)
    assert value.byteValue() == 10


def test_jfloat_short_value_with_value_inside_range():
    value = JFloat(300.9)
    assert value.shortValue() == 300


def test_jfloat_byte_value_wraps_like_signed_byte():
    value = JFloat(130.0)
    assert value.byteValue() == -126


def test_jfloat_short_value_wraps_like_signed_short():
    value = JFloat(32768.0)
    assert value.shortValue() == -32768

def test_parse_float_inteiro():
    assert JFloat.parseFloat("10") == 10.0
 
 
def test_parse_float_decimal():
    assert JFloat.parseFloat("3.14") == pytest.approx(3.14)
 
 
def test_parse_float_negativo():
    assert JFloat.parseFloat("-2.5") == -2.5
 
 
def test_parse_float_zero():
    assert JFloat.parseFloat("0") == 0.0
 
 
def test_parse_float_zero_decimal():
    assert JFloat.parseFloat("0.0") == 0.0
 
 
def test_parse_float_infinity():
    assert JFloat.parseFloat("Infinity") == float("inf")
 
 
def test_parse_float_negative_infinity():
    assert JFloat.parseFloat("-Infinity") == float("-inf")
 
 
def test_parse_float_nan():
    assert math.isnan(JFloat.parseFloat("NaN"))
 
 
def test_parse_float_entrada_invalida():
    with pytest.raises(ValueError):
        JFloat.parseFloat("abc")
 
 
def test_parse_float_entrada_vazia():
    with pytest.raises(ValueError):
        JFloat.parseFloat("")
 
 
def test_parse_float_tipo_errado():
    with pytest.raises(ValueError):
        JFloat.parseFloat(3.14)
 
def test_value_of_float():
    resultado = JFloat.valueOf(3.14)
    assert isinstance(resultado, JFloat)
    assert resultado.floatValue() == pytest.approx(3.14)
 
 
def test_value_of_inteiro():
    resultado = JFloat.valueOf(10)
    assert isinstance(resultado, JFloat)
    assert resultado.floatValue() == 10.0
 
 
def test_value_of_negativo():
    resultado = JFloat.valueOf(-7.5)
    assert isinstance(resultado, JFloat)
    assert resultado.floatValue() == -7.5
 
 
def test_value_of_zero():
    resultado = JFloat.valueOf(0)
    assert isinstance(resultado, JFloat)
    assert resultado.floatValue() == 0.0

def test_value_of_string_decimal():
    resultado = JFloat.valueOf("2.71")
    assert isinstance(resultado, JFloat)
    assert resultado.floatValue() == pytest.approx(2.71)
 
 
def test_value_of_string_negativa():
    resultado = JFloat.valueOf("-1.0")
    assert isinstance(resultado, JFloat)
    assert resultado.floatValue() == -1.0
 
 
def test_value_of_string_invalida():
    with pytest.raises(ValueError):
        JFloat.valueOf("texto")
 
 
def test_value_of_tipo_invalido():
    with pytest.raises(ValueError):
        JFloat.valueOf([1, 2, 3])
