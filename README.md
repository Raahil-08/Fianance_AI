# 💸 Finance + AI Investment Advisor

A smart AI-powered investment advisor that helps users allocate funds based on their risk profile, preferred sectors, and time window — by analyzing real-time stock market data.

This tool fetches filtered stock data by sector using the Finnhub API and then retrieves historical price, return, and volatility info via yFinance — perfect for powering investment insights or training machine learning models.

---

## 🚀 Features

- 🔍 Filter U.S. stocks by sector (e.g., Technology, Healthcare)
- 📊 Fetch historical stock data using Yahoo Finance
- 📈 Calculate daily return & 7-day rolling volatility
- 💾 Save output as a clean CSV (`data/final_stock_data.csv`)
- 🧠 Ready to plug into AI/ML models for financial prediction

---

## 🛠️ Technologies Used

| Layer      | Stack                     |
|------------|---------------------------|
| Data APIs  | [Finnhub.io](https://finnhub.io), [yFinance](https://pypi.org/project/yfinance/) |
| Language   | Python 3.10+              |
| Libraries  | `requests`, `pandas`, `yfinance`, `numpy` |
| Output     | CSV (for ML/analytics use) |

---

## ⚙️ Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/finance-ai-advisor.git
cd finance-ai-advisor
```

### 2. Install dependecies
```bash
pip install -r requirements.txt
```

### 3. Add your Finnhub API key
```bash
FINNHUB_API_KEY = "YOUR_API_KEY_HERE"
```

### 4. Run the pipeline
```bash
python scripts/full_stock_pipeline.py
```
