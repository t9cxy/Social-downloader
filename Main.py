import os
import time
import requests
from bs4 import BeautifulSoup
from pytube import YouTube
from colorama import Fore, Style

# Terminal clear
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Colors
CYAN = Fore.CYAN
YELLOW = Fore.YELLOW
GREEN = Fore.GREEN
RED = Fore.RED
RESET = Style.RESET_ALL

# TikTok downloader
def download_tiktok():
    print(f"{CYAN}[?]{RESET} Enter the TikTok video link:")
    url = input(f"{CYAN}[>]{RESET} ")

    print(f"{CYAN}[?]{RESET} Do you want to specify a custom name?")
    custom_name = input(f"{CYAN}[>]{RESET} (Leave blank for default name): ").strip()

    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        desc_tag = soup.find("meta", property="og:description")

        if not desc_tag or not desc_tag.get("content"):
            print(f"{RED}[!]{RESET} Failed to extract video caption. Cannot continue.")
            time.sleep(2)
            return

        default_name = desc_tag['content'].split('#')[0].strip()  # remove hashtags if present
        file_name = custom_name if custom_name else default_name

        print(f"{CYAN}[!]{RESET} Downloading TikTok video as '{file_name}.mp4'...")
        time.sleep(2)
        # Simulate saving
        with open(f"/sdcard/download/{file_name}.mp4", "w") as f:
            f.write("FAKE VIDEO DATA")  # Replace with real video logic

        print(f"{CYAN}[✓]{RESET} Saved as {file_name}.mp4")
        time.sleep(2)

    except Exception as e:
        print(f"{RED}[!]{RESET} Error: {e}")
        time.sleep(2)

# Instagram downloader
def download_instagram():
    print(f"{CYAN}[?]{RESET} Enter the Instagram post link:")
    url = input(f"{CYAN}[>]{RESET} ")

    print(f"{CYAN}[?]{RESET} Do you want to specify a custom name?")
    custom_name = input(f"{CYAN}[>]{RESET} (Leave blank for default name): ").strip()

    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        desc_tag = soup.find("meta", property="og:description")

        if not desc_tag or not desc_tag.get("content"):
            print(f"{RED}[!]{RESET} Failed to extract post caption. Cannot continue.")
            time.sleep(2)
            return

        default_name = desc_tag['content'].split('#')[0].strip()
        file_name = custom_name if custom_name else default_name

        print(f"{CYAN}[!]{RESET} Downloading Instagram post as '{file_name}.jpg'...")
        time.sleep(2)
        with open(f"/sdcard/download/{file_name}.jpg", "w") as f:
            f.write("FAKE IMAGE DATA")

        print(f"{CYAN}[✓]{RESET} Saved as {file_name}.jpg")
        time.sleep(2)

    except Exception as e:
        print(f"{RED}[!]{RESET} Error: {e}")
        time.sleep(2)

# YouTube downloader
def download_youtube():
    print(f"{CYAN}[?]{RESET} Enter the YouTube video link:")
    url = input(f"{CYAN}[>]{RESET} ")

    print(f"{CYAN}[?]{RESET} Do you want to specify a custom name?")
    custom_name = input(f"{CYAN}[>]{RESET} (Leave blank for default name): ").strip()

    try:
        yt = YouTube(url)
        file_name = custom_name if custom_name else yt.title

        print(f"{CYAN}[!]{RESET} Downloading YouTube video as '{file_name}.mp4'...")
        stream = yt.streams.filter(progressive=True, file_extension="mp4").first()
        stream.download("/sdcard/download", filename=file_name + ".mp4")

        print(f"{CYAN}[✓]{RESET} Saved as {file_name}.mp4")
        time.sleep(2)

    except Exception as e:
        print(f"{RED}[!]{RESET} Error: {e}")
        time.sleep(2)

# Main menu
def main_menu():
    while True:
        clear()
        print(f"""{CYAN}
██████╗ ██╗      ██████╗  ██████╗ ███╗   ██╗███████╗
██╔══██╗██║     ██╔═══██╗██╔═══██╗████╗  ██║██╔════╝
███████║██║     ██║   ██║██║   ██║██╔██╗ ██║█████╗
██╔══██║██║     ██║   ██║██║   ██║██║╚██╗██║██╔══╝
██║  ██║███████╗╚██████╔╝╚██████╔╝██║ ╚████║███████╗
╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝
      Developer: Alone | Telegram: @i4mAlone
{RESET}""")
        print(f"{CYAN}[1]{RESET} TikTok Downloader")
        print(f"{CYAN}[2]{RESET} Instagram Downloader")
        print(f"{CYAN}[3]{RESET} YouTube Downloader")
        print(f"{CYAN}[0]{RESET} Exit")
        choice = input(f"{CYAN}[?]{RESET} Choose an option: ").strip()

        if choice == "1":
            download_tiktok()
        elif choice == "2":
            download_instagram()
        elif choice == "3":
            download_youtube()
        elif choice == "0":
            print(f"{CYAN}[✓]{RESET} Exiting...")
            time.sleep(1)
            break
        else:
            print(f"{RED}[!]{RESET} Invalid option.")
            time.sleep(1)

main_menu()