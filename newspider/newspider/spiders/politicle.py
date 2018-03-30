# -*- coding: utf-8 -*-
import scrapy
from newspider.items import PoliticleItem


class PoliticleSpider(scrapy.Spider):
    name = 'politicle'
    allowed_domains = ['http://nasional.harianterbit.com']
    start_urls = ['http://nasional.harianterbit.com/index_kanal/41']

    def parse(self, response):
        info_lists = response.xpath("//div[@id='colorcontentwrap4']")
        for info in info_lists:
            self.title = info.xpath("//div[@id='colorcontentwrap4']/h2/a/text()").extract()[0]
            self.link = info.xpath("//div[@id='colorcontentwrap4']/h2/a/@href").extract()[0]
            self.time = info.xpath("//div[@id='colorcontentwrap4']/div/div[@id='meta_authorl']/text()").extract()[0]\
                .split(',')[1].strip()
            yield scrapy.Request(url = self.link, callback = self.prase_detail, meta = {'ID1': self.title, 'ID2': self.link,
                                                                                        'ID3': self.time})


    def prase_detail(self, response):
        item = PoliticleItem()
        item['title'] = response.meta['ID1']
        item['link'] = response.meta['ID2']
        item['time'] = response.meta['ID3']
        i = 1
        text = 1
        while text:
            text = response.xpath("//div[@class='post']/div")[i].xpath('string(.)').extract()[0].strip()
            i = i + 2
            item['text_content'] = item['text_content'] + text
        yield item
