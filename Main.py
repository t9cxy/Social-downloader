import os
import subprocess
import sys

# Function to install a package using pip if not already installed
def install_package(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"[ • ] Successfully installed {package}.")
    except subprocess.CalledProcessError:
        print(f"[ ! ] Failed to install {package}. Please install it manually.")
        sys.exit(1)

# Try importing the necessary packages, install if not found
try:
    from TikTokApi import TikTokApi
except ImportError:
    print("[ ! ] TikTokApi is not installed. Installing now...")
    install_package('TikTokApi')
    from TikTokApi import TikTokApi  # Re-import after installation

try:
    import instaloader
except ImportError:
    print("[ ! ] Instaloader is not installed. Installing now...")
    install_package('instaloader')
    import instaloader  # Re-import after installation

try:
    import yt_dlp as youtube_dl
except ImportError:
    print("[ ! ] yt-dlp is not installed. Installing now...")
    install_package('yt-dlp')
    import yt_dlp as youtube_dl  # Re-import after installation

# Initialize TikTok API
def search_tiktok(username):
    os.system("clear")
    print(f"[ • ] Searching TikTok for user: {username}\n")
    api = TikTokApi.get_instance()
    try:
        user = api.get_user(username)
        print(f"[ • ] Found TikTok user: {username}")
        print(f"[ • ] User details: {user['user']['nickname']}")
    except Exception as e:
        print(f"[ ! ] Error: {str(e)}")
    input("[ ? ] Press Enter to return to main menu...")

# Initialize Instagram scraping with Instaloader
def search_instagram(username):
    os.system("clear")
    print(f"[ • ] Searching Instagram for user: {username}\n")
    loader = instaloader.Instaloader()
    try:
        profile = instaloader.Profile.from_username(loader.context, username)
        print(f"[ • ] Found Instagram user: {profile.username}")
        print(f"[ • ] User bio: {profile.biography}")
        print(f"[ • ] Followers: {profile.followers}")
    except Exception as e:
        print(f"[ ! ] Error: {str(e)}")
    input("[ ? ] Press Enter to return to main menu...")

# Initialize YouTube scraping with yt-dlp
def search_youtube(video_url):
    os.system("clear")
    print(f"[ • ] Fetching YouTube details for video: {video_url}\n")
    try:
        ydl_opts = {
            'quiet': True,
            'extract_flat': True,
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            print(f"[ • ] Found YouTube video: {info['title']}")
            print(f"[ • ] Duration: {info['duration']} seconds")
            print(f"[ • ] Views: {info['view_count']}")
    except Exception as e:
        print(f"[ ! ] Error: {str(e)}")
    input("[ ? ] Press Enter to return to main menu...")

# TikTok function
def tiktok_menu():
    os.system("clear")
    print("[ • ] TikTok functionality is active.\n")
    username = input("[?] Enter TikTok username to search: ")
    search_tiktok(username)

# Instagram function
def instagram_menu():
    os.system("clear")
    print("[ • ] Instagram functionality is active.\n")
    username = input("[?] Enter Instagram username to search: ")
    search_instagram(username)

# YouTube function
def youtube_menu():
    os.system("clear")
    print("[ • ] YouTube functionality is active.\n")
    video_url = input("[?] Enter YouTube video URL to fetch details: ")
    search_youtube(video_url)

# Main menu loop
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

        choice = input("[?] Choose: ").strip()

        if choice == "1":
            tiktok_menu()
        elif choice == "2":
            instagram_menu()
        elif choice == "3":
            youtube_menu()
        elif choice == "0":
            print("[ • ] Exiting...")
            break
        else:
            print("[!] Invalid choice. Please try again.")
            input("[?] Press Enter to continue...")

# Run the main menu
if __name__ == "__main__":
    main_menu()