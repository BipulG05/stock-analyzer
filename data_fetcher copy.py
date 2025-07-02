# data_fetcher.py
import os
import pandas as pd
from nsetools import Nse
import yfinance as yf
nse = Nse()


def get_stock_by_sector(sector):
    return [
        {
            "symbol": "TCS",
            "companyName": "Tata Consultancy Services",
            "lastPrice": "3600",
            "pChange": "1.5",
            "dayHigh": "3625",
            "dayLow": "3550",
            "sector": "IT"
        },
        {
            "symbol": "INFY",
            "companyName": "Infosys",
            "lastPrice": "1450",
            "pChange": "-0.3",
            "dayHigh": "1462",
            "dayLow": "1435",
            "sector": "IT"
        }
    ]


# def get_stock_by_sector(sector):
#     # Placeholder: NSE API doesn't support this directly
#     # You'll need to build a sector-symbol mapping CSV or JSON file
#     return []

# def get_stock_by_sector(sector):
#     try:
#         df = pd.read_csv("sector_mapping.csv")
#         sector_stocks = df[df['sector'].str.lower() == sector.lower()]
        
#         stock_details = []
#         for symbol in sector_stocks['symbol']:
#             try:
#                 quote = nse.get_quote(symbol)
#                 stock_details.append({
#                     "symbol": symbol,
#                     "companyName": quote.get("companyName", ""),
#                     "lastPrice": quote.get("lastPrice", ""),
#                     "pChange": quote.get("pChange", ""),
#                     "dayHigh": quote.get("dayHigh", ""),
#                     "dayLow": quote.get("dayLow", ""),
#                     "sector": sector
#                 })
#             except:
#                 continue  # skip stock if API fails
#         return stock_details
#     except Exception as e:
#         print(f"Error loading sector mapping: {e}")
#         return []


# def get_stock_by_sector(sector):
#     try:
#         df = pd.read_csv("sector_mapping.csv")
#         if sector.lower() != "all":
#             df = df[df['sector'].str.lower() == sector.lower()]
        
#         stock_details = []
#         for symbol in df['symbol']:
#             try:
#                 quote = nse.get_quote(symbol)
#                 stock_details.append({
#                     "symbol": symbol,
#                     "companyName": quote.get("companyName", ""),
#                     "lastPrice": quote.get("lastPrice", ""),
#                     "pChange": quote.get("pChange", ""),
#                     "dayHigh": quote.get("dayHigh", ""),
#                     "dayLow": quote.get("dayLow", ""),
#                     "sector": sector
#                 })
#             except:
#                 continue
#         return stock_details
#     except Exception as e:
#         print(f"Error: {e}")
#         return []

# import os
# basedir = os.path.dirname(os.path.abspath(__file__))
# csv_path = os.path.join(basedir, "sector_mapping.csv")

# def get_stock_by_sector(sector):
#     try:
#         # df = pd.read_csv("sector_mapping.csv")
#         df = pd.read_csv(csv_path)
#         print("[DEBUG] Loaded sector_mapping.csv")

#         if sector.lower() != "all":
#             df = df[df['sector'].str.lower() == sector.lower()]
#         print(f"[DEBUG] Selected sector: {sector}, found {len(df)} stocks")

#         stock_details = []
#         for symbol in df['symbol']:
#             print(f"[DEBUG] Fetching: {symbol}")
#             try:
#                 quote = nse.get_quote(symbol)
#                 stock_details.append({
#                     "symbol": symbol,
#                     "companyName": quote.get("companyName", ""),
#                     "lastPrice": quote.get("lastPrice", ""),
#                     "pChange": quote.get("pChange", ""),
#                     "dayHigh": quote.get("dayHigh", ""),
#                     "dayLow": quote.get("dayLow", ""),
#                     "sector": sector
#                 })
#             except Exception as e:
#                 print(f"[ERROR] Failed to fetch data for {symbol}: {e}")
#                 continue
#         return stock_details
#     except Exception as e:
#         print(f"[ERROR] Failed to read sector mapping: {e}")
#         return []


# def get_all_sectors():
#     try:
#         df = pd.read_csv("sector_mapping.csv")
#         return sorted(df['sector'].unique().tolist())
#     except:
#         return []



# Resolve full path to sector_mapping.csv
basedir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(basedir, "sector_mapping.csv")

# def get_stock_by_sector(sector):
#     try:
#         # Load the CSV file
#         df = pd.read_csv(csv_path)
#         print("[DEBUG] Loaded sector_mapping.csv")

#         # Filter by sector if not 'all'
#         if sector.lower() != "all":
#             df = df[df['sector'].str.lower() == sector.lower()]
#         print(f"[DEBUG] Selected sector: {sector}, found {len(df)} stocks")

#         stock_details = []
#         for symbol in df['symbol']:
#             print(f"[DEBUG] Fetching: {symbol}")
#             try:
#                 quote = nse.get_quote(symbol)
#                 stock_details.append({
#                     "symbol": symbol,
#                     "companyName": quote.get("companyName", ""),
#                     "lastPrice": quote.get("lastPrice", ""),
#                     "pChange": quote.get("pChange", ""),
#                     "dayHigh": quote.get("dayHigh", ""),
#                     "dayLow": quote.get("dayLow", ""),
#                     "sector": sector
#                 })
#             except Exception as e:
#                 print(f"[ERROR] Failed to fetch data for {symbol}: {e}")
#                 continue
#         return stock_details
#     except Exception as e:
#         print(f"[ERROR] Failed to read sector mapping: {e}")
#         return []
# def get_stock_by_sector(sector):
#     try:
#         df = pd.read_csv(csv_path)
#         print("[DEBUG] Loaded sector_mapping.csv")

#         if sector.lower() != "all":
#             df = df[df['sector'].str.lower() == sector.lower()]
#         print(f"[DEBUG] Selected sector: {sector}, found {len(df)} stocks")

#         stock_details = []
#         for symbol in df['symbol']:
#             print(f"[DEBUG] Fetching: {symbol}")
#             try:
#                 quote = nse.get_quote(symbol)
#                 if not quote:
#                     print(f"[WARNING] No data for {symbol}")
#                     continue  # Skip this symbol, move to next

#                 # If quote is valid, append details
#                 stock_details.append({
#                     "symbol": symbol,
#                     "companyName": quote.get("companyName", ""),
#                     "lastPrice": quote.get("lastPrice", ""),
#                     "pChange": quote.get("pChange", ""),
#                     "dayHigh": quote.get("dayHigh", ""),
#                     "dayLow": quote.get("dayLow", ""),
#                     "sector": sector
#                 })
#             except Exception as e:
#                 print(f"[ERROR] Failed to fetch data for {symbol}: {e}")
#                 continue

#         return stock_details
#     except Exception as e:
#         print(f"[ERROR] Failed to read sector mapping: {e}")
#         return []


def get_stock_data_yf(symbol):
    try:
        stock = yf.Ticker(symbol + ".NS")  # NSE suffix for yfinance
        info = stock.info
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
        print(f"[ERROR] yfinance fetch failed for {symbol}: {e}")
        return None

def get_all_sectors():
    try:
        df = pd.read_csv(csv_path)
        return sorted(df['sector'].unique().tolist())
    except Exception as e:
        print(f"[ERROR] Failed to get sectors: {e}")
        return []

def get_stock_details(stock_code):
    try:
        return nse.get_quote(stock_code)
    except:
        return None
