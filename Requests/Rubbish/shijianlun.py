import requests
from lxml import etree

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) / "
                         "Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.1071 SLBChan/8",
           }
url = "http://www.360doc.com/content/20/1122/11/964300_947201530.shtml"
r = requests.get(url=url, headers=headers)
r.encoding = r.apparent_encoding
html = r.text

word = []
tree = etree.HTML(html)
# text = tree.xpath('string(//*[@id="artContent"])')
# with open("scrapy.txt", "w") as f:
#     f.write(text)
text = tree.xpath('//*[@id="artContent"]//text()')
print(text)
with open("scrapy.txt", "w") as f:
    for t in text:
        if t.strip() != '':
            if t[-1] == '，':
                f.write(t)
            else:
                f.write(t + "\n     ")
