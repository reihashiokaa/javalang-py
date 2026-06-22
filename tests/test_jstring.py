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


def test_jstring_code_point_at_returns_ascii_code_point():
    value = JString("abc")

    assert value.codePointAt(0) == ord("a")
    assert value.codePointAt(1) == ord("b")


def test_jstring_code_point_at_returns_unicode_code_point():
    value = JString("ação")

    assert value.codePointAt(0) == ord("a")
    assert value.codePointAt(1) == ord("ç")


def test_jstring_code_point_at_rejects_invalid_index():
    value = JString("abc")

    with pytest.raises(IndexError):
        value.codePointAt(-1)

    with pytest.raises(IndexError):
        value.codePointAt(3)


def test_jstring_code_point_at_rejects_non_integer_index():
    value = JString("abc")

    with pytest.raises(TypeError):
        value.codePointAt("1")


def test_jstring_code_point_before_returns_ascii_code_point():
    value = JString("abc")

    assert value.codePointBefore(1) == ord("a")
    assert value.codePointBefore(3) == ord("c")


def test_jstring_code_point_before_returns_unicode_code_point():
    value = JString("ação")

    assert value.codePointBefore(2) == ord("ç")
    assert value.codePointBefore(4) == ord("o")


def test_jstring_code_point_before_rejects_invalid_index():
    value = JString("abc")

    with pytest.raises(IndexError):
        value.codePointBefore(0)

    with pytest.raises(IndexError):
        value.codePointBefore(4)


def test_jstring_code_point_before_rejects_non_integer_index():
    value = JString("abc")

    with pytest.raises(TypeError):
        value.codePointBefore("1")


def test_jstring_code_point_count_returns_ascii_count():
    value = JString("abcdef")

    assert value.codePointCount(0, 3) == 3
    assert value.codePointCount(2, 6) == 4


def test_jstring_code_point_count_returns_unicode_count():
    value = JString("ação")

    assert value.codePointCount(0, 4) == 4
    assert value.codePointCount(1, 3) == 2


def test_jstring_code_point_count_allows_empty_range():
    value = JString("abc")

    assert value.codePointCount(1, 1) == 0


def test_jstring_code_point_count_rejects_invalid_range():
    value = JString("abc")

    with pytest.raises(IndexError):
        value.codePointCount(-1, 2)

    with pytest.raises(IndexError):
        value.codePointCount(2, 1)

    with pytest.raises(IndexError):
        value.codePointCount(0, 4)


def test_jstring_code_point_count_rejects_non_integer_indexes():
    value = JString("abc")

    with pytest.raises(TypeError):
        value.codePointCount("0", 2)


def test_jstring_offset_by_code_points_moves_forward():
    value = JString("abcdef")

    assert value.offsetByCodePoints(1, 3) == 4


def test_jstring_offset_by_code_points_moves_backward():
    value = JString("abcdef")

    assert value.offsetByCodePoints(4, -2) == 2


def test_jstring_offset_by_code_points_works_with_unicode():
    value = JString("ação")

    assert value.offsetByCodePoints(0, 2) == 2
    assert value.offsetByCodePoints(3, -2) == 1


def test_jstring_offset_by_code_points_allows_length_index():
    value = JString("abc")

    assert value.offsetByCodePoints(3, 0) == 3


def test_jstring_offset_by_code_points_rejects_invalid_result():
    value = JString("abc")

    with pytest.raises(IndexError):
        value.offsetByCodePoints(0, -1)

    with pytest.raises(IndexError):
        value.offsetByCodePoints(2, 2)


def test_jstring_offset_by_code_points_rejects_non_integer_values():
    value = JString("abc")

    with pytest.raises(TypeError):
        value.offsetByCodePoints("0", 1)

    with pytest.raises(TypeError):
        value.offsetByCodePoints(0, "1")


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


def test_contains_present():
    assert JString("hello world").contains("world")


def test_contains_absent():
    assert not JString("hello world").contains("python")


def test_starts_with():
    assert JString("hello").startsWith("he")


def test_starts_with_offset():
    assert JString("hello").startsWith("ll", 2)


def test_starts_with_invalid_offset():
    assert not JString("hello").startsWith("he", 10)


def test_ends_with():
    assert JString("hello").endsWith("lo")


def test_ends_with_false():
    assert not JString("hello").endsWith("he")


def test_region_matches():
    assert JString("abcdef").regionMatches(
        2,
        JString("xxcdeyy"),
        2,
        3,
    )


def test_region_matches_ignore_case():
    assert JString("ABCDEF").regionMatches(
        True,
        2,
        JString("xxcdeyy"),
        2,
        3,
    )


def test_region_matches_false():
    assert not JString("abcdef").regionMatches(
        2,
        JString("xxxyz"),
        2,
        3,
    )


def test_jstring_value_of_positive_integer():
    result = JString.valueOf(10)

    assert isinstance(result, JString)
    assert result._value == "10"


def test_jstring_value_of_negative_integer():
    result = JString.valueOf(-5)

    assert result._value == "-5"


def test_jstring_value_of_zero_integer():
    result = JString.valueOf(0)

    assert result._value == "0"


