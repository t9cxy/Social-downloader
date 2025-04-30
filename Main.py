# main.py

import os
import time
import requests
from colorama import Fore, Style, init

init(autoreset=True)

RED = Fore.RED
GREEN = Fore.GREEN
CYAN = Fore.CYAN
YELLOW = Fore.YELLOW
MAGENTA = Fore.MAGENTA
BLUE = Fore.BLUE
RESET = Style.RESET_ALL
BOLD = Style.BRIGHT

def clear(): os.system('clear')

def logo():
    print(f"""{CYAN}{BOLD}
     █████  ██       ██████  ███    ██ ███████ 
    ██   ██ ██      ██    ██ ████   ██ ██      
    ███████ ██      ██    ██ ██ ██  ██ █████   
    ██   ██ ██      ██    ██ ██  ██ ██ ██      
    ██   ██ ███████  ██████  ██   ████ ███████ 
    {RESET}""")


def main_menu():
    clear()
    logo()
    print(f"\n{MAGENTA}[ {YELLOW}MAIN MENU {MAGENTA}]{RESET}\n")
    print(f"{CYAN}[01]{RESET} TikTok Tools")
    print(f"{CYAN}[02]{RESET} Instagram Tools")
    print(f"{CYAN}[03]{RESET} Snapchat Tools")
    print(f"{CYAN}[04]{RESET} Facebook Tools")
    print(f"{CYAN}[05]{RESET} Exit\n")

    choice = input(f"{YELLOW}[{RED}•{YELLOW}] Select an option: {RESET}")
    if choice == "1" or choice.lower() == "tiktok":
        tiktok_menu()
    elif choice == "2" or choice.lower() == "instagram":
        instagram_menu()
    elif choice == "3" or choice.lower() == "snapchat":
        snapchat_menu()
    elif choice == "4" or choice.lower() == "facebook":
        facebook_menu()
    elif choice == "5":
        print(f"\n{GREEN}[✓]{RESET} Exiting...")
        time.sleep(1)
        exit()
    else:
        print(f"\n{RED}[×]{RESET} Invalid option!")
        time.sleep(1)
        main_menu()

# Helper function for fake downloads
def fake_download(title):
    print(f"\n{GREEN}[✓]{RESET} {title} feature selected.")
    link = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter the post/sound link: ")
    print(f"{YELLOW}[{MAGENTA}•{YELLOW}]{RESET} Processing: {link}")
    time.sleep(1.5)
    print(f"{GREEN}[✓]{RESET} Done!\n")
    input(f"{CYAN}Press Enter to return to the menu...{RESET}")
    main_menu()

# TikTok tools
def tiktok_menu():
    clear()
    logo()
    print(f"\n{MAGENTA}[ {BLUE}TIKTOK TOOLS {MAGENTA}]{RESET}\n")
    print(f"{CYAN}[01]{RESET} Download Profile Picture")
    print(f"{CYAN}[02]{RESET} Download Video")
    print(f"{CYAN}[03]{RESET} Download Photo")
    print(f"{CYAN}[04]{RESET} Download Sound")
    print(f"{CYAN}[05]{RESET} Back\n")

    opt = input(f"{YELLOW}[{RED}•{YELLOW}] Select an option: {RESET}")
    if opt == "1":
        fake_download("TikTok Profile Picture")
    elif opt == "2":
        fake_download("TikTok Video")
    elif opt == "3":
        fake_download("TikTok Photo")
    elif opt == "4":
        fake_download("TikTok Sound")
    elif opt == "5":
        main_menu()
    else:
        print(f"{RED}[×]{RESET} Invalid option!")
        time.sleep(1)
        tiktok_menu()

# Instagram tools
def instagram_menu():
    clear()
    logo()
    print(f"\n{MAGENTA}[ {BLUE}INSTAGRAM TOOLS {MAGENTA}]{RESET}\n")
    print(f"{CYAN}[01]{RESET} Download Profile Picture")
    print(f"{CYAN}[02]{RESET} Download Video")
    print(f"{CYAN}[03]{RESET} Download Photo")
    print(f"{CYAN}[04]{RESET} Download Sound")
    print(f"{CYAN}[05]{RESET} Back\n")

    opt = input(f"{YELLOW}[{RED}•{YELLOW}] Select an option: {RESET}")
    if opt == "1":
        fake_download("Instagram Profile Picture")
    elif opt == "2":
        fake_download("Instagram Video")
    elif opt == "3":
        fake_download("Instagram Photo")
    elif opt == "4":
        fake_download("Instagram Sound")
    elif opt == "5":
        main_menu()
    else:
        print(f"{RED}[×]{RESET} Invalid option!")
        time.sleep(1)
        instagram_menu()

# Snapchat tools
def snapchat_menu():
    clear()
    logo()
    print(f"\n{MAGENTA}[ {BLUE}SNAPCHAT TOOLS {MAGENTA}]{RESET}\n")
    print(f"{CYAN}[01]{RESET} Download Profile Picture")
    print(f"{CYAN}[02]{RESET} Download Video")
    print(f"{CYAN}[03]{RESET} Download Photo")
    print(f"{CYAN}[04]{RESET} Download Sound")
    print(f"{CYAN}[05]{RESET} Back\n")

    opt = input(f"{YELLOW}[{RED}•{YELLOW}] Select an option: {RESET}")
    if opt == "1":
        fake_download("Snapchat Profile Picture")
    elif opt == "2":
        fake_download("Snapchat Video")
    elif opt == "3":
        fake_download("Snapchat Photo")
    elif opt == "4":
        fake_download("Snapchat Sound")
    elif opt == "5":
        main_menu()
    else:
        print(f"{RED}[×]{RESET} Invalid option!")
        time.sleep(1)
        snapchat_menu()

# Facebook tools
def facebook_menu():
    clear()
    logo()
    print(f"\n{MAGENTA}[ {BLUE}FACEBOOK TOOLS {MAGENTA}]{RESET}\n")
    print(f"{CYAN}[01]{RESET} Download Profile Picture")
    print(f"{CYAN}[02]{RESET} Download Video")
    print(f"{CYAN}[03]{RESET} Download Photo")
    print(f"{CYAN}[04]{RESET} Download Sound")
    print(f"{CYAN}[05]{RESET} Back\n")

    opt = input(f"{YELLOW}[{RED}•{YELLOW}] Select an option: {RESET}")
    if opt == "1":
        fake_download("Facebook Profile Picture")
    elif opt == "2":
        fake_download("Facebook Video")
    elif opt == "3":
        fake_download("Facebook Photo")
    elif opt == "4":
        fake_download("Facebook Sound")
    elif opt == "5":
        main_menu()
    else:
        print(f"{RED}[×]{RESET} Invalid option!")
        time.sleep(1)
        facebook_menu()

# Start
if __name__ == "__main__":
    main_menu()