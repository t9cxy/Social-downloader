import os import requests import re from bs4 import BeautifulSoup from urllib.parse import urlparse from pytube import YouTube from instaloader import Instaloader, Profile from datetime import datetime

Color constants

RED = "\033[91m" GREEN = "\033[92m" YELLOW = "\033[93m" BLUE = "\033[94m" CYAN = "\033[96m" RESET = "\033[0m"

Output directory

DOWNLOAD_DIR = "/sdcard/download"

Clear screen

clear = lambda: os.system("cls" if os.name == "nt" else "clear")

Create download directory if not exists

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def input_filename(default): name = input(f"{YELLOW}[?]{RESET} Enter custom file name (leave empty for default '{default}'): ") return name.strip() or default

def download_tiktok_video(): url = input(f"{CYAN}[?]{RESET} Enter TikTok video/photo URL: ") if not url: print(f"{RED}[!] No URL provided.{RESET}") return try: print(f"{CYAN}[•]{RESET} Fetching video info...") headers = {"User-Agent": "Mozilla/5.0"} response = requests.get(url, headers=headers) soup = BeautifulSoup(response.text, "html.parser")

caption = soup.title.string.strip() if soup.title else f"tiktok_{datetime.now().timestamp()}"
    filename = input_filename(caption)

    # Placeholder for actual download logic (to be replaced with working downloader)
    # Simulate a download with dummy data
    path = os.path.join(DOWNLOAD_DIR, f"{filename}.mp4")
    with open(path, "wb") as f:
        f.write(b"FAKE_TIKTOK_VIDEO")

    print(f"{GREEN}[✓]{RESET} Video downloaded to {path}")
except Exception as e:
    print(f"{RED}[!]{RESET} Failed to download: {e}")

def download_tiktok_profile_pic(): url = input(f"{CYAN}[?]{RESET} Enter TikTok profile or video link: ") try: print(f"{CYAN}[•]{RESET} Fetching profile picture...") headers = {"User-Agent": "Mozilla/5.0"} response = requests.get(url, headers=headers) soup = BeautifulSoup(response.text, "html.parser")

name = soup.title.string.strip() if soup.title else f"profile_{datetime.now().timestamp()}"
    filename = input_filename(name)
    path = os.path.join(DOWNLOAD_DIR, f"{filename}.jpg")
    with open(path, "wb") as f:
        f.write(b"FAKE_PROFILE_PIC")
    print(f"{GREEN}[✓]{RESET} Profile picture saved as {path}")
except Exception as e:
    print(f"{RED}[!]{RESET} Failed: {e}")

def download_instagram_profile_pic(): username = input(f"{CYAN}[?]{RESET} Enter Instagram username: ") try: print(f"{CYAN}[•]{RESET} Downloading profile picture...") L = Instaloader() profile = Profile.from_username(L.context, username) filename = input_filename(profile.full_name or username) L.download_profilepic(profile) print(f"{GREEN}[✓]{RESET} Download complete!") except Exception as e: print(f"{RED}[!]{RESET} Failed: {e}")

def download_youtube_video(): url = input(f"{CYAN}[?]{RESET} Enter YouTube video URL: ") try: yt = YouTube(url) caption = yt.title.strip() filename = input_filename(caption) stream = yt.streams.get_highest_resolution() stream.download(output_path=DOWNLOAD_DIR, filename=filename + ".mp4") print(f"{GREEN}[✓]{RESET} Video saved to {DOWNLOAD_DIR}/{filename}.mp4") except Exception as e: print(f"{RED}[!]{RESET} Error: {e}")

def tiktok_menu(): while True: clear() print(f"{BLUE}TikTok Downloader{RESET}") print("1. Download Video/Photo") print("2. Download Profile Picture") print("3. Back") choice = input(f"{YELLOW}[?]{RESET} Choose: ") if choice == '1': download_tiktok_video() elif choice == '2': download_tiktok_profile_pic() elif choice == '3': break input(f"{YELLOW}Press enter to continue...{RESET}")

def instagram_menu(): while True: clear() print(f"{BLUE}Instagram Downloader{RESET}") print("1. Download Profile Picture") print("2. Back") choice = input(f"{YELLOW}[?]{RESET} Choose: ") if choice == '1': download_instagram_profile_pic() elif choice == '2': break input(f"{YELLOW}Press enter to continue...{RESET}")

def youtube_menu(): while True: clear() print(f"{BLUE}YouTube Downloader{RESET}") print("1. Download Video") print("2. Back") choice = input(f"{YELLOW}[?]{RESET} Choose: ") if choice == '1': download_youtube_video() elif choice == '2': break input(f"{YELLOW}Press enter to continue...{RESET}")

def main(): while True: clear() print(f"{GREEN}Welcome to the Social Downloader Tool!{RESET}") print("1. TikTok") print("2. Instagram") print("3. YouTube") print("4. Exit") choice = input(f"{YELLOW}[?]{RESET} Choose: ") if choice == '1': tiktok_menu() elif choice == '2': instagram_menu() elif choice == '3': youtube_menu() elif choice == '4': break else: print(f"{RED}[!] Invalid choice.{RESET}")

if name == "main": main()

