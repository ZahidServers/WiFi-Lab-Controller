Usage Guide
===========

Launching WiFi-Lab
------------------

Run:

.. code-block:: bash

   wifilab

This opens the main GUI window with the following tabs:

Home Tab
--------

.. image:: https://raw.githubusercontent.com/ZahidServers/WiFi-Lab-Controller/refs/heads/main/Screenshot1.png
   :alt: WiFi Lab Controller Screenshot
   :align: center
   :width: 600px

Tools available:

- Safe Disconnect (disable/enable wlan0)
- Start Duplicate AP (Fake AP)
- Stop Fake AP
- Restore Normal (cleanup dnsmasq, iptables, hostapd)

Network Tab
-----------

.. image:: https://raw.githubusercontent.com/ZahidServers/WiFi-Lab-Controller/refs/heads/main/Screenshot4.png
   :alt: WiFi Lab Controller Screenshot
   :align: center
   :width: 600px

- Show network interfaces (`ip a`)
- Enable NAT (iptables MASQUERADE)

Domain Redirection
------------------

.. image:: https://raw.githubusercontent.com/ZahidServers/WiFi-Lab-Controller/refs/heads/main/Screenshot3.png
   :alt: WiFi Lab Controller Screenshot
   :align: center
   :width: 600px

Allows redirecting specific domains to a chosen IP:Port using dnsmasq rules.

Scan Networks (Mode 3 & 4)
--------------------------

.. image:: https://raw.githubusercontent.com/ZahidServers/WiFi-Lab-Controller/refs/heads/main/Screenshot2.png
   :alt: WiFi Lab Controller Screenshot
   :align: center
   :width: 600px

Performs controlled wireless scanning using airodump-ng:

- Mode 3: 2.4 GHz scan
- Mode 4: 5 GHz scan

Creates a table listing:

- BSSID  
- Channel  
- Band  
- ESSID  

Selecting a network offers a **deauth demonstration** (authorized environment only).

About Tab
---------

.. image:: https://raw.githubusercontent.com/ZahidServers/WiFi-Lab-Controller/refs/heads/main/about.png
   :alt: WiFi Lab Controller Screenshot
   :align: center
   :width: 600px

Shows author information, links, and support options.
