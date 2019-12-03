from django.contrib import admin
# includeメソッドを追加
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 何もURLを記述しない場合の挙動はrootページ(home画面)となる
    # つまり、todoアプリを呼び出す
    path('', include('todo.urls')),
]
