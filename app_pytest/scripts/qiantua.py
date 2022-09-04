import os
import re
import urllib.request

def getHtml(url):
    page=urllib.request.urlopen(url)
    html=page.read()
    
    return html

def getImg(html):
    reg=r'src="(.+?\.jpg)" pic_ext'
    print(reg)
    img=re.compile(reg)
    h=html.decode('utf-8')
    # print(html)
    img_list=re.findall(img,h)
    path=os.getcwd()+'/qiantu/pic/'
    i=0
    for imgurl in img_list:
        urllib.request.urlretrieve(imgurl,path+'%s.jpg' % i)
        i+=1


html=getHtml("https://tieba.baidu.com/p/2460150866?red_tag=1839853617")
print(getImg(html)) 