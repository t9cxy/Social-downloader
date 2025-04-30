import os
import requests
from colorama import Fore, Style, init
import time

init(autoreset=True)

# Colors
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

def download_file(url, filename):
    print(f"{CYAN}[{YELLOW}•{CYAN}]{RESET} Downloading {filename}...")
    try:
        r = requests.get(url, stream=True)
        r.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"{GREEN}[✓]{RESET} Saved as: {filename}")
    except Exception as e:
        print(f"{RED}[×]{RESET} Error: {e}")

def main_menu():
    clear()
    logo()
    print(f"\n{MAGENTA}[ {YELLOW}MAIN MENU {MAGENTA}]{RESET}\n")
    print(f"{CYAN}[01]{RESET} TikTok Downloader")
    print(f"{CYAN}[02]{RESET} Instagram Downloader")
    print(f"{CYAN}[03]{RESET} Snapchat Downloader")
    print(f"{CYAN}[04]{RESET} Facebook Downloader")
    print(f"{CYAN}[05]{RESET} Exit\n")

    choice = input(f"{YELLOW}[{RED}•{YELLOW}] Select an option: {RESET}")
    if choice == "1": tiktok_menu()
    elif choice == "2": instagram_menu()
    elif choice == "3": snapchat_menu()
    elif choice == "4": facebook_menu()
    elif choice == "5":
        print(f"\n{GREEN}[✓]{RESET} Exiting...")
        time.sleep(1)
        exit()
    else:
        print(f"\n{RED}[×]{RESET} Invalid option!")
        time.sleep(1)
        main_menu()

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
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter profile pic URL: ")
        download_file(url, "tiktok_profile.jpg")
    elif opt == "2":
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter video URL: ")
        download_file(url, "tiktok_video.mp4")
    elif opt == "3":
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter photo URL: ")
        download_file(url, "tiktok_photo.jpg")
    elif opt == "4":
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter sound URL: ")
        download_file(url, "tiktok_sound.mp3")
    elif opt == "5":
        main_menu()
    else:
        tiktok_menu()

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
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter profile pic URL: ")
        download_file(url, "insta_profile.jpg")
    elif opt == "2":
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter video URL: ")
        download_file(url, "insta_video.mp4")
    elif opt == "3":
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter photo URL: ")
        download_file(url, "insta_photo.jpg")
    elif opt == "4":
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter sound URL: ")
        download_file(url, "insta_sound.mp3")
    elif opt == "5":
        main_menu()
    else:
        instagram_menu()

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
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter profile pic URL: ")
        download_file(url, "snap_profile.jpg")
    elif opt == "2":
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter video URL: ")
        download_file(url, "snap_video.mp4")
    elif opt == "3":
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter photo URL: ")
        download_file(url, "snap_photo.jpg")
    elif opt == "4":
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter sound URL: ")
        download_file(url, "snap_sound.mp3")
    elif opt == "5":
        main_menu()
    else:
        snapchat_menu()

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
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter profile pic URL: ")
        download_file(url, "fb_profile.jpg")
    elif opt == "2":
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter video URL: ")
        download_file(url, "fb_video.mp4")
    elif opt == "3":
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter photo URL: ")
        download_file(url, "fb_photo.jpg")
    elif opt == "4":
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter sound URL: ")
        download_file(url, "fb_sound.mp3")
    elif opt == "5":
        main_menu()
    else:
        facebook_menu()

# Run the script
main_menu()