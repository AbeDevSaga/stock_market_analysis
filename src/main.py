import os
from fetch_data import fetch_stock_data, save_data_to_csv
from visualize_data import plot_closing_price
from analysis import calculate_moving_average

def main():
    ticker = "AAPL"
    start_date = "2023-01-01"
    end_date = "2023-12-31"

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(BASE_DIR, "data", "stock_data.csv")
    # file_path = "../data/aapl_stock_data.csv"

    # Fetch and save stock data
    data = fetch_stock_data(ticker, start_date, end_date)
    save_data_to_csv(data, file_path)

    # Plot closing prices
    plot_closing_price(file_path)

    # Calculate moving average and print head
    ma_data = calculate_moving_average(file_path, window=20)
    print(ma_data.head())

if __name__ == "__main__":
    main()
