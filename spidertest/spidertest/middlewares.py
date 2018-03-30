# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random
from scrapy import signals
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
from spidertest.settings import POOL
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
import requests

def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").content


def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))

class SpidertestSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

class proxy(HttpProxyMiddleware):

    def __init__(self, ip=''):
        self.ip = ip

    def process_request(self, request, spider):
        thisip = random.choice(POOL)
        # print("------------ok--------------")
        # print("当前使用IP是：" + thisip["proxy"])
        # print(get_proxy())
        # request.meta["proxy"] = "http://"+thisip["proxy"]
        request.meta["proxy"] = "http://"+str(get_proxy())[2:-1]



class agent(UserAgentMiddleware):
    def __init__(self, user_agent=''):
        self.user_agent = user_agent

    def process_request(self, request, spider):
        ua = random.choice(self.user_agent_list)
        if ua:
            # request.header.setdefault('User-Agent', ua)
            request.headers['user-agent'] = ua
            print(ua, 'agent ok')

    user_agent_list = ["Mozilla/5.0+(Windows+NT+6.2;+WOW64)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/45.0.2454.101+Safari/537.36",
    "Mozilla/5.0+(Windows+NT+5.1)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/28.0.1500.95+Safari/537.36+SE+2.X+MetaSr+1.0",
    "Mozilla/5.0+(Windows+NT+6.1;+WOW64)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/50.0.2657.3+Safari/537.36",
    "Mozilla/5.0+(Windows+NT+6.1;+WOW64)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/51.0.2704.106+Safari/537.36",
    "Mozilla/5.0+(Windows+NT+6.1)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/47.0.2526.108+Safari/537.36+2345Explorer/7.1.0.12633",
    "Mozilla/5.0+(Macintosh;+Intel+Mac+OS+X+10_11_4)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/49.0.2623.110+Safari/537.36",
    "Mozilla/5.0+(Macintosh;+Intel+Mac+OS+X+10_9_5)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/42.0.2311.152+Safari/537.36",
    "Mozilla/5.0+(Windows+NT+6.1;+WOW64)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/42.0.2311.152+Safari/537.36",
    "Mozilla/5.0+(Macintosh;+Intel+Mac+OS+X+10_10_2)+AppleWebKit/600.3.18+(KHTML,+like+Gecko)+Version/8.0.3+Safari/600.3.18",
    "Mozilla/5.0+(Windows+NT+6.1;+WOW64)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/49.0.2623.22+Safari/537.36+SE+2.X+MetaSr+1.0",
    "Mozilla/5.0+(Macintosh;+Intel+Mac+OS+X+10_11_4)+AppleWebKit/601.5.17+(KHTML,+like+Gecko)+Version/9.1+Safari/601.5.17",
    "Mozilla/5.0+(Windows+NT+6.1;+WOW64)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/48.0.2564.103+Safari/537.36",
    "Mozilla/5.0+(Windows+NT+6.1;+WOW64)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/47.0.2526.80+Safari/537.36+Core/1.47.640.400+QQBrowser/9.4.8309.400",
    "Mozilla/5.0+(Macintosh;+Intel+Mac+OS+X+10_10_5)+AppleWebKit/600.8.9+(KHTML,+like+Gecko)+Version/8.0.8+Safari/600.8.9",
    "Mozilla/5.0+(Windows+NT+6.3;+WOW64)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/39.0.2171.99+Safari/537.36+2345Explorer/6.4.0.10356",
    "Mozilla/5.0+(Windows+NT+6.1;+WOW64)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/45.0.2454.87+Safari/537.36+QQBrowser/9.2.5584.400",
    "Mozilla/5.0+(Windows+NT+6.1;+WOW64)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/47.0.2526.111+Safari/537.36",
    "Mozilla/5.0+(Windows+NT+6.1;+WOW64)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/33.0.1750.146+BIDUBrowser/6.x+Safari/537.36",
    "Mozilla/5.0+(Windows+NT+6.1)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/39.0.2171.99+Safari/537.36+2345Explorer/6.5.0.11018",
    "Mozilla/5.0+(Windows+NT+6.2;+WOW64)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/42.0.2311.154+Safari/537.36+LBBROWSER"]


