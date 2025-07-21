# HardcodeFirewall

# Local Network Firewall Monitor

This script monitors your computer's network connections for unauthorized access attempts from other devices on your local network. If a new connection from a local IP address is detected, it displays a full-screen overlay warning of unauthorized access -> this is a very archaic firewall built from scratch 

## Features

- **Real-Time Network Monitoring:** Continuously checks for new incoming or outgoing connections.
- **Local IP Detection:** Identifies connections from common private IP ranges (192.168.x.x, 10.x.x.x, 172.16.x.x).
- **Unauthorized Access Alert:** Displays a full-screen overlay warning if a new local network connection is detected.
- **Cross-Platform:** Uses Python's standard libraries and `psutil` for compatibility.

## Requirements

- Python 3.x
- [psutil](https://pypi.org/project/psutil/)

Install the required package with:
```bash
pip install psutil
```

## Usage

Run the script with:
```bash
python firewall.py
```

The script will start monitoring your network connections. If it detects a new connection from a local IP address, it will display a full-screen warning overlay.

## How It Works

- The script uses `psutil` to monitor all network connections.
- It checks if any new connection's remote address falls within common private IP ranges.
- If such a connection is detected, a Tkinter-based full-screen overlay is shown, warning the user of unauthorized access.

## Customization

- You can modify the private IP ranges in the `is_local_ip` function to suit your network environment.
- The overlay message and appearance can be changed in the `create_overlay` function.

## Credits

- Script by [blakealmon](https://github.com/blakealmon).
- Built with [psutil](https://pypi.org/project/psutil/) and [Tkinter](https://docs.python.org/3/library/tkinter.html). 