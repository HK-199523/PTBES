from django.shortcuts import render
from django.http import JsonResponse
import pandas_datareader.data as pdr
import pandas as pd
from datetime import datetime, timedelta
import yfinance as yf

# yfinanceの設定をpandas_datareaderに適用
yf.pdr_override()

def home(request):
    return render(request, 'home.html')

def top(request):
    newsinfo = News.objects.all()
    return render(request, 'top.html', {'newsinfoList': newsinfo})

def exchange(request):
    currencyPairs = ['USDJPY=X', 'EURUSD=X', 'EURJPY=X', 'EURGBP=X', 'EURAUD=X', 'EURCAD=X', 'EURCHF=X', 'EURCNY=X', 'EURHKD=X', 'EURNZD=X', 'EURSEK=X']
    today = datetime.now().date()
    yesterday = today - timedelta(2)

    # 2024年3月24日の為替レートを取得
    rates = pdr.get_data_yahoo(currencyPairs, start=yesterday, end=today)

    context = {
        'rates': rates,
    }
    return render(request, 'exchange_rates.html', context)
