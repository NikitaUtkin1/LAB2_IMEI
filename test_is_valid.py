import unittest
from regex_logic import is_valid_imei


class TestIsValidIMEI(unittest.TestCase):

    def test_valid_plain(self):
        """Проверка обычного слитного IMEI (15 цифр)."""
        self.assertTrue(is_valid_imei("123456789012345"))

    def test_valid_with_separators(self):
        """Проверка IMEI с пробелами и дефисами."""
        self.assertTrue(is_valid_imei("12-345678-901234-5"))
        self.assertTrue(is_valid_imei("12 345678 901234 5"))

    def test_valid_with_edges_spaces(self):
        """Проверка, что случайные пробелы по краям не ломают номер."""
        self.assertTrue(is_valid_imei(" 123456789012345 "))

    def test_invalid_too_short(self):
        """Ошибка: слишком короткий (14 цифр)."""
        self.assertFalse(is_valid_imei("12345678901234"))

    def test_invalid_too_long(self):
        """Ошибка: слишком длинный (16 цифр)."""
        self.assertFalse(is_valid_imei("1234567890123456"))

    def test_invalid_with_letters(self):
        """Ошибка: содержит буквы."""
        self.assertFalse(is_valid_imei("12345678901234A"))
        self.assertFalse(is_valid_imei("A23456789012345"))

    def test_invalid_empty(self):
        """Ошибка: пустая строка."""
        self.assertFalse(is_valid_imei(""))

    def test_invalid_trailing_dash(self):
        """Ошибка: дефис в конце (номер обрезан)."""
        self.assertFalse(is_valid_imei("123456789012345-"))

if __name__ == "__main__":
    unittest.main()