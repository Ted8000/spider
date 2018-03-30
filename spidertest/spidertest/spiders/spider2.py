# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader.processors import MapCompose
from spidertest import items

ted = set()
class Spider2Spider(scrapy.Spider):
    name = 'spider2'
    # allowed_domains = ['douban.com']
    start_urls = ['http://nm.sci99.com/news/list.aspx?id=21&page={}'.format(i) for i in range(1, 53)]

    def parse(self, response):
        info_list = response.css('#NewsList li span a')

        for info in info_list:
            if '上海' in info.css('a::text')[0].extract().strip():
                if info.css('a::text')[0].extract().strip() not in ted:
                    ted.add(info.css('a::text')[0].extract().strip())
                    print('find one')
                    yield scrapy.Request(url='http://nm.sci99.com' + info.css('a::attr(href)')[0].extract().strip(),
                                         callback=self.parse_two, meta = {'Time':info.css('a::text')[0].extract().strip()[15:-1]})
                else:
                    print('去重')
            else:
                print('不是稀土')
        pass

    def parse_two(self, response):
        info_list = response.css('#zoom tr')
        print('running')
        num = len(info_list)
        item = items.XituItem()
        for i in range(1, num):
            item['Name'] = info_list[i].xpath('./td')[0].xpath('string(.)').extract()[0].strip()
            item['Format'] = info_list[i].xpath('./td')[1].xpath('string(.)').extract()[0].strip()
            item['Location'] = info_list[i].xpath('./td')[2].xpath('string(.)').extract()[0].strip()
            item['Price'] = info_list[i].xpath('./td')[3].xpath('string(.)').extract()[0].strip()
            item['MeanPrice'] = info_list[i].xpath('./td')[4].xpath('string(.)').extract()[0].strip()
            item['wave'] = info_list[i].xpath('./td')[5].xpath('string(.)').extract()[0].strip()
            item['Unit_price'] = info_list[i].xpath('./td')[6].xpath('string(.)').extract()[0].strip()
            item['Time'] = response.meta['Time']
            yield item



