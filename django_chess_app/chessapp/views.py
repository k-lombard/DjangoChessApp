from django.shortcuts import render, redirect
import chess
import chess.svg
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from .models import User
from django.contrib.auth.models import User
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect



# Create your views here.
board = chess.Board()

def index(request):
    context = {}
    if request.user.is_authenticated:
        global board

        if request.method == "POST" and "account_button" in request.POST:
            return redirect('account.html')

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
        #request.session.flush()
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




def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        # user = User.objects.get(Email=email)
        # if user.Password == password:
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('index')
        else:
            return redirect('login')

    return render(request, 'chessapp/login.html')

def signup(request):
    if request.method == 'POST':
        
        email = request.POST['email']
        password = request.POST['password']
        username = request.POST['username']
        user = User.objects.create_user(username, email, password)
        user.save()
        print(user)
        # user = User.objects.get(Email=email)
        # if user.Password == password:
        if user is not None:
            return redirect('login')
        
        else:
            return redirect('signup')
    
    return render(request, 'chessapp/signup.html')



def log_out(request):
    logout(request)
    return redirect('login')


def account_view(request):
    if request.user.is_authenticated: 

        if request.method=='POST':
            return HttpResponseRedirect('chessapp/index.html')
        user = request.user
        email = user.email
        username = user.username
        # date = user.Date_Joined

        context = {'user': request.user, 'email': email, 'username': username}



    return render(request, 'chessapp/account.html', context)










