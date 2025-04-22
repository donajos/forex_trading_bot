# utils/log_util.py

from datetime import datetime

def format_log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"{timestamp} - {message}"
def log_activity(self, message):
        """Method to log activity in the log panel with timestamps."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"{timestamp} - {message}"
        self.append_log(log_message)

def append_log(self, message):
    """ Append log activity to the log panel instead of overwriting."""
    current_log = self.log_label.text()
    self.log_label.setText(current_log + "\n" + message)