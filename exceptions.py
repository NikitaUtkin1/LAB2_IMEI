class IMEIFileError(Exception):
    """Собственное исключение для ошибок чтения файла."""
    pass


class IMEIWebError(Exception):
    """Собственное исключение для ошибок загрузки веб-страницы."""
    pass