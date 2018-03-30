# -*- coding: utf-8 -*-
import scrapy
from myspider import items

class CementSpider(scrapy.Spider):
    name = "cement"
    # allowed_domains = ["http://news.qihuiwang.com"]
    start_urls = ['http://news.qihuiwang.com/price/shuini/p{}'.format(i) for i in range(1, 25)]

    def parse(self, response):
        info_lists = response.css(".priceList ul li")

        for info in info_lists:
            link = "http://news.qihuiwang.com" + info.css("a::attr(href)").extract()[0]
            yield scrapy.Request(url=link, callback=self.parse_two)

    def parse_two(self, response):
        item = items.CementItem()
        print('running')
        if len(response.css("table tbody tr")[0].css("td")) == 6:
            num = len(response.css("table tbody tr"))
            for i in range(1, num):
                item['QuotationField'] = response.css("table tbody tr")[i].css("p::text").extract()[0].strip()
                item['PriceType'] = response.css("table tbody tr")[i].css("p::text").extract()[1].strip()
                item['Price'] = response.css("table tbody tr")[i].css("p::text").extract()[2].strip()
                item['Format'] = response.css("table tbody tr")[i].css("p::text").extract()[3].strip()
                item['Place'] = response.css("table tbody tr")[i].css("p::text").extract()[4].strip()
                item['Time'] = response.css("table tbody tr")[i].css("p::text").extract()[5].strip()
                yield item
        else:
            with open('./url.txt', 'a+') as f:
                f.write(response.url)
                f.write('\n')
            print('错误网页')