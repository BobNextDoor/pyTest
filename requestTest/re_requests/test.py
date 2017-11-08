import requests
import re
#codeing=utf-8

def getHtml(url):
	page = requests.get(url)
	return page.text

html = getHtml("https://tieba.baidu.com/p/5206905612")

parttern = 'BDE_Image"\ssrc="(.+?\.jpg)"\ssize'

index = 0

result = re.findall(parttern,html)
for imgUrl in result:
	print(imgUrl)
	imgSplitRes = imgUrl.split('/')
	imgName = imgSplitRes[len(imgSplitRes)-1]
	img = requests.get(imgUrl)
	print(imgName)
	imgPath = './pic/' + str(index) + '.jpg'
	index+=1
	print(imgPath)
	imgFile = open(imgPath,'wb')
	imgFile.write(img.content)
	imgFile.close()
