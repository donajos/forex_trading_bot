class OrderSimulator:
    def __init__(self, log_function):
        self.log_function = log_function  # Function to log messages

    def simulate_order(self, symbol, order_type, price, amount):
        # Simulate order execution and log the order
        self.log_function(f"{order_type} order executed: {symbol} at {price} for {amount}")
