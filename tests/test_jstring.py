import pytest

from javalang import JString


def test_jstring_can_be_created_empty():
    value = JString()

    assert value._value == ""


def test_jstring_can_be_created_from_string():
    value = JString("abc")

    assert value._value == "abc"


def test_jstring_can_be_created_from_jstring():
    original = JString("abc")

    value = JString(original)

    assert value._value == "abc"
    assert value is not original


def test_jstring_can_be_created_from_character_list():
    value = JString(["a", "b", "c"])

    assert value._value == "abc"


def test_jstring_can_be_created_from_character_tuple():
    value = JString(("a", "b", "c"))

    assert value._value == "abc"


def test_jstring_can_be_created_from_character_list_with_offset_and_count():
    value = JString(["a", "b", "c", "d"], 1, 2)

    assert value._value == "bc"


def test_jstring_rejects_character_list_with_invalid_element():
    with pytest.raises(ValueError):
        JString(["a", "bc"])


def test_jstring_rejects_invalid_range():
    with pytest.raises(IndexError):
        JString(["a", "b", "c"], 2, 5)


def test_jstring_rejects_range_with_string_value():
    with pytest.raises(TypeError):
        JString("abc", 1, 2)


def test_jstring_rejects_invalid_type():
    with pytest.raises(TypeError):
        JString(123)

def test_equals_returns_true_for_equal_strings():
    assert JString("abc").equals(JString("abc"))


def test_equals_returns_false_for_different_strings():
    assert not JString("abc").equals(JString("def"))


def test_equals_ignore_case_returns_true():
    assert JString("abc").equalsIgnoreCase(JString("ABC"))