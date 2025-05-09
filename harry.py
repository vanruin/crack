
import os
import re
import time
import requests
import random
import sys

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def Carlos_I():
    print("""
███████ ██ ██      ███████      ██████ ██████  ███████  █████  ████████ ███████ 
██      ██ ██      ██          ██      ██   ██ ██      ██   ██    ██    ██      
█████   ██ ██      █████       ██      ██████  █████   ███████    ██    █████   
██      ██ ██      ██          ██      ██   ██ ██      ██   ██    ██    ██      
██      ██ ███████ ███████      ██████ ██   ██ ███████ ██   ██    ██    ███████ 
                                                                                
                                                                                
""") 

def Isabel_I():
    return 'Your User-Agent String Here'  # Replace with your actual User-Agent

def Fernando_El_Catolico():
    try:
        clear()
        Carlos_I()
        cookie = input('   「 Cookie 」»  ')
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
        file_path = input(f'    「?」File path to save accounts: ')
        with open(file_path, 'w') as f:
            pass  # Just to create the file
    except Exception as e:
        print(f"  「!」Failed to create file: (")
        exit()
    
    try:
        jum = int(input('     「?」How many uid to input?: '))
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
        user_dump = input(f'   「?」Input uid {met + 1}: ')
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
                if 'friends' in friend_col:
                    for x in friend_col['friends']['data']:
                        try:
                            sys.stdout.write(f"\r      Dumping {len(nova)} IDs....")
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
