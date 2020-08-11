import requests
from urllib import parse
import json
from keywords_fit import nsword_fit as nsw_fit
import base64

imgpath = './1.jpg'
imgbase64 = None
with open(imgpath,'rb') as f:
    imgbase64 = base64.b64encode(f.read())
imgString2 = imgbase64.decode('utf-8')
imgString = 'base64,' + imgString2
data = {"imgString":imgString}
header = {'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
postUrl = 'http://127.0.0.1:8080/text'
data = json.dumps(data)
r = requests.post(postUrl, data=data, headers=header).text
# 增加异常捕捉，存在某些时候识别异常
sign = 0
try:
    r = json.loads(r)
    sign = 1
except BaseException:
    print('识别异常')
list_ = r['data']
text_out = ''
# 文字按行输出
print('=============图像内容-开始=============')
for n in list_:
    print(n['text'])
    text_out = text_out + n['text']
print('==============图像内容-结束==============')

nsw_out = nsw_fit(text_out)
if len(nsw_out) == 0:
    print('>>>无敏感字符')
else:
    print('>>>存在敏感字符',nsw_out)
