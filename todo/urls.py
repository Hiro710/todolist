from django.urls import path
# 呼び出す際のファイル場所を指示する(views.pyファイル内)
from .views import TodoList, TodoDetail, TodoCreate, TodoDelete, TodoUpdate

urlpatterns = [
    # nameでurlパターンに応じてviewに名前を付ける(関連付け)
    path('list/', TodoList.as_view(), name = 'list'),
    # <int:pk>でデータの各ID(primary_key)を持ってくる(指定してあげる)
    path('detail/<int:pk>', TodoDetail.as_view(), name = 'detail'),
    path('create/', TodoCreate.as_view(), name = 'create'),
    # 削除するデータを指定するため、urlに必ずID(primary_key)を指定する
    path('delete/<int:pk>', TodoDelete.as_view(), name = 'delete'),
    # 更新するデータを指定するため、urlに必ずID(primary_key)を指定する
    path('update/<int:pk>', TodoUpdate.as_view(), name = 'update'),
]
