from django.shortcuts import render
import chess
import chess.svg
from django.core.exceptions import ValidationError

# Create your views here.
board = chess.Board()
def index(request):
    global board
    if request.method == "POST":
       
        
        move = request.POST.get('move')
        try:
            the_move = chess.Move.from_uci(move)
        except:
            raise(ValueError)
        
        
        # if board.fullmove_number % 2 == 0 and board.turn == chess.BLACK:
        #     board.turn = chess.WHITE
        # elif board.fullmove_number == 1:
        #     board.turn = chess.WHITE
        # else:
        #     board.turn = chess.BLACK
        
        legal = board.legal_moves

        if the_move in legal:
            board.push(the_move)
        else:
            raise ValidationError(
                    ('Invalid value: %(the_move)s'),
                    code='invalid'
                )
        
        
        
        new_board = chess.svg.board(size=500, board = board)
        context = {
        "new_board" : new_board
        }
        board.turn
        request.session['board'] = board.fen()
        
        return render(request, 'chessapp/index.html', context)
    request.session.flush()
    if 'board' not in request.session:
        request.session['board'] = chess.STARTING_FEN
        board = chess.Board()
        board.clear_stack()
        board.set_fen(chess.STARTING_FEN)

    str_board = request.session.get('board')
    board.set_fen(str_board)

    new_board = chess.svg.board(size=500, board = board)
    context = {
        "new_board" : new_board
    }
    
    request.session['board'] = board.fen()
    return render(request, 'chessapp/index.html', context)




