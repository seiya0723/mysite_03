from django.contrib import admin

#管理サイトで操作したいモデルをimportする。
from .models import Topic

# Register your models here.
#TODO:ここに管理サイトで操作したいモデルを登録する
admin.site.register(Topic)


#TODO:下記コマンドで管理ユーザーを追加する
# python3 manage.py createsuperuser
