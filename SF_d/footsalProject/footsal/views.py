from datetime import date,timedelta,datetime
from pyexpat import model
from re import template
from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView,FormView,DetailView,TemplateView
from django.urls import reverse_lazy
from matplotlib.style import context
from django.http.response import JsonResponse
from django.template.loader import render_to_string
from .forms import ContactForm,TopicForm,TopicImageForm
from django.contrib import messages
# Create your views here.
import json
import codecs
from .models import NewslPost,PhotoPost,PhotoOnlyPost,ResultPost,Event
from footsal import forms



class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'news'
    model = NewslPost

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
            'photo1': PhotoPost.objects.all(),
            'result': ResultPost.objects.all(),
        })
        return context

    def get_queryset(self):
        return NewslPost.objects.order_by('-posted_at')[:4]


class PostAllView(ListView):
    template_name = 'postAll.html'
    context_object_name = 'news'
    queryset = NewslPost.objects.order_by('-posted_at')
    paginate_by = 20
    def get_context_data(self, **kwargs):
        context = super(PostAllView, self).get_context_data(**kwargs)
        context.update({
            'title': 'NEWS ALL PAGE',
            'term': 'NEWS ALL'
        })
        return context

class IchiView(ListView):
    template_name = 'postAll.html'
    context_object_name = 'news'
    queryset = NewslPost.objects.filter(place='市川市塩浜体育館').order_by('-posted_at')
    paginate_by = 20
    def get_context_data(self, **kwargs):
        context = super(IchiView, self).get_context_data(**kwargs)
        context.update({
            'title': '市川市塩浜体育館',
            'term': '会場：市川市塩浜体育館'
        })
        return context

class FunaView(ListView):
    template_name = 'postAll.html'
    context_object_name = 'news'
    queryset = NewslPost.objects.filter(place='船橋市運動公園体育館').order_by('-posted_at')
    paginate_by = 20
    def get_context_data(self, **kwargs):
        context = super(FunaView, self).get_context_data(**kwargs)
        context.update({
            'title': '船橋市運動公園体育館',
            'term': '会場：船橋市運動公園体育館'
        })
        return context

class KonoView(ListView):
    template_name = 'postAll.html'
    context_object_name = 'news'
    queryset = NewslPost.objects.filter(place='国府台体育館').order_by('-posted_at')
    paginate_by = 20
    def get_context_data(self, **kwargs):
        context = super(KonoView, self).get_context_data(**kwargs)
        context.update({
            'title': '国府台体育館',
            'term': '会場：国府台体育館'
        })
        return context

class TobuView(ListView):
    template_name = 'postAll.html'
    context_object_name = 'news'
    queryset = NewslPost.objects.filter(place='東部スポーツ体育館').order_by('-posted_at')
    paginate_by = 20
    def get_context_data(self, **kwargs):
        context = super(TobuView, self).get_context_data(**kwargs)
        context.update({
            'title': '東部スポーツ体育館',
            'term': '会場：東部スポーツ体育館'
        })
        return context

class KashiView(ListView):
    template_name = 'postAll.html'
    context_object_name = 'news'
    queryset = NewslPost.objects.filter(place='柏井小学校体育館').order_by('-posted_at')
    paginate_by = 20
    def get_context_data(self, **kwargs):
        context = super(KashiView, self).get_context_data(**kwargs)
        context.update({
            'title': '柏井小学校体育館',
            'term': '会場：柏井小学校体育館'
        })
        return context

class SchoolView(ListView):
    template_name = 'postAll.html'
    context_object_name = 'news'
    queryset = NewslPost.objects.filter(category='SCHOOL').order_by('-posted_at')
    paginate_by = 20
    def get_context_data(self, **kwargs):
        context = super(SchoolView, self).get_context_data(**kwargs)
        context.update({
            'title': 'SCHOOL',
            'term': 'カテゴリ：SCHOOL'
        })
        return context

class LegendView(ListView):
    template_name = 'postAll.html'
    context_object_name = 'news'
    queryset = NewslPost.objects.filter(category='LEGEND FC').order_by('-posted_at')
    paginate_by = 20
    def get_context_data(self, **kwargs):
        context = super(LegendView, self).get_context_data(**kwargs)
        context.update({
            'title': 'LEGEND FC',
            'term': 'カテゴリ：LEGEND FC'
        })
        return context


