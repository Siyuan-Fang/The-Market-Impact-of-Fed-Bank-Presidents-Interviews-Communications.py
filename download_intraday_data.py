# # Import TimeSeries class
# from alpha_vantage.timeseries import TimeSeries
#
# ALPHA_VANTAGE_API_KEY = 'X4BWF4OCWFYQPEB1'
#
# # Initialize the TimeSeries class with key and output format
# ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format='pandas')
#
# # Get json object with the intraday data and information of the data
# intraday_data, data_info = ts.get_intraday(
#     'TN', outputsize='full', interval='1min')
#
# # Print the information of the data
# intraday_data.to_csv('D:/AA econ/research track/data/output4.csv')

#yahoo!!!!!!!!!!!!!!!!!!!!!!!
import pandas as pd
import yfinance as yf

# data = yf.download(tickers="ZN=F",
#                    period="5y",
#                    interval="2h")
data = yf.download(tickers="ZQU24.CBT",
                   period="1mo",
                   interval="1h")
df = pd.DataFrame(data)
df.to_csv('D:/AA econ/research track/data/intraday data/ZQV4.csv', index=True, encoding='utf-8')

data = yf.download(tickers="SR1U24.CME",
                   period="1mo",
                   interval="1h")
df = pd.DataFrame(data)
df.to_csv('D:/AA econ/research track/data/intraday data/SR1V4.csv', index=True, encoding='utf-8')
