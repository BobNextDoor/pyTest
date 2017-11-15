from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from urllib import request

def url_open(url):
	req = request.Request(url,headers=headers)
	response = request.urlopen(req)
	return response.read()

desUrl = 'https://baidu.com'

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

req = request.Request(desUrl, headers=headers)

html = request.urlopen(req).read()

bsObj = BeautifulSoup(html,"html.parser")
imgs = bsObj.findAll("img",{"src":re.compile("jpg")})
index = 0
for img in imgs:
	imgPath = './pic/' + str(index) + '.jpg'
	index+=1
	print(imgPath)
	imgFile = open(imgPath,'wb')
	imgFile.write(url_open(img['src']))
	imgFile.close()
#print(img['src'])
