from django.db import models

# Create your models here.

# Modelクラスを継承
class TodoModel(models.Model):
    # CharField()を使う際は必ずmax_lengthで文字の長さを指定する
    # タイトルに使う場合はCharField()
    title = models.CharField(max_length=100)
    # タイトルよりも長い文章を扱う場合はTextField()
    memo = models.TextField()
    # __str__という特殊メソッドを使ってadmin画面のタイトルを個別のタイトルが表示されるようにする
    # selfを使ってそのオブジェクト自身のタイトルを返すようにする
    def __str__(self):
        return self.title