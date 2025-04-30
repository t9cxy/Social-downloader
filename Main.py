import os
import time
import random
from colorama import Fore, init

init(autoreset=True)

def clear():
    os.system("clear" if os.name == "posix" else "cls")

def fast_print(text, delay=0.001):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def banner():
    print(Fore.GREEN + """
██╗  ██╗ █████╗ ██╗      ██████╗ ███╗   ███╗███████╗
██║ ██╔╝██╔══██╗██║     ██╔═══██╗████╗ ████║██╔════╝
█████╔╝ ███████║██║     ██║   ██║██╔████╔██║█████╗  
██╔═██╗ ██╔══██║██║     ██║   ██║██║╚██╔╝██║██╔══╝  
██║  ██╗██║  ██║███████╗╚██████╔╝██║ ╚═╝ ██║███████╗
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝
""" + Fore.LIGHTBLACK_EX + "            [ Underground Attack Suite v1.0 ]\n")

options = [
    "TikTok Server Overload",
    "Instagram Bruteforce",
    "Facebook ID Scraper",
    "Telegram DDoS",
    "Snapchat Packet Flood",
    "WhatsApp Session Hijack",
    "Gmail Login Cracker",
    "IP Logger Deployment",
    "Deep Web Scan",
    "Botnet Expansion",
    "UDP Packet Storm",
    "SYN Flood Protocol",
    "Port Scanner",
    "MAC Spoofer",
    "DNS Poison Injector",
    "Anonymous Proxy Rotator",
    "Firewall Bypass",
    "API Key Sniffer",
    "Reverse Shell Spawner",
    "Zero Day Hunter"
]

def menu():
    for i, opt in enumerate(options, start=1):
        print(Fore.CYAN + f"[{i:02}] {opt}")
    print(Fore.RED + "[00] Exit\n")

def fake_ip():
    return f"{random.randint(11, 250)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}"

def launch_attack(opt_name):
    print(Fore.RED + f"\n[!] Executing: {opt_name}")
    time.sleep(1)
    print(Fore.YELLOW + "[*] Initiating attack environment...")
    time.sleep(1)

    targets = [fake_ip() for _ in range(10)]
    methods = ['UDP-FLOOD', 'XMAS', 'HTTP-GET', 'ICMP-OVERLOAD', 'SYN-BOMB']

    for i in range(300):
        ip = random.choice(targets)
        method = random.choice(methods)
        port = random.randint(20, 9000)
        pkt = random.randint(100, 10000)
        log = f"[+] {method} | {pkt} packets => {ip}:{port}"
        print(Fore.GREEN + log)
        time.sleep(0.005)

    print(Fore.CYAN + "\n[✓] Operation complete.\n")
    input(Fore.LIGHTBLACK_EX + "[ Press Enter to return to menu... ]")

def main():
    while True:
        clear()
        banner()
        menu()
        try:
            choice = input(Fore.LIGHTGREEN_EX + "\n[>] Select option: ")
            if choice == "00":
                print(Fore.LIGHTRED_EX + "\n[!] Exiting...")
                break
            elif choice.isdigit() and 1 <= int(choice) <= 20:
                launch_attack(options[int(choice) - 1])
            else:
                print(Fore.RED + "[!] Invalid option.")
                time.sleep(1.5)
        except:
            print(Fore.RED + "[!] Unexpected error.")
            time.sleep(1.5)

if __name__ == "__main__":
    main()