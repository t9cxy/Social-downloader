import os
import requests
from rich.console import Console
from rich.panel import Panel
from rich import print
from datetime import datetime

console = Console()

def clear(): os.system("clear")

def logo():
    return """
[bold blue]
 █████╗ ██╗      ██████╗ ███╗   ██╗███████╗
██╔══██╗██║     ██╔═══██╗████╗  ██║██╔════╝
███████║██║     ██║   ██║██╔██╗ ██║█████╗  
██╔══██║██║     ██║   ██║██║╚██╗██║██╔══╝  
██║  ██║███████╗╚██████╔╝██║ ╚████║███████╗
╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
[/bold blue]
"""

def main_menu():
    clear()
    console.print(Panel.fit(logo() + f"\n[bold green]1.[/bold green] TikTok\n[bold red]0.[/bold red] Exit", title=f"[bold cyan]Main Menu • {datetime.now().strftime('%Y-%m-%d')}[/bold cyan]"))

def tiktok_menu():
    clear()
    console.print(Panel.fit(logo() + """
[bold green]1.[/bold green] Download Video (No Watermark)
[bold green]2.[/bold green] Download Sound (MP3)
[bold red]0.[/bold red] Back
""", title="[bold cyan]TikTok Downloader[/bold cyan]"))

def move_to_sdcard(filename):
    os.system(f"mv \"{filename}\" /sdcard/download")
    print(f"[green][✔] Saved to /sdcard/download/{filename}[/green]")

def custom_filename(ext):
    name = input("[?] Enter custom file name (no extension): ").strip()
    return name + ext

def download_video_nowm(url):
    print("[yellow][•] Contacting TikTok downloader API...[/yellow]")
    try:
        session = requests.Session()
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        # Step 1: get token
        res1 = session.post("https://ttdownloader.com/req/", headers=headers, data={
            "url": url,
            "format": "",
            "token": ""
        })
        if "videonowm" not in res1.text:
            print("[red][×] Failed to get download link. Possibly rate limited.[/red]")
            return

        # Step 2: extract URL
        video_url = res1.text.split('id="download-now"')[1].split('href="')[1].split('"')[0]
        filename = custom_filename(".mp4")
        os.system(f'wget -q --show-progress "{video_url}" -O "{filename}"')
        move_to_sdcard(filename)
    except Exception as e:
        print(f"[red][×] Error: {e}[/red]")

def download_sound(url):
    print("[yellow][•] Extracting audio...[/yellow]")
    try:
        api = f"https://www.tikwm.com/api/?url={url}"
        r = requests.get(api).json()
        if not r.get("data"):
            print("[red][×] Failed to get sound.[/red]")
            return
        sound_url = r['data']['music']
        filename = custom_filename(".mp3")
        os.system(f'wget -q --show-progress "{sound_url}" -O "{filename}"')
        move_to_sdcard(filename)
    except Exception as e:
        print(f"[red][×] Error: {e}[/red]")

def tiktok_handler():
    while True:
        tiktok_menu()
        opt = input("[?] Choose option: ").strip()
        if opt == "1":
            url = input("[?] Paste TikTok video URL: ").strip()
            download_video_nowm(url)
        elif opt == "2":
            url = input("[?] Paste TikTok video URL: ").strip()
            download_sound(url)
        elif opt == "0":
            break
        else:
            print("[red][×] Invalid option[/red]")
        input("[Press ENTER to return to TikTok menu]")

def main():
    while True:
        main_menu()
        opt = input("[?] Choose option: ").strip()
        if opt == "1":
            tiktok_handler()
        elif opt == "0":
            clear()
            break
        else:
            print("[red][×] Invalid option[/red]")
            input("[Press ENTER]")

if __name__ == "__main__":
    main()