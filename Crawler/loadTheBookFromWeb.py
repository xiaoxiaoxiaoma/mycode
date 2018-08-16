# -*- coding:UTF-8 -*-
'''
Learn from the website https://blog.csdn.net/c406495762/article/details/78123502
'''
import requests,sys
from bs4 import BeautifulSoup

class downloader(object):

    def __init__(self):
        self.server = 'https://www.qu.la/'               #笔趣网的url
        self.target = 'https://www.qu.la/book/45730/'   #该小说在笔趣网的url
        self.names = []     #用于存放章节名
        self.urls = []      #用于存放每个章节的url
        self.nums = 0       #用于存放总的章节数量

    #在该小说目录下获取所有章节的url，同时还要把前12个url去掉，还有把url的前缀都补全
    def get_download_url(self):
        re = requests.get(url = self.target)
        html = re.text
        div_bf = BeautifulSoup(html,'html.parser')
        div = div_bf.find_all('div',id = 'list')
        a_bf = BeautifulSoup(str(div),'html.parser')
        a = a_bf.find_all('a')
        self.nums = len(a[12:])
        for each in a[12:]:
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))

    #获取该url所显示的章节的内容，并对内容进行文本转化（将HTML的标签去掉）
    def get_contents(self,target):
        re = requests.get(url = target)
        html = re.text
        bf = BeautifulSoup(html,'html.parser')
        texts = bf.find_all('div', id = 'content')
        texts = texts[0].text.replace('\xa0'*4,'\n\n')
        return texts

    #将所有获取到的章节内容追加到选定的文件中
    def writer(self,name,path,text):
        write_flag = True
        with open(path,'a') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')

if __name__ == '__main__':
    dl = downloader()
    dl.get_download_url()
    print('《厉害了我的原始人》开始下载')

    #为了下载速度快一点，不重复进行打开和关闭文件操作
    with open('F:\\厉害了我的原始人.txt', 'a',encoding='UTF-8') as f:
        for i in range(dl.nums):
            f.write(dl.names[i] + '\n')
            f.writelines(dl.get_contents(dl.urls[i]))
            f.write('\n\n')
            f.flush()
            print("已下载：%.3f%%" % float(i / dl.nums) + '\r')

    # for i in range(dl.nums):
    #     dl.writer(dl.names[i],'F:\\厉害了我的原始人.txt',dl.get_contents(dl.urls[i]))
    #     sys.stdout.write("已下载：%.3f%%" % float(i/dl.nums)+'\r')
    #     sys.stdout.flush()

    print("《厉害了我的原始人》下载完成")