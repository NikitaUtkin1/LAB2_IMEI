from regex_logic import is_valid_imei
from data_parser import read_from_file, read_from_url
from exceptions import IMEIFileError, IMEIWebError


def main():
    print(" ПРОГРАММА ПОИСКА IMEI ")

    while True:
        print("\nВыберите действие:")
        print("1. Проверить один IMEI вручную")
        print("2. Найти IMEI в текстовом файле")
        print("3. Найти IMEI на веб-странице")
        print("0. Выход")

        choice = input("\nВаш выбор: ")

        if choice == "1":
            imei = input("Введите IMEI для проверки: ")
            if is_valid_imei(imei):
                print(" Это корректный IMEI!")
            else:
                print(" Ошибка! Некорректный IMEI.")

        elif choice == "2":
            filepath = input("Введите путь к файлу (например, test.txt): ")
            print("Ищем...")
            try:
                results = read_from_file(filepath)
                if results:
                    print(f"Найдено {len(results)} IMEI:")
                    for num in results:
                        print(f" - {num}")
                else:
                    print("IMEI не найдены (файл пуст или нет номеров).")
            except IMEIFileError as e:
                print(f" Ошибка: {e}")

        elif choice == "3":
            url = input("Введите URL сайта (например, https://example.com): ")
            print("Загружаем страницу и ищем...")
            try:
                results = read_from_url(url)
                if results:
                    print(f"Найдено {len(results)} IMEI:")
                    for num in results:
                        print(f" - {num}")
                else:
                    print("IMEI не найдены на этой странице.")
            except IMEIWebError as e:
                print(f" Ошибка: {e}")

        elif choice == "0":
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()