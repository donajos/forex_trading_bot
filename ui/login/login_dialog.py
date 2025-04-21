import json
import os
from PyQt5.QtWidgets import QDialog, QLineEdit, QCheckBox, QPushButton, QVBoxLayout

class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Login")
        
        self.login_field = QLineEdit(self)
        self.password_field = QLineEdit(self)
        self.password_field.setEchoMode(QLineEdit.Password)
        
        self.remember_me_checkbox = QCheckBox("Remember Me", self)
        self.login_button = QPushButton("OK", self)
        self.login_button.clicked.connect(self.login)
        
        self.load_saved_user()
        
        layout = QVBoxLayout()
        layout.addWidget(self.login_field)
        layout.addWidget(self.password_field)
        layout.addWidget(self.remember_me_checkbox)
        layout.addWidget(self.login_button)
        self.setLayout(layout)
        
    def login(self):
        # Get the user credentials
        login = self.login_field.text()
        password = self.password_field.text()
        
        # Handle the actual login logic (to be implemented as per your logic)
        # On success, save the credentials if "Remember Me" is checked
        if self.remember_me_checkbox.isChecked():
            self.save_user_credentials(login, password)
        
        self.accept()  # Proceed to the main application
    
    def save_user_credentials(self, login, password):
        # Save credentials to settings.json file
        settings = {
            "login": login,
            "password": password
        }
        
        with open("config/settings.json", "w") as f:
            json.dump(settings, f)
        
    def load_saved_user(self):
        # Check if settings.json exists and load user credentials if present
        if os.path.exists("config/settings.json"):
            with open("config/settings.json", "r") as f:
                settings = json.load(f)
                
            if settings.get("login") and settings.get("password"):
                self.login_field.setText(settings["login"])
                self.password_field.setText(settings["password"])
                self.remember_me_checkbox.setChecked(True)  # Set the checkbox if credentials exist

