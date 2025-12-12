WiFi Lab Controller
===================

A graphical toolkit for controlled Wi-Fi testing, analysis, fake AP simulation,
DNS redirection, network scans, and educational cybersecurity demonstrations.

.. image:: https://raw.githubusercontent.com/ZahidServers/WiFi-Lab-Controller/refs/heads/main/Screenshot1.png
   :alt: WiFi Lab Controller Screenshot
   :align: center
   :width: 600px

Overview
--------

WiFi Lab Controller is a desktop GUI application built using Tkinter.  
It provides a safe demonstration environment for common wireless security concepts:

- Safe disconnect and Wi-Fi reset
- Fake Access Point (AP) generation (hostapd / dnsmasq)
- Domain redirection (DNS spoofing)
- Network scans (2.4 GHz & 5 GHz)
- Monitor mode automation (airmon-ng)
- Deauthentication demonstrations
- Log & metadata previews
- Educational security testing toolkit

**Important:**  
WiFi-Lab is intended *only for educational and controlled laboratory testing*  
on equipment you own or are explicitly authorized to test.

Contents
--------

.. toctree::
   :maxdepth: 2
   :caption: Documentation

   installation
   usage
   features
   warnings
   contributing
   author


API Reference
-------------

.. automodule:: wifilab
   :members:
   :undoc-members:
   :show-inheritance:
