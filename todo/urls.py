from django.urls import path
# 呼び出す際のファイル場所を指示する
from .views import TodoList, TodoDetail

urlpatterns = [
    path('list/', TodoList.as_view()),
    # <int:pk>でデータの各ID(primary_key)を持ってくる(指定してあげる)
    path('detail/<int:pk>', TodoDetail.as_view()),
]
