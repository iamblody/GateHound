# GateHound - Port Scanner by blody
# instagram: https://instagram.com/blody.sh
# github: https://github.com/iamblody

import socket
import os
import sys
from colorama import Fore, Style, init
from datetime import datetime

init(autoreset=True)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def usage():
    print(Fore.YELLOW + "Usage: python gatehound.py <target_ip>")
    print(Fore.YELLOW + "Example: python gatehound.py 192.168.1.1")
    sys.exit()

def check_host(ip):
    try:
        socket.inet_aton(ip)
    except socket.error:
        print(Fore.RED + "[!] Invalid IP address.")
        sys.exit()

def port_scan(targetHost, targetPorts):
    print(Fore.CYAN + f"\n[🔍] Target: {targetHost}")
    print(Fore.CYAN + f"[⏳] Scan started at: {datetime.now().strftime('%H:%M:%S')}\n")
    
    for port in targetPorts:
        try:
            sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sockt.settimeout(0.5)
            result = sockt.connect_ex((targetHost, port))

            if result == 0:
                print(Fore.GREEN + f"[+] Port {port} is OPEN")
            else:
                print(Fore.RED + f"[-] Port {port} is closed")

            sockt.close()
        except KeyboardInterrupt:
            print(Fore.LIGHTRED_EX + "\n[!] Scan aborted by user.")
            break
        except socket.error:
            print(Fore.LIGHTMAGENTA_EX + "[!] Unable to connect to target.")
            break

# 🐺 Banner
banner = Fore.RED + Style.BRIGHT + """
   ██████╗  █████╗ ████████╗███████╗██╗  ██╗ ██████╗ ██╗   ██╗███╗   ██╗██████╗ 
  ██╔════╝ ██╔══██╗╚══██╔══╝██╔════╝██║  ██║██╔═══██╗██║   ██║████╗  ██║██╔══██╗
  ██║  ███╗███████║   ██║   █████╗  ███████║██║   ██║██║   ██║██╔██╗ ██║██║  ██║
  ██║   ██║██╔══██║   ██║   ██╔══╝  ██╔══██║██║   ██║██║   ██║██║╚██╗██║██║  ██║
  ╚██████╔╝██║  ██║   ██║   ███████╗██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║██████╔╝
   ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═════╝ 
                             GateHound v1.0 by blody 🐺
"""

# Entry point
if len(sys.argv) != 2:
    usage()

targetHost = sys.argv[1]
check_host(targetHost)

clear()
print(banner)

# Most common ports
targetPorts = [
    20, 21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445,
    993, 995, 873, 115, 3306, 3389, 5900, 8080, 8443,
    161, 389, 636, 1723, 1900, 6667, 8000, 10000, 5000,
    514, 27017, 135, 137
]

port_scan(targetHost, targetPorts)
