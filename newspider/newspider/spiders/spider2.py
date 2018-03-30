# -*- coding: utf-8 -*-
import scrapy
from newspider import items

class SpiderSpider(scrapy.Spider):
    name = 'spider2'
    allowed_domains = ['goodreads.com']
    start_urls = ['http://goodreads.com/quotes']

    def parse(self, response):
        item = items.NewspiderItem()
        for quote in response.css('div.quote'):
            a = response.xpath('//div[@class="greyText smallText left"]')
            item['author'] = quote.css('.authorOrTitle::text').extract()[0].strip()
            item['text'] = quote.css('.quoteText::text').extract()[0].strip()
            item['tag'] = a.xpath('string(.)').extract()[0].replace('\n', '').replace('\r', '').replace(' ', '')
            yield item

        next_page = response.xpath('//a[@rel="next"]/@href').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)