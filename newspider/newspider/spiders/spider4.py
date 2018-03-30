# -*- coding: utf-8 -*-
import scrapy
import requests
from newspider.items import spider4Item


class Spider4Spider(scrapy.Spider):
    name = 'spider4'
    # allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/cp01.25.17.00.00.00.html']

    def parse(self, response):
        item = spider4Item()
        info_lists = response.xpath("//ul[@class='bigimg']/li")
        for info in info_lists:
            try:
                item['_id'] = info.xpath("./a/@href").extract()[0]
                item['title'] = info.xpath("./a/@title").extract()
                _discount = info.xpath(".//p[@class='price']/span/text()").extract()[2][2:]
                item['discount'] = list(filter(str.isdigit, _discount))[0]
                item['press'] = info.xpath(".//p[@class='search_book_author']/span[3]/a/@title").extract()[0]
                item['price'] = info.xpath("//span[@class='search_now_price']/text()").extract()[0][1:]
            except Exception:
                pass
            # item['category1'] =
            # item[''] =
            yield item
        for i in range(2, 101):
            next_page = 'http://category.dangdang.com' + '/pg{}-cp01.25.17.00.00.00.html'.format(i)
            yield response.follow(next_page, self.parse)
        pass
