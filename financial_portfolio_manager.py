"""
Financial Portfolio Manager

Author: Danilo Vunza
Course: COSC 2436

Description:
Portfolio management system for
investment analysis and risk evaluation.
"""


class Asset:

    def __init__(
        self,
        symbol,
        shares,
        purchase_price,
        current_price
    ):

        self.symbol = symbol

        self.shares = shares

        self.purchase_price = purchase_price

        self.current_price = current_price


class Stock(Asset):

    pass


class Portfolio:

    def __init__(self):

        self.stocks = []

    def add_stock(
        self,
        symbol,
        shares,
        purchase_price,
        current_price
    ):

        stock = Stock(
            symbol,
            shares,
            purchase_price,
            current_price
        )

        self.stocks.append(stock)

        print(
            "\nStock added successfully."
        )

    def remove_stock(
        self,
        symbol
    ):

        for stock in self.stocks:

            if stock.symbol.upper() == symbol.upper():

                self.stocks.remove(stock)

                print(
                    "\nStock removed successfully."
                )

                return

        print("\nStock not found.")

    def calculate_portfolio_value(self):

        total = 0

        for stock in self.stocks:

            total += (
                stock.current_price *
                stock.shares
            )

        return total

    def calculate_total_cost(self):

        total = 0

        for stock in self.stocks:

            total += (
                stock.purchase_price *
                stock.shares
            )

        return total

    def calculate_return_percentage(self):

        cost = self.calculate_total_cost()

        value = self.calculate_portfolio_value()

        if cost == 0:

            return 0

        return (
            (value - cost)
            / cost
        ) * 100

    def analyze_portfolio(self):

        value = self.calculate_portfolio_value()

        cost = self.calculate_total_cost()

        profit = value - cost

        print("\nPORTFOLIO ANALYSIS")

        print("-" * 60)

        print(
            f"Total Investment: "
            f"${cost:.2f}"
        )

        print(
            f"Portfolio Value: "
            f"${value:.2f}"
        )

        print(
            f"Profit/Loss: "
            f"${profit:.2f}"
        )

        print(
            f"Return: "
            f"{self.calculate_return_percentage():.2f}%"
        )

    def risk_metrics(self):

        print("\nRISK METRICS")

        print("-" * 60)

        if len(self.stocks) == 0:

            print("Portfolio is empty.")

            return

        largest_position = max(
            self.stocks,
            key=lambda stock:
            stock.current_price *
            stock.shares
        )

        position_value = (
            largest_position.current_price *
            largest_position.shares
        )

        portfolio_value = (
            self.calculate_portfolio_value()
        )

        concentration = (
            position_value /
            portfolio_value
        ) * 100

        print(
            f"Largest Position: "
            f"{largest_position.symbol}"
        )

        print(
            f"Concentration: "
            f"{concentration:.2f}%"
        )

        if concentration > 50:

            print(
                "Risk Level: High"
            )

        elif concentration > 25:

            print(
                "Risk Level: Medium"
            )

        else:

            print(
                "Risk Level: Low"
            )

    def display_portfolio(self):

        print("\nPORTFOLIO")

        print("-" * 70)

        if len(self.stocks) == 0:

            print(
                "No stocks available."
            )

            return

        for stock in self.stocks:

            print(
                f"{stock.symbol} | "
                f"Shares: {stock.shares} | "
                f"Purchase: ${stock.purchase_price:.2f} | "
                f"Current: ${stock.current_price:.2f}"
            )


def display_menu():

    print("\n" + "=" * 60)

    print("FINANCIAL PORTFOLIO MANAGER")

    print("=" * 60)

    print("1. Add Stock")

    print("2. Remove Stock")

    print("3. View Portfolio")

    print("4. Portfolio Analysis")

    print("5. Risk Metrics")

    print("6. Exit")

    print("=" * 60)


def main():

    portfolio = Portfolio()

    while True:

        display_menu()

        choice = input(
            "Select an option: "
        )

        if choice == "1":

            portfolio.add_stock(
                input("Symbol: "),
                int(input("Shares: ")),
                float(input("Purchase Price: ")),
                float(input("Current Price: "))
            )

        elif choice == "2":

            portfolio.remove_stock(
                input("Symbol: ")
            )

        elif choice == "3":

            portfolio.display_portfolio()

        elif choice == "4":

            portfolio.analyze_portfolio()

        elif choice == "5":

            portfolio.risk_metrics()

        elif choice == "6":

            print(
                "\nThank you for using the system."
            )

            break

        else:

            print(
                "\nInvalid option."
            )


main()
