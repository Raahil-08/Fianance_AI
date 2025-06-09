import requests
import pandas as pd
import yfinance as yf
import time
import os


FINNHUB_API_KEY = "d13hoa1r01qs7glhm490d13hoa1r01qs7glhm49g"     
SECTOR = "Technology"                     
MAX_RESULTS = 2                        
START_DATE = "2024-05-01"
END_DATE = "2024-06-01"
OUTPUT_CSV = "data/final_stock_data.csv"



def get_all_us_stocks():
    print("📥 Fetching all US stock symbols from Finnhub...")
    url = f"https://finnhub.io/api/v1/stock/symbol?exchange=US&token={FINNHUB_API_KEY}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def filter_by_sector(stock_list, sector, max_results):
    print(f"\n🔍 Filtering for sector: {sector}")
    filtered = []
    count = 0

    for stock in stock_list:
        symbol = stock.get("symbol")
        if not symbol or "." in symbol:  
            continue

        try:
            url = f"https://finnhub.io/api/v1/stock/profile2?symbol={symbol}&token={FINNHUB_API_KEY}"
            r = requests.get(url)
            r.raise_for_status()
            profile = r.json()
            industry = profile.get("finnhubIndustry", None)
            name = profile.get("name", None)

            if industry == sector:
                filtered.append({
                    "symbol": symbol,
                    "name": name,
                    "industry": industry
                })
                print(f"✅ {symbol}: {name}")
                count += 1

            if count >= max_results:
                break

            time.sleep(0.25)  
        except Exception as e:
            print(f"⚠️ Error for {symbol}: {e}")

    return filtered


def get_historical_data(symbols, start_date, end_date):
    all_data = []

    for symbol in symbols:
        try:
            print(f"📊 Fetching price history for {symbol}...")
            data = yf.download(symbol, start=start_date, end=end_date)
            data['Symbol'] = symbol
            data['Daily Return'] = data['Close'].pct_change()
            data['Volatility'] = data['Daily Return'].rolling(window=7).std()
            data = data.reset_index()
            all_data.append(data)
        except Exception as e:
            print(f"⚠️ Failed for {symbol}: {e}")

    return pd.concat(all_data, ignore_index=True)


if __name__ == "__main__":
    all_stocks = get_all_us_stocks()
    filtered_stocks = filter_by_sector(all_stocks, SECTOR, MAX_RESULTS)

    if not filtered_stocks:
        print("❌ No stocks found for the specified sector.")
        exit()

    symbols = [s['symbol'] for s in filtered_stocks]
    price_data = get_historical_data(symbols, START_DATE, END_DATE)

    symbol_to_name = {s['symbol']: s['name'] for s in filtered_stocks}
    price_data['Company Name'] = price_data['Symbol'].map(symbol_to_name)

    price_data.to_csv(OUTPUT_CSV, index=False)
    print(f"\n✅ Done! Saved data to {OUTPUT_CSV}")
