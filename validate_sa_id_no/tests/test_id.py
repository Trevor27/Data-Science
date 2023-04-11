import pytest

from validate_sa_id import validate_id


@pytest.mark.parametrize(
    "id_length, expected", [("2001014800086", True), ("200101480008", False)]
)
def test_validate_length_of_id(id_length, expected):
    assert (
        validate_id.length(id_length) == expected
    ), "This ID number does not contain 13 digits"


@pytest.mark.parametrize(
    "digits, expected", [("2001014800086", True), ("20a1014800086", False)]
)
def test_validate_digits(digits, expected):
    assert (
        validate_id.check_if_digits(digits) == expected
    ), "This ID number does not contain 13 digits"


@pytest.mark.parametrize(
    "constant, expected", [("2001014800086", True), ("2001014800076", False)]
)
def test_validate_constant(constant, expected):
    assert (
        validate_id.constant(constant) == expected
    ), "The constant number is not equal to 8"


@pytest.mark.parametrize(
    "birth_date, expected", [("2001014800086", True), ("2001324800086", False)]
)
def test_validate_check_date_of_birth(birth_date, expected):
    assert (
        validate_id.check_date_of_birth(birth_date) == expected
    ), "date of birth is out of range"


@pytest.mark.parametrize(
    "gender, expected", [("2001014800086", True), ("200101000086", False)]
)
def test_validate_gender(gender, expected):
    assert validate_id.gender(gender) == expected, "gender cannot be identified"


@pytest.mark.parametrize(
    "citizenship, expected", [("2001014800086", True), ("2001014800286", False)]
)
def test_validate_citizenship(citizenship, expected):
    assert validate_id.citizenship(citizenship) == expected, "citizenship is invalid"


@pytest.mark.parametrize(
    "luhn_algorithm, expected", [("2001014800086", True), ("2001014800089", False)]
)
def test_validate_checksum(luhn_algorithm, expected):
    assert validate_id.checksum(luhn_algorithm) == expected, "luhn algorithm has failed"
