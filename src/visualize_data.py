import pandas as pd
import matplotlib.pyplot as plt

def plot_closing_price(file_path):
    data = pd.read_csv(file_path, index_col='Date', parse_dates=True)
    plt.figure(figsize=(12, 6))
    plt.plot(data['Close'], label='Closing Price')
    plt.title('Stock Closing Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True)
    plt.show()
