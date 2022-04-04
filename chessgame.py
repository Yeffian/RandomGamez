import chess


def get_move_str(board):
    if board.turn:
        return "White"
    else:
        return "Black"


print('Welcome to Console Chess!')

board = chess.Board()

while not board.is_checkmate():
    move = input(f'{get_move_str(board)} moves: ')

    if move == 'resign':
        print(f'{get_move_str(board)} resigns!')
        print('Game FEN, in case you want to inspect it:')
        print(board.fen())
        break

    try:
        board.push_san(move)
    except ValueError:
        print('Invalid move, try again!')
        continue

    if board.is_checkmate():
        print(f'{get_move_str(board)} king is in checkmate, game over!')
        print('Game FEN, in case you want to inspect it:')
        print(board.fen())
        break
    elif board.is_check():
        print(f'{get_move_str(board)} king is in check!')

    print(board)
