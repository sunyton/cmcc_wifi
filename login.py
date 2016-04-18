# -*- coding:utf-8 -*-

import requests
from lxml import etree

import re


# 获取登陆时的paramStr(cstr2)
url = "http://wlan.jsyd139.com/?wlanacname=0027.0514.250.00&wlanuserip=10.79.108.188&ssid=CMCC-EDU&vlan=300&wlanacip=120.195.127.130&NASID=0749051425000460";

headers = {
"Host": "wlan.jsyd139.com",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Language": "zh-CN,en-US;q=0.7,en;q=0.3",
"Accept-Encoding": "gzip, deflate",
"Content-Length": "0",
"Cache-Control": "max-age=0"

}
r = requests.get(url,headers=headers)

re_html = r.text

print re_html

doc = etree.HTML(re_html)

paramstr = doc.xpath('//frame[2]/@src')

#print paramstr

cstr = paramstr[0]

cstr1 = cstr.replace('style/university/index.jsp?','')

cstr2 = cstr1.replace('%0A','%0D%0A')

print cstr2

#输入用户名，密码

username= raw_input("输入用户名： ")
password = raw_input("输入密码： " )


#post登陆

login_url = "http://wlan.jsyd139.com/authServlet"

login_data = cstr2+"&UserType=1&province=&pwdType=1&UserName="+username+"&PassWord="+password

num_data = len(login_data)

print num_data

#reffer

reffer = "http://wlan.jsyd139.com/style/university/index.jsp?" + cstr2

login_headers = {

"Host": "wlan.jsyd139.com",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Language": "zh-CN,en-US;q=0.7,en;q=0.3",
"Accept-Encoding": "gzip, deflate",
"Referer": reffer ,
"Content-Type": "application/x-www-form-urlencoded",
"Content-Length": num_data

}

page = requests.post(login_url,data=login_data,headers=login_headers,allow_redirects=False)

print page.headers['location']


#下面的操作就是存取用户名，密码，下线location的相关io


















