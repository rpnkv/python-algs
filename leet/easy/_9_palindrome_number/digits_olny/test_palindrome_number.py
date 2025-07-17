import pytest

# from easy._9_palindrome_number.digits_olny import palindrome_number
from palindrome_number import get_digit, is_palindrome, define_num_length


class TestAuxiliary:
    @pytest.mark.parametrize(
        argnames=["number", "position", "expected_positioned_value"],
        argvalues=[
            (12345, 0, 5),
            (12345, 1, 4),
            (12345, 2, 3),
            (12345, 3, 2),
            (12345, 4, 1),
        ]
    )
    def test_get_digits(self, number, position, expected_positioned_value):
        assert get_digit(number, position) == expected_positioned_value

    @pytest.mark.parametrize(
        argnames=["number", "expected_length"],
        argvalues=[
            (1, 1),
            (12, 2),
            (123, 3),
            (1234, 4),
        ]
    )
    def test_define_num_length(self, number, expected_length):
        assert define_num_length(number) == expected_length


class TestFull:
    @pytest.mark.parametrize(
        argnames=["number", "expected_response"],
        argvalues=[
            (22, True),
            (-22, False),
            (23, False),
            (24, False),
            (222, True),
            (232, True),
            (2222, True),
            (2332, True),
        ]
    )
    def test_sample(self, number, expected_response):
        assert is_palindrome(number) == expected_response
