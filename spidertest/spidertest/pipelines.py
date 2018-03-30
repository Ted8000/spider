# -*- coding: utf-8 -*-
import pymongo
from spidertest import settings

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SpidertestPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient('localhost', 27017)
        self.db = client.mydata
        self.col = self.db.collection1

    def process_item(self, item, spider):
        # print(item['image_urls'])
        self.col.insert_one(dict(item))
        return item

class XituItem(object):
    def __init__(self):
        client = pymongo.MongoClient('localhost', 27017)
        self.db = client.teddata
        self.col = self.db.cement

    def process_item(self, item, spider):
        try:
            self.col.insert_one(dict(item))
        except Exception:
            pass
            print('未爬下~')
        return item

