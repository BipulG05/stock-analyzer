import os
import pandas as pd
import yfinance as yf

# Define CSV path
basedir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(basedir, "sector_mapping.csv")

def get_stock_by_sector(sector):
    try:
        df = pd.read_csv(csv_path)
        print("[DEBUG] Loaded sector_mapping.csv")

        if sector.lower() != "all":
            df = df[df['sector'].str.lower() == sector.lower()]
        print(f"[DEBUG] Selected sector: {sector}, found {len(df)} stocks")

        stock_details = []
        for symbol in df['symbol']:
            print(f"[DEBUG] Fetching: {symbol}")
            try:
                ticker = yf.Ticker(symbol + ".NS")  # NSE stocks use `.NS`
                info = ticker.info

                stock_details.append({
                    "symbol": symbol,
                    "companyName": info.get("shortName", ""),
                    "lastPrice": info.get("regularMarketPrice", ""),
                    "pChange": info.get("regularMarketChangePercent", ""),
                    "dayHigh": info.get("dayHigh", ""),
                    "dayLow": info.get("dayLow", ""),
                    "sector": sector
                })
            except Exception as e:
                print(f"[ERROR] Failed to fetch data for {symbol}: {e}")
                continue
        return stock_details
    except Exception as e:
        print(f"[ERROR] Failed to read sector mapping: {e}")
        return []

def get_all_sectors():
    try:
        df = pd.read_csv(csv_path)
        return sorted(df['sector'].unique().tolist())
    except Exception as e:
        print(f"[ERROR] Failed to get sectors: {e}")
        return []


def get_stock_data_yf(symbol):
    try:
        ticker = yf.Ticker(symbol + ".NS")
        info = ticker.info
        return {
            "symbol": symbol,
            "companyName": info.get("shortName", ""),
            "lastPrice": info.get("regularMarketPrice", ""),
            "pChange": info.get("regularMarketChangePercent", ""),
            "dayHigh": info.get("dayHigh", ""),
            "dayLow": info.get("dayLow", ""),
            "sector": info.get("sector", "")
        }
    except Exception as e:
        print(f"[ERROR] Failed to fetch stock details for {symbol}: {e}")
        return None


def get_stock_details(symbol):
    try:
        ticker = yf.Ticker(symbol + ".NS")
        info = ticker.info
        return {
            "symbol": symbol.upper(),
            "companyName": info.get("shortName", ""),
            "lastPrice": info.get("regularMarketPrice", ""),
            "pChange": info.get("regularMarketChangePercent", ""),
            "dayHigh": info.get("dayHigh", ""),
            "dayLow": info.get("dayLow", ""),
            "sector": info.get("sector", ""),
            "industry": info.get("industry", ""),
            "marketCap": info.get("marketCap", ""),
            "volume": info.get("volume", "")
        }
    except Exception as e:
        print(f"[ERROR] Failed to fetch stock details for {symbol}: {e}")
        return None