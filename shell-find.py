import sys
import requests
from os import system
from googlesearch import search

banner="""
░██████╗██╗░░██╗███████╗██╗░░░░░██╗░░░░░
██╔════╝██║░░██║██╔════╝██║░░░░░██║░░░░░
╚█████╗░███████║█████╗░░██║░░░░░██║░░░░░
░╚═══██╗██╔══██║██╔══╝░░██║░░░░░██║░░░░░
██████╔╝██║░░██║███████╗███████╗███████╗
╚═════╝░╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝"""

system('clear')
print('\33[36;1m{}'.format(banner))
print('\33[1;33m================================')
print('\33[32;1m  Author   \33[37;1m:  \33[32;1mHadsXdevPy')
print('\33[32;1m  Version  \33[37;1m:  \33[32;1m1.0.2')
print('\33[32;1m  Team     \33[37;1m:  \33[32;1mBamboSecurity1337')
print('\33[32;1m  Python V \33[37;1m:  \33[32;1m3.9.7')
print('\33[32;1m  TOOL     \33[37;1m:  \33[32;1mShell grabber')
print('\33[1;33m================================')
types=input('\33[31;1m[\33[37;1m+\33[31;1m]\33[37;1m type (uploader/shell) : ')
print('\33[31;1m[\33[37;1m+\33[31;1m]\33[37;1m HASIL : ')
if types=='uploader':
    for url in search('intitle:Uploader By?'):
        req=requests.get(url)
        if req.status_code == 200:
            print('\33[31;1m[\33[37;1m√\33[31;1m]\33[37;1m URL : '+url)
            save=open('hasil.txt', 'w')
            save.write(url)
        else:
            print('\33[31;1m[\33[37;1mx\33[31;1m]\33[37;1m URL : '+url)
elif types=='shell':
    for urll in search('intitle:mini shell by?'):
        reqs=requests.get(urll)
        if reqs.status_code == 200:
            print('\33[31;1m[\33[37;1m√\33[31;1m]\33[37;1m URL : '+urll)
            save=open('hasil.txt', 'w')                 
            save.write(urll)
        else:
            print('\33[31;1m[\33[37;1mx\33[31;1m]\33[37;1m URL : '+urll)
