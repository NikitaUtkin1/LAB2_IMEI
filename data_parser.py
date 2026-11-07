import requests
from regex_logic import find_imei_in_text
from exceptions import IMEIFileError, IMEIWebError


def read_from_file(filepath: str) -> list:
    """Читает файл и ищет в нем IMEI."""
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
            return find_imei_in_text(content)
    except FileNotFoundError:
        raise IMEIFileError(f"Файл {filepath} не найден.")


def read_from_url(url: str) -> list:
    """Скачивает страницу по URL и ищет на ней IMEI."""
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return find_imei_in_text(response.text)

    except requests.exceptions.RequestException as e:
        raise IMEIWebError(f"Ошибка при запросе к сайту: {e}")