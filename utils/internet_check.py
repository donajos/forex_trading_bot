# Stable internet validation 
import socket

def check_internet_connection():
    try:
        # Try to connect to a well-known site (Google DNS)
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        return True
    except (socket.timeout, socket.gaierror):
        return False
