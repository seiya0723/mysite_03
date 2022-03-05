from django.shortcuts import render,redirect
from django.views import View

from .models import Topic

#TODO:フォームクラスをimportする。
from .forms import TopicForm


class BbsView(View):

    def get(self, request, *args, **kwargs):
        topics  = Topic.objects.all()

        print("GETメソッド")

        """
        topics = [
            {"id": 1, "comment": "Hello"},
            {"id": 2, "comment": "Hello"},
            {"id": 3, "comment": "Hello"},
            {"id": 4, "comment": "Hello"},
        ]
        """
        import datetime
        print(datetime.datetime.now())

        context = { "test":"あああああああ",
                    "topics":topics,
                    "flag":False,
                    "dt": datetime.datetime.now()
                    }

        return render(request,"bbs/index.html",context)

    def post(self, request, *args, **kwargs):
        print("POSTメソッド")

        #TODO:クライアントから受け取ったデータをDBへ保存する処理
        print(request.POST)
        print(request.POST["comment"])

        #ここで受け取ったデータを保存する(バリデーションをしていない、)
        """
        posted  = Topic( comment=request.POST["comment"] )
        posted.save()

        print(posted.comment)
        """

        #TODO:バリデーションありDB保存
        form    = TopicForm(request.POST)

        #フォームクラスで定義したルールに則っているかチェックする。(バリデーションチェック)
        if form.is_valid():
            print("バリデーションOK")
            #モデルを使う場合と同様に.save()で保存できる。.is_valid()を実行して、なおかつTrueがでないとエラーが出る。
            form.save()
        else:
            print("バリデーションNG")

        return redirect("bbs:index")


index   = BbsView.as_view()
