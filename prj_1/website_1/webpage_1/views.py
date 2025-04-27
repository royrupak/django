from django.shortcuts import render
from . import models
import yfinance as yf
import pandas as pd
import json



def index(request):
    return render(request, 'webpage_1/index.html')
def home(request):
    return render(request, 'webpage_1/homepage.html')
def topic_listing(request):
    return render(request, 'webpage_1/topics-listing.html')
def topic_detail(request):
    return render(request, 'webpage_1/topics-detail.html')
def contact(request):
    return render(request, 'webpage_1/contact.html')
def finance_topic_detail(request):
    return render(request, 'webpage_1/index_finance.html')
def finance_topic_onecolumn(request):
    return render(request, 'webpage_1/onecolumn.html')
def finance_topic_twocolumn(request):
    df=models.BSE_history_5days()
    # Convert DataFrame to JSON format
    json_records = df.reset_index().to_json(orient='records')
    data = json.loads(json_records)
    # Pass data to template
    context = {'dataframe': data}
    return render(request, 'webpage_1/twocolumn1.html',context)
def finance_topic_twocolumnset(request):
    return render(request, 'webpage_1/twocolumn2.html')
def finance_topic_threecolumn(request):
    return render(request, 'webpage_1/threecolumn.html')


