from unittest import TestCase
import palindrome_number


class TestAuxiliary(TestCase):
    def test_threshold_2(self):
        self.assertEqual(
            palindrome_number.threshold(2),
            1,
        )

    def test_threshold_3(self):
        self.assertEqual(
            palindrome_number.threshold(3),
            1,
        )

    def test_threshold_4(self):
        self.assertEqual(
            palindrome_number.threshold(4),
            2,
        )

    def test_threshold_5(self):
        self.assertEqual(
            palindrome_number.threshold(5),
            2,
        )

    def test_mirror_index_odd_0(self):
        self.assertEqual(
            palindrome_number.mirror_index(0, 5),
            4
        )

    def test_mirror_index_odd_1(self):
        self.assertEqual(
            palindrome_number.mirror_index(1, 5),
            3
        )

    def test_mirror_index_even_0(self):
        self.assertEqual(
            palindrome_number.mirror_index(0, 4),
            3
        )

    def test_mirror_index_even_1(self):
        self.assertEqual(
            palindrome_number.mirror_index(1, 4),
            2
        )


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
