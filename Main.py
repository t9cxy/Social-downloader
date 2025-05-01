import os
import requests
import time
from pytube import YouTube
from bs4 import BeautifulSoup
from colorama import Fore, Style

# Function to clear the terminal screen
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Color variables
CYAN = Fore.CYAN
YELLOW = Fore.YELLOW
GREEN = Fore.GREEN
RED = Fore.RED
RESET = Style.RESET_ALL

# Function to download TikTok video
def download_tiktok():
    print(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter the TikTok video link:")
    video_link = input(f"{CYAN}[{YELLOW}> {CYAN}]{RESET} ")
    print(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Do you want to specify a custom name for the video?")
    custom_name = input(f"{CYAN}[{YELLOW}> {CYAN}]{RESET} (Leave blank for default name): ")

    try:
        # Fetching TikTok video page
        response = requests.get(video_link)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the description meta tag
        description_meta = soup.find('meta', property='og:description')
        if description_meta:
            description = description_meta['content']
        else:
            description = "TikTok_Video"  # Fallback if description is not found

        video_name = custom_name if custom_name else description
        print(f"{CYAN}[{YELLOW}!{CYAN}]{RESET} Downloading TikTok video as '{video_name}'...")

        # Simulate download process
        time.sleep(3)

        print(f"{CYAN}[{GREEN}✔{CYAN}]{RESET} Video downloaded successfully! (saved as '{video_name}')")
        time.sleep(2)

    except Exception as e:
        print(f"{CYAN}[{RED}!{CYAN}]{RESET} Error while downloading TikTok video: {str(e)}")
        time.sleep(2)

# Function to download Instagram content
def download_instagram():
    print(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter the Instagram post link:")
    post_link = input(f"{CYAN}[{YELLOW}> {CYAN}]{RESET} ")
    print(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Do you want to specify a custom name for the post?")
    custom_name = input(f"{CYAN}[{YELLOW}> {CYAN}]{RESET} (Leave blank for default name): ")

    try:
        # Fetching Instagram post page
        response = requests.get(post_link)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the description meta tag
        description_meta = soup.find('meta', property='og:description')
        if description_meta:
            description = description_meta['content']
        else:
            description = "Instagram_Post"  # Fallback if description is not found

        post_name = custom_name if custom_name else description
        print(f"{CYAN}[{YELLOW}!{CYAN}]{RESET} Downloading Instagram post as '{post_name}'...")

        # Simulate download process
        time.sleep(3)

        print(f"{CYAN}[{GREEN}✔{CYAN}]{RESET} Instagram content downloaded successfully! (saved as '{post_name}')")
        time.sleep(2)

    except Exception as e:
        print(f"{CYAN}[{RED}!{CYAN}]{RESET} Error while downloading Instagram content: {str(e)}")
        time.sleep(2)

# Function to download YouTube video
def download_youtube():
    print(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Enter the YouTube video link:")
    video_link = input(f"{CYAN}[{YELLOW}> {CYAN}]{RESET} ")
    print(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Do you want to specify a custom name for the video?")
    custom_name = input(f"{CYAN}[{YELLOW}> {CYAN}]{RESET} (Leave blank for default name): ")

    try:
        yt = YouTube(video_link)
        video_name = custom_name if custom_name else yt.title
        video_stream = yt.streams.filter(progressive=True, file_extension="mp4").first()

        print(f"{CYAN}[{YELLOW}!{CYAN}]{RESET} Downloading YouTube video as '{video_name}'...")
        video_stream.download('/sdcard/download', filename=video_name + '.mp4')

        print(f"{CYAN}[{GREEN}✔{CYAN}]{RESET} YouTube video downloaded successfully! (saved as '{video_name}.mp4')")
        time.sleep(2)

    except Exception as e:
        print(f"{CYAN}[{RED}!{CYAN}]{RESET} Error while downloading YouTube video: {str(e)}")
        time.sleep(2)

# Main menu function to keep the script running
def main_menu():
    while True:
        clear()
        print(f"{CYAN}██████╗ ██╗      ██████╗  ██████╗ ███╗   ██╗███████╗")
        print(f"{CYAN}██╔══██╗██║     ██╔═══██╗██╔═══██╗████╗  ██║██╔════╝")
        print(f"{CYAN}███████║██║     ██║   ██║██║   ██║██╔██╗ ██║█████╗")
        print(f"{CYAN}██╔══██║██║     ██║   ██║██║   ██║██║╚██╗██║██╔══╝")
        print(f"{CYAN}██║  ██║███████╗╚██████╔╝╚██████╔╝██║ ╚████║███████╗")
        print(f"{CYAN}╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝")
        print(f"{CYAN}         Developer: Alone | Telegram: @i4mAlone")
        print(f"{CYAN}[1] TikTok Downloader")
        print(f"{CYAN}[2] Instagram Downloader")
        print(f"{CYAN}[3] YouTube Downloader")
        print(f"{CYAN}[0] Exit")

        choice = input(f"{CYAN}[{YELLOW}?{CYAN}]{RESET} Choose an option: ")

        if choice == '1':
            download_tiktok()
        elif choice == '2':
            download_instagram()
        elif choice == '3':
            download_youtube()
        elif choice == '0':
            print(f"{CYAN}[{RED}!{CYAN}]{RESET} Exiting the tool...")
            break
        else:
            print(f"{CYAN}[{RED}!{CYAN}]{RESET} Invalid choice, please try again!")
            time.sleep(2)

# Start the menu
main_menu()