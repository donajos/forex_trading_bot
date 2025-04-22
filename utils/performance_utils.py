# Collect system metrics 
import psutil
from datetime import datetime

def get_cpu_usage():
    """Returns the current CPU usage percentage."""
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    """Returns the current memory usage percentage."""
    return psutil.virtual_memory().percent

def format_log_message(message: str) -> str:
    """Prepends timestamp to the log message."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"{timestamp} - {message}"

def update_performance(self):
    """
    Method to update performance monitoring (CPU, memory usage).
    """
    cpu_usage = psutil.cpu_percent(interval=1)  # Get CPU usage percentage
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent  # Get memory usage percentage
    self.cpu_usage_label.setText(f"CPU Usage: {cpu_usage}%")
    self.memory_usage_label.setText(f"Memory Usage: {memory_usage}%")

