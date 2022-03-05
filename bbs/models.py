from django.db import models

#settings.pyに書いたTIMEZONEに準拠して日時を記録するためtimezoneをimport
from django.utils import timezone


class Topic(models.Model):

    #models.Modelを継承した時点でここに主キーである、idフィールドが作られている。だからあえてidフィールドを書く必要はない。

    #文字列型で、2000文字まで許容し、入力必須(Null禁止、空文字列禁止)
    comment     = models.CharField(verbose_name="コメント",max_length=2000)

    #DateTimeFieldで日時のフィールド(記録欄)を作る、何も入力がない場合defaultで指定したtimezone.nowを入れる。これで投稿された日時が記録される。
    #新しいフィールドを追加・編集・削除した後はマイグレーションをする。
    dt          = models.DateTimeField(verbose_name="投稿日時", default=timezone.now)


    #TODO:後に投稿日時、投稿者の名前、画像、などの入力を受け付けるフィールドを追加する。
    #このようにnull禁止、default無しのフィールドを新たに追加した時、『You are trying to add a non-nullable field』という警告文が出る。

    #参照: https://noauto-nolife.com/post/django-models-add-field/
    #参照: https://noauto-nolife.com/post/django-non-nullable/

    #name   = models.CharField(verbose_name="名前",max_length=20)


    




    #モデルオブジェクト単体をprint()文あるいはテンプレートでモデルオブジェクトを表示させた時、何を返すかを指定している。この場合はcommentを出す。
    #これがないとTopic Objects (1) などと表示される
    def __str__(self):
        return self.comment

