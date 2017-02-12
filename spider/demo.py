# -*- coding: utf-8 -*-
import requests

HEADERS = {
    'Cookie':'',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
if __name__ == '__main__':
    s = requests.session()
    # 添加浏览器头
    # 获取话题的url，注意 offset已经改为了0，表示从0开始后面的80条
    url = 'https://www.zhihu.com/followed_topics?offset=0&limit=80'
    z = s.get(url,headers=HEADERS)
    #获取所有话题
    topic = z.json()['payload']
    #打印出关注了多少条话题
    print len(topic)
    #这边返回36，与我实际的一样，所以话题是应该抓取成功了