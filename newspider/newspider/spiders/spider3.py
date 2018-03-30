# -*- coding: utf-8 -*-
import scrapy
import urllib.request
from newspider import settings
import json

class Spider3Spider(scrapy.Spider):
    name = 'spider3'
    # allowed_domains = ['baidu.com']
    start_urls = [
        'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E7%BE%8E%E5%A5%B3&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%E7%BE%8E%E5%A5%B3&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&cg=girl&pn=30'
    ]

    def parse(self, response):
        imgs = json.loads(response.body)['data']
        for img in imgs:
            url = img['middleURL']
        # for i in response.selector.re('https://.*0\.jpg'):
            urllib.request.urlretrieve('url', 'C:/Users/U/Desktop/ted/tu'+ str(settings.m))
            settings.m += 1
        pass
