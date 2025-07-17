import tkinter as tk
import psutil
import time
import ipaddress
import os
import subprocess

# Function to check if an IP address is within the local network
def is_local_ip(ip):
    try:
        local_networks = [
            ipaddress.IPv4Network('192.168.0.0/16'),  # Common private IP range
            ipaddress.IPv4Network('10.0.0.0/8'),      # Another common range
            ipaddress.IPv4Network('172.16.0.0/12')    # Private IP range used in some networks
        ]
        
        ip_addr = ipaddress.IPv4Address(ip)
        
        return any(ip_addr in network for network in local_networks)
    except Exception as e:
        return False

# Function to create a full-screen overlay
def create_overlay():
    overlay = tk.Tk()
    overlay.attributes("-fullscreen", True)  # Set to fullscreen
    overlay.configure(bg="black")  # Set background to black (you can change it to any color)
    
    # Optionally, add some text to the overlay to indicate unauthorized access
    label = tk.Label(overlay, text="Unauthorized Access Detected", fg="white", font=("Helvetica", 24))
    label.pack(expand=True)
    
    overlay.mainloop()

# Function to detect remote access and trigger the overlay
def monitor_connections():
    previous_connections = set()

    while True:
        # Get the current network connections
        current_connections = set()
        try:
            current_connections = set((conn.laddr, conn.raddr, conn.status, conn.pid) for conn in psutil.net_connections())
        except psutil.AccessDenied:
            print("Access Denied: Could not retrieve some connection details.")
            continue  # Skip this iteration and continue monitoring

        # Check for new connections
        new_connections = current_connections - previous_connections
        if new_connections:
            for conn in new_connections:
                remote_address = conn[1]

                # Only handle connections with a remote address
                if remote_address:
                    # Check if the remote IP is local (from other devices on the same Wi-Fi)
                    if is_local_ip(remote_address[0]):
                        print(f"Unauthorized access detected from local IP: {remote_address[0]}")
                        
                        # Trigger the overlay when unauthorized access is detected
                        create_overlay()

        # Update previous connections
        previous_connections = current_connections

        # Wait before the next check (set to 1 second for frequent checking)
        time.sleep(0.5)

if __name__ == "__main__":
    monitor_connections()
