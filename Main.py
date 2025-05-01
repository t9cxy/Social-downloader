import os
import shutil
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

def move_to_sdcard(filename):
    destination = "/sdcard/download"
    os.makedirs(destination, exist_ok=True)
    try:
        shutil.move(filename, os.path.join(destination, filename))
        console.print(f"[green][✔] Saved to {destination}/{filename}[/green]")
    except Exception as e:
        console.print(f"[red][×] Failed to move file: {e}[/red]")

def get_custom_filename(extension=".mp4"):
    name = input("[?] Enter custom file name (without extension): ").strip()
    return f"{name}{extension}"

def download_with_yt_dlp(url, extension=".mp4"):
    filename = get_custom_filename(extension)
    try:
        console.print("[yellow][•] Downloading...[/yellow]")
        subprocess.run(["yt-dlp", "-o", filename, url], check=True)
        move_to_sdcard(filename)
    except subprocess.CalledProcessError as e:
        console.print(f"[red][×] yt-dlp error: {e}[/red]")

def tiktok_menu():
    while True:
        clear()
        console.print(Panel.fit(logo() + f"""
[bold green]1.[/bold green] Download Video (No Watermark)
[bold green]2.[/bold green] Download Profile Picture
[bold green]3.[/bold green] Download Sound
[bold green]4.[/bold green] Download Photos
[bold red]0.[/bold red] Back
""", title="[bold cyan]TikTok Tool[/bold cyan]"))

        choice = input("[?] Choose option: ").strip()
        if choice == "1":
            url = input("[?] Paste TikTok video URL: ").strip()
            download_with_yt_dlp(url)
        elif choice == "2":
            user = input("[?] Enter TikTok username (without @): ").strip()
            url = f"https://www.tiktok.com/@{user}"
            download_with_yt_dlp(url, extension=".jpg")
        elif choice == "3":
            url = input("[?] Paste TikTok video or sound URL: ").strip()
            filename = get_custom_filename(".mp3")
            try:
                subprocess.run(["yt-dlp", "-x", "--audio-format", "mp3", "-o", filename, url], check=True)
                move_to_sdcard(filename)
            except subprocess.CalledProcessError as e:
                console.print(f"[red][×] Error downloading audio: {e}[/red]")
        elif choice == "4":
            url = input("[?] Paste TikTok photo post URL: ").strip()
            filename = get_custom_filename(".zip")
            try:
                subprocess.run(["yt-dlp", "--write-all-thumbnails", "--convert-thumbnails", "jpg", "-o", filename, url], check=True)
                move_to_sdcard(filename)
            except subprocess.CalledProcessError as e:
                console.print(f"[red][×] Error downloading photos: {e}[/red]")
        elif choice == "0":
            break
        else:
            console.print("[red][×] Invalid option[/red]")
        input("[Press ENTER to return to menu]")

def main_menu():
    while True:
        clear()
        console.print(Panel.fit(logo() + f"""
[bold green]1.[/bold green] TikTok
[bold red]0.[/bold red] Exit
""", title=f"[bold cyan]Main Menu • {datetime.now().strftime('%Y-%m-%d')}[/bold cyan]"))

        opt = input("[?] Choose option: ").strip()
        if opt == "1":
            tiktok_menu()
        elif opt == "0":
            clear()
            break
        else:
            console.print("[red][×] Invalid option[/red]")
            input("[Press ENTER]")

if __name__ == "__main__":
    main()