def test_jstring_value_of_float():
    result = JString.valueOf(10.5)

    assert isinstance(result, JString)
    assert result._value == "10.5"


def test_jstring_value_of_negative_float():
    result = JString.valueOf(-2.5)

    assert result._value == "-2.5"


def test_jstring_value_of_boolean_true():
    result = JString.valueOf(True)

    assert result._value == "true"


def test_jstring_value_of_boolean_false():
    result = JString.valueOf(False)

    assert result._value == "false"


def test_jstring_value_of_char():
    result = JString.valueOf("a")

    assert result._value == "a"


def test_jstring_value_of_string_text():
    result = JString.valueOf("abc")

    assert result._value == "abc"


def test_jstring_value_of_character_list():
    result = JString.valueOf(["a", "b", "c"])

    assert isinstance(result, JString)
    assert result._value == "abc"


def test_jstring_value_of_character_tuple():
    result = JString.valueOf(("a", "b", "c"))

    assert result._value == "abc"


def test_jstring_value_of_rejects_invalid_character_list():
    with pytest.raises(ValueError):
        JString.valueOf(["a", "bc"])


def test_index_of_character_returns_first_occurrence():
    value = JString("banana")

    assert value.indexOf(ord("a")) == 1


def test_index_of_character_returns_minus_one_when_not_found():
    value = JString("banana")

    assert value.indexOf(ord("x")) == -1


def test_index_of_character_uses_start_index():
    value = JString("banana")

    assert value.indexOf(ord("a"), 2) == 3


def test_index_of_character_negative_start_index_starts_from_zero():
    value = JString("banana")

    assert value.indexOf(ord("b"), -5) == 0


def test_index_of_character_start_index_greater_than_length_returns_minus_one():
    value = JString("banana")

    assert value.indexOf(ord("a"), 20) == -1


def test_index_of_character_rejects_invalid_start_index_type():
    value = JString("banana")

    with pytest.raises(TypeError):
        value.indexOf(ord("a"), "1")


def test_index_of_character_rejects_invalid_value_type():
    value = JString("banana")

    with pytest.raises(TypeError):
        value.indexOf(1.5)


def test_index_of_substring_returns_first_occurrence():
    value = JString("banana")

    assert value.indexOf("na") == 2


def test_index_of_substring_returns_minus_one_when_not_found():
    value = JString("banana")

    assert value.indexOf("xy") == -1


def test_index_of_substring_uses_start_index():
    value = JString("banana")

    assert value.indexOf("na", 3) == 4


def test_index_of_substring_accepts_jstring_value():
    value = JString("banana")

    assert value.indexOf(JString("na")) == 2


def test_index_of_substring_empty_string_returns_start_index():
    value = JString("banana")

    assert value.indexOf("", 3) == 3


class SampleObject:
    def __str__(self):
        return "sample-object"


def test_jstring_value_of_accepts_generic_object():
    result = JString.valueOf(SampleObject())

    assert isinstance(result, JString)
    assert result._value == "sample-object"


def test_jstring_value_of_none_returns_null_text():
    result = JString.valueOf(None)

    assert isinstance(result, JString)
    assert result._value == "null"


def test_jstring_copy_value_of_creates_string_from_character_list():
    result = JString.copyValueOf(["a", "b", "c"])

    assert isinstance(result, JString)
    assert result._value == "abc"


def test_jstring_copy_value_of_rejects_invalid_character_list():
    with pytest.raises(ValueError):
        JString.copyValueOf(["a", "bc"])


def test_jstring_format_with_string_argument():
    result = JString.format("Hello, %s", "World")

    assert isinstance(result, JString)
    assert result._value == "Hello, World"


def test_jstring_format_with_number_argument():
    result = JString.format("Value: %d", 10)

    assert isinstance(result, JString)
    assert result._value == "Value: 10"


def test_jstring_format_without_arguments_returns_original_text():
    result = JString.format("No arguments")

    assert isinstance(result, JString)
    assert result._value == "No arguments"


def test_jstring_format_rejects_invalid_format_string_type():
    with pytest.raises(TypeError):
        JString.format(123, "abc")


def test_jstring_format_rejects_invalid_arguments():
    with pytest.raises(ValueError):
        JString.format("Value: %d", "abc")


def test_jstring_join_with_python_strings():
    result = JString.join(", ", "a", "b", "c")

    assert isinstance(result, JString)
    assert result._value == "a, b, c"


def test_jstring_join_with_list_of_strings():
    result = JString.join("-", ["a", "b", "c"])

    assert isinstance(result, JString)
    assert result._value == "a-b-c"


def test_jstring_join_accepts_jstring_delimiter_and_elements():
    result = JString.join(JString("-"), JString("a"), JString("b"))

    assert isinstance(result, JString)
    assert result._value == "a-b"


def test_jstring_join_rejects_invalid_delimiter():
    with pytest.raises(TypeError):
        JString.join(123, "a", "b")


def test_jstring_join_rejects_invalid_element():
    with pytest.raises(TypeError):
        JString.join("-", "a", 123)
