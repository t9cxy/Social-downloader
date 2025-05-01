import os
import requests
from pytube import YouTube
from datetime import datetime

# Colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RESET = '\033[0m'

DOWNLOAD_PATH = "/sdcard/download"

def clear():
    os.system("clear")

def logo():
    print(f"""{CYAN}
████████╗██╗██╗  ██╗████████╗ ██████╗  ██████╗ ██╗     ███████╗
╚══██╔══╝██║██║ ██╔╝╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
   ██║   ██║█████╔╝    ██║   ██║   ██║██║   ██║██║     █████╗  
   ██║   ██║██╔═██╗    ██║   ██║   ██║██║   ██║██║     ██╔══╝  
   ██║   ██║██║  ██╗   ██║   ╚██████╔╝╚██████╔╝███████╗███████╗
   ╚═╝   ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
        {YELLOW}Developer: Alone | Telegram: @i4mAlone{RESET}
""")

def ask_filename(default_name, ext):
    name = input(f"{CYAN}[?] Custom filename (press Enter to use '{default_name}'): {RESET}").strip()
    return os.path.join(DOWNLOAD_PATH, f"{name or default_name}.{ext}")

def sanitize(text):
    return ''.join(c if c.isalnum() or c in (' ', '-', '_') else '_' for c in text).strip()

# TikTok (Placeholder)
def download_tiktok_video():
    url = input(f"\n{CYAN}[?] TikTok Video URL: {RESET}")
    caption = f"tiktok_video_{datetime.now().strftime('%H%M%S')}"
    filename = ask_filename(sanitize(caption), "mp4")
    with open(filename, 'w') as f:
        f.write("TikTok video data")
    print(f"{GREEN}[✓] Saved to: {filename}{RESET}")

def download_tiktok_photo():
    url = input(f"\n{CYAN}[?] TikTok Photo URL: {RESET}")
    caption = f"tiktok_photo_{datetime.now().strftime('%H%M%S')}"
    filename = ask_filename(sanitize(caption), "jpg")
    with open(filename, 'w') as f:
        f.write("TikTok photo data")
    print(f"{GREEN}[✓] Saved to: {filename}{RESET}")

def download_tiktok_sound():
    url = input(f"\n{CYAN}[?] TikTok Sound URL: {RESET}")
    caption = f"tiktok_sound_{datetime.now().strftime('%H%M%S')}"
    filename = ask_filename(sanitize(caption), "mp3")
    with open(filename, 'w') as f:
        f.write("TikTok sound data")
    print(f"{GREEN}[✓] Saved to: {filename}{RESET}")

def download_tiktok_pfp():
    url = input(f"\n{CYAN}[?] TikTok Profile URL: {RESET}")
    name = f"tiktok_pfp_{datetime.now().strftime('%H%M%S')}"
    filename = ask_filename(sanitize(name), "jpg")
    with open(filename, 'w') as f:
        f.write("TikTok profile picture")
    print(f"{GREEN}[✓] Saved to: {filename}{RESET}")

# Instagram (Placeholder)
def download_instagram_video():
    url = input(f"\n{CYAN}[?] Instagram Video URL: {RESET}")
    caption = f"insta_video_{datetime.now().strftime('%H%M%S')}"
    filename = ask_filename(sanitize(caption), "mp4")
    with open(filename, 'w') as f:
        f.write("Instagram video data")
    print(f"{GREEN}[✓] Saved to: {filename}{RESET}")

def download_instagram_pfp():
    url = input(f"\n{CYAN}[?] Instagram Profile URL: {RESET}")
    name = f"insta_pfp_{datetime.now().strftime('%H%M%S')}"
    filename = ask_filename(sanitize(name), "jpg")
    with open(filename, 'w') as f:
        f.write("Instagram profile picture")
    print(f"{GREEN}[✓] Saved to: {filename}{RESET}")

# YouTube
def download_youtube_video():
    url = input(f"\n{CYAN}[?] YouTube Video URL: {RESET}")
    yt = YouTube(url)
    default_name = sanitize(yt.title)
    filename = ask_filename(default_name, "mp4")
    yt.streams.get_highest_resolution().download(DOWNLOAD_PATH, filename=os.path.basename(filename))
    print(f"{GREEN}[✓] Downloaded to: {filename}{RESET}")

# Menus
def tiktok_menu():
    while True:
        print(f"""\n{CYAN}--- TikTok ---{RESET}
1. Download Video
2. Download Photo
3. Download Sound
4. Download Profile Picture
0. Back""")
        c = input(f"{CYAN}[>] Choose: {RESET}")
        if c == '1': download_tiktok_video()
        elif c == '2': download_tiktok_photo()
        elif c == '3': download_tiktok_sound()
        elif c == '4': download_tiktok_pfp()
        elif c == '0': break

def instagram_menu():
    while True:
        print(f"""\n{CYAN}--- Instagram ---{RESET}
1. Download Video
2. Download Profile Picture
0. Back""")
        c = input(f"{CYAN}[>] Choose: {RESET}")
        if c == '1': download_instagram_video()
        elif c == '2': download_instagram_pfp()
        elif c == '0': break

def youtube_menu():
    while True:
        print(f"""\n{CYAN}--- YouTube ---{RESET}
1. Download Video
0. Back""")
        c = input(f"{CYAN}[>] Choose: {RESET}")
        if c == '1': download_youtube_video()
        elif c == '0': break

def main():
    while True:
        clear()
        logo()
        print(f"""{CYAN}
1. TikTok
2. Instagram
3. YouTube
0. Exit{RESET}""")
        choice = input(f"{CYAN}[>] Choose: {RESET}")
        if choice == '1': tiktok_menu()
        elif choice == '2': instagram_menu()
        elif choice == '3': youtube_menu()
        elif choice == '0':
            print(f"{YELLOW}Goodbye!{RESET}")
            break

if __name__ == "__main__":
    main()