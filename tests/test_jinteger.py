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