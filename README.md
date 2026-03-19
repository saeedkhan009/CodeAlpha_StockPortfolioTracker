# Simple Stock Tracker

A beginner-friendly Python script that helps you track a small stock portfolio from the command line.

You enter stock ticker symbols and share quantities, and the script calculates the total cost using a built-in list of prices. At the end it shows a summary and can optionally save the results to `portfolio.txt`.

## Features

- **Simple flow:** enter tickers, enter share counts, see a summary
- **Input validation:** rejects unknown tickers, non-integer quantities, and negative numbers
- **Display output:** shows each position and total investment
- **Save to file:** optionally writes `portfolio.txt` to the current directory

## Getting Started

### Prerequisites

- Python 3 installed (3.6+ works)

### Run

```bash
python StockTracker.py
```

Follow the prompts:

1. Enter a stock ticker from the list (e.g., `AAPL`).
2. Enter how many shares you own.
3. Repeat the above until you type `done`.
4. Choose whether to save the summary to `portfolio.txt`.

## Customizing Prices

The stock prices are hard-coded at the top of `StockTracker.py`:

```python
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320,
    "AMZN": 150,
}
```

Update these values to match current prices or add/remove tickers.

## Ideas for Improvement

- Fetch live prices from a public API (e.g., Yahoo Finance, Alpha Vantage).
- Add unit tests for input parsing and summary output.
- Add command-line options for specifying the output file path.
