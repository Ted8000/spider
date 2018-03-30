# -*- coding: utf-8 -*-
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    author = scrapy.Field()
    text = scrapy.Field()
    tag = scrapy.Field()

class spider3Item(scrapy.Item):
    imgname = scrapy.Field()
    imgurl = scrapy.Field()
    img = scrapy.Field()

class spider4Item(scrapy.Item):
    _id = scrapy.Field()
    title = scrapy.Field()
    press = scrapy.Field()
    price = scrapy.Field()
    discount = scrapy.Field()
    # category1 = scrapy.Field()
    # category2 = scrapy.Field()


class PoliticleItem(scrapy.Item):
    title = scrapy.Field()
    text_content = scrapy.Field()
    time = scrapy.Field()
    link = scrapy.Field()
