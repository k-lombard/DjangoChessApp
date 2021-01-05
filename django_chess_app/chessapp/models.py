from django.db import models
from django.utils import timezone

# Create your models here.


class User(models.Model):
    Email= models.EmailField(primary_key=True)
    Date_Joined=models.DateTimeField(default=timezone.now)
    Password = models.TextField(default='')

    def __str__(self):
        return self.Email

class Board(models.Model):
    ID = models.IntegerField(primary_key=True)
    Latest_Board = models.TextField(default='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
    def __str__(self):
        return self.Latest_Board

class Move(models.Model):
    ID = models.IntegerField(primary_key=True)
    Latest_Move = models.TextField(default="")
    def __str__(self):
        return self.Latest_Move