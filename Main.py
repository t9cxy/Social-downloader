import os
import requests
from pytube import YouTube
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from datetime import datetime

# Colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RESET = '\033[0m'

DOWNLOAD_PATH = "/sdcard/download"

def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

def print_logo():
    print(f"""{CYAN}
 █████╗ ██╗      ██████╗  ██████╗ ███╗   ██╗███████╗
██╔══██╗██║     ██╔═══██╗██╔═══██╗████╗  ██║██╔════╝
███████║██║     ██║   ██║██║   ██║██╔██╗ ██║█████╗
██╔══██║██║     ██║   ██║██║   ██║██║╚██╗██║██╔══╝
██║  ██║███████╗╚██████╔╝╚██████╔╝██║ ╚████║███████╗
╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝
     {YELLOW}Developer: Alone | Telegram: @i4mAlone{RESET}
""")

def ask_filename(default_name):
    custom = input(f"{CYAN}[{YELLOW}?{CYAN}] Enter custom filename or press Enter to use default ({default_name}): {RESET}").strip()
    return custom if custom else default_name

def sanitize_filename(name):
    return ''.join(c for c in name if c.isalnum() or c in ' .-_').strip()

# TikTok Placeholder Functions (Add real API logic here)
def download_tiktok_video():
    print(f"\n{CYAN}[ TikTok Video Download ]{RESET}\n")
    url = input(f"{CYAN}[{YELLOW}?{CYAN}] Paste TikTok video link: {RESET}").strip()
    caption = "tiktok_video_" + datetime.now().strftime("%Y%m%d%H%M%S")
    filename = sanitize_filename(ask_filename(caption)) + ".mp4"
    path = os.path.join(DOWNLOAD_PATH, filename)
    # Fake download
    with open(path, 'w') as f:
        f.write("TikTok video placeholder")
    print(f"{GREEN}[✓] Saved as: {path}{RESET}\n")

def download_tiktok_photo():
    print(f"\n{CYAN}[ TikTok Photo Download ]{RESET}\n")
    url = input(f"{CYAN}[{YELLOW}?{CYAN}] Paste TikTok post link: {RESET}").strip()
    filename = sanitize_filename(ask_filename("tiktok_photo")) + ".jpg"
    path = os.path.join(DOWNLOAD_PATH, filename)
    with open(path, 'w') as f:
        f.write("TikTok photo placeholder")
    print(f"{GREEN}[✓] Saved as: {path}{RESET}\n")

def download_tiktok_sound():
    print(f"\n{CYAN}[ TikTok Sound Download ]{RESET}\n")
    url = input(f"{CYAN}[{YELLOW}?{CYAN}] Paste sound link or post link: {RESET}").strip()
    filename = sanitize_filename(ask_filename("tiktok_sound")) + ".mp3"
    path = os.path.join(DOWNLOAD_PATH, filename)
    with open(path, 'w') as f:
        f.write("TikTok sound placeholder")
    print(f"{GREEN}[✓] Saved as: {path}{RESET}\n")

def download_tiktok_pfp():
    print(f"\n{CYAN}[ TikTok Profile Picture Download ]{RESET}\n")
    url = input(f"{CYAN}[{YELLOW}?{CYAN}] Paste profile link or any post link: {RESET}").strip()
    display_name = "tiktok_user_" + datetime.now().strftime("%H%M%S")
    filename = sanitize_filename(ask_filename(display_name)) + ".jpg"
    path = os.path.join(DOWNLOAD_PATH, filename)
    with open(path, 'w') as f:
        f.write("TikTok profile picture placeholder")
    print(f"{GREEN}[✓] Saved as: {path}{RESET}\n")

# Instagram Placeholder Functions
def download_instagram_video():
    print(f"\n{CYAN}[ Instagram Video Download ]{RESET}\n")
    url = input(f"{CYAN}[{YELLOW}?{CYAN}] Paste Instagram video link: {RESET}").strip()
    filename = sanitize_filename(ask_filename("instagram_video")) + ".mp4"
    path = os.path.join(DOWNLOAD_PATH, filename)
    with open(path, 'w') as f:
        f.write("Instagram video placeholder")
    print(f"{GREEN}[✓] Saved as: {path}{RESET}\n")

def download_instagram_pfp():
    print(f"\n{CYAN}[ Instagram Profile Picture Download ]{RESET}\n")
    url = input(f"{CYAN}[{YELLOW}?{CYAN}] Paste profile URL: {RESET}").strip()
    display_name = "insta_user_" + datetime.now().strftime("%H%M%S")
    filename = sanitize_filename(ask_filename(display_name)) + ".jpg"
    path = os.path.join(DOWNLOAD_PATH, filename)
    with open(path, 'w') as f:
        f.write("Instagram profile picture placeholder")
    print(f"{GREEN}[✓] Saved as: {path}{RESET}\n")

# YouTube Downloader (using pytube)
def download_youtube_video():
    print(f"\n{CYAN}[ YouTube Video Download ]{RESET}\n")
    url = input(f"{CYAN}[{YELLOW}?{CYAN}] Paste YouTube link: {RESET}").strip()
    yt = YouTube(url)
    default_title = sanitize_filename(yt.title)
    filename = ask_filename(default_title)
    yt.streams.get_highest_resolution().download(DOWNLOAD_PATH, filename + ".mp4")
    print(f"{GREEN}[✓] Downloaded: {filename}.mp4 to {DOWNLOAD_PATH}{RESET}\n")

# Submenus
def tiktok_menu():
    while True:
        print(f"""\n{CYAN}--- TikTok Options ---{RESET}
1. Download Video
2. Download Photo
3. Download Sound
4. Download Profile Picture
0. Back\n""")
        c = input(f"{CYAN}[{YELLOW}?{CYAN}] Choose: {RESET}")
        if c == '1':
            download_tiktok_video()
        elif c == '2':
            download_tiktok_photo()
        elif c == '3':
            download_tiktok_sound()
        elif c == '4':
            download_tiktok_pfp()
        elif c == '0':
            break

def instagram_menu():
    while True:
        print(f"""\n{CYAN}--- Instagram Options ---{RESET}
1. Download Video
2. Download Profile Picture
0. Back\n""")
        c = input(f"{CYAN}[{YELLOW}?{CYAN}] Choose: {RESET}")
        if c == '1':
            download_instagram_video()
        elif c == '2':
            download_instagram_pfp()
        elif c == '0':
            break

def youtube_menu():
    while True:
        print(f"""\n{CYAN}--- YouTube Options ---{RESET}
1. Download Video
0. Back\n""")
        c = input(f"{CYAN}[{YELLOW}?{CYAN}] Choose: {RESET}")
        if c == '1':
            download_youtube_video()
        elif c == '0':
            break

def main_menu():
    while True:
        clear()
        print_logo()
        print(f"""{CYAN}
[1] TikTok
[2] Instagram
[3] YouTube
[0] Exit
{RESET}""")
        choice = input(f"{CYAN}[{YELLOW}?{CYAN}] Choose: {RESET}")
        if choice == '1':
            tiktok_menu()
        elif choice == '2':
            instagram_menu()
        elif choice == '3':
            youtube_menu()
        elif choice == '0':
            print(f"{YELLOW}Exiting...{RESET}")
            break
        else:
            print(f"{RED}Invalid option!{RESET}")

if __name__ == "__main__":
    try:
        main_menu()
    except Exception as e:
        print(f"{RED}Error: {e}{RESET}")