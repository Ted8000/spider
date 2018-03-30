# -*- coding: utf-8 -*-
import scrapy
import json
import urllib.request
from spidertest import items
import requests
from spidertest import settings


class MyspiderSpider(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['baidu.com']
    start_urls = [
        "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=小清新&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&word=小清新&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&fr=&pn=%d" % i
        for i in range(0, 61, 30)]#

    def parse(self, response):
        item = items.SpidertestItem()
        imgs = json.loads(response.body)['data']
        # response.body

        for img in imgs:
            try:
                item['image_urls'] = img['middleURL']
            except BaseException:
                print("爬虫失败！")
            url = img['middleURL']
            settings.m += 1
            requests.get
            urllib.request.urlretrieve(url, 'C:/Users/U/Desktop/ted/tu3/' + str(settings.m) + '.jpg')
            yield item
