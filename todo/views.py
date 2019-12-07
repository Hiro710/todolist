from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
# TodoModelが入っている場所を指示する(ファイルのパス)
from .models import TodoModel
# reverse_lazy('')が入っている場所を指示する
from django.urls import reverse_lazy

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

class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    # formでフォームを表示する際はfieldsを使ってどのモデルのデータを持ってくるのか指定する
    fields = ('title', 'memo', 'priority', 'duedate')
    # データの作成が完了した時のリダイレクト先を指定する(必須)
    # reverse_lazy('')はclassの中で指定する際に使用する
    # urls.pyでnameを使って指定したものをviewと関連付ける
    success_url = reverse_lazy('list')

class TodoDelete(DeleteView):
    template_name = 'delete.html'
    # どのモデルのデータを削除するのかを指定する
    model = TodoModel
    # 削除が完了したらどのページに飛ぶのかを必ず指定
    success_url = reverse_lazy('list')