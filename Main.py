#!/usr/bin/env python3
import os
import re
import sys
import subprocess
import requests
import yt_dlp
from urllib.parse import urlencode
from tqdm import tqdm

# ─── Utilities ─────────────────────────────────────────────────────────────────

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    print(r"""
 █████╗ ██╗      ██████╗  ██████╗ ███╗   ██╗███████╗
██╔══██╗██║     ██╔═══██╗██╔═══██╗████╗  ██║██╔════╝
███████║██║     ██║   ██║██║   ██║██╔██╗ ██║█████╗  
██╔══██║██║     ██║   ██║██║   ██║██║╚██╗██║██╔══╝  
██║  ██║███████╗╚██████╔╝╚██████╔╝██║ ╚████║███████╗
╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝
       Developer: Alone | Telegram: @i4mAlone
""")

def pause():
    input("\n[•] Press Enter to continue...")

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
        total = int(r.headers.get("content-length", 0))
        with open(fname, "wb") as f, tqdm(desc=fname, total=total, unit="B", unit_scale=True) as bar:
            for chunk in r.iter_content(1024):
                if not chunk: break
                f.write(chunk)
                bar.update(len(chunk))
        return True
    except Exception as e:
        print(f"[!] Download error: {e}")
        return False

def move_file(fname):
    dst = "/sdcard/download"
    os.makedirs(dst, exist_ok=True)
    os.system(f"mv '{fname}' {dst}/")
    print(f"[✓] Moved to {dst}/{fname}")

# ─── TikTok Menu ───────────────────────────────────────────────────────────────

def tiktok_menu():
    while True:
        clear(); banner()
        print("TikTok Options:\n")
        print(" 1. Download Profile Picture")
        print(" 2. Download Post Video")
        print(" 3. Download Post Photo(s)")
        print(" 4. Download Post Sound")
        print(" 0. Back to Main Menu\n")
        choice = input("[?] Choose: ").strip()
        if choice == "0":
            break
        url = input("\n[?] Enter TikTok URL: ").strip()
        api = f"https://tikwm.com/api/?url={url}"
        try:
            d = requests.get(api).json().get("data", {})
        except:
            print("[!] Failed to fetch TikTok data."); pause(); continue

        # Profile Picture
        if choice == "1":
            pic = d.get("author", {}).get("avatarThumb")
            name = prompt_filename("tiktok_pp"); fn=f"{name}.jpg"
            if save_with_progress(pic, fn): move_file(fn)

        # Post Video
        elif choice == "2":
            link = d.get("play")
            name = prompt_filename("tiktok_video"); fn=f"{name}.mp4"
            if save_with_progress(link, fn): move_file(fn)

        # Post Photos
        elif choice == "3":
            imgs = d.get("images", [])
            for i, img in enumerate(imgs, 1):
                name = prompt_filename(f"tiktok_img_{i}"); fn=f"{name}.jpg"
                if save_with_progress(img, fn): move_file(fn)

        # Post Sound
        elif choice == "4":
            link = d.get("music")
            name = prompt_filename("tiktok_sound"); fn=f"{name}.mp4"
            if save_with_progress(link, fn): move_file(fn)

        else:
            print("[!] Invalid choice.")
        pause()

# ─── Instagram Menu ───────────────────────────────────────────────────────────

