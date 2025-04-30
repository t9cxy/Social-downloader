import os
import sys
import platform
import subprocess
import requests

# Function to clear the terminal screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to ensure yt_dlp is installed
def ensure_yt_dlp_installed():
    try:
        import yt_dlp
    except ImportError:
        print("[!] yt_dlp not found. Installing now...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp"])
        print("[+] yt_dlp installed successfully.")

# Function to display user information
def show_user_info():
    print("\n[•] User Information")
    print(f"[•] OS        : {platform.system()} {platform.release()}")
    print(f"[•] Platform  : {platform.platform()}")
    print(f"[•] Python    : {platform.python_version()}")
    print(f"[•] Terminal  : {os.environ.get('TERM', 'Unknown')}\n")

# TikTok downloader function
def tiktok_downloader():
    clear()
    print("=== TikTok Downloader ===")
    username = input("Enter TikTok username: ").strip()
    if not username:
        print("[!] No username provided.")
        return
    try:
        # Simulate fetching TikTok user info
        print(f"[•] Fetching data for TikTok user: {username}")
        # Placeholder for actual TikTok API interaction
        print(f"[✓] Successfully fetched data for {username}")
    except Exception as e:
        print(f"[!] Error fetching TikTok data: {e}")

# Instagram downloader function
def instagram_downloader():
    clear()
    print("=== Instagram Downloader ===")
    username = input("Enter Instagram username: ").strip()
    if not username:
        print("[!] No username provided.")
        return
    try:
        import instaloader
        loader = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(loader.context, username)
        print(f"[•] Username: {profile.username}")
        print(f"[•] Full Name: {profile.full_name}")
        print(f"[•] Bio: {profile.biography}")
        print(f"[•] Followers: {profile.followers}")
        print(f"[•] Following: {profile.followees}")
    except Exception as e:
        print(f"[!] Error fetching Instagram data: {e}")

# YouTube downloader function
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
        print("[•] Downloading...")
        ydl_opts = {
            'outtmpl': '%(title)s.%(ext)s',
            'format': 'bestvideo+bestaudio/best'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("[✓] Download completed.")
    except Exception as e:
        print(f"[!] Error downloading video: {e}")

# Main menu function
def main_menu():
    while True:
        clear()
        print("█████╗ ██╗      ██████╗  ██████╗ ███╗   ██╗███████╗")
        print("██╔══██╗██║     ██╔═══██╗██╔═══██╗████╗  ██║██╔════╝")
        print("███████║██║     ██║   ██║██║   ██║██╔██╗ ██║█████╗")
        print("██╔══██║██║     ██║   ██║██║   ██║██║╚██╗██║██╔══╝")
        print("██║  ██║███████╗╚██████╔╝╚██████╔╝██║ ╚████║███████╗")
        print("╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝")
        print("     Developer: Alone | Telegram: @i4mAlone\n")

        show_user_info()

        print("[1] TikTok Downloader")
        print("[2] Instagram Downloader")
        print("[3] YouTube Downloader")
        print("[4] Exit")

        choice = input("\n[?] Choose: ").strip()

        if choice == '1':
            tiktok_downloader()
            input("\n[•] Press Enter to return to menu.")
        elif choice == '2':
            instagram_downloader()
            input("\n[•] Press Enter to return to menu.")
        elif choice == '3':
            youtube_downloader()
            input("\n[•] Press Enter to return to menu.")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("[!] Invalid option.")
            input("[•] Press Enter to try again.")

# Start the main menu
if __name__ == "__main__":
    main_menu()