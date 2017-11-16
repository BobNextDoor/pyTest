#codeing=utf-8
import re
import os
from bs4 import BeautifulSoup
from urllib import request


#set headers
opener = request.build_opener()
opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36')]
request.install_opener(opener)

#get beautifulobject
def getBSObj(url):
	html = request.urlopen(url)
	return BeautifulSoup(html)

def getContentUrlList(url):
	contentBS = getBSObj(url)
	listBS = bsObj.findAll('a',{'href':re.compile("^viewthread.*(\d){5}$"), 'style':re.compile(".*")})
	urlList = []
	for content in listBS:
		urlList.append(content['href'])
	return urlList

def fixUrl(url):
	baseUrl = 'http://91.t9p.today/index.php'
	return baseUrl[:-9] + url
#get whole pic from a single url
def downloadPic(url):
	pageBS = getBSObj(url)
	title = pageBS.head.title.text[:-45].rstrip()
	picDir = './pic/' + title
	if os.path.isdir(picDir):
		pass
	else:
		os.mkdir(picDir)
	
	imgUrlList = pageBS.findAll('img',{'file':re.compile(".*(attachments).*")})
	for imgUrl in imgUrlList:
		imgPath = url[:url.rfind('/')+1]+imgUrl['file']
		#imgName = picDir + imgUrl['file'][imgUrl['file'].rfind('/'):]
		imgName = './pic/' + imgUrl['file'][imgUrl['file'].rfind('/'):] 
		print(imgPath)
		print(imgName)
		#print(imgPath)
		request.urlretrieve(imgPath,imgName)
		print("done")

#def getImg(url):
	
#get content url

desUrl = "http://91.t9p.today/index.php"

bsObj = getBSObj(desUrl)

urlList = getContentUrlList(desUrl)

urlList = map(fixUrl,urlList)

for url in urlList:
	print(url)
	bs = getBSObj(url)
	print(bs.head.title.text[:-45])
	#print (bs.prettify)
	imgurl = bs.findAll('img',{'file':re.compile(".*(attachments).*")})
	#for img in imgurl:
	#	print(img)
	downloadPic(url)
	print("sigle page Done")
