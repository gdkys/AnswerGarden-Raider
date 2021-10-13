import time

import requests
import random
import string

id = input("Input the answergarden id: ")
replays = input("How many words should get spammed: ")

header  = {

"Cookie" : "PHPSESSID=uje6grehhf37125cc2fcc0eu05; _ga=GA1.2.377536955.1634148278; _gid=GA1.2.960881651.1634148278; __gads=ID=cc3657b1b01f43a3-22c00c50f4ca00f4:T=1634148279:RT=1634148279:S=ALNI_MbIPVVOUZ__AmkYp_IEttnlh9PSVQ; _gat=1",
"Content-Length" : "72",
"Cache-Control" : "max-age=0",
"Sec-Ch-Ua" : '";Not A Brand";v="99", "Chromium";v="94"',
"Sec-Ch-Ua-Mobile" : "?0",
"Sec-Ch-Ua-Platform": "Windows",
"Upgrade-Insecure-Requests" : "1",
"Origin" : "https://answergarden.ch",
"Content-Type" : "application/x-www-form-urlencoded",
"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Sec-Fetch-Site" : "same-origin",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-User" : "?1",
"Sec-Fetch-Dest" : "document",
"Referer" : "https://answergarden.ch/" + id,
"Accept-Encoding": "gzip, deflate",
"Accept-Language" : "en-US,en;q=0.9"
}

replays = int(replays)
for i in range(replays):
    word = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    requests.post("https://answergarden.ch/" + id,data="answer=" + word + "&action=websubmit&id="+ id + "output=html&submit.x=0&submit.y=0", headers=header)