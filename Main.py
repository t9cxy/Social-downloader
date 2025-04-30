import os
import requests
from colorama import Fore, Style, init
import time

# Initialize colorama
init(autoreset=True)

# Colors for output
RED = Fore.RED
GREEN = Fore.GREEN
CYAN = Fore.CYAN
YELLOW = Fore.YELLOW
MAGENTA = Fore.MAGENTA
BLUE = Fore.BLUE
RESET = Style.RESET_ALL
BOLD = Style.BRIGHT

DOWNLOAD_DIR = "/sdcard/download"  # Directory to save files

def clear():
    os.system('clear')

def logo():
    print(f"""{CYAN}{BOLD}
     █████  ██       ██████  ███    ██ ███████ 
    ██   ██ ██      ██    ██ ████   ██ ██      
    ███████ ██      ██    ██ ██ ██  ██ █████   
    ██   ██ ██      ██    ██ ██  ██ ██ ██      
    ██   ██ ███████  ██████  ██   ████ ███████ 
    {RESET}""")

def download_file(url, filename):
    print(f"{CYAN}[{YELLOW}•{CYAN}]{RESET} Downloading {filename}...")
    try:
        r = requests.get(url, stream=True)
        r.raise_for_status()
        file_path = os.path.join(DOWNLOAD_DIR, filename)
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"{GREEN}[✓]{RESET} Saved as: {file_path}")
    except Exception as e:
        print(f"{RED}[×]{RESET} Error: {e}")

