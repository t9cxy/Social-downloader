import os
import subprocess
import sys

# Function to install missing packages
def install_package(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except subprocess.CalledProcessError:
        print(f"[!] Failed to install {package}")
        sys.exit(1)

# Ensure required packages are installed
try:
    from TikTokApi import TikTokApi
except ImportError:
    print("[!] Installing TikTokApi...")
    install_package("TikTokApi")
    from TikTokApi import TikTokApi

try:
    import instaloader
except ImportError:
    print("[!] Installing instaloader...")
    install_package("instaloader")
    import instaloader

try:
    import yt_dlp as youtube_dl
except ImportError:
    print("[!] Installing yt-dlp...")
    install_package("yt-dlp")
    import yt_dlp as youtube_dl

# TikTok handler
def tiktok_menu():
    os.system("clear")
    print("[•] TikTok Scraper\n")
    username = input("[?] Enter TikTok username: ")
    try:
        api = TikTokApi.get_instance()
        user = api.user(username=username)
        user_info = user.info()
        print(f"[•] Username: {user_info['user']['uniqueId']}")
        print(f"[•] Nickname: {user_info['user']['nickname']}")
        print(f"[•] Followers: {user_info['stats']['followerCount']}")
        print(f"[•] Videos: {user_info['stats']['videoCount']}")
    except Exception as e:
        print(f"[!] Error: {e}")
    input("\n[?] Press Enter to return...")

# Instagram handler
def instagram_menu():
    os.system("clear")
    print("[•] Instagram Scraper\n")
    username = input("[?] Enter Instagram username: ")
    try:
        loader = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(loader.context, username)
        print(f"[•] Username: {profile.username}")
        print(f"[•] Full Name: {profile.full_name}")
        print(f"[•] Bio: {profile.biography}")
        print(f"[•] Followers: {profile.followers}")
        print(f"[•] Following: {profile.followees}")
    except Exception as e:
        print(f"[!] Error: {e}")
    input("\n[?] Press Enter to return...")

# YouTube handler
def youtube_menu():
    os.system("clear")
    print("[•] YouTube Scraper\n")
    url = input("[?] Enter YouTube video URL: ")
    try:
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            print(f"[•] Title: {info.get('title')}")
            print(f"[•] Uploader: {info.get('uploader')}")
            print(f"[•] Views: {info.get('view_count')}")
            print(f"[•] Duration: {info.get('duration')}s")
    except Exception as e:
        print(f"[!] Error: {e}")
    input("\n[?] Press Enter to return...")

# Main menu
def main_menu():
    while True:
        os.system("clear")
        print("""
 █████╗ ██╗      ██████╗  ██████╗ ███╗   ██╗███████╗  
██╔══██╗██║     ██╔═══██╗██╔═══██╗████╗  ██║██╔════╝  
███████║██║     ██║   ██║██║   ██║██╔██╗ ██║█████╗    
██╔══██║██║     ██║   ██║██║   ██║██║╚██╗██║██╔══╝    
██║  ██║███████╗╚██████╔╝╚██████╔╝██║ ╚████║███████╗  
╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝  
         Developer: Alone | Telegram: @i4mAlone
""")
        print("[1] TikTok")
        print("[2] Instagram")
        print("[3] YouTube")
        print("[0] Exit\n")
        choice = input("[?] Choose: ")
        if choice == "1":
            tiktok_menu()
        elif choice == "2":
            instagram_menu()
        elif choice == "3":
            youtube_menu()
        elif choice == "0":
            print("[•] Exiting...")
            break
        else:
            print("[!] Invalid choice")
            input("[?] Press Enter to try again...")

if __name__ == "__main__":
    main_menu()