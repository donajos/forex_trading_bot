# Strategy selector UI
# ui/strategy_menu.py

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QMenu, QAction
from PyQt5.QtCore import Qt

class StrategyMenu(QWidget):
    def __init__(self, start_strategy_callback):
        """
        Initialize StrategyMenu and accept a callback for starting strategies.
        """
        super().__init__()

        self.setWindowTitle("Strategy Menu")

        self.start_strategy_callback = start_strategy_callback  # Callback function to start a strategy

        # Create main layout
        layout = QVBoxLayout()

        # Create strategy selector button
        self.strategy_button = QPushButton("Select Strategy", self)
        self.strategy_button.setMenu(self.create_strategy_menu())
        layout.addWidget(self.strategy_button)

        self.setLayout(layout)

    def create_strategy_menu(self):
        """
        Creates the strategy selection menu.
        """
        menu = QMenu(self)

        # SMC strategy submenu
        smc_menu = QMenu("SMC Strategy", self)
        smc_menu.addAction(self.create_timeframe_action("Scalping (5M)", self.select_scalping))
        smc_menu.addAction(self.create_timeframe_action("Day Trading (15M–1H)", self.select_day_trading))
        smc_menu.addAction(self.create_timeframe_action("Swing (4H–D1)", self.select_swing))

        # Add the SMC menu to the main menu
        menu.addMenu(smc_menu)

        return menu

    def create_timeframe_action(self, label, callback):
        """
        Creates an action for selecting a timeframe under the SMC Strategy submenu.
        """
        action = QAction(label, self)
        action.triggered.connect(callback)
        return action

    def select_scalping(self):
        print("Scalping (5M) strategy selected")
        # Call the callback to start the scalping strategy
        self.start_strategy_callback("Scalping")

    def select_day_trading(self):
        print("Day Trading (15M–1H) strategy selected")
        # Call the callback to start the day trading strategy
        self.start_strategy_callback("Day Trading")

    def select_swing(self):
        print("Swing (4H–D1) strategy selected")
        # Call the callback to start the swing trading strategy
        self.start_strategy_callback("Swing")