def get_filename_from_caption_or_display_name(url, default_name="video"):
    # Here, you can extract video caption or display name from the URL.
    # For this example, I’ll use a placeholder since the real implementation will depend on API integration or scraping the data.
    video_caption = "Sample Video Caption"  # This is a placeholder
    display_name = "Sample_Display_Name"   # This is a placeholder
    
    # If you want to use the display name or caption (fallback)
    filename = video_caption if video_caption else display_name

    print(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Use this default filename: {filename}? (y/n): ", end="")
    user_input = input().strip().lower()

    if user_input == 'n':
        filename = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter a custom filename (without extension): ")
    
    return f"{filename}.mp4"  # Adjust the extension based on the file type (video, photo, etc.)

def main_menu():
    clear()
    logo()
    print(f"\n{MAGENTA}[ {YELLOW}MAIN MENU {MAGENTA}]{RESET}\n")
    print(f"{CYAN}[01]{RESET} TikTok Downloader")
    print(f"{CYAN}[02]{RESET} Instagram Downloader")
    print(f"{CYAN}[03]{RESET} Snapchat Downloader")
    print(f"{CYAN}[04]{RESET} Facebook Downloader")
    print(f"{CYAN}[05]{RESET} Exit\n")

    choice = input(f"{YELLOW}[{RED}•{YELLOW}] Select an option: {RESET}")
    if choice == "1": tiktok_menu()
    elif choice == "2": instagram_menu()
    elif choice == "3": snapchat_menu()
    elif choice == "4": facebook_menu()
    elif choice == "5":
        print(f"\n{GREEN}[✓]{RESET} Exiting...")
        time.sleep(1)
        exit()
    else:
        print(f"\n{RED}[×]{RESET} Invalid option!")
        time.sleep(1)
        main_menu()

def tiktok_menu():
    clear()
    logo()
    print(f"\n{MAGENTA}[ {BLUE}TIKTOK TOOLS {MAGENTA}]{RESET}\n")
    print(f"{CYAN}[01]{RESET} Download Profile Picture")
    print(f"{CYAN}[02]{RESET} Download Video")
    print(f"{CYAN}[03]{RESET} Download Photo")
    print(f"{CYAN}[04]{RESET} Download Sound")
    print(f"{CYAN}[05]{RESET} Back\n")

    opt = input(f"{YELLOW}[{RED}•{YELLOW}] Select an option: {RESET}")
    if opt == "1":
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter profile pic URL: ")
        filename = get_filename_from_caption_or_display_name(url, "tiktok_profile")
        download_file(url, filename)
    elif opt == "2":
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter video URL: ")
        filename = get_filename_from_caption_or_display_name(url, "tiktok_video")
        download_file(url, filename)
    elif opt == "3":
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter photo URL: ")
        filename = get_filename_from_caption_or_display_name(url, "tiktok_photo")
        download_file(url, filename)
    elif opt == "4":
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter sound URL: ")
        filename = get_filename_from_caption_or_display_name(url, "tiktok_sound")
        download_file(url, filename)
    elif opt == "5":
        main_menu()
    else:
        tiktok_menu()

def instagram_menu():
    clear()
    logo()
    print(f"\n{MAGENTA}[ {BLUE}INSTAGRAM TOOLS {MAGENTA}]{RESET}\n")
    print(f"{CYAN}[01]{RESET} Download Profile Picture")
    print(f"{CYAN}[02]{RESET} Download Video")
    print(f"{CYAN}[03]{RESET} Download Photo")
    print(f"{CYAN}[04]{RESET} Download Sound")
    print(f"{CYAN}[05]{RESET} Back\n")

    opt = input(f"{YELLOW}[{RED}•{YELLOW}] Select an option: {RESET}")
    if opt == "1":
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter profile pic URL: ")
        filename = get_filename_from_caption_or_display_name(url, "insta_profile")
        download_file(url, filename)
    elif opt == "2":
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter video URL: ")
        filename = get_filename_from_caption_or_display_name(url, "insta_video")
        download_file(url, filename)
    elif opt == "3":
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter photo URL: ")
        filename = get_filename_from_caption_or_display_name(url, "insta_photo")
        download_file(url, filename)
    elif opt == "4":
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter sound URL: ")
        filename = get_filename_from_caption_or_display_name(url, "insta_sound")
        download_file(url, filename)
    elif opt == "5":
        main_menu()
    else:
        instagram_menu()

def snapchat_menu():
    clear()
    logo()
    print(f"\n{MAGENTA}[ {BLUE}SNAPCHAT TOOLS {MAGENTA}]{RESET}\n")
    print(f"{CYAN}[01]{RESET} Download Profile Picture")
    print(f"{CYAN}[02]{RESET} Download Video")
    print(f"{CYAN}[03]{RESET} Download Photo")
    print(f"{CYAN}[04]{RESET} Download Sound")
    print(f"{CYAN}[05]{RESET} Back\n")

    opt = input(f"{YELLOW}[{RED}•{YELLOW}] Select an option: {RESET}")
    if opt == "1":
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter profile pic URL: ")
        filename = get_filename_from_caption_or_display_name(url, "snap_profile")
        download_file(url, filename)
    elif opt == "2":
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter video URL: ")
        filename = get_filename_from_caption_or_display_name(url, "snap_video")
        download_file(url, filename)
    elif opt == "3":
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter photo URL: ")
        filename = get_filename_from_caption_or_display_name(url, "snap_photo")
        download_file(url, filename)
    elif opt == "4":
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter sound URL: ")
        filename = get_filename_from_caption_or_display_name(url, "snap_sound")
        download_file(url, filename)
    elif opt == "5":
        main_menu()
    else:
        snapchat_menu()

def facebook_menu():
    clear()
    logo()
    print(f"\n{MAGENTA}[ {BLUE}FACEBOOK TOOLS {MAGENTA}]{RESET}\n")
    print(f"{CYAN}[01]{RESET} Download Profile Picture")
    print(f"{CYAN}[02]{RESET} Download Video")
    print(f"{CYAN}[03]{RESET} Download Photo")
    print(f"{CYAN}[04]{RESET} Download Sound")
    print(f"{CYAN}[05]{RESET} Back\n")

    opt = input(f"{YELLOW}[{RED}•{YELLOW}] Select an option: {RESET}")
    if opt == "1":
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter profile pic URL: ")
        filename = get_filename_from_caption_or_display_name(url, "fb_profile")
        download_file(url, filename)
    elif opt == "2":
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter video URL: ")
        filename = get_filename_from_caption_or_display_name(url, "fb_video")
        download_file(url, filename)
    elif opt == "3":
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter photo URL: ")
        filename = get_filename_from_caption_or_display_name(url, "fb_photo")
        download_file(url, filename)
    elif opt == "4":
        url = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter sound URL: ")
        filename = get_filename_from_caption_or_display_name(url, "fb_sound")
        download_file(url, filename)
    elif opt == "5":
        main_menu()
    else:
        facebook_menu()

if __name__ == "__main__":
    main_menu()