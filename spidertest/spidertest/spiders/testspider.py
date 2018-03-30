# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver

class TedspiderSpider(scrapy.Spider):
    name = 'tedspider'
    # allowed_domains = ['baidu.com']
    start_urls = ['https://jiage.cngold.org/jinshuwu/list_3633_all.html']

    def parse(self, response):
        # print('run 1')
        a = len(response.css('.history_news_content ul li a'))
        for i in range(380, a):
            item = response.css('.history_news_content ul li a')[i]
            yield scrapy.Request(url=item.css('a::attr(href)').extract()[0], callback=self.parse_two, meta = {'time':item.css('a::text').extract()[0]})
        # yield scrapy.Request(url = response.css('.history_news_content ul li a::attr(href)').extract()[0], callback = self.parse_two, meta = {'time':})
    def parse_two(self, response):
        print('run 2')
        yield scrapy.Request(url=response.css('.left_info ul li a::attr(href)').extract()[0],
                             callback=self.parse_three, meta = {'time':response.meta['time']})
    def parse_three(self, response):
        print('running')
        # items = response.xpath('//*[@id="zoom"]/table/*')
        # for i in range(3, len(items)):
        #     yield {
        #         'name':items[i].xpath('./td/text()')[0].extract().lstrip().rstrip(),
        #         'price':items[i].xpath('./td/text()')[1].extract().lstrip().rstrip(),
        #         'yuan/kg':items[i].xpath('./td/text()')[2].extract().lstrip().rstrip(),
        #         'wave':items[i].xpath('./td/text()')[3].extract().lstrip().rstrip(),
        #         'time':response.meta['time'],
        #     }
        yield {
            'name':response.xpath('//*[@id="zoom"]/table/tr/td/text()')[0].extract().lstrip().rstrip(),
            'price':response.xpath('//*[@id="zoom"]/table/tr/td/text()')[1].extract().lstrip().rstrip(),
            'wave':response.xpath('//*[@id="zoom"]/table/tr/td/text()')[3].extract().lstrip().rstrip(),
            'time':response.xpath('//*[@id="zoom"]/table/tr/td/text()')[4].extract().lstrip().rstrip()[:10]
        }



