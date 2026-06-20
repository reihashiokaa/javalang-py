import math

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