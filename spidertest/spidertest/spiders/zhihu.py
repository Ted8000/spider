# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver

class zhihuspider(scrapy.Spider):
    name = 'zhihu'
    start_urls = ('https://www.baidu.com/',)


    def get_cookies(self):
        driver = webdriver.Chrome()
        driver.get(self.start_urls[0])
        driver.find_element("dlemail").click()
        driver.find_element_by_class_name("dlemail").send_keys("17628292357")
        driver.find_element_by_class_name("dlpwd").click()
        driver.find_element_by_class_name("dlpwd").send_keys("a353442710")
        SignInURL = "http://mail.163.com/"
        try:
            if driver.find_element_by_id('captcha'):
                while True:
                    if not SignInURL == driver.current_url:
                        break
                    pass
                pass
        finally:
            if SignInURL == driver.current_url:
                driver.find_element_by_css_selector("button.sign-button.submit").click()
            cookies = driver.get_cookies()
            driver.close()
            print(cookies)
            return cookies

    def parse(self, response):
        return scrapy.Request(url = self.start_urls[0], callback = self.parse_two, meta = {'key':'ted~'})

    def parse_two(self, response):
        yield scrapy.Request(url = self.start_urls[0], callback = self.parse_three, dont_filter = True)

    def parse_three(self, response):
        print('running 3')
        print(response.meta['key'])



