# -*- coding:utf-8 -*-
__author__ = 'Ankele'
__date__ = '2020/10/21 0021'

import random
import os
from datetime import datetime

from aip import AipSpeech
from playsound import playsound


class Technology:
    """
    输入权重并根据从所有技术中随机选择一样
    """
    technologies = [
        {'OpenStack': 3},
        {'KVM': 1},
        {'Ceph': 1},
        {'Linux': 1},
        {'Python': 3},
        {'Django': 2},
        {'Vue': 1},
        {'JS': 1},
        {'Algorithm': 1},
    ]

    # Free time research technology
    def ftrt(self):
        self.choose_technology()
        new_list = []
        for dict_item in self.technologies:
            n = list(dict_item.items())[0][0]
            k = list(dict_item.items())[0][1]
            for i in range(k):
                new_list.append(n)
        random.shuffle(new_list)
        print('* ' * 20)
        result = '接下来请研究 ' + random.choice(new_list) + '，主人要好好努力哟，我在家等你回来！'
        print(result)
        print('* ' * 20)
        return result

    def choose_technology(self):
        try:
            for i, t in enumerate(self.technologies):
                name = list(t.keys())[0]
                print('%d: %s' % (i+1, name))
            choose_index = input('请输入您想研究的技术编号：')
            choose = self.technologies[int(choose_index)-1]
            n = list(choose.keys())[0]
            v = list(choose.values())[0]
            choose.update({n: v+5})
        except:
            pass


class Speech:
    """
    调用百度语音合成API，实现文字到语音的转换并播放语音
    """
    APP_ID = "你的APPID"
    API_KEY = '你的AK'
    SECRET_KEY = '你的SK'
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    def speech(self, text, lang='zh', speed=None, volume=5):
        try:
            # ppath = os.getcwd()
            ppath = 'C:\\Users\\Administrator\\Desktop\\python\\mytest1\\video'
            mp3name = 'audio_' + str(datetime.now().timestamp()).split('.')[0] + '.mp3'
            mp3path = os.path.join(ppath, mp3name)
            if type(text) != str or len(text) > 1024:
                print('文字太多了！')
            result = self.client.synthesis(text, lang, 1, {
                'vol': volume,
                'spd': speed,
                'per': 4
            })
            if not isinstance(result, dict):
                print('ok')
                with open(mp3path, 'ab') as f:
                    f.write(result)
                # 播放
                print(1)
                playsound(mp3path)
                print(2)
            else:
                print(result)
        except Exception as e:
            print(e)


def main():
    tech = Technology()
    res = tech.ftrt()
    speech = Speech()
    speech.speech(text=res)


if __name__ == '__main__':
    main()
