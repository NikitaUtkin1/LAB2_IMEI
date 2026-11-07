import unittest
from regex_logic import find_imei_in_text


class TestFindIMEI(unittest.TestCase):

    def test_find_single(self):
        """Поиск одного IMEI в тексте."""
        text = "Мой IMEI: 123456789012345."
        self.assertEqual(find_imei_in_text(text), ["123456789012345"])

    def test_find_multiple_and_clean(self):
        """Поиск нескольких IMEI и их очистка от разделителей."""
        text = "Номера: 123456789012345, 12-345678-901234-5, 12 345678 901234 5."
        expected = ["123456789012345", "123456789012345", "123456789012345"]
        self.assertEqual(find_imei_in_text(text), expected)

    def test_find_does_not_catch_long_numbers(self):
        """Проверка, что не находим 15 цифр внутри длинного числа."""
        text = "Длинный заказ: 98765123456789012345"
        self.assertEqual(find_imei_in_text(text), [])

    def test_find_nothing(self):
        """Поиск в тексте, где нет IMEI."""
        text = "Здесь просто текст без номеров."
        self.assertEqual(find_imei_in_text(text), [])

if __name__ == "__main__":
    unittest.main()