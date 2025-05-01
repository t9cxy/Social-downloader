import os
import requests
import re
from urllib.parse import urlparse

DOWNLOAD_DIR = "/sdcard/download"

def clear(): os.system("clear" if os.name != "nt" else "cls")

def sanitize_filename(name): return re.sub(r'[\/*?:"<>|]', "", name)

def download_file(url, default_name): print(f"\n[?] Enter custom filename (leave blank to use default: '{default_name}'): ", end="") custom_name = input().strip() file_name = sanitize_filename(custom_name if custom_name else default_name) ext = os.path.splitext(urlparse(url).path)[1] path = os.path.join(DOWNLOAD_DIR, f"{file_name}{ext}")

try:
    print(f"[•] Downloading to {path} ...")
    r = requests.get(url, stream=True)
    r.raise_for_status()
    with open(path, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"[✓] Download completed: {path}\n")
except Exception as e:
    print(f"[!] Download failed: {e}\n")

def download_tiktok(): clear() print("\n=== TikTok Options ===") print("[1] Download Video/Photo") print("[2] Download Profile Picture") print("[3] Download Sound (MP3/MP4)") print("[0] Back") choice = input("\nChoose: ")

if choice == "1":
    url = input("Enter TikTok post link: ").strip()
    caption = "tiktok_video"  # Placeholder
    download_file(url, caption)

elif choice == "2":
    url = input("Enter TikTok profile or video link: ").strip()
    display_name = "tiktok_user"  # Placeholder
    download_file(url, display_name)

elif choice == "3":
    url = input("Enter TikTok sound link: ").strip()
    sound_title = "tiktok_sound"  # Placeholder
    download_file(url, sound_title)

def download_instagram(): clear() print("\n=== Instagram Options ===") print("[1] Download Post (Video/Photo)") print("[2] Download Profile Picture") print("[0] Back") choice = input("\nChoose: ")

if choice == "1":
    url = input("Enter Instagram post link: ").strip()
    caption = "instagram_post"  # Placeholder
    download_file(url, caption)

elif choice == "2":
    url = input("Enter Instagram profile link: ").strip()
    display_name = "instagram_user"  # Placeholder
    download_file(url, display_name)

def download_youtube(): clear() print("\n=== YouTube Options ===") print("[1] Download Video") print("[2] Download Thumbnail") print("[0] Back") choice = input("\nChoose: ")

if choice == "1":
    url = input("Enter YouTube video link: ").strip()
    caption = "youtube_video"  # Placeholder
    download_file(url, caption)

elif choice == "2":
    url = input("Enter YouTube video link (to get thumbnail): ").strip()
    video_id = url.split("v=")[-1][:11]
    thumb_url = f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
    download_file(thumb_url, f"youtube_thumb_{video_id}")

def main(): os.makedirs(DOWNLOAD_DIR, exist_ok=True) while True: clear() print(""" ███████╗██╗████████╗ ██████╗ ██╗  ██╗ ██╔════╝██║╚══██╔══╝██╔═══██╗██║ ██╔╝ █████╗  ██║   ██║   ██║   ██║█████╔╝ ██╔══╝  ██║   ██║   ██║   ██║██╔═██╗ ███████╗██║   ██║   ╚██████╔╝██║  ██╗ ╚══════╝╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝ Downloader by @i4mAlone """) print("[1] TikTok") print("[2] Instagram") print("[3] YouTube") print("[0] Exit\n") choice = input("Choose: ")

if choice == "1":
        download_tiktok()
    elif choice == "2":
        download_instagram()
    elif choice == "3":
        download_youtube()
    elif choice == "0":
        break
    else:
        print("[!] Invalid choice")

if name == "main": main()

