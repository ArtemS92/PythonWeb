# Напишите программу, которая получает целое число
# и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.


def hex_num(num: int, mod: int = 16):
    result = ''
    while num != 0:
        temp = num % mod if (num % mod) < 10 else chr(num % mod + 55)
        result = str(temp) + result
        num //= mod
    result = "0x" + result
    return result


print(hex_num(1515))
print(hex(1515))
