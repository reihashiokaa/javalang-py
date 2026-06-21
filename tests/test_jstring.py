import pytest

from javalang import JString


def test_jstring_length_returns_number_of_characters():
    value = JString("abc")

    assert value.length() == 3

def test_jstring_length_returns_zero_for_empty_string():
    value = JString()

    assert value.length() == 0

def test_jstring_is_empty_returns_true_for_empty_string():
    value = JString()

    assert value.isEmpty() is True

def test_jstring_is_empty_returns_false_for_non_empty_string():
    value = JString("abc")

    assert value.isEmpty() is False

def test_jstring_char_at_returns_character_at_index():
    value = JString("abc")

    assert value.charAt(1) == "b"

def test_jstring_char_at_rejects_negative_index():
    value = JString("abc")

    with pytest.raises(IndexError):
        value.charAt(-1)

def test_jstring_char_at_rejects_index_out_of_range():
    value = JString("abc")

    with pytest.raises(IndexError):
        value.charAt(3)

def test_jstring_char_at_rejects_non_integer_index():
    value = JString("abc")

    with pytest.raises(TypeError):
        value.charAt("1")

def test_jstring_to_char_array_returns_character_list():
    value = JString("abc")

    assert value.toCharArray() == ["a", "b", "c"]

def test_jstring_to_char_array_returns_new_list():
    value = JString("abc")
    characters = value.toCharArray()
    characters[0] = "x"

    assert value._value == "abc"

def test_jstring_get_chars_copies_range_to_destination():
    value = JString("abcdef")
    destination = ["", "", "", "", ""]
    value.getChars(1, 4, destination, 1)

    assert destination == ["", "b", "c", "d", ""]

def test_jstring_get_chars_rejects_invalid_source_range():
    value = JString("abc")
    destination = ["", "", ""]

    with pytest.raises(IndexError):
        value.getChars(2, 5, destination, 0)

def test_jstring_get_chars_rejects_invalid_destination_range():
    value = JString("abc")
    destination = [""]

    with pytest.raises(IndexError):
        value.getChars(0, 3, destination, 0)

def test_jstring_get_chars_rejects_non_list_destination():
    value = JString("abc")

    with pytest.raises(TypeError):
        value.getChars(0, 2, "abc", 0)

def test_jstring_get_bytes_uses_utf8_by_default():
    value = JString("abc")

    assert value.getBytes() == b"abc"

def test_jstring_get_bytes_accepts_charset():
    value = JString("abc")

    assert value.getBytes("utf-8") == b"abc"

def test_jstring_get_bytes_rejects_invalid_charset_type():
    value = JString("abc")

    with pytest.raises(TypeError):
        value.getBytes(123)

def test_jstring_get_bytes_rejects_unknown_charset():
    value = JString("abc")

    with pytest.raises(LookupError):
        value.getBytes("charset-inexistente")

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


def test_compare_to_equal_strings():
    assert JString("abc").compareTo(JString("abc")) == 0


def test_compare_to_smaller_string():
    assert JString("abc").compareTo(JString("abd")) < 0


def test_compare_to_greater_string():
    assert JString("abd").compareTo(JString("abc")) > 0


def test_compare_to_ignore_case():
    assert JString("abc").compareToIgnoreCase(JString("ABC")) == 0


def test_content_equals_jstring():
    assert JString("abc").contentEquals(JString("abc"))


def test_content_equals_string():
    assert JString("abc").contentEquals("abc")


def test_hash_code_equal_strings():
    first = JString("abc")
    second = JString("abc")

    assert first.hashCode() == second.hashCode()


def test_hash_code_different_strings():
    first = JString("abc")
    second = JString("def")

    assert first.hashCode() != second.hashCode()

def test_jstring_substring_from_begin_index():
    value = JString("abcdef")
    result = value.substring(2)

    assert isinstance(result, JString)

    assert result._value == "cdef"

def test_jstring_substring_with_begin_and_end_index():
    value = JString("abcdef")
    result = value.substring(1, 4)

    assert isinstance(result, JString)

    assert result._value == "bcd"

def test_jstring_substring_allows_empty_result():
    value = JString("abcdef")
    result = value.substring(2, 2)

    assert result._value == ""

def test_jstring_substring_rejects_negative_begin_index():
    value = JString("abcdef")

    with pytest.raises(IndexError):
        value.substring(-1)

def test_jstring_substring_rejects_end_before_begin():
    value = JString("abcdef")

    with pytest.raises(IndexError):
        value.substring(4, 2)

def test_jstring_substring_rejects_end_out_of_range():
    value = JString("abcdef")

    with pytest.raises(IndexError):
        value.substring(1, 10)

def test_jstring_substring_rejects_invalid_begin_type():
    value = JString("abcdef")

    with pytest.raises(TypeError):
        value.substring("1")

def test_jstring_substring_rejects_invalid_end_type():
    value = JString("abcdef")

    with pytest.raises(TypeError):
        value.substring(1, "4")

def test_jstring_sub_sequence_returns_substring():
    value = JString("abcdef")
    result = value.subSequence(1, 4)

    assert isinstance(result, JString)

    assert result._value == "bcd"

def test_jstring_concat_accepts_python_string():
    value = JString("abc")
    result = value.concat("def")

    assert isinstance(result, JString)

    assert result._value == "abcdef"

def test_jstring_concat_accepts_jstring():
    value = JString("abc")
    other = JString("def")
    result = value.concat(other)

    assert isinstance(result, JString)

    assert result._value == "abcdef"

def test_jstring_concat_does_not_change_original_value():
    value = JString("abc")
    result = value.concat("def")

    assert value._value == "abc"

    assert result._value == "abcdef"

def test_jstring_concat_rejects_invalid_type():
    value = JString("abc")

    with pytest.raises(TypeError):
        value.concat(123)

def test_jstring_trim_removes_spaces_from_edges():
    value = JString(" abc ")
    result = value.trim()

    assert isinstance(result, JString)

    assert result._value == "abc"

def test_jstring_trim_does_not_change_original_value():
    value = JString(" abc ")
    result = value.trim()

    assert value._value == " abc "

    assert result._value == "abc"

def test_jstring_trim_keeps_internal_spaces():
    value = JString(" a b c ")
    result = value.trim()

    assert result._value == "a b c"

def test_jstring_intern_returns_same_instance():
    value = JString("abc")
    
    assert value.intern() is value