# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
from typing import Tuple

# Имена файлов для отображения
abs_path = "d:\\path1\\sub_path1\\file_1.png"


def split_path(path: str) -> tuple[str, str, str]:
    """Парсинг абсолютного пути на каталог, имя и расширение файла"""
    path_only, _, file_name = path.rpartition('\\')
    file_name, _, file_ext = file_name.rpartition('.')
    return path_only, file_name, file_ext


print(split_path(abs_path))
