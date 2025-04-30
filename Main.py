import os
import requests
from colorama import Fore, Style, init
import time

init(autoreset=True)

# Color Definitions
RED = Fore.RED
GREEN = Fore.GREEN
CYAN = Fore.CYAN
YELLOW = Fore.YELLOW
MAGENTA = Fore.MAGENTA
BLUE = Fore.BLUE
RESET = Style.RESET_ALL
BOLD = Style.BRIGHT

# Clear screen function
def clear(): os.system('clear')

# Logo Display
def logo():
    print(f"""{CYAN}{BOLD}
     █████  ██       ██████  ███    ██ ███████ 
    ██   ██ ██      ██    ██ ████   ██ ██      
    ███████ ██      ██    ██ ██ ██  ██ █████   
    ██   ██ ██      ██    ██ ██  ██ ██ ██      
    ██   ██ ███████  ██████  ██   ████ ███████ 
    {RESET}""")


# Main Menu
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
    if choice == "1":
        tiktok_menu()
    elif choice == "2":
        instagram_menu()
    elif choice == "3":
        snapchat_menu()
    elif choice == "4":
        facebook_menu()
    elif choice == "5":
        print(f"\n{GREEN}[✓]{RESET} Exiting...")
        time.sleep(1)
        exit()
    else:
        print(f"\n{RED}[×]{RESET} Invalid option!")
        time.sleep(1)
        main_menu()

# Real download function (Placeholder)
def download_file(url, file_name):
    print(f"{CYAN}[{YELLOW}•{CYAN}] {RESET}Downloading {file_name}...")
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(file_name, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"{GREEN}[✓]{RESET} {file_name} has been downloaded successfully!")
    except requests.exceptions.RequestException as e:
        print(f"{RED}[×]{RESET} Failed to download: {e}")

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
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter TikTok profile picture URL: ")
        download_file(url, "tiktok_profile_picture.jpg")
    elif opt == "2":
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter TikTok video URL: ")
        download_file(url, "tiktok_video.mp4")
    elif opt == "3":
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter TikTok photo URL: ")
        download_file(url, "tiktok_photo.jpg")
    elif opt == "4":
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter TikTok sound URL: ")
        download_file(url, "tiktok_sound.mp3")
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
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter Instagram profile picture URL: ")
        download_file(url, "instagram_profile_picture.jpg")
    elif opt == "2":
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter Instagram video URL: ")
        download_file(url, "instagram_video.mp4")
    elif opt == "3":
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter Instagram photo URL: ")
        download_file(url, "instagram_photo.jpg")
    elif opt == "4":
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter Instagram sound URL: ")
        download_file(url, "instagram_sound.mp3")
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
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter Snapchat profile picture URL: ")
        download_file(url, "snapchat_profile_picture.jpg")
    elif opt == "2":
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter Snapchat video URL: ")
        download_file(url, "snapchat_video.mp4")
    elif opt == "3":
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter Snapchat photo URL: ")
        download_file(url, "snapchat_photo.jpg")
    elif opt == "4":
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter Snapchat sound URL: ")
        download_file(url, "snapchat_sound.mp3")
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
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter Facebook profile picture URL: ")
        download_file(url, "facebook_profile_picture.jpg")
    elif opt == "2":
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter Facebook video URL: ")
        download_file(url, "facebook_video.mp4")
    elif opt == "3":
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter