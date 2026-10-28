# 🪙 Professional Python Automation & Real-Time Financial Tracking Engine

A professional-grade, resilient Python automation and tracking framework designed to fetch real-time market data, handle network exceptions robustly, manage persistent UTC logging, and evaluate threshold-based alerts continuously.

---

## 🛠️ Project Modules & Core Architecture

This repository contains modularized scripts built with structural rigor and global engineering standards:

1. **Market Data Worker (`get_gold_price`)**: 
   - Connects directly to Yahoo Finance API using the global ticker standard (`GC=F` for Gold Futures).
   - Extracts live closing prices dynamically and handles upstream exceptions safely via `try-except` blocks.
2. **Control Orchestrator (`monitor_gold`)**: 
   - Manages non-blocking infinite loops (`while True`) with optimized polling intervals (`time.sleep`) to prevent CPU overhead and API rate limits.
   - Evaluates dynamic high/low threshold limits to generate immediate market signals.
3. **UTC Chronological Logger**: 
   - Uses Coordinated Universal Time (`UTC`) for standardized, server-grade logging.
   - Automatically appends real-time data streams into persistent local storage (`gold_tracker.log`).

---

## ⚙️ Tech Stack

- **Language:** Python 3.x
- **Core Market Engine:** `yfinance`
- **Standard Libraries:** `datetime`, `time`

---

## 🚀 Installation & Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yavuz-ciftci/xauusd-gold-tracker.git
   cd xauusd-gold-tracker
   ```

2. **Install dependencies:**
   ```bash
   pip install yfinance
   ```

3. **Run the tracking engine:**
   ```bash
   python main.py
   ```

---

## 📝 Example Log Output (`gold_tracker.log`)

```text
[2026-10-27 19:00:16 UTC] 📊 XAU/USD Current Price: $4076.2
[2026-10-27 19:00:26 UTC] 📊 XAU/USD Current Price: $4077.5
[2026-10-27 19:00:36 UTC] 🚨 SIGNAL: Gold reached target resistance level! ($4100.0)
```

---

## 👨‍💻 Author
**Yavuz Çiftçi** *(yavuzaga)*