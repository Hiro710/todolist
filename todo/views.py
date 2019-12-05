from django.shortcuts import render
from django.views.generic import ListView
# TodoModelが入っている場所を指示する(ファイルのパス)
from .models import TodoModel

class TodoList(ListView):
    template_name = 'list.html'
    # DBのどのモデルを使うのかを指定する
    model = TodoModel