# -*- coding: utf-8 -*-
from newspider.items import spider4Item
import pymongo
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class NewspiderPipeline(object):
    def process_item(self, item, spider):
        return item


class DangDangPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient('localhost', 27017)
        self.db = client.mydata
        self.col = self.db.dangdangdata

    def process_item(self, item, spider):
        try:
            self.col.insert_one(dict(item))
        except Exception:
            pass
        return item
