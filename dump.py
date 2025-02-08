import os
import re
import time
import requests
import random
import sys
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
def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def Carlos_I():
    print(f"""

     {red}██████╗ ███████╗ █████╗ ████████╗██╗  ██╗
     ██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║  ██║
     ██║  ██║█████╗  ███████║   ██║   ███████║
     ██║  ██║██╔══╝  ██╔══██║   ██║   ██╔══██║
     ██████╔╝███████╗██║  ██║   ██║   ██║  ██║
     ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝
\033[34m───────────────────────────────────────────────────────────────\033[0m                                        
    {white}Created {yellow}& Manipulated By: Jovan a.k.a {red}D34TH
\033[34m───────────────────────────────────────────────────────────────\033[0m                                                                                
""") 

import os

def ensure_file_exists(filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)  # Create directory if not exists
    if not os.path.exists(filepath):  # Create file if not exists
        with open(filepath, "w") as f:
            pass  # Just create an empty file

# Ensure the necessary files exist before accessing them
ensure_file_exists("ambot/crack/cookie.txt")
ensure_file_exists("ambot/crack/token.txt")

def Isabel_I():
    return 'Your User-Agent String Here'  # Replace with your actual User-Agent

def Fernando_El_Catolico():
    try:
        ensure_file_exists('ambot/crack/cookie.txt')
        clear()
        Carlos_I()
        cookie = input(f'   {green}IMPORT {red}[COOKIE] {white}:  ')
        print(f"\033[34m───────────────────────────────────────────────────────────────\033[0m    ")
        open("ambot/crack/cookie.txt", "w").write(cookie)
        
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
                    open("ambot/crack/token.txt", "w").write(token)
                    print('Logged in successfully!')
                    Felipe_II()  # Call Felipe_II after successful login
                    return  # Exit if the first login attempt is successful
                else:
                    print("The process will be slow or may not work...")
            except Exception as e:
                print("Failed to Login")
                print(e)

        with requests.Session() as session:
            try:
                cur = session.get('https://adsmanager.facebook.com/adsmanager/manage/campaigns?&breakdown_regrouping=1', cookies={'cookie': cookie}).text
                act = re.findall('act=(\d+)', cur)[0]
                act_response = session.get(f"https://adsmanager.facebook.com/adsmanager/manage/campaigns?act={act}&breakdown_regrouping=1", cookies={'cookie': cookie}).text
                tok = re.search('accessToken="(.*?)"', act_response).group(1)
                open("ambot/crack/token.txt", "w").write(tok)
                print('Logged in successfully!')
                Felipe_II()  # Call Felipe_II after successful login
            except Exception as e:
                print("Failed to Get Token")
                print(e)
        
        time.sleep(2)
        menu()
    except Exception as e:
        os.system("rm -f ambot/crack/token.txt")
        os.system("rm -f ambot/crack/cookie.txt")
        print("Failed to Login")
        print(e)
        exit()

def Felipe_II():
    clear()
    try:
        token = open('ambot/crack/token.txt', 'r').read()
        cok = open('ambot/crack/cookie.txt', 'r').read()
    except (IOError, KeyError, FileNotFoundError):
        print('  - Your cookies are invalid.')
        time.sleep(2)
        clear()
        Fernando_El_Catolico()
        return
    except KeyError:
        try:
            os.remove("ambot/crack/cookie.txt")
            os.remove("ambot/crack/token.txt")
        except:
            pass
        print('  - It seems your account is checkpointed...')
        time.sleep(2)
        menu()
        clear()
    Carlos_I()
    Santiago_Apostol()

def Santiago_Apostol():
    try:
        token = open('ambot/crack/token.txt', 'r').read()
        cok = open('ambot/crack/cookie.txt', 'r').read()
    except IOError:
        exit()
    try:
        file_path = input(f'    {red}WHERE TO SAVE DUMPED IDS :  ')
        with open(file_path, 'w') as f:
            pass  # Just to create the file
    except Exception as e:
        print(f"  「!」Failed to create file: (")
        exit()
    
    try:
        print(f"\033[34m───────────────────────────────────────────────────────────────\033[0m    ")
        jum = int(input(f'     {green}HOW MANY UID :  '))
        print(f"\033[34m───────────────────────────────────────────────────────────────\033[0m    ")
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
        user_dump = input(f'   {green}INPUT UID {met + 1}: ')
        print(f"\033[34m───────────────────────────────────────────────────────────────\033[0m    ")
        uid.append(user_dump)
    
    with open(file_path, 'a') as f:
        for userr in uid:
            try:
                col = ses.get(f"https://graph.facebook.com/{userr}?fields=friends&access_token={token}", cookies={'cookies': cok}).json()
                for x in col['friends']['data']:
                    try:
                        sys.stdout.write(f"\r       Dumping {len(nova)} IDs....")
                        sys.stdout.flush()
                        nova.append(x['id'] + '|' + x['name'])
                        f.write(x['id'] + '|' + x['name'] + '\n')
                    except:
                        continue
            except (KeyError, IOError):
                pass
            except requests.exceptions.ConnectionError:
                print('Unstable signal connection')
                exit()

       
        for friend in nova:
            friend_id = friend.split('|')[0]
            try:
                friend_col = ses.get(f"https://graph.facebook.com/{friend_id}?fields=friends&access_token={token}", cookies={'cookies': cok}).json()
                print(friend_col)
                if 'friends' in friend_col:
                    for x in friend_col['friends']['data']:
                        try:
                            print(f"\033[91m[DUMPING] = \033[93m{x['id']} \033[97m= \033[93m{x['name']}")
                            sys.stdout.flush()
                            nova.append(x['id'] + '|' + x['name'])
                            f.write(x['id'] + '|' + x['name'] + '\n')
                        except:
                            continue
            except (KeyError, IOError):
                continue
            except requests.exceptions.ConnectionError:
                print('Unstable signal connection')
                exit()
    
    linex()
    print(f"      Total IDs dumped: {len(nova)}")

def menu():
    print("Menu function")  

def linex():
    print("-" * 50)

if __name__ == "__main__":
    Fernando_El_Catolico()
