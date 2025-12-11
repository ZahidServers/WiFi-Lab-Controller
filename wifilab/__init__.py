"""
WiFi Lab Controller - Educational Wi-Fi lab toolkit.

This package provides a Tkinter-based GUI to control Wi-Fi lab modes,
network tools, domain redirection, and scanning features.
"""

from .app import main

__version__ = "1.1.2"
__all__ = ["main", "__version__"]

def run():
    """Entry point for python -m wifilab"""
    return main()
