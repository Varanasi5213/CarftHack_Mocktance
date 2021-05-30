from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import TickerForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
import yfinance as yf
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd

class HomeView(View):
    def get(self, request, *args, **kwargs):

        return render(request,'charts.html')


def ticker(request,*args, **kwargs):
        name = ''
        request.session['tickerid'] = ''
        if request.method == 'POST':
            ticker = request.POST['ticker']
            context={}
            request.session['ticker']=ticker
            
        return render(request,'tickerchart.html',{'ticker':ticker})


class ChartData(APIView):
 
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        ticker = request.session['ticker']
        data = yf.Ticker(ticker)
        today_date = datetime.now().date().strftime("%y-%m-%d")
        today_date = '20'+today_date
        onemon_date = datetime.today() - relativedelta(days=+30)
        onemon_date = onemon_date.strftime("%y-%m-%d")
        onemon_date = '20'+onemon_date

        df = data.history(start=onemon_date,end=today_date)

        month_close = df['Close'].tolist()
        month_low = df['Low'].tolist()
        month_high = df['High'].tolist()
        month_open = df['Open'].tolist()
        ok = pd.DataFrame(columns=['date'])
        labels =[]
        ok['date'] = df.index
        lis = pd.to_datetime(ok['date']).dt.date
        for l in lis:
    
            labels.append(str(l))

        data = {"labels":labels,
                 "close":month_close,
                 "open":month_open,
                 "high":month_high,
                 "low":month_low,
                 }
        return Response(data)

# def ticker(request):
    
        
#     context={}
    
#     ticker = request.session['ticker']

#     return render(request,'ticker.html',{'ticker':ticker})