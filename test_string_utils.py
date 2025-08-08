import pytest
from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.positive
def test_capitilize_positive():
    assert string_utils.capitilize("тест") == "Тест"

@pytest.mark.negative
def test_capitilize_negative():
    assert string_utils.capitilize("") == ""

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
