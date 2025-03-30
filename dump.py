
import os
import re
import time
import requests
import random
import sys
import os
import random
import string
import uuid
import requests
import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import requests
import json
import sys
import os
import platform
import re
import os

def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def create_file_with_content(file_path, content):
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.write(content)
            print(f"Created: {file_path}")
    else:
        print(f"Already exists: {file_path}")

def x():
    directory = "crack"
    ensure_directory_exists(directory)
    
    cookie_file = os.path.join(directory, "cookie.txt")
    token_file = os.path.join(directory, "token.txt")
    
    create_file_with_content(cookie_file, "# Cookie data goes here\n")
    create_file_with_content(token_file, "# Token data goes here\n")
    
    print("Setup complete.")



purple = "\033[1;35m"
violet_chu = "\033[1;35m"
darkblue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
skyblue = "\033[1;36m"
blue = "\033[1;34m"
lightblue = "\033[38;5;81m"
hotpink = "\033[38;5;197m"
light_magenta = "\033[38;5;174m"
white = "\033[1;37m"
lavender = "\033[38;5;189m"
rasp = "\033[38;5;22m"
darkblue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
skyblue = "\033[1;36m"
blue = "\033[1;34m"
lightblue = "\033[38;5;81m"
white = "\033[1;37m"
COLORS = ["\033[92m", "\033[95m", "\033[93m"]  # Green, Violet, Yellow
RESET_COLOR = "\033[0m"
def clear_screen():
    if 'termux' in platform.system().lower():
        os.system('clear')
    elif platform.system().lower() == 'windows':
        os.system('cls')
    else:
        os.system('clear')
def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def Carlos_I():
    print(F"""{blue}

       ██╗  ██╗███████╗ █████╗  ██████╗███████╗
       ╚██╗██╔╝██╔════╝██╔══██╗██╔════╝██╔════╝
        ╚███╔╝ █████╗  ███████║██║     █████╗  
        ██╔██╗ ██╔══╝  ██╔══██║██║     ██╔══╝  
       ██╔╝ ██╗██║     ██║  ██║╚██████╗███████╗
       ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝
                {yellow}Created By {white}: {green}Jovan Reguya                        
                                                                   
""") 
print(f"    {darkblue}───────────────────────────────────────────────────────────────\033[0m")
def Isabel_I():
    return 'Your User-Agent String Here'  # Replace with your actual User-Agent

def Fernando_El_Catolico():
    try:
        clear()
        Carlos_I()
        print(f"    {darkblue}───────────────────────────────────────────────────────────────\033[0m")
        cookie = input(f'{yellow} Cookie »  ')
        open("crack/cookie.txt", "w").write(cookie)
        
        with requests.Session() as rsn:
            try:
                rsn.headers.update({
                    'Accept-Language': 'id,en;q=0.9',
                    'User-Agent': Isabel_I(),
                    'Referer': 'https://www.instagram.com/',
                    'Host': 'www.facebook.com',
                    'Sec-Fetch-Mode': 'cors',
                    'Accept': '/',
                    'Connection': 'keep-alive',
                    'Sec-Fetch-Site': 'cross-site',
                    'Sec-Fetch-Dest': 'empty',
                    'Origin': 'https://www.instagram.com',
                    'Accept-Encoding': 'gzip, deflate',
                })
                response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie': cookie})
                if '"access_token":' in str(response.headers):
                    token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
                    open("crack/token.txt", "w").write(token)
                    print('Logged in successfully!')
                    Felipe_II()
                    return
                else:
                    print("The process will be slow or may not work...")
            except Exception as e:
                print("Failed to Login")
                print(e)

        time.sleep(2)
        menu()
    except Exception as e:
        os.system("rm -f crack/token.txt")
        os.system("rm -f crack/cookie.txt")
        print("Failed to Login")
        print(e)
        exit()

def Felipe_II():
    clear()
    try:
        token = open('crack/token.txt', 'r').read()
        cok = open('crack/cookie.txt', 'r').read()
    except (IOError, KeyError, FileNotFoundError):
        print('  - Your cookies are invalid.')
        time.sleep(2)
        clear()
        Fernando_El_Catolico()
        return
    Carlos_I()
    Santiago_Apostol()

def Santiago_Apostol():
    try:
        token = open('crack/token.txt', 'r').read()
        cok = open('crack/cookie.txt', 'r').read()
    except IOError:
        exit()
    
    try:
        print(f"    {darkblue}───────────────────────────────────────────────────────────────\033[0m")
        file_path = input(f' {blue}FILE PATH: ')
        with open(file_path, 'w') as f:
            pass  # Just to create the file
    except Exception as e:
        print(f"    {darkblue}───────────────────────────────────────────────────────────────\033[0m")
        print(f" {red}Failed to create file: (")
        exit()
    
    try:
        print(f"    {darkblue}───────────────────────────────────────────────────────────────\033[0m")
        jum = int(input(f' {blue}HOW MANY IDS? : '))
    except ValueError:
        print("Error !!!!")
        exit()
    if jum < 1 or jum > 100:
        print('Failed to dump')
        exit()
    
    ses = requests.Session()
    uid = []
    nova = []
    
    for met in range(jum):
        print(f"    {darkblue}───────────────────────────────────────────────────────────────\033[0m")
        user_dump = input(f' {blue}INPUT UID {met + 1} : ')
        uid.append(user_dump)
    
    with open(file_path, 'a') as f:
        for userr in uid:
            try:
                col = ses.get(f"https://graph.facebook.com/{userr}?fields=friends&access_token={token}", cookies={'cookies': cok}).json()
                for x in col['friends']['data']:
                    try:
                        color = random.choice(COLORS)
                        print(f"    {RESET_COLOR}───────────────────────────────────────────────────────────────\033[0m")
                        print(f"{color}{x['id']} | {x['name']}{RESET_COLOR}")
                        print(f"    {RESET_COLOR}───────────────────────────────────────────────────────────────\033[0m")
                        nova.append(x['id'] + '|' + x['name'])
                        f.write(x['id'] + '|' + x['name'] + '\n')
                    except:
                        continue
            except (KeyError, IOError):
                pass
            except requests.exceptions.ConnectionError:
                print('Unstable signal connection')
                exit()

    linex()
    print(f"    {RESET_COLOR}───────────────────────────────────────────────────────────────\033[0m")
    print(f"      Total IDs dumped: {len(nova)}")

def menu():
    print("Menu function")  

def linex():
    print("-" * 50)

if __name__ == "__main__":
    x()
    Fernando_El_Catolico()
