# -*- coding: UTF-8 -*-

import os
import re
import base64
import sys


def decode(file):
    jiamifilename = file  # 待解密文件
    lines = []
    # 打开文件，将数据放入列表
    with open(jiamifilename, 'r') as fp:
        for line in fp:
            lines.append(line)

        # 判断是不是加密文件，如果是才进行解密
        if 'OOO0O0O00' in lines[1]:

            # 第一次base64解码
            p = re.compile("O0O0000O0\('.*'\)")
            y = p.findall(lines[1])
            content = ''
            if y:
                content = y[0].replace("O0O0000O0('", "")
                content = content.replace("')", "")
                content = str(base64.b64decode(content))

            # 准备从第一次base64解码后的内容中查找密钥
            decode_key = ""
            p = re.compile("\),'.*',")
            k = p.findall(content)
            if k:
                decode_key = k[0].replace("),'", "")
                decode_key = decode_key.replace("',", "")

            # 查找要截取字符串长度
            str_length = re.findall(",(\d*)\),", content)

            # 截取文件加密后的密文
            Secret = lines[2][int(str_length[0]):]

            # 准备还原密文

            li = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')
            li_len = len(li)
            xx = ''
            for x in Secret:
                i = decode_key.index(x)
                if i >= li_len:
                    xx += x
                    continue
                xx += li[i]
            # 整理还原后的数据，准备输出到文件。
            strs = base64.b64decode(xx.encode('utf-8'))
            with open(file, 'w') as f:
                f.write('<?php\n\r' + strs.decode('utf-8') + '?>')
            print('file decode success！')


# 遍历文件夹下指定后缀
def traverse_php():
    for root, dirs, files in os.walk('./'):
        for name in files:
            if (name.endswith(".php")):
                php_file = os.path.join(root, name)
                decode(php_file)



def main():
    helpinfo = r"""
                *****************************************************************************
                将解密文件夹放在脚本同目录下
                python O0O0000O0_decode.py 
                *****************************************************************************
            """

    if sys.argv[0]:
        traverse_php()


if __name__ == '__main__':
    main()
