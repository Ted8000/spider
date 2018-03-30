# -*- coding: utf-8 -*-
import pymongo
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MyspiderPipeline(object):
    def process_item(self, item, spider):
        return item


class CementPipeline(object):
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