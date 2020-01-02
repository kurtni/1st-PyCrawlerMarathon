# -*- coding: utf-8 -*-
import scrapy


class PptcrawlerSpider(scrapy.Spider):
    name = 'PPTCrawler'
    allowed_domains = ['www.ptt.cc/bbs/Stock/M.1577939296.A.511.html']
    start_urls = ['http://www.ptt.cc/bbs/Stock/M.1577939296.A.511.html/']

    def parse(self, response):
        pass
