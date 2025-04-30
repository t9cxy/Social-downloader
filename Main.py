import os
import re
import requests
import yt_dlp
from bs4 import BeautifulSoup
from tqdm import tqdm
from urllib.parse import urlencode

# Color codes for terminal output
R = '\033[91m'; G = '\033[92m'; Y = '\033[93m'; C = '\033[96m'; W = '\033[97m'; B = '\033[94m'; RESET = '\033[0m'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print(f"""{R}
 █████╗ ██╗      ██████╗  ██████╗ ███╗   ██╗███████╗
██╔══██╗██║     ██╔═══██╗██╔═══██╗████╗  ██║██╔════╝
███████║██║     ██║   ██║██║   ██║██╔██╗ ██║█████╗  
██╔══██║██║     ██║   ██║██║   ██║██║╚██╗██║██╔══╝  
██║  ██║███████╗╚██████╔╝╚██████╔╝██║ ╚████║███████╗
╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝
         {W}Developer: {C}Alone{W} | Telegram: {C}@i4mAlone{RESET}
""")

def sanitize_filename(name):
    name = re.sub(r'[\\/*?:"<>|]', "", name)
    return name.strip().capitalize()[:50]

def prompt_filename(default_name):
    custom = input(f"{C}[?]{W} Enter file name (or press Enter for default: {default_name}): ")
    final = sanitize_filename(custom) if custom else sanitize_filename(default_name)
    os.system(f"termux-clipboard-set '{final}'")
    print(f"{G}[✓]{W} Name copied to clipboard: {final}")
    return final

def save_with_progress(url, filename):
    try:
        r = requests.get(url, stream=True)
        total = int(r.headers.get('content-length', 0))
        with open(filename, 'wb') as f, tqdm(
            desc=filename, total=total, unit='B', unit_scale=True, unit_divisor=1024
        ) as bar:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    bar.update(len(chunk))
    except Exception as e:
        print(f"{R}[x]{W} Download failed: {e}")
        return False
    return True

def move_file(filename):
    try:
        os.makedirs('/sdcard/download', exist_ok=True)
        os.system(f"mv '{filename}' /sdcard/download/")
        print(f"{G}[✓]{W} Moved to /sdcard/download/{filename}")
    except Exception as e:
        print(f"{R}[x]{W} Move error: {e}")

#
# TikTok Helpers
#
def get_tiktok_user_info(username):
    url = f'https://www.tiktok.com/@{username}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')
        try:
            info = {
                'Username': username,
                'Bio': soup.find('meta', {'name': 'description'})['content'],
                'Followers': soup.find('strong', {'title': 'Followers'}).text.strip(),
                'Following': soup.find('strong', {'title': 'Following'}).text.strip(),
                'Likes': soup.find('strong', {'title': 'Likes'}).text.strip(),
                'Posts': soup.find('span', {'class': 'video-count'}).text.strip(),
                'Profile Picture': soup.find('meta', {'property': 'og:image'})['content']
            }
            return info
        except Exception as e:
            print(f"{R}[x]{W} Error while extracting TikTok info: {e}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"{R}[x]{W} Failed to fetch TikTok user info: {e}")
        return None

def tiktok_profile_picture():
    username = input(f"{C}[?]{W} TikTok username: ")
    info = get_tiktok_user_info(username)
    if info:
        url = info['Profile Picture']
        name = prompt_filename(username + "_pp")
        fname = f"{name}.jpg"
        if save_with_progress(url, fname):
            move_file(fname)
    else:
        print(f"{R}[x]{W} Could not fetch info.")

# Add the same for Instagram and YouTube helpers

def main():
    while True:
        clear(); banner()
        print(f"{Y}[1]{W} TikTok")
        print(f"{Y}[2]{W} Instagram")
        print(f"{Y}[3]{W} YouTube")
        print(f"{Y}[0]{W} Exit")
        ch = input(f"\n{B}[?]{W} Choose: ")
        if ch=='1': tiktok_menu()
        elif ch=='2': instagram_menu()
        elif ch=='3': youtube_menu()
        elif ch=='0':
            print(f"{G}[✓]{W} Bye."); break
        else:
            print(f"{R}[x]{W} Invalid choice.")
        input(f"\n{C}[↩]{W} Enter to continue...")

if __name__ == '__main__':
    main()