def instagram_menu():
    while True:
        clear(); banner()
        print("Instagram Options:\n")
        print(" 1. Download Profile Picture")
        print(" 2. Download Post Video/Photo")
        print(" 3. Download Post Sound")
        print(" 0. Back to Main Menu\n")
        choice = input("[?] Choose: ").strip()
        if choice == "0":
            break
        url = input("\n[?] Enter Instagram URL: ").strip()
        if choice == "1":
            try:
                html = requests.get(url).text
                m = re.search(r'"profile_pic_url_hd":"([^"]+)"', html)[1]
                link = m.replace("\\u0026","&")
            except:
                print("[!] Failed to fetch profile pic."); pause(); continue
            name = prompt_filename("insta_pp"); fn=f"{name}.jpg"
            if save_with_progress(link, fn): move_file(fn)

        elif choice in ("2","3"):
            api = "https://instasupersave.com/api/convert"
            data = urlencode({"q":url})
            try:
                res = requests.post(api, data=data, headers={'Content-Type':'application/x-www-form-urlencoded'}).json()
                vids = re.findall(r'https.*?\.mp4', str(res))
                imgs = re.findall(r'https.*?(?:jpg|png)', str(res))
            except:
                print("[!] Failed to fetch post."); pause(); continue

            # Video / Photo choice
            if choice == "2":
                if vids:
                    link = vids[0]; ext = ".mp4"
                elif imgs:
                    link = imgs[0]; ext = ".jpg"
                else:
                    print("[!] No media found."); pause(); continue
            # Sound only
            else:
                music = re.findall(r'https.*?\.mp4', str(res))  # Instasupersave returns mp4 sound?
                link = music[0] if music else None
                ext = ".mp4"
                if not link:
                    print("[!] No sound found."); pause(); continue

            name = prompt_filename("insta_media"); fn=f"{name}{ext}"
            if save_with_progress(link, fn): move_file(fn)

        else:
            print("[!] Invalid choice.")
        pause()

# ─── YouTube Menu ─────────────────────────────────────────────────────────────

def youtube_menu():
    ensure_package("yt-dlp","yt_dlp")
    import yt_dlp
    while True:
        clear(); banner()
        print("YouTube Options:\n")
        print(" 1. Download Profile Picture (channel thumbnail)")
        print(" 2. Download Video")
        print(" 3. Download Audio (mp3)")
        print(" 4. Download Thumbnail")
        print(" 0. Back to Main Menu\n")
        choice = input("[?] Choose: ").strip()
        if choice == "0":
            break
        url = input("\n[?] Enter YouTube URL/ID: ").strip()

        # grab info
        try:
            ydl_opts = {'quiet':True,'extract_flat':True}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
        except Exception as e:
            print(f"[!] Failed: {e}"); pause(); continue

        # Profile pic (channel thumbnail)
        if choice == "1":
            link = info.get("thumbnail"); ext=".jpg"
        # Video
        elif choice == "2":
            name = prompt_filename("yt_video")
            opts={'outtmpl':f'{name}.%(ext)s','format':'bestvideo+bestaudio'}
            try:
                with yt_dlp.YoutubeDL(opts) as ydl:
                    ydl.download([url])
                move_file(f"{name}.{info.get('ext','mp4')}")
            except Exception as e:
                print(f"[!] {e}")
            pause(); continue
        # Audio
        elif choice == "3":
            name = prompt_filename("yt_audio")
            opts={'outtmpl':f'{name}.%(ext)s','format':'bestaudio','postprocessors':[{'key':'FFmpegExtractAudio','preferredcodec':'mp3'}]}
            try:
                with yt_dlp.YoutubeDL(opts) as ydl:
                    ydl.download([url])
                move_file(f"{name}.mp3")
            except Exception as e:
                print(f"[!] {e}")
            pause(); continue
        # Thumbnail
        elif choice == "4":
            link = info.get("thumbnail"); ext=".jpg"
        else:
            print("[!] Invalid choice.")
            pause(); continue

        # for choices 1 & 4
        name = prompt_filename("yt_media"); fn=f"{name}{ext}"
        if save_with_progress(link, fn): move_file(fn)
        pause()

# ─── Main Menu ─────────────────────────────────────────────────────────────────

def main():
    while True:
        clear(); banner()
        print("[1] TikTok\n[2] Instagram\n[3] YouTube\n[0] Exit\n")
        ch = input("[?] Choose: ").strip()
        if ch == "1":
            tiktok_menu()
        elif ch == "2":
            instagram_menu()
        elif ch == "3":
            youtube_menu()
        elif ch == "0":
            print("Bye."); break
        else:
            print("[!] Invalid choice.")
            pause()

if __name__ == "__main__":
    main()