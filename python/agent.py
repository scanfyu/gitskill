# -*- coding: utf-8 -*-

from scrapy import signals
import urllib.request
import urllib.parse
import socket

class QqvideoSpiderMiddleware(object):
    User_Agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13'
    header = {}
    header['User_Agent'] = User_Agent
    user_agent_ip = []
    socket.setdefaulttimeout(5)
    url = 'http://ip.chinaz.com/getip.aspx'
    user_agent_ip_list = []
    for eveDaili in open('daili.txt'):
        eveDaili = str(eveDaili).replace(u'\n', '')
        user_agent_ip_list.append(eveDaili)
