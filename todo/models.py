from django.db import models


# 優先度の選択肢をタプル型で記述
PRIORITY = (('danger', 'high'), ('info', 'normal'), ('success', 'low'))
# Modelクラスを継承
class TodoModel(models.Model):
    # CharField()を使う際は必ずmax_lengthで文字の長さを指定する
    # タイトルに使う場合はCharField()
    title = models.CharField(max_length = 100)
    # タイトルよりも長い文章を扱う場合はTextField()
    memo = models.TextField()
    # 優先度を変える項目の管理をするモデルを追加
    priority = models.CharField(
        max_length = 50,
        choices = PRIORITY
    )
    # 期日を管理するモデルを追加
    duedate = models.DateField()

    # __str__という特殊メソッドを使ってadmin画面のタイトルを個別のタイトルが表示されるようにする
    # selfを使ってそのオブジェクト自身のタイトルを返すようにする
    def __str__(self):
        return self.title