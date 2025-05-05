import pandas as pd

def calculate_moving_average(file_path, window=20):
    data = pd.read_csv(file_path, index_col='Date', parse_dates=True)
    data[f'MA_{window}'] = data['Close'].rolling(window=window).mean()
    return data
