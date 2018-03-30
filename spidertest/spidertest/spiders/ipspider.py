# -*- coding: utf-8 -*-
import scrapy


class IpspiderSpider(scrapy.Spider):
    name = 'ipspider'
    allowed_domains = ['kuaidaili.com']
    start_urls = ['http://www.kuaidaili.com/free/inha/{}'.format(i) for i in range(1, 1991)]

    def parse(self, response):
        for x in response.xpath("//tbody/tr"):
            yield {
                'IP':x.xpath("td/text()")[0].extract(),
                'port':x.xpath("td/text()")[1].extract(),
                'Anonymity':x.xpath("td/text()")[2].extract(),
                'Type':x.xpath("td/text()")[3].extract(),
                'Local':x.xpath("td/text()")[4].extract(),
                'Speed':x.xpath("td/text()")[5].extract(),
                'Last test time':x.xpath("td/text()")[6].extract(),
            }

