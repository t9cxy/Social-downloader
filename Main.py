import os
import re
import sys
import platform
import subprocess
import requests
import yt_dlp
from urllib.parse import urlencode
from tqdm import tqdm

# ─── Utilities ─────────────────────────────────────────────────────────────────

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print(f"""
 █████╗ ██╗      ██████╗  ██████╗ ███╗   ██╗███████╗
██╔══██╗██║     ██╔═══██╗██╔═══██╗████╗  ██║██╔════╝
███████║██║     ██║   ██║██║   ██║██╔██╗ ██║█████╗  
██╔══██║██║     ██║   ██║██║   ██║██║╚██╗██║██╔══╝  
██║  ██║███████╗╚██████╔╝╚██████╔╝██║ ╚████║███████╗
╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝
       Developer: Alone | Telegram: @i4mAlone
""")

def pause():
    input("\n[•] Press Enter to return...")

def ensure_package(pkg, imp=None):
    try:
        __import__(imp or pkg)
    except ImportError:
        print(f"[!] Installing {pkg}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

def sanitize_filename(name):
    name = re.sub(r'[\\/*?:"<>|]', "", name)
    return name.strip().capitalize()[:50]

def prompt_filename(default):
    custom = input(f"[?] File name (Enter for '{default}'): ").strip()
    final = sanitize_filename(custom) if custom else sanitize_filename(default)
    # copy to clipboard (Termux)
    os.system(f"termux-clipboard-set '{final}'")
    print(f"[✓] Name copied: {final}")
    return final

def save_with_progress(url, fname):
    try:
        r = requests.get(url, stream=True)
        total = int(r.headers.get('content-length', 0))
        with open(fname, 'wb') as f, tqdm(desc=fname, total=total, unit='B', unit_scale=True) as bar:
            for chunk in r.iter_content(1024):
                f.write(chunk); bar.update(len(chunk))
        return True
    except Exception as e:
        print(f"[!] Download error: {e}")
        return False

def move_file(fname):
    dst = '/sdcard/download'
    os.makedirs(dst, exist_ok=True)
    os.system(f"mv '{fname}' {dst}/")
    print(f"[✓] Moved to {dst}/{fname}")

# ─── TikTok ────────────────────────────────────────────────────────────────────

def tiktok_profile_pic():
    clear(); banner()
    url = input("[?] TikTok profile URL: ").strip()
    api = f"https://tikwm.com/api/?url={url}"
    try:
        data = requests.get(api).json()['data']
        pic = data['author']['avatarThumb']
        name = prompt_filename("tiktok_pp")
        fname = f"{name}.jpg"
        if save_with_progress(pic, fname): move_file(fname)
    except Exception as e:
        print(f"[!] {e}")
    pause()

def tiktok_post():
    clear(); banner()
    url = input("[?] TikTok post URL: ").strip()
    api = f"https://tikwm.com/api/?url={url}"
    try:
        d = requests.get(api).json()['data']
        desc = sanitize_filename(d.get('title') or "tiktok_post")
        # detect type
        if d.get('images'):
            print("[•] Photo post detected")
            print("[1] Download photos\n[2] Download sound\n[0] Back")
            ch = input("[?] Choose: ").strip()
            if ch=='1':
                for i,img in enumerate(d['images'],1):
                    name = prompt_filename(f"{desc}_{i}")
                    fn=f"{name}.jpg"
                    if save_with_progress(img, fn): move_file(fn)
            elif ch=='2':
                name=prompt_filename(desc+"_sound"); fn=f"{name}.mp4"
                if save_with_progress(d['music'], fn): move_file(fn)
        else:
            print("[•] Video post detected")
            print("[1] Download video\n[2] Download sound\n[0] Back")
            ch = input("[?] Choose: ").strip()
            if ch=='1':
                name=prompt_filename(desc); fn=f"{name}.mp4"
                if save_with_progress(d['play'], fn): move_file(fn)
            elif ch=='2':
                name=prompt_filename(desc+"_sound"); fn=f"{name}.mp4"
                if save_with_progress(d['music'], fn): move_file(fn)
    except Exception as e:
        print(f"[!] {e}")
    pause()

def tiktok_copy_name():
    clear(); banner()
    username = input("[?] TikTok username: ").strip()
    if username:
        os.system(f"termux-clipboard-set '{username}'")
        print(f"[✓] '{username}' copied to clipboard")
    else:
        print("[!] No username entered")
    pause()

def tiktok_menu():
    while True:
        clear(); banner()
        print("[TikTok Menu]\n1.Profile Pic  2.Post Downloader  3.Copy Name  0.Back")
        ch = input("[?] Choose: ").strip()
        if ch=='1': tiktok_profile_pic()
        elif ch=='2': tiktok_post()
        elif ch=='3': tiktok_copy_name()
        elif ch=='0': break

# ─── Instagram ─────────────────────────────────────────────────────────────────

def instagram_profile_pic():
    clear(); banner()
    url = input("[?] Instagram profile URL: ").strip()
    try:
        res = requests.get(url).text
        img = re.search(r'"profile_pic_url_hd":"([^"]+)"', res)[1].replace('\\u0026','&')
        name = prompt_filename("insta_pp"); fn=f"{name}.jpg"
        if save_with_progress(img, fn): move_file(fn)
    except Exception as e: print(f"[!] {e}")
    pause()

def instagram_post():
    clear(); banner()
    url = input("[?] Instagram post URL: ").strip()
    api = "https://instasupersave.com/api/convert"
    data = urlencode({'q':url})
    try:
        res = requests.post(api, data=data, headers={'Content-Type':'application/x-www-form-urlencoded'}).json()
        vids = re.findall(r'https.*?\.mp4', str(res))
        imgs = re.findall(r'https.*?\.(?:jpg|png)', str(res))
        print(f"[•] {len(vids)} videos, {len(imgs)} images found")
        if vids:
            name=prompt_filename("insta_video"); fn=f"{name}.mp4"
            if save_with_progress(vids[0], fn): move_file(fn)
        elif imgs:
            name=prompt_filename("insta_img"); fn=f"{name}.jpg"
            if save_with_progress(imgs[0], fn): move_file(fn)
    except Exception as e: print(f"[!] {e}")
    pause()

def instagram_copy_name():
    clear(); banner()
    username = input("[?] Instagram username: ").strip()
    if username:
        os.system(f"termux-clipboard-set '{username}'")
        print(f"[✓] '{username}' copied")
    else: print("[!] No username")
    pause()

def instagram_menu():
    while True:
        clear(); banner()
        print("[Instagram Menu]\n1.Profile Pic  2.Post Downloader  3.Copy Name  0.Back")
        ch = input("[?] Choose: ").strip()
        if ch=='1': instagram_profile_pic()
        elif ch=='2': instagram_post()
        elif ch=='3': instagram_copy_name()
        elif ch=='0': break

# ─── YouTube ────────────────────────────────────────────────────────────────────

def youtube_profile_pic():
    clear(); banner()
    channel = input("[?] YouTube channel ID/URL: ").strip()
    try:
        info = yt_dlp.YoutubeDL({'quiet':True, 'extract_flat':True}).extract_info(channel, download=False)
        thumb = info.get('thumbnail')
        name=prompt_filename("yt_pp"); fn=f"{name}.jpg"
        if save_with_progress(thumb, fn): move_file(fn)
    except Exception as e: print(f"[!] {e}")
    pause()

def youtube_video():
    clear(); banner()
    url = input("[?] YouTube video URL: ").strip()
    name = prompt_filename("yt_video"); fn_pattern = f"{name}.%(ext)s"
    try:
        with yt_dlp.YoutubeDL({'outtmpl':fn_pattern, 'format':'best'}) as ydl:
            ydl.download([url])
        move_file(next(f for f in os.listdir('.') if f.startswith(name)))
    except Exception as e: print(f"[!] {e}")
    pause()

def youtube_audio():
    clear(); banner()
    url = input("[?] YouTube video URL: ").strip()
    name = prompt_filename("yt_audio"); fn_pattern = f"{name}.%(ext)s"
    try:
        opts={'outtmpl':fn_pattern,'format':'bestaudio/best','postprocessors':[{'key':'FFmpegExtractAudio','preferredcodec':'mp3'}]}
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download([url])
        move_file(f"{name}.mp3")
    except Exception as e: print(f"[!] {e}")
    pause()

def youtube_copy_name():
    clear(); banner()
    url = input("[?] YouTube channel ID/URL: ").strip()
    try:
        info = yt_dlp.YoutubeDL({'quiet':True, 'extract_flat':True}).extract_info(url, download=False)
        name=info.get('uploader')
        os.system(f"termux-clipboard-set '{name}'")
        print(f"[✓] Channel '{name}' copied")
    except Exception as e: print(f"[!] {e}")
    pause()

def youtube_menu():
    while True:
        clear(); banner()
        print("[YouTube Menu]\n1.Profile Pic  2.Download Video  3.Download Audio  4.Copy Name  0.Back")
        ch = input("[?] Choose: ").strip()
        if ch=='1': youtube_profile_pic()
        elif ch=='2': youtube_video()
        elif ch=='3': youtube_audio()
        elif ch=='4': youtube_copy_name()
        elif ch=='0': break

# ─── Main ──────────────────────────────────────────────────────────────────────

def main():
    while True:
        clear(); banner()
        print("[1] TikTok\n[2] Instagram\n[3] YouTube\n[0] Exit")
        ch = input("[?] Choose: ").strip()
        if ch=='1': tiktok_menu()
        elif ch=='2': instagram_menu()
        elif ch=='3': youtube_menu()
        elif ch=='0':
            print("Bye."); break

if __name__ == '__main__':
    main()