class DetailPageView(DetailView):
    template_name = 'detail.html'
    model = NewslPost
    context_object_name = 'news'


class GalleryView(ListView):
    template_name = 'photoGallery.html'
    queryset = PhotoPost.objects.all()
    paginate_by = 9
    def get_context_data(self, **kwargs):
        results = []
        photoResults = PhotoPost.objects.all()
        print(photoResults)
        for photoResult in photoResults:
            photoOnlyFirst = photoResult.photoonlypost_set.first()
            if photoOnlyFirst:
                results.append((photoResult, photoOnlyFirst))
        context = {
            'title':'Photo Gallery',
            'photoall':results
        }
        return context


class DetailPhotoView(DetailView):
    template_name = 'detail_photo.html'
    model = PhotoPost
    context_object_name = 'photopost'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        p_pk = self.kwargs.get('pk')
        context['photoonly'] = PhotoOnlyPost.objects.filter(p_id = p_pk)
        print(context)
        return context


class ScheduleView(ListView):
    template_name='schedule.html'
    print(Event)
    context_object_name = 'Event'
    model = Event
    def get_context_data(self, **kwargs):
        today = datetime.now()
        choice_query_set = Event.objects.filter(start_date__gte=today)
        choice_list = list(choice_query_set.values())
        datetime_format_change = []
        for e in choice_list:
            e_one = e
            e_start = e.get("start_date")
            e_end = e.get("end_date")
            e_last = e.get("last_update")
            e_one["start_date"] = e_start.strftime('%Y-%m-%dT%H:%M')
            e_one["end_date"] = e_end.strftime('%Y-%m-%dT%H:%M')
            e_one["start_time"] = e_start.strftime('%H時%M分')
            e_one["end_time"] = e_end.strftime('%H時%M分')
            e_one["last_update"] = e_last.strftime('%Y年%m月%d日')
            if(e["period"]=="LEGEND FC"):
                e_one["color"]="#800080"
            else:
                e_one["color"]="#0000ff"
            datetime_format_change.append(e_one)
        print(datetime_format_change)
        toJson = json.dumps(datetime_format_change,ensure_ascii=False)
        print()
        print("tojsonのやつ")
        print(toJson)
        context={
            "event_data":toJson
        }
        return context


class ContactView(FormView):
    template_name='contact.html'
    form_class=ContactForm                     #HTMLとDjangoの橋渡しをするためのクラス変数（django.views.generic.edit.FromMixinで定義されている）
    success_url=reverse_lazy('footsal:contact')   #フォーム処理が正常に処理できた時にリダイレクトするURLを登録する。
    def form_valid(self,form):
        form.send_email()
        messages.success(
            self.request,'お問い合わせは正常に送信されました。'
        )
        return super().form_valid(form)


class UploadView(TemplateView):
    template_name = 'photoUpload.html'
    fields = ()
    def get_context_data(self, **kwargs):
        context = super(UploadView, self).get_context_data(**kwargs)
        context.update({
            'one_for_one':forms.TopicForm(),
            'multi_for_one':forms.TopicImageForm()
        })
        return context
    def post(self, request, *args, **kwargs):
        print(request.POST)
        print(request.FILES)
        form_main = TopicForm(request.POST)
        main_PK = None
        msgs_list = [
            {'tags':'success',
             'msg':'問題が発生し保存ができませんでした。'}
        ]
        if form_main.is_valid():
            post_main = form_main.save(commit=False)
            post_main.save()
            main_PK = post_main.id #上で保存したレコードのid値を取得
            print(main_PK)
        else:
            context = super(UploadView, self).get_context_data(**kwargs)
            context.update({
                'one_for_one':forms.TopicForm(),
                'multi_for_one':forms.TopicImageForm(),
                'messages':msgs_list
            })
            return render(request,'photoUpload.html',context)
        photoes = request.FILES.getlist('image1')
        print(photoes)
        for photo in photoes:
            PhotoOnlyPost.objects.create(
                p_id = PhotoPost.objects.get(id = main_PK),
                image1 = photo
            )
        msgs_list[0]['msg'] = '画像保存完了しました。'
        context = super(UploadView, self).get_context_data(**kwargs)
        context.update({
            'one_for_one':forms.TopicForm(),
            'multi_for_one':forms.TopicImageForm(),
            'messages':msgs_list
        })
        return render(request,'photoUpload.html',context)
        

