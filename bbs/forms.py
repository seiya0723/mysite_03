from django import forms

from .models import Topic


#TODO:モデルを継承したフォームクラスを作る
#https://noauto-nolife.com/post/django-forms-validate/

class TopicForm(forms.ModelForm):
    #継承対象のモデルと、バリデーションをするモデル内のフィールドの指定
    class Meta:
        model   = Topic
        fields  = [ "comment" ]

