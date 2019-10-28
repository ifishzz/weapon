import urllib.request
import sys

def get_tplog(url):
    for y in range(5,8):
        for r in range(1,32):
            if r < 10:
                r = '0' + str(r)
            get_url = f"{url}/Runtime/Logs/Home/19_0{y}_{r}.log"
            try:
                response = urllib.request.urlopen(get_url)
                html = response.read()         # 获取到页面的源代码
                txt = html.decode('utf-8')     # 转化为 utf-8 编码
                print(txt)
                with open(f'./log.txt','w+') as f:
                    f.write(txt)
            except Exception as e:
                print(e)
    return 1
if get_tplog('http://www.xx.com'):
    print('over!')


    # def get_url(url):
    #     url_list = list()
    #     for _ in range(5, 9):
    #         for x in range(1, 32):
    #             if x < 10:
    #                 x = '0' + str(x)
    #             url_format = url.format(_, x)
    #             # print(url)
    #             url_list.append(url_format)
    #     return url_list
    #
    #
    # print(get_url('http://www.xx.com/Runtime/Logs/Home/19_0{}_{}.log'))

