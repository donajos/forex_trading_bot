import psutil
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QGroupBox, QFormLayout, QHBoxLayout, QTabWidget, QMessageBox
from ui.strategy_menu import StrategyMenu  # Import the StrategyMenu widget
from platform_layer.platform_manager import initialize_platform, check_connection
from PyQt5.QtCore import QTimer
from symbol_manager import AddSymbolDialog  # Import the AddSymbolDialog
from utils.performance_utils import get_cpu_usage, get_memory_usage
from utils.logging_utils import format_log_message
class MainDashboard(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Dashboard")
        self.setGeometry(200, 200, 800, 600)

        # Main layout
        main_layout = QVBoxLayout()

        # Add a label to indicate that the dashboard is loaded
        main_layout.addWidget(QLabel("Welcome to the Trading Dashboard"))

        # Add Strategy Menu (dropdown)
        self.strategy_menu = StrategyMenu(self.start_strategy)  # Pass callback for strategy start
        main_layout.addWidget(self.strategy_menu)

        # Create a tab widget for symbol management
        self.symbol_tabs = QTabWidget()
        main_layout.addWidget(self.symbol_tabs)

        # Add button to add a symbol
        self.add_symbol_button = QPushButton("Add Symbol")
        self.add_symbol_button.clicked.connect(self.add_symbol_dialog)
        main_layout.addWidget(self.add_symbol_button)

        # Create the trade controls (Start/Stop buttons)
        self.trade_panel = QGroupBox("Trade Controls")
        trade_layout = QHBoxLayout()
        self.start_button = QPushButton("Start Trading")
        self.stop_button = QPushButton("Stop Trading")
        self.start_button.clicked.connect(self.start_trading)  # Connect start button to start_trading method
        self.stop_button.clicked.connect(self.stop_trading)  # Connect stop button to stop_trading method
        trade_layout.addWidget(self.start_button)
        trade_layout.addWidget(self.stop_button)
        self.trade_panel.setLayout(trade_layout)
        main_layout.addWidget(self.trade_panel)

        # Performance monitoring panel (CPU, memory usage)
        self.performance_panel = QGroupBox("Performance Monitoring")
        performance_layout = QFormLayout()
        self.cpu_usage_label = QLabel("CPU Usage: --%")
        self.memory_usage_label = QLabel("Memory Usage: --%")
        performance_layout.addRow(self.cpu_usage_label)
        performance_layout.addRow(self.memory_usage_label)
        self.performance_panel.setLayout(performance_layout)
        main_layout.addWidget(self.performance_panel)

        # Log Panel for showing log information
        self.log_panel = QGroupBox("Log Panel")
        self.log_label = QLabel("Logs will appear here...")
        self.log_panel.setLayout(QVBoxLayout())
        self.log_panel.layout().addWidget(self.log_label)
        main_layout.addWidget(self.log_panel)

        # Create a container widget to hold all the elements
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        # Set up a timer to update performance data every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_performance_data)
        self.timer.start(1000)  # Update every second

        # Initialize trading status
        self.trading_active = False

        # Strategy variables
        self.selected_strategy = None  # To track the selected strategy

    def add_symbol_dialog(self):
        """Open dialog to add a new symbol."""
        dialog = AddSymbolDialog(self)
        dialog.exec_()

    def add_symbol_tab(self, symbol_name):
        """Create a tab for a symbol."""
        symbol_tab = QWidget()
        symbol_layout = QVBoxLayout()
        symbol_layout.addWidget(QLabel(f"Trading {symbol_name}"))
        symbol_tab.setLayout(symbol_layout)
        self.symbol_tabs.addTab(symbol_tab, symbol_name)

    def update_performance(self):
        """Method to update performance monitoring."""
        cpu_usage = psutil.cpu_percent(interval=1)  # Get CPU usage percentage
        memory_info = psutil.virtual_memory()
        memory_usage = memory_info.percent  # Get memory usage percentage
        self.cpu_usage_label.setText(f"CPU Usage: {cpu_usage}%")
        self.memory_usage_label.setText(f"Memory Usage: {memory_usage}%")

    def update_performance_data(self):
        """Periodically update performance data in the dashboard."""
        self.update_performance()

    def log_activity(self, message):
        """Method to log activity in the log panel."""
        self.log_label.setText(message)

    def append_log(self, message):
        """Append log activity to log panel instead of overwriting."""
        current_log = self.log_label.text()
        self.log_label.setText(current_log + "\n" + message)

    def start_trading(self):
        """Simulate starting the trading process."""
        if self.trading_active:
            self.append_log("Trading is already active.")
            return

        if not self.selected_strategy:
            self.append_log("No strategy selected.")
            return

        # Start the trading logic here
        login = self.login_input.text()
        password = self.password_input.text()
        server = self.server_input.text()
        platform = self.platform_selector.currentText()

        # Check if connection is successful before starting trading
        if not check_connection(platform, login, password, server):
            self.append_log("Connection failed. Please check your credentials.")
            return

        if platform == "MT5":
            # Initialize MT5 platform
            success = initialize_platform("MT5", login, password, server)
        elif platform == "Binance":
            # Initialize Binance platform
            success = initialize_platform("Binance", login, password, server)

        if success:
            self.trading_active = True
            self.append_log(f"Trading started with {self.selected_strategy} strategy.")
            print(f"Trading started with {self.selected_strategy} strategy.")
        else:
            self.append_log("Error initializing platform.")
            print("Error initializing platform.")

    def stop_trading(self):
        """Simulate stopping the trading process."""
        if not self.trading_active:
            self.append_log("No active trading session to stop.")
            return

        # Confirmation before stopping trading
        reply = QMessageBox.question(self, "Stop Trading", "Are you sure you want to stop trading?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.append_log("Stopping trading...")
            print("Trading stopped.")
            # Disconnect from platform logic here (if needed)
            self.trading_active = False
        else:
            self.append_log("Trading stop canceled.")
            print("Trading stop canceled.")

    # New methods to handle strategy selection
    def start_strategy(self, strategy_type):
        """Start the selected trading strategy."""
        self.selected_strategy = strategy_type
        if strategy_type == "Scalping":
            self.start_scalping()
        elif strategy_type == "Day Trading":
            self.start_day_trading()
        elif strategy_type == "Swing":
            self.start_swing_trading()

    def start_scalping(self):
        """Simulate Scalping strategy."""
        self.append_log("Scalping strategy started")
        # Placeholder logic for Scalping (5M timeframes)
        print("Starting Scalping (5M) strategy")

    def start_day_trading(self):
        """Simulate Day Trading strategy."""
        self.append_log("Day Trading strategy started")
        # Placeholder logic for Day Trading (15M–1H timeframes)
        print("Starting Day Trading (15M–1H) strategy")

    def start_swing_trading(self):
        """Simulate Swing Trading strategy."""
        self.append_log("Swing Trading strategy started")
        # Placeholder logic for Swing Trading (4H–D1 timeframes)
        print("Starting Swing (4H–D1) strategy")

    def update_performance(self):
        cpu_usage = get_cpu_usage()
        memory_usage = get_memory_usage()
        self.cpu_usage_label.setText(f"CPU Usage: {cpu_usage}%")
        self.memory_usage_label.setText(f"Memory Usage: {memory_usage}%")

    def log_activity(self, message):
        self.append_log(format_log_message(message))

    def update_performance_data(self):
        """Periodically updates performance data in the dashboard."""
        self.update_performance()

    def start_trading(self):
        """
        Simulate starting the trading process.
        Connect to the platform and begin trading operations."""
        if self.trading_active:
            self.log_activity("Trading is already active.")
            return

        if not self.selected_strategy:
            self.log_activity("No strategy selected.")
            return

        # Log the connection attempt
        login = self.login_input.text()
        password = self.password_input.text()
        server = self.server_input.text()
        platform = self.platform_selector.currentText()

        self.log_activity(f"Attempting to connect to {platform} with account {login}")

        # Check if connection is successful before starting trading
        if not check_connection(platform, login, password, server):
            self.log_activity("Connection failed. Please check your credentials.")
            return

        # Initialize platform (MT5 or Binance)
        if platform == "MT5":
            success = initialize_platform("MT5", login, password, server)
        elif platform == "Binance":
            success = initialize_platform("Binance", login, password, server)

        if success:
            self.trading_active = True
            self.log_activity(f"Trading started with {self.selected_strategy} strategy.")
        else:
            self.log_activity("Error initializing platform.")
    

    def stop_trading(self):
        """
        Simulate stopping the trading process.
        Stop any ongoing trades and disconnect from the platform.
        """
        if not self.trading_active:
            self.log_activity("No active trading session to stop.")
            return

        # Confirmation before stopping trading
        reply = QMessageBox.question(self, "Stop Trading", "Are you sure you want to stop trading?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.log_activity("Stopping trading...")
            self.trading_active = False
        else:
            self.log_activity("Trading stop canceled.")


