import os
import re
import time
import requests
from bs4 import BeautifulSoup
from pytube import YouTube
from termcolor import colored

# Download directory
DOWNLOAD_DIR = "/sdcard/download/"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def clr(text, color="cyan"):
    return colored(text, color)

def banner():
    print(clr(r""" 
     ▄▄▄      ▓██   ██▓ ▒█████   ███▄ ▄███▓ ▓█████ 
    ▒████▄     ▒██  ██▒▒██▒  ██▒▓██▒▀█▀ ██▒ ▓█   ▀ 
    ▒██  ▀█▄    ▒██ ██░▒██░  ██▒▓██    ▓██░ ▒███   
    ░██▄▄▄▄██   ░ ▐██▓░▒██   ██░▒██    ▒██  ▒▓█  ▄ 
     ▓█   ▓██▒  ░ ██▒▓░░ ████▓▒░▒██▒   ░██▒ ░▒████▒
     ▒▒   ▓▒█░   ██▒▒▒ ░ ▒░▒░▒░ ░ ▒░   ░  ░ ░░ ▒░ ░
      ▒   ▒▒ ░ ▓██ ░▒░   ░ ▒ ▒░ ░  ░      ░  ░ ░  ░
      ░   ▒    ▒ ▒ ░░  ░ ░ ░ ▒  ░      ░       ░   
          ░  ░ ░ ░         ░ ░         ░       ░  ░
                ░ ░                                  
    """, "magenta"))
    print(clr("[ • ] Tool by ALONE", "green"))
    print(clr("[ • ] Telegram: @i4mAlone", "yellow"))
    print(clr("[ • ] Date: " + time.strftime('%Y-%m-%d'), "blue"))
    print()

def sanitize_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "", name)

def download_file(url, filename):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        filepath = os.path.join(DOWNLOAD_DIR, filename)
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(clr(f"[ ✔ ] Saved as {filepath}", "blue"))
    except Exception as e:
        print(clr(f"[ × ] Error downloading file: {e}", "red"))

def download_profile_picture():
    url = input(clr("[ ? ] TikTok/YouTube video or profile URL: ", "yellow")).strip()
    custom_name = input(clr("[ ? ] Custom filename (leave blank for default): ", "yellow")).strip()
    try:
        if "tiktok.com" in url:
            match = re.search(r"@([\w\.]+)", url)
            username = match.group(1) if match else None
            if not username:
                print(clr("[ × ] Cannot extract TikTok username.", "red"))
                return
            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.get(f"https://www.tiktok.com/@{username}", headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            img_tag = soup.find("img", {"alt": f"{username}'s profile picture"})
            img_url = img_tag['src'] if img_tag else None
            display_name = username
        elif "youtube.com" in url or "youtu.be" in url:
            yt = YouTube(url)
            display_name = yt.author or yt.channel_id
            # Use YouTube API for actual profile pic, here it's fallback
            img_url = yt.thumbnail_url
        else:
            print(clr("[ × ] Unsupported URL.", "red"))
            return
        if not img_url:
            print(clr("[ × ] Profile picture not found.", "red"))
            return
        filename = sanitize_filename(custom_name if custom_name else display_name) + ".jpg"
        download_file(img_url, filename)
    except Exception as e:
        print(clr(f"[ × ] Error: {e}", "red"))

def download_youtube_video():
    url = input(clr("[ ? ] YouTube video URL: ", "yellow")).strip()
    custom_name = input(clr("[ ? ] Custom filename (leave blank for default): ", "yellow")).strip()
    try:
        yt = YouTube(url)
        title = sanitize_filename(yt.title)
        filename = sanitize_filename(custom_name if custom_name else title) + ".mp4"
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        filepath = os.path.join(DOWNLOAD_DIR, filename)
        stream.download(output_path=DOWNLOAD_DIR, filename=filename)
        print(clr(f"[ ✔ ] Saved as {filepath}", "blue"))
    except Exception as e:
        print(clr(f"[ × ] Error: {e}", "red"))

def download_photo():
    url = input(clr("[ ? ] Image URL: ", "yellow")).strip()
    custom_name = input(clr("[ ? ] Custom filename (leave blank for default): ", "yellow")).strip()
    try:
        if not custom_name:
            filename = "photo_" + time.strftime("%Y%m%d%H%M%S") + ".jpg"
        else:
            filename = sanitize_filename(custom_name) + ".jpg"
        download_file(url, filename)
    except Exception as e:
        print(clr(f"[ × ] Error: {e}", "red"))

def download_sound():
    url = input(clr("[ ? ] Sound URL: ", "yellow")).strip()
    custom_name = input(clr("[ ? ] Custom filename (leave blank for default): ", "yellow")).strip()
    try:
        filename = sanitize_filename(custom_name if custom_name else "sound_" + time.strftime("%Y%m%d%H%M%S")) + ".mp3"
        download_file(url, filename)
    except Exception as e:
        print(clr(f"[ × ] Error: {e}", "red"))

def menu():
    while True:
        os.system("clear")
        banner()
        print(clr("1. Download Profile Picture", "cyan"))
        print(clr("2. Download YouTube Video", "cyan"))
        print(clr("3. Download Photo", "cyan"))
        print(clr("4. Download Sound", "cyan"))
        print(clr("0. Exit", "red"))
        choice = input(clr("\n[ ? ] Choose an option: ", "yellow")).strip()
        if choice == "1":
            download_profile_picture()
        elif choice == "2":
            download_youtube_video()
        elif choice == "3":
            download_photo()
        elif choice == "4":
            download_sound()
        elif choice == "0":
            print(clr("\n[ ✔ ] Exiting... Have a good day!", "green"))
            break
        else:
            print(clr("[ × ] Invalid choice!", "red"))
        input(clr("\n[ • ] Press Enter to return to menu...", "magenta"))

if __name__ == "__main__":
    menu()