import logging
from platform_layer.mt5_connector import initialize_mt5, check_mt5_connection, shutdown_mt5
from platform_layer.binance_connector import initialize_binance

class PlatformManager:
    def __init__(self):
        self.platform = None

    def select_platform(self, platform_name):
        if platform_name.lower() == 'mt5':
            self.platform = 'MT5'
            if not initialize_mt5():
                return False
            if not check_mt5_connection():
                return False
        else:
            logging.error(f"Platform {platform_name} not supported")
            return False
        return True
    

    

    def initialize_platform(platform_name, login, password, server):
        """Initializes the selected platform with user credentials."""
        if platform_name == "MT5":
            return initialize_mt5(login, password, server)
        elif platform_name == "Binance":
            return initialize_binance(api_key=login, secret=password)
        else:
            #raise ValueError(f"Unsupported platform: {platform_name}")
            print(f"Platform {platform} not supported")
            return False

    def close_platform(self):
        if self.platform == 'MT5':
            shutdown_mt5()
        self.platform = None
