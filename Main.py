import os
import re
import subprocess
from rich.console import Console
from rich.panel import Panel

console = Console()

def clear(): os.system("cls" if os.name == "nt" else "clear")

def banner():
    console.print(Panel.fit("[bold cyan]TIKTOK DOWNLOADER TOOL[/bold cyan]\n[green]by Alone[/green]"))

def menu():
    banner()
    console.print("[bold yellow]Choose an option:[/bold yellow]")
    console.print("[cyan]1.[/cyan] Download Profile Picture")
    console.print("[cyan]2.[/cyan] Download Video")
    console.print("[cyan]3.[/cyan] Download All Photos from Video")
    console.print("[cyan]4.[/cyan] Download Sound from Video")
    console.print("[cyan]5.[/cyan] Exit")

def get_video_id(url):
    match = re.search(r'/video/(\d+)', url)
    return match.group(1) if match else None

def download_profile_pic(link):
    console.print("[blue]Fetching profile picture...[/blue]")
    username = re.findall(r'tiktok\.com/@([a-zA-Z0-9_.]+)', link)
    if not username:
        console.print("[red]Invalid profile URL![/red]")
        return
    try:
        from TikTokApi import TikTokApi
        api = TikTokApi()
        user = api.user(username[0])
        user_info = user.info()
        avatar_url = user_info['user']['avatarLarger']
        os.system(f"wget -O {username[0]}_profile.jpg \"{avatar_url}\"")
        console.print(f"[green]Profile picture saved as {username[0]}_profile.jpg[/green]")
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")

def download_video(link):
    console.print("[blue]Downloading video...[/blue]")
    try:
        subprocess.run(["yt-dlp", "-o", "%(title)s.%(ext)s", link])
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")

def download_photos(link):
    console.print("[blue]Extracting photos from video...[/blue]")
    try:
        subprocess.run(["yt-dlp", "--write-thumbnail", "--skip-download", "-o", "%(title)s.%(ext)s", link])
        console.print("[green]Photos downloaded (thumbnail). Full photo extraction is limited by TikTok.[/green]")
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")

def download_sound(link):
    console.print("[blue]Downloading audio...[/blue]")
    try:
        subprocess.run(["yt-dlp", "-x", "--audio-format", "mp3", "-o", "%(title)s.%(ext)s", link])
        console.print("[green]Sound downloaded as MP3.[/green]")
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")

def main():
    while True:
        clear()
        menu()
        choice = input("\n[?] Enter choice: ").strip()
        if choice == "1":
            link = input("[?] Enter TikTok profile URL: ").strip()
            download_profile_pic(link)
        elif choice == "2":
            link = input("[?] Enter TikTok video URL: ").strip()
            download_video(link)
        elif choice == "3":
            link = input("[?] Enter TikTok video URL: ").strip()
            download_photos(link)
        elif choice == "4":
            link = input("[?] Enter TikTok video or sound URL: ").strip()
            download_sound(link)
        elif choice == "5":
            console.print("[cyan]Exiting...[/cyan]")
            break
        else:
            console.print("[red]Invalid option[/red]")
        input("\n[press ENTER to return to menu]")

if __name__ == "__main__":
    main()