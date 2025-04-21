# Switch/remember users 
import json
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QListWidget, QDialog

class ManageUsers(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Manage Users')
        self.setGeometry(500, 300, 300, 300)

        self.init_ui()
        self.load_users()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel("Select a user to switch:")
        layout.addWidget(self.label)

        # List of users
        self.users_list = QListWidget(self)
        layout.addWidget(self.users_list)

        # Switch button
        self.switch_button = QPushButton('Switch User', self)
        self.switch_button.clicked.connect(self.switch_user)
        layout.addWidget(self.switch_button)

        # Logout button
        self.logout_button = QPushButton('Logout', self)
        self.logout_button.clicked.connect(self.logout_user)
        layout.addWidget(self.logout_button)

        self.setLayout(layout)

    def load_users(self):
        """Load saved users from a JSON file"""
        try:
            with open('users.json', 'r') as file:
                users_data = json.load(file)
                for user in users_data:
                    self.users_list.addItem(user['user_id'])
        except FileNotFoundError:
            print("No saved users found.")

    def switch_user(self):
        """Switch to the selected user"""
        selected_user = self.users_list.currentItem().text()
        print(f"Switching to user: {selected_user}")
        # In a real app, you would load user-specific preferences here.

    def logout_user(self):
        """Logout current user"""
        print("Logging out current user.")
        # Implement logout logic here (e.g., clear user session)

    def save_user(self, user_id, platform, remember_me):
        """Save user data if Remember Me is checked"""
        user_data = {
            'user_id': user_id,
            'platform': platform,
            'remember_me': remember_me
        }
        try:
            # Load existing users and append new one
            with open('users.json', 'r') as file:
                users_data = json.load(file)
        except FileNotFoundError:
            users_data = []

        users_data.append(user_data)

        # Save the updated list back to the file
        with open('users.json', 'w') as file:
            json.dump(users_data, file)

        print(f"User {user_id} saved.")

