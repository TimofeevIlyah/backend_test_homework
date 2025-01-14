from gameparts import Board
from gameparts.exceptions import CellOccupiedError, FieldIndexError


def main():
    """Игра Крестики-Нолики"""
    game = Board()
    current_player = 'X'
    running = True
    game.display()
    # game.save_results('test')
    # return

    while running:
        print(f'Ход делает {current_player}')

        while True:
            try:
                row = int(input('Введите номер строки: '))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.field_size:
                    raise FieldIndexError
                if game.board[row][column] != ' ':
                    raise CellOccupiedError
            except FieldIndexError:
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}'
                )
                print('Введите значения заново')
                continue
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print('Введите значения заново')
                continue
            except CellOccupiedError:
                print('Ячейка занята')
                print('Введите значения заново')
                continue
            except Exception as e:
                print(f'Возникла ошибка {e}')
                continue
            else:
                break

        game.make_move(row, column, current_player)
        game.display()
        if game.check_win(current_player):
            result = f'Победили {current_player}'
            print(result)
            game.save_results(result)
            running = False
        elif game.is_board_full():
            result = 'Ничья!'
            print(result)
            game.save_results(result)
            running = False

        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()
