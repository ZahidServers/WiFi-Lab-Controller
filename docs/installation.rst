Installation
============

WiFi-Lab Controller supports Linux distributions such as:

- Kali Linux
- Parrot OS
- Ubuntu
- Debian
- Raspbian (Raspberry Pi)

Requirements
------------

Install system dependencies:

.. code-block:: bash

   sudo apt update
   sudo apt install python3 python3-tk \
        aircrack-ng hostapd dnsmasq network-manager xdg-utils

Optional (Raspberry Pi users):

.. code-block:: bash

   sudo systemctl enable NetworkManager
   sudo systemctl start NetworkManager

Install from PyPI
-----------------

.. code-block:: bash

   pip install wifilab

If your distribution blocks system installs (PEP 668), use:

.. code-block:: bash

   python3 -m venv venv
   source venv/bin/activate
   pip install wifilab

Or with pipx (recommended):

.. code-block:: bash

   pipx install wifilab

Run the application:

.. code-block:: bash

   wifilab
