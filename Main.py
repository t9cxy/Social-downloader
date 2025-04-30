import os
import sys
import requests
import platform
import subprocess

# Function to clear the terminal screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Check and install yt_dlp if not present
def ensure_yt_dlp_installed():
    try:
        import yt_dlp
    except ImportError:
        print("[!] yt_dlp not found. Installing now...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp"])
        print("[+] yt_dlp installed successfully.")

# Display user info (no API used)
def show_user_info():
    print("\n[•] User Information")
    print(f"[•] OS        : {platform.system()} {platform.release()}")
    print(f"[•] Platform  : {platform.platform()}")
    print(f"[•] Python    : {platform.python_version()}")
    print(f"[•] Terminal  : {os.environ.get('TERM', 'Unknown')}\n")

# YouTube downloader
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

# Function to fetch and execute the code from GitHub
def fetch_and_run_code(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        exec(response.text)
    except requests.RequestException as e:
        print(f"[!] Error fetching script: {e}")
    except Exception as e:
        print(f"[!] Error executing the script: {e}")

# Main menu
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
            print("[!] TikTok feature under update.")
        elif choice == '2':
            print("[!] Instagram feature under update.")
        elif choice == '3':
            youtube_downloader()
            input("\n[•] Press Enter to return to menu.")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("[!] Invalid option.")
            input("[•] Press Enter to try again.")

# Run the fetch code from GitHub if needed
# github_raw_url = "https://raw.githubusercontent.com/t9cxy/Social-downloader/refs/heads/main/Main.py"
# fetch_and_run_code(github_raw_url)

# Start the menu
main_menu()