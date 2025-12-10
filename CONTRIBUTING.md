# ✅ **CONTRIBUTING.md for WiFi-Lab-Controller**

# Contributing to WiFi-Lab-Controller

Thank you for your interest in contributing to **WiFi-Lab-Controller**, an educational Wi-Fi attack & defense lab tool built with Python + Tkinter.

⚠️ **Important:**  
This project is strictly for **educational, research, and controlled lab environments only**.  
Contributors must ensure all contributions reinforce safe and ethical usage.

---

## 🚀 Getting Started

### 1. Fork the Repository
Click **Fork** on GitHub.

### 2. Clone Your Fork
```bash
git clone https://github.com/<your-username>/WiFi-Lab-Controller.git
cd WiFi-Lab-Controller
````

### 3. Install System Dependencies

```bash
sudo apt update
sudo apt install -y python3 python3-tk aircrack-ng hostapd dnsmasq network-manager xdg-utils
```

### 4. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -e .
```

### 5. Run App Locally

```bash
python -m wifilab
```

---

## 🛠️ How You Can Contribute

### Improve GUI / UX

* Better layout, icons, interactive logs
* Status indicators
* Progress bars for scans

### Add New Features

* Network interface auto-detection
* MAC spoofing for lab testing
* Capture replay modes
* Save/export logs

### Enhance Safety

* Add warnings before dangerous operations
* Add permission checks
* Ensure no harmful actions outside controlled environments

### Improve Documentation

* Screenshots
* Tutorials
* Setup guides for Kali / Parrot / Raspberry Pi OS

### Optimize Code

* Separate logic from GUI
* Improve threading
* Add async/non-blocking scan loops

---

## 🧪 Testing Your Changes

Before submitting, confirm:

* GUI starts successfully
* Monitor-mode features work (only in supported environments)
* Fake AP start/stop works
* dnsmasq redirection works
* No errors on startup
* No dangerous default behavior

---

## 📤 Submit Your Pull Request

1. Create a descriptive branch:

```bash
git checkout -b fix/network-tab-bug
```

2. Commit your changes:

```bash
git commit -m "Fix: network interface detection bug"
```

3. Push and open a PR on GitHub:
   [https://github.com/ZahidServers/WiFi-Lab-Controller/pulls](https://github.com/ZahidServers/WiFi-Lab-Controller/pulls)

Please explain:

* What you changed
* Why
* Any risks or system dependencies

---

## 🐞 Reporting Issues

Include:

* Description of the problem
* What OS/distro
* Python version
* Whether running inside VM
* Full error log
* Screenshots if GUI-related

Open issues here:
[https://github.com/ZahidServers/WiFi-Lab-Controller/issues](https://github.com/ZahidServers/WiFi-Lab-Controller/issues)

---

## ⚠️ Ethical Notice

All work must comply with the following:

* **Only for lab environments**
* **User must own the network or have explicit permission**
* No malicious or illegal use cases
* Contributors must follow responsible security guidelines

---

## ❤️ Thank You

Your contributions help strengthen cybersecurity education and make WiFi-Lab-Controller better for students, researchers, and professionals.
