import os
import subprocess
from rich.console import Console
from rich.panel import Panel
from datetime import datetime

console = Console()

def clear():
    os.system("clear")

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
[bold red]0.[/bold red] Back
""", title="[bold cyan]TikTok Downloader[/bold cyan]"))

def move_to_sdcard(filename):
    destination = "/sdcard/download"
    os.makedirs(destination, exist_ok=True)
    os.rename(filename, os.path.join(destination, filename))
    console.print(f"[green][✔] Saved to {destination}/{filename}[/green]")

def custom_filename():
    name = input("[?] Enter custom file name (without extension): ").strip()
    return f"{name}.mp4"

def download_video_nowm(url):
    console.print("[yellow][•] Downloading video using yt-dlp...[/yellow]")
    filename = custom_filename()
    try:
        # Download video without watermark using yt-dlp
        subprocess.run(["yt-dlp", "-o", filename, url], check=True)
        move_to_sdcard(filename)
    except subprocess.CalledProcessError as e:
        console.print(f"[red][×] Error downloading video: {e}[/red]")

def tiktok_handler():
    while True:
        tiktok_menu()
        opt = input("[?] Choose option: ").strip()
        if opt == "1":
            url = input("[?] Paste TikTok video URL: ").strip()
            download_video_nowm(url)
        elif opt == "0":
            break
        else:
            console.print("[red][×] Invalid option[/red]")
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
            console.print("[red][×] Invalid option[/red]")
            input("[Press ENTER]")

if __name__ == "__main__":
    main()