import iexfinance as iex
from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt
import pandas as pd
from iexfinance import get_available_symbols
import json
from iexfinance import Stock
import requests_cache
import matplotlib.pyplot as plt
import plotly
import plotly.plotly as plot
import plotly.graph_objs as obj
import numpy as np
'''
This will create an automatic caching session key, which will be passed into all request functions to cache results
Expiry default is 1 minute
'''
def create_cache_session():
	print("In Create_session")
	expiry = timedelta(minutes=15)
	session = requests_cache.CachedSession(cache_name='finance_cache', backend='sqlite', expire_after=expiry)
	assert session is not None
	return session

cache_session = create_cache_session()
print(cache_session)
'''
Use this as an assertion that a decorated child method
is indeed overriding its parent.
Usage: add @overrides([parent class name]) before child method
'''
def overrides(interface_class):
    print("interfcae_class")
    def overrider(method):
        assert(method.__name__ in dir(interface_class))
        return method
    return overrider

'''
NASDAQ company listing, access from API
Returns Pandas dataframe
'''

def get_symbols():
	print("get_symbols")
	company_list = iex.get_available_symbols(session = cache_session)
	symbol_list = []
	for company in company_list:
		symbol_list.append(company['symbol'])
	return symbol_list

'''
Use code, (e.g. AAPL) and a time slice to get data from iexfinance API
Returns Pandas dataframe
'''
def get_company_data_start_end(company_code, start, end):
	print("get_company_data_start_end")
	#here, make a call to the api using a company code
	df = iex.get_historical_data(company_code, start=start, end=end, output_format='json')
	return df


"""
Yields the stock endpoint from the iexfinance iAPI, caches data
"""
def get_stock(company_code):
	print("get_stock")
	if not isinstance(company_code, str):
		raise TypeError('company_code should be a str.')
		return False

	stock_reader = Stock(company_code, output_format='json', session=cache_session)
	return stock_reader


"""
Gives the LATEST stock quote, ignoring all cached data
"""
def get_latest_stock_quote(company_code):
	print("get_latest_stock_quote")
	if not isinstance(company_code, str):
		raise TypeError("Company_code should be a string.")
		return False
	stock_reader = Stock(company_code, output_format='json').get_quote()
	return stock_reader

"""
Returns all the conveniently formatted data from the API which will be used for charting.
"""
def get_chart_data(company_code):
	print("get_chart_data")
	stock_reader = Stock(company_code, output_formt='json', session=cache_session)
	chart_dict = stock_reader.get_chart()
	print(chart_dict)
	return chart_dict

"""
Input a company name (exact text) and return the symbol:
"""
def symbol_from_name(name):
	for key, value in Companies.available_symbols_dict.items():
		if value == name:
			return key
			return None

import plotly.plotly as plot
import plotly
import plotly.graph_objs as obj

"""
Input json data to plot a candle stick graph
"""
chart_dict = {}
def plot_chart(chart_dict):
	date = []
	open=[]
	high=[]
	close=[]
	low=[]

for t in chart_dict:
	print(t["date"])
	date.append(t["date"])
	open.append(t["open"])
	high.append(t["high"])
	low.append(t["low"])
	close.append(t["close"])

	trace = obj.Candlestick(x=date,
                       open=open,
                       high=high,
                       low=low,
                       close=close)
	data = [trace]
	plotly.offline.plot(data, filename='sample.html', auto_open=True)
