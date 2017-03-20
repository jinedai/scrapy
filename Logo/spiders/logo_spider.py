#!/usr/bin/env python
# -*- coding:utf-8 -*-

from scrapy.contrib.spiders import CrawlSpider, Rule 
from scrapy.selector import Selector
from Logo.items import LogoItem
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spider import Spider


class LogoSpider(CrawlSpider) : #CrawlSpider用来遍布抓取，通过rules来查找所有符合的URL来爬去信息

    name = "Logo" #名字唯一，启动爬虫是用到 scrapy crawl logo -o items.json
    allowed_domains = ["pcauto.com.cn"]
    start_urls = ["http://www.pcauto.com.cn/zt/chebiao/faguo/"]
    rules = (
        Rule(SgmlLinkExtractor(allow = (r'http://www.pcauto.com.cn/zt/chebiao/.*?/$')), follow = True, callback = 'parse_page'),
        #将读取的网页进行分析
        # Rule(SgmlLinkExtractor(allow = ('http://www\.pcauto.com\.cn/zt/chebiao/.*?/')), callback = 'parse_page')
        )

    def parse_page(self, response) :
        sel = Selector(response)
        item = LogoItem()
        item['country'] = ''.join(sel.xpath('//div[@class="th"]/span[@class="mark"]/a/text()').extract())
        item['carname'] = sel.xpath('//div[@class="dTxt"]/i[@class="iTit"]/a/text()').extract()
        item['imageurl'] = sel.xpath('//div[@class="dPic"]/i[@class="iPic"]/a/img/@src').extract()
        return item
