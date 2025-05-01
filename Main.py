import os
import requests
import re
from pytube import YouTube
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# Terminal Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

# Download directory
DOWNLOAD_DIR = "/sdcard/download"

# Clear screen

def clear():
    os.system("clear" if os.name != "nt" else "cls")

# ASCII Art Logo

def logo():
    clear()
    print(f"{CYAN}{BOLD}")
    print(" █████╗ ██╗      ██████╗  ██████╗ ███╗   ██╗███████╗")
    print("██╔══██╗██║     ██╔═══██╗██╔═══██╗████╗  ██║██╔════╝")
    print("███████║██║     ██║   ██║██║   ██║██╔██╗ ██║█████╗")
    print("██╔══██║██║     ██║   ██║██║   ██║██║╚██╗██║██╔══╝")
    print("██║  ██║███████╗╚██████╔╝╚██████╔╝██║ ╚████║███████╗")
    print("╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝")
    print(f"{RESET}{YELLOW}         Developer: Alone | Telegram: @i4mAlone{RESET}\n")

# Helper to sanitize filenames

def sanitize_filename(text):
    return re.sub(r'[^\w\-_\. ]', '_', text)

# TikTok Downloader (Mock)

def tiktok_menu():
    clear()
    logo()
    print(f"{CYAN}[ TikTok Options ]{RESET}\n")
    print("1. Download Video/Photo")
    print("2. Download Profile Picture")
    print("3. Download Sound (MP3/MP4)")
    print("0. Back\n")

    choice = input(f"{BLUE}[?]{RESET} Choose an option: ")
    if choice == '1':
        url = input(f"{CYAN}[?]{RESET} Enter TikTok video/photo URL: ")
        caption = input(f"{CYAN}[?]{RESET} Custom filename (leave blank to use caption): ")
        default_name = "caption_from_url"  # Placeholder
        file_name = sanitize_filename(caption) if caption.strip() else default_name
        print(f"{GREEN}[✓]{RESET} Would download video/photo as: {file_name}")
    elif choice == '2':
        url = input(f"{CYAN}[?]{RESET} Enter TikTok profile or video URL: ")
        name = input(f"{CYAN}[?]{RESET} Custom filename (leave blank for display name): ")
        default_name = "display_name_from_profile"  # Placeholder
        file_name = sanitize_filename(name) if name.strip() else default_name
        print(f"{GREEN}[✓]{RESET} Would download profile picture as: {file_name}.jpg")
    elif choice == '3':
        url = input(f"{CYAN}[?]{RESET} Enter TikTok sound/video URL: ")
        name = input(f"{CYAN}[?]{RESET} Custom filename (leave blank to use caption): ")
        default_name = "sound_caption"  # Placeholder
        file_name = sanitize_filename(name) if name.strip() else default_name
        print(f"{GREEN}[✓]{RESET} Would download sound as: {file_name}.mp3")
    else:
        return

# Instagram Downloader (Mock)

def instagram_menu():
    clear()
    logo()
    print(f"{CYAN}[ Instagram Options ]{RESET}\n")
    print("1. Download Video/Photo")
    print("2. Download Profile Picture")
    print("0. Back\n")

    choice = input(f"{BLUE}[?]{RESET} Choose an option: ")
    if choice == '1':
        url = input(f"{CYAN}[?]{RESET} Enter Instagram post URL: ")
        caption = input(f"{CYAN}[?]{RESET} Custom filename (leave blank to use caption): ")
        default_name = "insta_caption"  # Placeholder
        file_name = sanitize_filename(caption) if caption.strip() else default_name
        print(f"{GREEN}[✓]{RESET} Would download media as: {file_name}.mp4")
    elif choice == '2':
        url = input(f"{CYAN}[?]{RESET} Enter Instagram profile URL: ")
        name = input(f"{CYAN}[?]{RESET} Custom filename (leave blank to use display name): ")
        default_name = "insta_display_name"  # Placeholder
        file_name = sanitize_filename(name) if name.strip() else default_name
        print(f"{GREEN}[✓]{RESET} Would download profile picture as: {file_name}.jpg")
    else:
        return

# YouTube Downloader (Real Download)

def youtube_menu():
    clear()
    logo()
    print(f"{CYAN}[ YouTube Options ]{RESET}\n")
    print("1. Download Video")
    print("2. Download Thumbnail")
    print("0. Back\n")

    choice = input(f"{BLUE}[?]{RESET} Choose an option: ")
    if choice == '1':
        url = input(f"{CYAN}[?]{RESET} Enter YouTube video URL: ")
        yt = YouTube(url)
        name = input(f"{CYAN}[?]{RESET} Custom filename (leave blank to use caption): ")
        default_name = sanitize_filename(yt.title)
        file_name = sanitize_filename(name) if name.strip() else default_name
        yt.streams.get_highest_resolution().download(output_path=DOWNLOAD_DIR, filename=file_name + ".mp4")
        print(f"{GREEN}[✓]{RESET} Downloaded as: {file_name}.mp4")
    elif choice == '2':
        url = input(f"{CYAN}[?]{RESET} Enter YouTube video URL: ")
        yt = YouTube(url)
        thumbnail_url = yt.thumbnail_url
        name = input(f"{CYAN}[?]{RESET} Custom filename (leave blank to use title): ")
        default_name = sanitize_filename(yt.title)
        file_name = sanitize_filename(name) if name.strip() else default_name
        img_data = requests.get(thumbnail_url).content
        with open(os.path.join(DOWNLOAD_DIR, file_name + ".jpg"), 'wb') as f:
            f.write(img_data)
        print(f"{GREEN}[✓]{RESET} Thumbnail saved as: {file_name}.jpg")
    else:
        return

# Main Menu

def main_menu():
    while True:
        logo()
        print(f"{CYAN}[ Main Menu ]{RESET}\n")
        print("1. TikTok")
        print("2. Instagram")
        print("3. YouTube")
        print("0. Exit\n")

        choice = input(f"{BLUE}[?]{RESET} Choose: ")
        if choice == '1':
            tiktok_menu()
        elif choice == '2':
            instagram_menu()
        elif choice == '3':
            youtube_menu()
        elif choice == '0':
            print(f"{YELLOW}Goodbye!{RESET}")
            break
        else:
            print(f"{RED}[!] Invalid option. Try again.{RESET}")
            input("Press Enter to continue...")

if __name__ == "__main__":
    try:
        main_menu()
    except Exception as e:
        print(f"{RED}[!] Error while running the script: {e}{RESET}")
