from django.urls import path
# 呼び出す際のファイル場所を指示する
from .views import TodoList

urlpatterns = [
    path('list/', TodoList.as_view()),
]
