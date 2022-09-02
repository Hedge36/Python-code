import requests
from urllib import parse
import time
import re
import pprint


class KuGou():
    def __init__(self, name):
        self.Name = name

    def get_reponse(self, url):
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
                   'cookie': '',
                   'referer': 'https://www.kugou.com/yy/html/search.html'
                   }  # 携带user-agent，cookie，referer三个参数
        time.sleep(2)  # 加来玩的
        response = requests.get(url=url, headers=headers)
        return response

    def get_song_info(self):
        song_name = parse.quote(self.Name)
        url = 'https://songsearch.kugou.com/song_search_v2?callback=jQuery112406923427025623534_1585454373397&keyword={}&page=1&pagesize=30&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0&_=1585454373399'.format(
            song_name)
        time.sleep(2)
        response = self.get_reponse(url=url).content.decode('utf-8')
        return response

    def get_song_list(self):
        data_info = self.get_song_info()
        file_name = re.findall('"FileName":"(.*?)"', data_info)
        song_name_list = []
        for index, songs in enumerate(file_name):
            song_name = songs.replace(
                '<em>{}<\\/em>'.format(self.Name), '{}'.format(self.Name))
            song_name_list.append(str(index) + '、' + song_name)
        return song_name_list

    def get_song_hash(self):
        data_info = self.get_song_info()
        song_hash = re.findall('"FileHash":"(.*?)"', data_info)
        return song_hash

    def save_song(self, choice):
        song_hash = self.get_song_hash()
        url = 'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&callback=jQuery191017845313983799804_1591241136863&hash={}&album_id=37376237&dfid=0j14jN41N6PP0q6mOr1iALP1&mid=be4d7c2fb6112a816b8dece9812cdfc8&platid=4&_=1591241136865'.format(
            song_hash[choice])
        # 进入歌曲播放页面内，有一个index.php文件，play_url属性即是我们所需的url
        response = self.get_reponse(url=url).content.decode('unicode_escape')
        pattern = re.compile('"play_backup_url":"(.*?)"')
        song_info = re.findall(pattern, response)[0]
        # print(song_info)
        audio_name = re.findall('"audio_name":"(.*?)"', response)[0]
        # print(audio_name)
        song_url = song_info.replace('\\/', '/')
        # print(song_url.replace('\/','/'))
        data = self.get_reponse(url=song_url).content
        with open('{}.mp3'.format(audio_name), 'wb') as f:
            f.write(data)
            print('你已经下载:%s' % audio_name)


if __name__ == '__main__':
    name = input('请输入你想下载的歌曲:')
    kugou = KuGou(name)
    song_list = kugou.get_song_list()
    pprint.pprint(song_list)
    choice = int(input('请输入你想下载歌曲的序号:'))
    kugou.save_song(choice)
