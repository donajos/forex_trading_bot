import sys
import json
import os
from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QFormLayout, QCheckBox)
from platform_layer.platform_manager import initialize_platform  # Ensure platform_manager is imported
from ui.dashboard.main_dashboard import MainDashboard  # Import the dashboard

class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 300, 200)

        # Initialize UI components
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        form_layout = QFormLayout()

        self.login_input = QLineEdit(self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)

        self.server_input = QLineEdit(self)

        # Platform selection combo box
        self.platform_selector = QComboBox(self)
        self.platform_selector.addItems(["MT5", "Binance"])  # Add platforms

        self.remember_me_checkbox = QCheckBox("Remember Me", self)

        form_layout.addRow("Login:", self.login_input)
        form_layout.addRow("Password:", self.password_input)
        form_layout.addRow("Server:", self.server_input)
        form_layout.addRow("Platform:", self.platform_selector)
        form_layout.addRow(self.remember_me_checkbox)

        self.login_button = QPushButton("OK", self)
        self.login_button.clicked.connect(self.handle_login)

        layout.addLayout(form_layout)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

        self.load_saved_user()  # Load saved credentials if available

    def handle_login(self):
        login = self.login_input.text()
        password = self.password_input.text()
        server = self.server_input.text()
        platform = self.platform_selector.currentText()

        if platform == "MT5":
            # Initialize MT5 platform
            success = initialize_platform("MT5", login, password, server)
        elif platform == "Binance":
            # Initialize Binance platform
            success = initialize_platform("Binance", login, password, server)

        if success:
            print("Platform initialized successfully!")
            if self.remember_me_checkbox.isChecked():
                self.save_user_credentials(login, password, server)
            self.accept()  # Proceed to the main application
            self.show_main_dashboard()  # Show the main dashboard
        else:
            print("Error initializing platform.")
            self.reject()

    def save_user_credentials(self, login, password, server):
        # Save credentials to settings.json file
        settings = {
            "login": login,
            "password": password,
            "server": server
        }

        with open("config/settings.json", "w") as f:
            json.dump(settings, f)

    def load_saved_user(self):
        # Check if settings.json exists and load user credentials if present
        if os.path.exists("config/settings.json"):
            with open("config/settings.json", "r") as f:
                settings = json.load(f)

            if settings.get("login") and settings.get("password") and settings.get("server"):
                self.login_input.setText(settings["login"])
                self.password_input.setText(settings["password"])
                self.server_input.setText(settings["server"])
                self.remember_me_checkbox.setChecked(True)  # Set the checkbox if credentials exist

    def show_main_dashboard(self):
        # Create and show the main dashboard after successful login
        self.main_dashboard = MainDashboard()
        self.main_dashboard.show()
        self.close()  # Close the login dialog
