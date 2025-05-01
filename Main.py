import os
import time
import random
import string
from pytube import YouTube
import requests
from bs4 import BeautifulSoup

# Terminal Colors
RED = '\033[91m'
GREEN = '\033[92m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
RESET = '\033[0m'


def clear():
    os.system('clear' if os.name != 'nt' else 'cls')


def generate_random_name(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def download_youtube():
    clear()
    print(f"""{CYAN}

YouTube Downloader

{RESET}")

    url = input(f"{CYAN}[?]{RESET} Enter YouTube video URL: ")
    if not url:
        print(f"{RED}[!] Invalid URL.{RESET}")
        return

    try:
        yt = YouTube(url)
        title = yt.title.strip().split('|')[0].split('#')[0]

        custom_name = input(f"{CYAN}[?]{RESET} Custom filename? (Leave blank for default): ").strip()
        filename = custom_name if custom_name else title or generate_random_name()
        filename = filename.replace(' ', '_')

        print(f"{YELLOW}[~]{RESET} Downloading {filename}...")
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path='/sdcard/download', filename=f"{filename}.mp4")

        print(f"{GREEN}[✓]{RESET} Saved as /sdcard/download/{filename}.mp4")

    except Exception as e:
        print(f"{RED}[!]{RESET} Error: {e}")

    time.sleep(3)


def download_tiktok():
    clear()
    print(f"""{CYAN}

TikTok Downloader

{RESET}")

    url = input(f"{CYAN}[?]{RESET} Enter TikTok video URL: ")
    if not url:
        print(f"{RED}[!] Invalid URL.{RESET}")
        return

    try:
        session = requests.Session()
        r = session.get("https://snaptik.app")
        soup = BeautifulSoup(r.text, 'html.parser')
        token = soup.find('input', {'id': 'token'})['value']

        payload = {'url': url, 'token': token}
        headers = {'User-Agent': 'Mozilla/5.0'}
        res = session.post("https://snaptik.app/abc2.php", data=payload, headers=headers)
        links = BeautifulSoup(res.text, 'html.parser').find_all('a')
        dl_url = next((a['href'] for a in links if 'http' in a['href']), None)

        if not dl_url:
            raise Exception("Failed to extract download link.")

        caption = "tiktok_video"
        filename = input(f"{CYAN}[?]{RESET} Custom filename? (Leave blank for default): ").strip()
        filename = filename if filename else caption or generate_random_name()
        filename = filename.replace(' ', '_')

        video_data = session.get(dl_url).content
        with open(f"/sdcard/download/{filename}.mp4", "wb") as f:
            f.write(video_data)

        print(f"{GREEN}[✓]{RESET} Saved as /sdcard/download/{filename}.mp4")

    except Exception as e:
        print(f"{RED}[!]{RESET} Error: {e}")

    time.sleep(3)


def main():
    while True:
        clear()
        print(f"""{CYAN}

 █████╗ ██╗      ██████╗ ███╗   ██╗███████╗    
██╔══██╗██║     ██╔═══██╗████╗  ██║██╔════╝    
███████║██║     ██║   ██║██╔██╗ ██║█████╗      
██╔══██║██║     ██║   ██║██║╚██╗██║██╔══╝      
██║  ██║███████╗╚██████╔╝██║ ╚████║███████╗    
╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝    

       {YELLOW}Developer: Alone | Telegram: @i4mAlone{RESET}

[1] TikTok Downloader

[2] YouTube Downloader

[0] Exit

""")
        choice = input(f"{CYAN}[?]{RESET} Choose an option: ")

        if choice == '1':
            download_tiktok()

        elif choice == '2':
            download_youtube()

        elif choice == '0':
            break

        else:
            print(f"{RED}[!] Invalid choice.{RESET}")
            time.sleep(2)


if __name__ == '__main__':
    main()
