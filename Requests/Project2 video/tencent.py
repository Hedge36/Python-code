
import re
import random
import urllib.request


# 构建用户代理
uapools = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
           "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
           "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0",
           ]
# 从用户代理池随机选取一个用户代理


def ua(uapools):
    thisua = random.choice(uapools)
    # print(thisua)
    headers = ("User-Agent", thisua)
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    # 设置为全局变量
    urllib.request.install_opener(opener)


# 获取源码
def get_content(page, lastId):
    url = "https://video.coral.qq.com/varticle/3242201702/comment/v2?callback=_varticle3242201702commentv2&orinum=10&oriorder=o&pageflag=1&cursor=" + \
        lastId+"&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=132&_=" + \
        str(page)
    html = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
    return html


# 从源码中获取评论的数据
def get_comment(html):
    pat = '"content":"(.*?)"'
    rst = re.compile(pat, re.S).findall(html)
    return rst


# 从源码中获取下一轮刷新页的ID
def get_lastId(html):
    pat = '"last":"(.*?)"'
    lastId = re.compile(pat, re.S).findall(html)[0]
    return lastId


def main():
    ua(uapools)
    # 初始页面
    page = 1576567187274
    # 初始待刷新页面ID
    lastId = "6460393679757345760"
    for i in range(1, 6):
        html = get_content(page, lastId)
        # 获取评论数据
        commentlist = get_comment(html)
        print("------第"+str(i)+"轮页面评论------")
        for j in range(1, len(commentlist)):
            print("第"+str(j)+"条评论：" + str(commentlist[j]))
        # 获取下一轮刷新页ID
        lastId = get_lastId(html)
        page += 1


main()
