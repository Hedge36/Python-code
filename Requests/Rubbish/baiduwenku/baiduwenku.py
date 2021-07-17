import requests
import re
import json
import os

session = requests.Session()


def fetch_url(url):
    return session.get(url).content.decode('GBK')


def get_doc_id(url):
    return re.findall("view/(.*).html", url)[0]


def parse_type(content):
    return re.findall(r"docType.*?\:.*?\'(.*?)\'\,", content)[0]


def parse_title(content):
    return re.findall(r"title.*?\:.*?\'(.*?)\'\,", content)[0]


def parse_doc(content):
    result = ''
    url_list = re.findall('(https.*?0.json.*?)\\\\x22}', content)
    url_list = [addr.replace("\\\\\\/") for addr in url_list]
    for url in url_list[:-5]:
        content = fetch_url(url)
        y = 0
        txtlists = re.findall('"c":"(.*?)".*?"y":"(.*?)",', content)
        for item in txtlists:
            if not y == item[1]:
                y = item[1]
                n = '\n'
            else:
                n = ''
            result += n
            result += item[0].encode('utf-8').decode('unicode_escape', 'ignore')
        return result


def parse_txt(doc_id):
    content_url = 'https://wenku.baidu.com/api/doc/getdocinfo?callback=cb&doc_id=' + doc_id
    content = fetch_url(content_url)
    md5 = re.findall('"md5sum":"(.*?)"', content)[0]
    pn = re.findall('"totalPageNum":"(.*?)"', content)[0]
    rsign = re.findall('"rsign":"(.*?)"', content)[0]
    content_url = 'https://wkretype.bdimg.com/retype/text/' + \
        doc_id+'?rn='+pn+'&type=txt'+md5+'&rsign='+rsign
    content = json.loads(fetch_url(content_url))
    result = ''
    for item in content:
        for i in item['parages']:
            result += i['c'].replace('\\r', '\r').replace('\\n', '\n')
    return result


def parse_other(doc_id):
    content_url = "https://wenku.baidu.com/browse/getbcsurl?doc_id=" + \
        doc_id + "&pn=1&rn=99999&type=ppt"
    content = fetch_url(content_url)
    url_list = re.findall('{"zoom":"(.*?)","page"', content)
    url_list = [item.replace('\\', '') for item in url_list]
    if not os.path.exists(doc_id):
        os.mkdir(doc_id)
    for index, url in enumerate(url_list):
        content = session.get(url).content
        path = os.path.join(doc_id, str(index)+'.jpg')
        with open(path, 'wb') as f:
            f.write(content)
        print("Image is saved in dir " + doc_id)


def save_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Saved as " + filename)


def main():
    # url = input("Enter the url of wenku")
    url = text_url
    content = fetch_url(url)
    doc_id = get_doc_id(url)
    filetype = parse_type(content)
    title = parse_title(content)
    if filetype == 'doc':
        result = parse_doc(content)
        save_file(title + ".txt", result)
    elif filetype == 'txt':
        result = parse_txt(doc_id)
        save_file(title + ".txt", result)
    else:
        parse_other(doc_id)


if __name__ == '__main__':
    text_url = 'https://wenku.baidu.com/view/fad890f04a7302768f993929.html?fron=search'
    main()
