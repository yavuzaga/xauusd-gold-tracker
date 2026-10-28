import yfinance as yf
import datetime
import time


def get_gold_price():
    """Fetches real-time XAU/USD (Gold Futures) price via Yahoo Finance API."""
    try:
        gold = yf.Ticker("GC=F")
        data = gold.history(period="1d")

        if not data.empty:
            current_price = data['Close'].iloc[-1]
            return round(current_price, 2)
        else:
            return None
    except Exception as e:
        # Log fetch errors with UTC timestamp
        utc_now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        print(f"[{utc_now}] ERROR: Failed to fetch market data - {e}")
        return None


def monitor_gold():
    # Target price thresholds (Set according to trading strategy)
    target_high = 4100.0
    target_low = 4000.0

    print("🚀 XAU/USD Real-Time Monitoring Service Started...")
    print("🔄 Engine Active: Fetching market data every 10 seconds. Press Ctrl+C to terminate.")
    print("-" * 80)

    # Continuous Monitoring Loop
    while True:
        # Standardized UTC Timestamp for global servers
        utc_now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        price = get_gold_price()

        if price:
            message = f"[{utc_now}] 📊 XAU/USD Current Price: ${price}"
            print(message)

            # Threshold Check / Signal Generator
            if price >= target_high:
                print(f"🚨 SIGNAL: Gold reached target resistance level! (${target_high})")
            elif price <= target_low:
                print(f"🚨 SIGNAL: Gold dropped to target support level! (${target_low})")

            # Append data to persistent log file
            with open("gold_tracker.log", "a", encoding="utf-8") as log_file:
                log_file.write(message + "\n")
        else:
            print(f"[{utc_now}] ⚠️ WARNING: Price data unavailable, retrying...")

        # 10-second polling interval
        time.sleep(10)


if __name__ == "__main__":
    monitor_gold()