from django.shortcuts import render
from django.views.generic import ListView, DetailView
# TodoModelが入っている場所を指示する(ファイルのパス)
from .models import TodoModel

# ListViewはListを表示するための機能が付いている
class TodoList(ListView):
    template_name = 'list.html'
    # DBのどのモデルを使うのかを指定する
    model = TodoModel

# DetailViewはpkというものをURLに付けることによって、
# 一個一個のデータを取得してそれを表示する機能が付いている
class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel