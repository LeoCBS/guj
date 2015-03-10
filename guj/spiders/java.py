# -*- coding: utf-8 -*-
import scrapy
from guj.items import GujItem
#from scrapy.contrib.spiders import CrawlSpider, Rule
#from scrapy.contrib.linkextractors import LinkExtractor

class JavaSpider(scrapy.Spider):
    name = "java"
    allowed_domains = ["guj.com.br"]
    start_urls = ['http://www.guj.com.br/?p=%s' % page for page in xrange(0,5)]
    #rules = (Rule(LinkExtractor(allow=('/?p=', )), callback='parse_item'),)
	


    def parse(self, response):
    	self.log('url: %s' % response.url)
        for a in response.xpath('/html/body/div/section/ol/li/div/div/h3/a/text()'):
        	item = GujItem()
        	item['title'] = a.extract()
        	yield item
