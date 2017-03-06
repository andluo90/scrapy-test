#-*-coding:utf-8-*-
import scrapy
class deomSpider(scrapy.Spider):

    name = 'demo'
    start_urls = ['http://fund.eastmoney.com/513500.html?spm=search']

    def parse(self, response):
        print(response)