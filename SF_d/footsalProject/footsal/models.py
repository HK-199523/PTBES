from sre_constants import CATEGORY
from unicodedata import category
from django.db import models
from matplotlib.pyplot import title

# Create your models here.

#投稿についてのテーブルクラス
class NewslPost(models.Model):
    CATEGORY = (('LEGEND FC','legend'),('SCHOOL','school'))
    PLACE = (('船橋市運動公園体育館','funabashi'),
            ('国府台体育館','konodai'),
            ('東部スポーツ体育館','tobu'),
            ('市川市塩浜体育館','ichikawa'),
            ('柏井小学校体育館','kashiwai'))

    title = models.CharField(
            verbose_name='タイトル',
            max_length=200
            )
    content = models.TextField(
              verbose_name='本文'
            )
    image1 = models.ImageField(
             verbose_name='イメージ画像1',
             upload_to = 'photo1'
            )
    image2 = models.ImageField(
             verbose_name='イメージ画像2',
             upload_to = 'photo1',
             blank = True,
             null = True
            )
    category = models.CharField(
               verbose_name='カテゴリ',
               max_length=50,
               choices = CATEGORY
            )
    place = models.CharField(
            verbose_name='会場',
            max_length=50,
            choices = PLACE
            )
    cost = models.CharField(
                verbose_name='金額',
                max_length=20
            )
    posted_at = models.DateTimeField(
                verbose_name='投稿日時',
                auto_now_add=True 
            )

    def __str__(self):
        return self.title


class PhotoPost(models.Model):
    CATEGORY = (('LEGEND FC','legend'),('SCHOOL','school'))
    title = models.CharField(
            verbose_name='タイトル',
            max_length=200,
            blank = True,
            null =True
            )
    category = models.CharField(
            verbose_name = 'カテゴリ',
            max_length=50,
            choices=CATEGORY
            )
    posted_at = models.DateTimeField(
            verbose_name='投稿日時',
            auto_now_add=True 
            )

    def __str__(self):
        return self.title


class PhotoOnlyPost(models.Model):
    p_id = models.ForeignKey(
            PhotoPost,
            on_delete=models.CASCADE
            )
    image1 = models.ImageField(
             verbose_name='イメージ画像1',
             upload_to = 'photo2'
            )

class SPP(PhotoPost):
        class Meta:
            proxy = True


class SPOP(PhotoOnlyPost):
    class Meta:
        proxy = True


class ResultPost(models.Model):
    CATEGORY = (('LEGEND FC','legend'),('SCHOOL','school'))
    opponent = models.CharField(
            verbose_name='相手チーム名',
            max_length=200,
            )
    category = models.CharField(
            verbose_name = 'カテゴリ',
            max_length=50,
            choices=CATEGORY
            )
    myresult = models.CharField(
            verbose_name = '自チームの得点',
            max_length = 10,
            )
    oppresult = models.CharField(
            verbose_name = '相手チームの得点',
            max_length = 10,
            )
    posted_at = models.DateField(
            verbose_name='投稿日',
            auto_now_add=True 
            )

    def __str__(self):
        return self.opponent


class Event(models.Model):
    PERIOD_CHOICE = (('LEGEND FC','legend'),('SCHOOL','school'))

    title = models.CharField( verbose_name='予定タイトル',
                              max_length=200)
    start_date = models.DateTimeField(verbose_name='イベント開始時間')                         # イベント開始時間
    end_date = models.DateTimeField(verbose_name='イベント終了時間')                           # イベント終了時間
    last_update = models.DateField(verbose_name='最終更新時間',
                                   auto_now=True)
    content = models.TextField(verbose_name='イベント概要')
    period = models.CharField(verbose_name='イベントカテゴリ',
                                 max_length=50,
                                 choices=PERIOD_CHOICE)     # イベント内容
    url = models.URLField(verbose_name='LINK用',
                          blank = True, null = True )       # Link用
    def __str__(self):
        return self.title
