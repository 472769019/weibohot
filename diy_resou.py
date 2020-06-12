#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
from lxml import etree
import sys
import time
from time import strftime, localtime

###网址
url="https://s.weibo.com/ajax/jsonp/gettopsug?uid=5558357013&ref=PC_topsug&url=https%3A%2F%2Fs.weibo.com%2Ftop%2Fsummary%3FRefer%3Dtop_hot%26topnav%3D1%26wvr%3D6&Mozilla=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F78.0.3904.97%20Safari%2F537.36&_cb=STK_15919425917543"
###模拟浏览器
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}

###主函数
def main():
    outputFile = open("reshou.html", 'a')
    sys.stdout = outputFile
    print()
    print(strftime("%Y-%m-%d %H:%M:%S", localtime()))
    list = []
    for i in range(50):
        #执行太快微博会报异常而拒绝访问
        time.sleep(1)
        ###获取html页面
        html=etree.HTML(requests.get(url,headers=header).text)
        html_data = etree.tostring(html, encoding="utf-8",pretty_print=True)
        res = html_data.decode('utf-8')

        #对内容进行截取，会出现js没获取到内容的情况
        try:
            res = res[res.index("is_ad"):]
            res = res[res.index("word"):res.index("}")]
            res = res[res.index(":")+1:]
        except:
            continue
        else:
            if res not in list:
                list.append(res)
                print('<br />')
                print('<a href = "https://s.weibo.com/weibo/'+res[1:-1]+'?topnav=1&wvr=6&Refer=top_button" target = _blank>'+res+'</a>')
    # print(list)

if __name__ == '__main__':
    main()
