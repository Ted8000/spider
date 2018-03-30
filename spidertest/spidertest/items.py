# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpidertestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    image_urls = scrapy.Field()  # 就编写个图片路径就好
    pass

class DoubanItem(scrapy.Item):
    book_name = scrapy.Field()
    author = scrapy.Field()
    # class_ = scrapy.Field()
    # press = scrapy.Field()
    grade = scrapy.Field()
    count = scrapy.Field()
    introduction = scrapy.Field()

class XituItem(scrapy.Item):
    Name = scrapy.Field()
    Format = scrapy.Field()
    Location = scrapy.Field()
    Price = scrapy.Field()
    MeanPrice = scrapy.Field()
    wave= scrapy.Field()
    Unit_price = scrapy.Field()
    Time = scrapy.Field()
