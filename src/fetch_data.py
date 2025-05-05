import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, start_date, end_date):
    stock = yf.Ticker(ticker)
    data = stock.history(start=start_date, end=end_date)
    return data

def save_data_to_csv(data, filename):
    data.to_csv(filename)
    print(f"Data saved to {filename}")
