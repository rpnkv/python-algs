from unittest import TestCase
import palindrome_number


class TestFull(TestCase):
    def test_sample_1(self):
        self.assertTrue(
            palindrome_number.is_palindrome(0),
            "True expected for palindrome '0'"
        )

    def test_sample_2(self):
        self.assertTrue(
            palindrome_number.is_palindrome(121),
            "True expected for palindrome '121'"
        )

    def test_sample_3(self):
        self.assertFalse(
            palindrome_number.is_palindrome(-121),
            "False expected for non-palindrome '-121'"
        )

    def test_sample_4(self):
        self.assertFalse(
            palindrome_number.is_palindrome(10),
            "False expected for non-palindrome '10'"
        )
