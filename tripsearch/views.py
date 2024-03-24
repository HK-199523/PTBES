from django.shortcuts import render
from .models import News

def home(request):
    return render(request, 'home.html')

def exchange(request):
    return render(request, 'exchange.html')

def top(request):
    newsinfo = News.objects.all()  # データベースから全てのニュースを取得
    return render(request, 'top.html', {'newsinfoList': newsinfo})

# Define other views similarly...
