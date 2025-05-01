import os import requests import re from bs4 import BeautifulSoup from urllib.parse import urlparse

Define colors

RED = "\033[91m" GREEN = "\033[92m" YELLOW = "\033[93m" CYAN = "\033[96m" RESET = "\033[0m"

DOWNLOAD_DIR = "/sdcard/download"

Clear screen function

def clear(): os.system('cls' if os.name == 'nt' else 'clear')

Safe filename

def sanitize_filename(name): return re.sub(r'[^a-zA-Z0-9_- ]', '', name).strip().replace(' ', '_')

Downloader functions

def download_file(url, filename): try: if not os.path.exists(DOWNLOAD_DIR): os.makedirs(DOWNLOAD_DIR) response = requests.get(url, stream=True) filepath = os.path.join(DOWNLOAD_DIR, filename) with open(filepath, "wb") as f: for chunk in response.iter_content(chunk_size=1024): if chunk: f.write(chunk) print(f"{GREEN}[✓]{RESET} Saved to: {filepath}") except Exception as e: print(f"{RED}[!]{RESET} Download failed: {e}")

TikTok Menu

def tiktok_menu(): clear() print(f"{CYAN}TikTok Downloader{RESET}\n") print("[1] Download Video / Photo") print("[2] Download Profile Picture") print("[3] Download Sound") print("[0] Back") choice = input(f"\n{CYAN}[{YELLOW}?{CYAN}]{RESET} Choose an option: ")

if choice == '1':
    url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter TikTok Video or Photo URL: ")
    caption = get_tiktok_caption(url)
    filename = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} File name (press Enter for default: caption): ")
    if not filename:
        filename = sanitize_filename(caption or "tiktok_video") + ".mp4"
    download_file(url, filename)
elif choice == '2':
    url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter TikTok Video/Profile URL: ")
    profile_pic_url, display_name = get_tiktok_profile_pic(url)
    filename = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} File name (Enter for default: display name): ")
    if not filename:
        filename = sanitize_filename(display_name or "profile") + ".jpg"
    download_file(profile_pic_url, filename)
elif choice == '3':
    url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter TikTok Video/Sound URL: ")
    sound_url, caption = get_tiktok_sound(url)
    filename = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} File name (Enter for default: caption): ")
    if not filename:
        filename = sanitize_filename(caption or "sound") + ".mp3"
    download_file(sound_url, filename)
else:
    return

Instagram Menu

def instagram_menu(): clear() print(f"{CYAN}Instagram Downloader{RESET}\n") print("[1] Download Video / Photo") print("[2] Download Profile Picture") print("[0] Back") choice = input(f"\n{CYAN}[{YELLOW}?{CYAN}]{RESET} Choose an option: ")

if choice == '1':
    url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter Instagram post URL: ")
    media_url, caption = get_instagram_media(url)
    filename = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} File name (Enter for default: caption): ")
    if not filename:
        filename = sanitize_filename(caption or "insta_post") + ".mp4"
    download_file(media_url, filename)
elif choice == '2':
    url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter Instagram profile URL: ")
    pic_url, display_name = get_instagram_profile_pic(url)
    filename = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} File name (Enter for default: display name): ")
    if not filename:
        filename = sanitize_filename(display_name or "profile") + ".jpg"
    download_file(pic_url, filename)
else:
    return

YouTube Menu

def youtube_menu(): clear() print(f"{CYAN}YouTube Downloader{RESET}\n") print("[1] Download Video") print("[0] Back") choice = input(f"\n{CYAN}[{YELLOW}?{CYAN}]{RESET} Choose an option: ")

if choice == '1':
    url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter YouTube video URL: ")
    yt_url, title = get_youtube_video(url)
    filename = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} File name (Enter for default: title): ")
    if not filename:
        filename = sanitize_filename(title or "youtube_video") + ".mp4"
    download_file(yt_url, filename)
else:
    return

Placeholder scraping functions

def get_tiktok_caption(url): return "Funny Dance Video"

def get_tiktok_profile_pic(url): return ("https://example.com/profile.jpg", "CoolCreator")

def get_tiktok_sound(url): return ("https://example.com/sound.mp3", "Epic Sound")

def get_instagram_media(url): return ("https://example.com/insta.mp4", "Insta Post Caption")

def get_instagram_profile_pic(url): return ("https://example.com/insta_profile.jpg", "InstaUser")

def get_youtube_video(url): return ("https://example.com/youtube.mp4", "YouTube Title")

Main Menu

def main(): while True: clear() print(f"{YELLOW}====================================={RESET}") print(f"{CYAN}       Social Media Downloader{RESET}") print(f"{YELLOW}====================================={RESET}\n") print("[1] TikTok") print("[2] Instagram") print("[3] YouTube") print("[0] Exit") choice = input(f"\n{CYAN}[{YELLOW}?{CYAN}]{RESET} Choose a platform: ")

if choice == '1':
        tiktok_menu()
    elif choice == '2':
        instagram_menu()
    elif choice == '3':
        youtube_menu()
    elif choice == '0':
        break
    else:
        print(f"{RED}[!]{RESET} Invalid choice!")
        input("Press Enter to continue...")

if name == 'main': main()

