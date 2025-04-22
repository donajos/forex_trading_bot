import psutil
from PyQt5.QtWidgets import QLabel

class PerformanceMonitor:
    def __init__(self):
        self.cpu_usage_label = QLabel("CPU Usage: --%")
        self.memory_usage_label = QLabel("Memory Usage: --%")

    def update_performance(self):
        # Method to update performance monitoring
        cpu_usage = psutil.cpu_percent(interval=1)  # Get CPU usage percentage
        memory_info = psutil.virtual_memory()
        memory_usage = memory_info.percent  # Get memory usage percentage
        self.cpu_usage_label.setText(f"CPU Usage: {cpu_usage}%")
        self.memory_usage_label.setText(f"Memory Usage: {memory_usage}%")
