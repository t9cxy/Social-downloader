import os
import requests
from rich.console import Console
from rich.panel import Panel
from rich import print

console = Console()

def clear(): os.system("clear")

def logo():
    return """
[bold cyan]
████████╗██╗██╗░░██╗██╗░█████╗░██╗░░██╗
╚══██╔══╝██║╚██╗██╔╝██║██╔══██╗██║░██╔╝
░░░██║░░░██║░╚███╔╝░██║███████║█████═╝░
░░░██║░░░██║░██╔██╗░██║██╔══██║██╔═██╗░
░░░██║░░░██║██╔╝╚██╗██║██║░░██║██║░╚██╗
░░░╚═╝░░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚═╝╚═╝░░╚═╝
[/bold cyan]
"""

def main_menu():
    clear()
    console.print(Panel.fit(logo() + "\n[bold green]1.[/bold green] TikTok\n[bold red]0.[/bold red] Exit", title="[bold blue]MAIN MENU[/bold blue]"))

def tiktok_menu():
    clear()
    console.print(Panel.fit(logo() + """
[bold green]1.[/bold green] Download Profile Picture
[bold green]2.[/bold green] Download Video (No Watermark)
[bold green]3.[/bold green] Download Thumbnail
[bold green]4.[/bold green] Download Sound (MP3)
[bold red]0.[/bold red] Back
""", title="[bold blue]TIKTOK MENU[/bold blue]"))

def move_to_sdcard(filename):
    os.system(f"mv \"{filename}\" /sdcard/download")
    print(f"[green][✔] Moved to /sdcard/download/{filename}[/green]")

def custom_filename(ext):
    name = input("[?] Enter custom file name (no extension): ").strip()
    return name + ext

def download_video_nowm(url):
    print("[yellow][•] Getting direct download link...[/yellow]")
    try:
        video_id = url.split("/video/")[-1].split("?")[0]
        api = f"https://www.tikwm.com/api/?url={url}"
        r = requests.get(api).json()
        if not r.get("data"):
            print("[red][×] Failed to get video.[/red]")
            return
        dl_url = r['data']['play']
        filename = custom_filename(".mp4")
        os.system(f'wget -q "{dl_url}" -O "{filename}"')
        move_to_sdcard(filename)
    except Exception as e:
        print(f"[red][×] Error: {e}[/red]")

def download_sound(url):
    print("[yellow][•] Getting sound link...[/yellow]")
    try:
        api = f"https://www.tikwm.com/api/?url={url}"
        r = requests.get(api).json()
        if not r.get("data"):
            print("[red][×] Failed to get sound.[/red]")
            return
        sound_url = r['data']['music']
        filename = custom_filename(".mp3")
        os.system(f'wget -q "{sound_url}" -O "{filename}"')
        move_to_sdcard(filename)
    except Exception as e:
        print(f"[red][×] Error: {e}[/red]")

def download_thumbnail(url):
    print("[yellow][•] Getting thumbnail...[/yellow]")
    try:
        api = f"https://www.tikwm.com/api/?url={url}"
        r = requests.get(api).json()
        if not r.get("data"):
            print("[red][×] Failed to get thumbnail.[/red]")
            return
        thumb_url = r['data']['cover']
        filename = custom_filename(".jpg")
        os.system(f'wget -q "{thumb_url}" -O "{filename}"')
        move_to_sdcard(filename)
    except Exception as e:
        print(f"[red][×] Error: {e}[/red]")

def download_profile_pic(url):
    print("[yellow][•] Getting profile picture...[/yellow]")
    try:
        username = url.strip().split("@")[-1].split("/")[0]
        api = f"https://www.tikwm.com/api/user/info?unique_id={username}"
        r = requests.get(api).json()
        avatar_url = r['data']['user']['avatar']
        filename = custom_filename(".jpg")
        os.system(f'wget -q "{avatar_url}" -O "{filename}"')
        move_to_sdcard(filename)
    except Exception as e:
        print(f"[red][×] Error: {e}[/red]")

def tiktok_handler():
    while True:
        tiktok_menu()
        opt = input("[?] Choose option: ").strip()
        if opt == "1":
            url = input("[?] Enter TikTok profile URL: ").strip()
            download_profile_pic(url)
        elif opt == "2":
            url = input("[?] Enter TikTok video URL: ").strip()
            download_video_nowm(url)
        elif opt == "3":
            url = input("[?] Enter TikTok video URL: ").strip()
            download_thumbnail(url)
        elif opt == "4":
            url = input("[?] Enter TikTok video/sound URL: ").strip()
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