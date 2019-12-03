from django.contrib import admin
# 設定したモデルがある場所を設定
# パスは同じディレクトリ内なので.とする
from .models import TodoModel

# Register your models here.

# adminでデータを扱っていくコマンドを定義する
# models.pyで定義したモデル名を設定
admin.site.register(TodoModel)