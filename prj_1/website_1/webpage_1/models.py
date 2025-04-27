from django.db import models
import yfinance as yf
import pandas as pd



def BSE_history_5days(start="2023-01-01",end="2023-12-31"):
    bse_ = yf.Ticker("^BSESN")
    hist = bse_.history(period="5d")
    #df = ticker.history(start , end )
    return pd.DataFrame(hist)
