import os
import sys
import platform
import subprocess
import requests
from urllib.parse import urlencode
from tqdm import tqdm

# ─── Utility Functions ─────────────────────────────────────────────────────────

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print(f"""
 █████╗ ██╗      ██████╗  ██████╗ ███╗   ██╗███████╗
██╔══██╗██║     ██╔═══██╗██╔═══██╗████╗  ██║██╔════╝
███████║██║     ██║   ██║██║   ██║██╔██╗ ██║█████╗  
██╔══██║██║     ██║   ██║██║   ██║██║╚██╗██║██╔══╝  
██║  ██║███████╗╚██████╔╝╚██████╔╝██║ ╚████║███████╗
╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝
       Developer: Alone | Telegram: @i4mAlone
""")

def pause():
    input("\n[•] Press Enter to return to menu...")

def ensure_package(pkg_name, import_name=None):
    """Install pkg_name via pip if import import_name (or pkg_name) fails."""
    try:
        __import__(import_name or pkg_name)
    except ImportError:
        print(f"[!] {pkg_name} not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg_name])

# ─── Feature Stubs ────────────────────────────────────────────────────────────

def proxy_ua_generator():
    clear(); banner()
    print("[•] Proxy & User-Agent Generator")
    # TODO: implement generator logic here
    print("[✓] (stub) Proxy/User-Agent Generator executed.")
    pause()

def send_requests():
    clear(); banner()
    print("[•] HTTP Request Sender")
    # TODO: implement request sending logic here
    print("[✓] (stub) Requests sent.")
    pause()

def look_ip_info():
    clear(); banner()
    print("[•] IP Geolocation Info")
    ip = input("[?] Enter IP (or blank for your own): ").strip() or None
    try:
        url = f"https://ipapi.co/{ip or ''}/json/"
        data = requests.get(url).json()
        for k, v in data.items():
            print(f"[•] {k.capitalize()}: {v}")
    except Exception as e:
        print(f"[!] Error: {e}")
    pause()

def social_reports():
    clear(); banner()
    print("[•] Social Reports")
    target = input("[?] Enter target username: ").strip()
    number = input("[?] Number of reports: ").strip()
    # TODO: implement social reporting here
    print(f"[✓] (stub) Reported {target} {number} times.")
    pause()

def facebook_id_extractor():
    clear(); banner()
    print("[•] Facebook IDs Extractor")
    profile = input("[?] Target profile URL/ID: ").strip()
    # TODO: implement extractor here
    print(f"[✓] (stub) Extracted friends IDs from {profile}.")
    pause()

def encryption_tool():
    clear(); banner()
    print("[•] Encrypt Code")
    lang = input("[?] Language (Python/JS/...): ").strip()
    # TODO: implement encryption logic here
    print(f"[✓] (stub) Code encrypted for {lang}.")
    pause()

# ─── Downloaders ──────────────────────────────────────────────────────────────

def tiktok_downloader():
    clear(); banner()
    print("=== TikTok Downloader ===")
    username = input("Enter TikTok username (simulated): ").strip()
    if username:
        print(f"[✓] Simulated download for TikTok user: {username}")
    else:
        print("[!] No username provided.")
    pause()

def instagram_downloader():
    clear(); banner()
    print("=== Instagram Downloader ===")
    ensure_package('instaloader')
    import instaloader
    username = input("Enter Instagram username: ").strip()
    if not username:
        print("[!] No username provided.")
        pause(); return
    try:
        loader = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(loader.context, username)
        print(f"[•] Username : {profile.username}")
        print(f"[•] Full Name: {profile.full_name}")
        print(f"[•] Bio      : {profile.biography}")
        print(f"[•] Posts    : {profile.mediacount}")
        print(f"[•] Followers: {profile.followers}")
        print(f"[•] Following: {profile.followees}")
        # Download latest post as example:
        loader.download_profile(username, profile_pic=False, download_videos=True, max_count=1)
        print(f"[✓] Downloaded latest post of {username}.")
    except Exception as e:
        print(f"[!] Error: {e}")
    pause()

def youtube_downloader():
    clear(); banner()
    print("=== YouTube Downloader ===")
    ensure_package('yt-dlp', 'yt_dlp')
    import yt_dlp
    url = input("Enter YouTube video URL: ").strip()
    if not url:
        print("[!] No URL provided."); pause(); return
    try:
        ydl_opts = {
            'outtmpl': '%(title)s.%(ext)s',
            'format': 'bestvideo+bestaudio/best'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("[✓] Download complete.")
    except Exception as e:
        print(f"[!] Error: {e}")
    pause()

# ─── System/User Info ─────────────────────────────────────────────────────────

def show_user_info():
    print("\n[•] System / User Info")
    print(f"[•] OS        : {platform.system()} {platform.release()}")
    print(f"[•] Platform  : {platform.platform()}")
    print(f"[•] Python    : {platform.python_version()}")
    print(f"[•] Terminal  : {os.environ.get('TERM', 'Unknown')}\n")

# ─── Main Menu ────────────────────────────────────────────────────────────────

def main():
    while True:
        clear(); banner()
        show_user_info()
        print("[1] Proxy & UA Generator")
        print("[2] HTTP Request Sender")
        print("[3] IP Geolocation Info")
        print("[4] Social Reports")
        print("[5] Facebook IDs Extractor")
        print("[6] Encrypt Code")
        print("[7] TikTok Downloader")
        print("[8] Instagram Downloader")
        print("[9] YouTube Downloader")
        print("[0] Exit")
        choice = input("\n[?] Choose: ").strip()

        if choice == '1':
            proxy_ua_generator()
        elif choice == '2':
            send_requests()
        elif choice == '3':
            look_ip_info()
        elif choice == '4':
            social_reports()
        elif choice == '5':
            facebook_id_extractor()
        elif choice == '6':
            encryption_tool()
        elif choice == '7':
            tiktok_downloader()
        elif choice == '8':
            instagram_downloader()
        elif choice == '9':
            youtube_downloader()
        elif choice == '0':
            print("\n[•] Bye.")
            break
        else:
            print("[!] Invalid choice.")
            pause()

if __name__ == '__main__':
    main()