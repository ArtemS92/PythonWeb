from Chess.chess_queen import successful_position, is_queen_beat

print(is_queen_beat([[1, 1], [5, 2], [8, 3], [6, 4], [3, 5], [7, 6], [2, 7],
                     [4, 8]]))  # функция определяет успешно или нет расставлены ферзи на доске 8*8
successful_position(4)  # функция вывода n успешных расстановок ферзей на доске 8*8
