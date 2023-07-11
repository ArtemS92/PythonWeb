# Напишите однострочный генератор словаря, который принимает на вход три списка
# одинаковой длины: имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

names = ["Андрей", "Владимир", "Михаил", "Сергей"]
salaries = [8_000, 12_000, 22_000, 18_000]
prize_percents = ["10.25%", "15.00%", "6.50%", "12.75%"]


def gen_dict(name: list[str], salary: list[int], percent: list[str]):
    yield {d[0]: d[1] for d in
           list(map(lambda y: (y[0], y[1] * y[2] / 100), zip(name, salary, map(lambda x: float(x[:-1]), percent))))}


print(*gen_dict(names, salaries, prize_percents))
