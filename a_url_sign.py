# -*- coding: UTF-8 -*-

import hashlib
import time
import httplib

# 防盗链A类鉴权算法实现
domain = "vdn1.vzuu.com"
host = "218.64.94.195"
url = "/SD/"
file = "2ed292f0-ddb8-11e8-8886-0242ac112a15.mp4"
ts = "1542188723"
print ts
key = '********'
strtosign = url + file + '-' + str(ts) + '-0-0-' + key

md5=hashlib.md5(strtosign.encode('utf-8')).hexdigest()
print(md5)

request_url = "https://" + domain + url + file + "?auth_key=" + str(ts) + "-0-0-" + md5 + "&expiration=" + str(ts) + "&disable_local_cache=0"
print request_url

conn = httplib.HTTPConnection(host)
conn.request(method="GET",url=request_url)

response = conn.getresponse()
print response
res = response.read()
print "http_code: " + str(response.status)
print res

ts_list = res.split("\n")
ts_l = []
for l in ts_list:
    if "ts" in l:
        ts_l.append(l)

print ts_l

for l in ts_l:
    request_url = "https://" + domain + url + l
    print request_url

    conn = httplib.HTTPConnection(host)
    conn.request(method="GET", url=request_url)

    response = conn.getresponse()
    res = response.read()
    print "http_code: " + str(response.status)



