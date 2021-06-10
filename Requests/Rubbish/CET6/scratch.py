from lxml import etree
import requests
from PIL import Image
import os
import re


def geturls(url):
    with open('log.txt', 'r', encoding='utf-8') as file:
        r = file.read()
    return re.findall('href=\"(.*?)\"', r)


def getsingle(url):
    "获取单期试卷所有图片"
    response = requests.get(url)
    if response.status_code == 200:
        tree = etree.HTML(response.text)

        titlexpath = '//*[@id="activity-name"]/text()'
        imgxpath = '//*[@id="js_content"]//img'
        audioxpath = '/html/body/div[1]/div[2]/div[1]/div/div[1]/div[3]/section[1]/span/span/@id'
        # 获取标题
        title = tree.xpath(titlexpath)[0].replace(" ", "").replace("\n", "")
        title = re.findall("(.*?)\+", title)[0]+re.findall("打印(.*)", title)[0]
        # 获取听力
        if not os.path.exists('./%s' % title):
            os.mkdir('./%s' % title)
        mediaid, = re.findall('"voice_id":"(.*?)"', response.text)
        mediaurl = 'https://res.wx.qq.com/voice/getvoice?mediaid=%s' % mediaid
        audio = requests.get(mediaurl)
        if audio.status_code == 200:
            with open("./%s/Listening.mp3" % title, "wb") as f:
                f.write(audio.content)
        else:
            print("Audio Error")
        # 获取试卷相片
        detail = tree.xpath(imgxpath)
        i = 0
        for du in detail:
            imglist = du.xpath("./@data-src")[0]
            image = requests.get(imglist).content
            if len(image) > 100 * 1024:
                i += 1
                with open("%s.png" % i, 'wb') as file:
                    file.write(image)
    else:
        print("Error!Your request was declined by website!")
    return title


def topdf(title):
    """将单期图片全部打包成pdf"""
    imglist = os.listdir(".")
    imglist = [img for img in imglist if img.endswith(".png")]
    imgall = []
    for i in range(len(imglist)):
        img = Image.open(imglist[i])
        if img.mode == "RGBA":
            img = img.convert('RGB')
            imgall.append(img)
        else:
            imgall.append(img)
    img1 = imgall[0]
    img2 = imgall[1:]
    img1.save('./%s/%s.pdf' % (title, title), "PDF", resolution=100.0,
              save_all=True, append_images=img2)
    [os.remove(file) for file in imglist]
    print("Downloaded:%s" % title)


def getmaterial(url):
    title = getsingle(url)
    topdf(title)


home = 'https://mp.weixin.qq.com/mp/homepage?__biz=MzUyODQ2OTkxMg==&hid=12&sn=f4afb8b34f4b12ca6514791d308599d7&scene=18'
urls = geturls(home)
for url in urls:
    getmaterial(url)
print("Finished!")
print("%s in total!" % len(urls))
