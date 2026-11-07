import re


def is_valid_imei(text: str) -> bool:
    """Проверяет корректность IMEI."""
    text = text.strip()
    # Регулярка: 15 цифр, между которыми могут быть пробелы или дефисы
    pattern = r"^(\d[\s-]?){14}\d$"
    return bool(re.fullmatch(pattern, text))


def find_imei_in_text(text: str) -> list:
    """Ищет все IMEI в тексте и возвращает список чистых номеров."""
    pattern = r"\b(?:\d[\s-]?){14}\d\b"
    matches = re.findall(pattern, text)

    clean_imeis = []
    for match in matches:
        # Убираем всё, кроме цифр
        clean_imeis.append(re.sub(r"\D", "", match))

    return clean_imeis
