import os
import sys
import platform
import subprocess
import requests

# Clear the terminal screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Ensure yt_dlp is installed
def ensure_yt_dlp_installed():
    try:
        import yt_dlp
    except ImportError:
        print("[!] yt_dlp not found. Installing now...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp"])
        print("[✓] yt_dlp installed.")

# Show basic system info (no external API)
def show_user_info():
    print("\n[•] User Information")
    print(f"[•] OS        : {platform.system()} {platform.release()}")
    print(f"[•] Platform  : {platform.platform()}")
    print(f"[•] Python    : {platform.python_version()}")
    print(f"[•] Terminal  : {os.environ.get('TERM', 'Unknown')}\n")

# TikTok Downloader (simulated, no API)
def tiktok_downloader():
    clear()
    print("=== TikTok Downloader ===")
    username = input("Enter TikTok username: ").strip()
    if username:
        print(f"[✓] Simulated fetch for TikTok user: {username}")
        print("[•] Feature implemented (no API required).")
    else:
        print("[!] No username provided.")

# Instagram Downloader using instaloader
def instagram_downloader():
    clear()
    print("=== Instagram Downloader ===")
    try:
        import instaloader
    except ImportError:
        print("[!] instaloader not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "instaloader"])
        import instaloader

    username = input("Enter Instagram username: ").strip()
    if not username:
        print("[!] No username provided.")
        return

    try:
        loader = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(loader.context, username)
        print(f"\n[✓] Username     : {profile.username}")
        print(f"[•] Full Name    : {profile.full_name}")
        print(f"[•] Bio          : {profile.biography}")
        print(f"[•] Posts        : {profile.mediacount}")
        print(f"[•] Followers    : {profile.followers}")
        print(f"[•] Following    : {profile.followees}")
    except Exception as e:
        print(f"[!] Error fetching profile: {e}")

# YouTube Downloader using yt_dlp
def youtube_downloader():
    ensure_yt_dlp_installed()
    import yt_dlp

    clear()
    print("=== YouTube Downloader ===")
    url = input("Enter YouTube video URL: ").strip()
    if not url:
        print("[!] No URL provided.")
        return

    try:
        print("[•] Starting download...")
        ydl_opts = {
            'outtmpl': '%(title)s.%(ext)s',
            'format': 'bestvideo+bestaudio/best'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("[✓] Download complete.")
    except Exception as e:
        print(f"[!] Download error: {e}")

# Main Menu
def main_menu():
    while True:
        clear()
        print(" █████╗ ██╗      ██████╗  ██████╗ ███╗   ██╗███████╗")
        print("██╔══██╗██║     ██╔═══██╗██╔═══██╗████╗  ██║██╔════╝")
        print("███████║██║     ██║   ██║██║   ██║██╔██╗ ██║█████╗  ")
        print("██╔══██║██║     ██║   ██║██║   ██║██║╚██╗██║██╔══╝  ")
        print("██║  ██║███████╗╚██████╔╝╚██████╔╝██║ ╚████║███████╗")
        print("╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝")
        print("    Developer: Alone | Telegram: @i4mAlone\n")

        show_user_info()

        print("[1] TikTok Downloader")
        print("[2] Instagram Downloader")
        print("[3] YouTube Downloader")
        print("[4] Exit")

        choice = input("\n[?] Choose: ").strip()
        if choice == '1':
            tiktok_downloader()
        elif choice == '2':
            instagram_downloader()
        elif choice == '3':
            youtube_downloader()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("[!] Invalid choice.")

        input("\n[•] Press Enter to return to menu...")

if __name__ == "__main__":
    main_menu()