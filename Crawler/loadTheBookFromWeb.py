# -*- coding:UTF-8 -*-

'''
Learn from the website https://blog.csdn.net/c406495762/article/details/78123502
'''
import requests

if __name__ == '__main__':
    target = 'https://read.qidian.com/chapter/qHFoqEcgjbPH0qbqCO3QNg2/9qTgTluu6hb4p8iEw--PPw2'
    req = requests.get(url=target)
    print(req.text)
