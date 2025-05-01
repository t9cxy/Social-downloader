import os
import re
import subprocess
from rich.console import Console
from rich.panel import Panel

console = Console()

def clear(): os.system("clear")

def banner():
    console.print(Panel.fit("[bold cyan]TIKTOK DOWNLOADER TOOL[/bold cyan]\n[green]by Alone[/green]"))

def main_menu():
    banner()
    console.print("[bold yellow]Main Menu:[/bold yellow]")
    console.print("[cyan]1.[/cyan] TikTok")
    console.print("[cyan]0.[/cyan] Exit")

def tiktok_menu():
    clear()
    banner()
    console.print("[bold yellow]TikTok Options:[/bold yellow]")
    console.print("[cyan]1.[/cyan] Download Profile Picture")
    console.print("[cyan]2.[/cyan] Download Video")
    console.print("[cyan]3.[/cyan] Download Thumbnail/Photo")
    console.print("[cyan]4.[/cyan] Download Sound")
    console.print("[cyan]0.[/cyan] Back")

def ask_filename():
    custom_name = input("\n[?] Enter custom filename (no extension): ").strip()
    return custom_name

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
        filename = ask_filename() + ".jpg"
        os.system(f"wget -O {filename} \"{avatar_url}\"")
        os.system(f"mv {filename} /sdcard/download")
        console.print(f"[green]Saved as {filename} in /sdcard/download[/green]")
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")

def download_video(link):
    console.print("[blue]Downloading video...[/blue]")
    filename = ask_filename() + ".mp4"
    try:
        subprocess.run([
            "yt-dlp", "-o", filename, link
        ])
        os.system(f"mv \"{filename}\" /sdcard/download")
        console.print(f"[green]Saved as {filename} in /sdcard/download[/green]")
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")

def download_photo(link):
    console.print("[blue]Downloading thumbnail...[/blue]")
    filename = ask_filename() + ".jpg"
    try:
        subprocess.run([
            "yt-dlp", "--write-thumbnail", "--skip-download", "-o", filename, link
        ])
        # yt-dlp adds .webp by default, rename it
        webp_file = filename + ".webp"
        if os.path.exists(webp_file):
            os.rename(webp_file, filename)
            os.system(f"mv {filename} /sdcard/download")
            console.print(f"[green]Saved as {filename} in /sdcard/download[/green]")
        else:
            console.print("[red]Thumbnail not found[/red]")
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")

def download_sound(link):
    console.print("[blue]Downloading sound...[/blue]")
    filename = ask_filename() + ".mp3"
    try:
        subprocess.run([
            "yt-dlp", "-x", "--audio-format", "mp3", "-o", filename, link
        ])
        os.system(f"mv \"{filename}\" /sdcard/download")
        console.print(f"[green]Saved as {filename} in /sdcard/download[/green]")
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")

def tiktok_handler():
    while True:
        tiktok_menu()
        choice = input("\n[?] Enter choice: ").strip()
        if choice == "1":
            link = input("[?] Enter TikTok profile URL: ").strip()
            download_profile_pic(link)
        elif choice == "2":
            link = input("[?] Enter TikTok video URL: ").strip()
            download_video(link)
        elif choice == "3":
            link = input("[?] Enter TikTok video URL: ").strip()
            download_photo(link)
        elif choice == "4":
            link = input("[?] Enter TikTok video or sound URL: ").strip()
            download_sound(link)
        elif choice == "0":
            break
        else:
            console.print("[red]Invalid option[/red]")
        input("\n[press ENTER to continue]")

def main():
    while True:
        clear()
        main_menu()
        choice = input("\n[?] Enter choice: ").strip()
        if choice == "1":
            tiktok_handler()
        elif choice == "0":
            console.print("[cyan]Goodbye![/cyan]")
            break
        else:
            console.print("[red]Invalid option[/red]")
            input("\n[press ENTER to continue]")

if __name__ == "__main__":
    main()