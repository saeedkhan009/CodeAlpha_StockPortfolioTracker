# Simple Stock Tracker

# Hardcoded declaration of stock symbols and their prices.
stock_prices = {
    "AAPL": 180,  # Price per share for Apple
    "TSLA": 250,  # Price per share for Tesla
    "GOOG": 140,  # Price per share for Google
    "MSFT": 320,  # Price per share for Microsoft
    "AMZN": 150,  # Price per share for Amazon
}

# Function to format numbers as currency for nicer display.
def format_currency(value):
    """Format a number as U.S. dollars with two decimal places."""

    # Return a string like "$1,234.56" for nicer display.
    return f"${value:,.2f}"

# Main function to run the stock tracker application. inside main function take input using loop
def main():
    # Keep track of how many shares the user has entered for each stock.
    portfolio = {}

    # Print header and list of available stocks.
    print(" Welcome to Simple Stock Tracker")
    print("Available Stocks:")
    for symbol, price in stock_prices.items():
        print(f"  {symbol} : {format_currency(price)}")

    print("\nType 'done' when finished.\n")

    # Loop until the user indicates they are finished.
    while True:
        # Ask for the stock ticker symbol.
        symbol = input("Enter stock symbol (or 'done'): ").strip().upper()

        # If the user typed nothing or 'done', stop the loop.
        if not symbol or symbol == "DONE":
            break

        # If the symbol isn't in our list, tell the user and ask again.
        if symbol not in stock_prices:
            print(" Stock not available. Please choose a symbol from the list.")
            continue

        # Ask for the number of shares and keep asking until it's valid.
        while True:
            quantity_input = input(f"Enter quantity of {symbol} shares: ").strip()
            try:
                quantity = int(quantity_input)  # Convert the input to an integer.
            except ValueError:
                # If conversion fails, ask again.
                print(" Please enter a whole number (e.g., 5).")
                continue

            # Prevent negative share counts.
            if quantity < 0:
                print(" Stock quantity must be zero or positive.")
                continue

            # If we reach this point, the quantity is valid.
            break

        # Add the shares to the portfolio (sum if the stock already exists).
        portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        value = stock_prices[symbol] * quantity
        # Show the value of this position to the user.
        print(f" Added: {symbol} | Value: {format_currency(value)}\n")

    # Show the final summary of the portfolio.
    print("\n Investment Summary")
    total = 0
    if not portfolio:
        # If the portfolio is empty, tell the user.
        print("(No positions entered)")
    else:
        # Show each stock line-by-line.
        for symbol, qty in portfolio.items():
            price = stock_prices[symbol]  # Price per share.
            value = qty * price  # Total value for this stock.
            total += value  # Add to the portfolio total.
            print(f"  {symbol} → {qty} shares × {format_currency(price)} = {format_currency(value)}")

    # Print the total investment value.
    print(f"\n Total Investment: {format_currency(total)}")

    # Ask if the user wants to save the summary to a file.
    save = input("\nDo you want to save this to file? (yes/no): ").strip().lower()
    if save in {"y", "yes"}:
        # Write the summary to 'portfolio.txt' in the current directory.
        with open("portfolio.txt", "w", encoding="utf-8") as f:
            f.write("Stock Portfolio Summary\n\n")
            for symbol, qty in portfolio.items():
                price = stock_prices[symbol]
                value = qty * price
                f.write(f"{symbol} : {qty} × {format_currency(price)} = {format_currency(value)}\n")
            f.write(f"\nTotal Investment: {format_currency(total)}\n")
        print(" Data saved in portfolio.txt")


# If this script is run directly (not imported), execute the main() function.
if __name__ == "__main__":
    main()
