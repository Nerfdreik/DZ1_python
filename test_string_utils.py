import pytest
from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.positive
def test_capitalize_positive():
    assert string_utils.capitalize("тест") == "Тест"

@pytest.mark.negative
def test_capitalize_negative():
    assert string_utils.capitalize("") == ""

@pytest.mark.positive
def test_trim_positive():
    assert string_utils.trim("   04 апреля 2023") == "04 апреля 2023"

@pytest.mark.negative
def test_trim_negative():
    assert string_utils.trim("   ") == ""

@pytest.mark.positive
def test_to_list_positive():
    assert string_utils.to_list("1,2,3", ",") == ["1", "2", "3"]

@pytest.mark.negative
def test_to_list_negative():
    assert string_utils.to_list("", ",") == ['']

@pytest.mark.positive
def test_contains_positive():
    assert string_utils.contains("04 апреля 2023", "апреля") is True

@pytest.mark.negative
def test_contains_negative():
    assert string_utils.contains("", "a") is False

@pytest.mark.positive
def test_delele_symbol_positive():
    assert string_utils.delete_symbol("04 апреля 2023", " ") == "04апреля2023"

@pytest.mark.negative
def test_delete_symbol_negative():
    assert string_utils.delete_symbol("", "a") == ""
