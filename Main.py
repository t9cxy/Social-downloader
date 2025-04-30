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
    res = requests.get(url)
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
    except Exception:
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

def tiktok_post_downloader():
    url = input(f"{C}[?]{W} TikTok post URL: ")
    api = f"https://tikwm.com/api/?url={url}"
    res = requests.get(api).json().get('data', {})
    desc = sanitize_filename(res.get('title') or 'TiktokPost')
    images = res.get('images')
    music = res.get('music')
    play = res.get('play')
    name = prompt_filename(desc)
    if images:
        for i, img in enumerate(images, 1):
            fname = f"{name}_{i}.jpg"
            if save_with_progress(img, fname):
                move_file(fname)
    if play:
        fname = f"{name}.mp4"
        if save_with_progress(play, fname):
            move_file(fname)
    if music:
        fname = f"{name}_sound.mp4"
        if save_with_progress(music, fname):
            move_file(fname)

def tiktok_user_info():
    username = input(f"{C}[?]{W} TikTok username: ")
    info = get_tiktok_user_info(username)
    if info:
        for k, v in info.items():
            print(f"{G}[•] {k}: {C}{v}")
    else:
        print(f"{R}[x]{W} Could not fetch info.")

def tiktok_menu():
    while True:
        clear(); banner()
        print(f"{Y}[TikTok Options]{W}")
        print(f"{Y}[1]{W} Profile Picture")
        print(f"{Y}[2]{W} Post Downloader")
        print(f"{Y}[3]{W} User Info")
        print(f"{Y}[0]{W} Back")
        ch = input(f"\n{B}[?]{W} Choose: ")
        if ch=='1': tiktok_profile_picture()
        elif ch=='2': tiktok_post_downloader()
        elif ch=='3': tiktok_user_info()
        elif ch=='0': break
        else: print(f"{R}[x]{W} Invalid.") 
        input(f"\n{C}[↩]{W} Enter to continue...")

#
# Instagram Helpers
#
def get_instagram_user_info(username):
    url = f'https://www.instagram.com/{username}/'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    try:
        info = {
            'Username': username,
            'Bio': soup.find('meta', {'name': 'description'})['content'],
            'Followers': soup.find('meta', {'name': 'followers'})['content'],
            'Following': soup.find('meta', {'name': 'following'})['content'],
            'Posts': soup.find('meta', {'name': 'posts'})['content'],
            'Profile Picture': soup.find('meta', {'property': 'og:image'})['content']
        }
        return info
    except Exception:
        return None

def instagram_profile_picture():
    username = input(f"{C}[?]{W} Instagram username: ")
    info = get_instagram_user_info(username)
    if info:
        url = info['Profile Picture']
        name = prompt_filename(username + "_pp")
        fname = f"{name}.jpg"
        if save_with_progress(url, fname):
            move_file(fname)
    else:
        print(f"{R}[x]{W} Could not fetch info.")

def instagram_post_downloader():
    url = input(f"{C}[?]{W} Instagram post URL: ")
    api = "https://instasupersave.com/api/convert"
    data = urlencode({'q': url})
    res = requests.post(api, data=data, headers={'Content-Type':'application/x-www-form-urlencoded'}).json()
    matches = re.findall(r'https.*?\.mp4', str(res))
    name = prompt_filename("InstagramPost")
    for link in matches:
        fname = f"{name}.mp4"
        if save_with_progress(link, fname):
            move_file(fname)

def instagram_user_info():
    username = input(f"{C}[?]{W} Instagram username: ")
    info = get_instagram_user_info(username)
    if info:
        for k, v in info.items():
            print(f"{G}[•] {k}: {C}{v}")
    else:
        print(f"{R}[x]{W} Could not fetch info.")

def instagram_menu():
    while True:
        clear(); banner()
        print(f"{Y}[Instagram Options]{W}")
        print(f"{Y}[1]{W} Profile Picture")
        print(f"{Y}[2]{W} Post Downloader")
        print(f"{Y}[3]{W} User Info")
        print(f"{Y}[0]{W} Back")
        ch = input(f"\n{B}[?]{W} Choose: ")
        if ch=='1': instagram_profile_picture()
        elif ch=='2': instagram_post_downloader()
        elif ch=='3': instagram_user_info()
        elif ch=='0': break
        else: print(f"{R}[x]{W} Invalid.")
        input(f"\n{C}[↩]{W} Enter to continue...")

#
# YouTube Helpers
#
def get_youtube_user_info(channel_id):
    url = f'https://www.youtube.com/channel/{channel_id}'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    try:
        info = {
            'Channel ID': channel_id,
            'Subscribers': soup.find('yt-formatted-string', {'id':'subscriber-count'}).text.strip(),
            'Profile Picture': soup.find('link', {'rel':'image_src'})['href'],
            'About': soup.find('yt-formatted-string', {'id':'description'}).text.strip()
        }
        return info
    except Exception:
        return None

def youtube_profile_picture():
    cid = input(f"{C}[?]{W} YouTube channel ID: ")
    info = get_youtube_user_info(cid)
    if info:
        url = info['Profile Picture']
        name = prompt_filename(cid + "_pp")
        fname = f"{name}.jpg"
        if save_with_progress(url, fname):
            move_file(fname)
    else:
        print(f"{R}[x]{W} Could not fetch info.")

def youtube_post_downloader():
    url = input(f"{C}[?]{W} YouTube video URL: ")
    name = prompt_filename("YouTubeVideo")
    opts = {'format':'bestvideo+bestaudio/best','outtmpl':f'{name}.%(ext)s','noplaylist':True,'quiet':True}
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=True)
    ext = info.get('ext','mp4')
    fname = f"{name}.{ext}"
    move_file(fname)

def youtube_user_info():
    cid = input(f"{C}[?]{W} YouTube channel ID: ")
    info = get_youtube_user_info(cid)
    if info:
        for k, v in info.items():
            print(f"{G}[•] {k}: {C}{v}")
    else:
        print(f"{R}[x]{W} Could not fetch info.")

def youtube_menu():
    while True:
        clear(); banner()
        print(f"{Y}[YouTube Options]{W}")
        print(f"{Y}[1]{W} Profile Picture")
        print(f"{Y}[2]{W} Post Downloader")
        print(f"{Y}[3]{W} User Info")
        print(f"{Y}[0]{W} Back")
        ch = input(f"\n{B}[?]{W} Choose: ")
        if ch=='1': youtube_profile_picture()
        elif ch=='2': youtube_post_downloader()
        elif ch=='3': youtube_user_info()
        elif ch=='0': break
        else: print(f"{R}[x]{W} Invalid.")
        input(f"\n{C}[↩]{W} Enter to continue...")

#
# Main Menu
#
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
