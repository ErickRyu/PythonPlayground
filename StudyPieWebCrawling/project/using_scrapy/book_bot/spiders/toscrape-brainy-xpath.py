# -*- coding: utf-8 -*-
import scrapy


class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'toscrape-brainy-xpath'
    start_urls = [
        'https://www.brainyquote.com/authors/oscar_wilde/',
    ]

    def parse(self, response):
        for quote in response.xpath('//div[@class="m-brick grid-item boxy bqQt"]'):
            yield {
                'text': quote.xpath('.//div/div[1]/div/a/text()').extract_first(),
                'author': quote.xpath('.//div/div[1]/div/div/a/text()').extract_first(),
                'tags': quote.xpath('.//div/div[1]/div/div/div/div/a[@class="qkw-btn btn btn-xs oncl_list_kc"]/text()').extract()
            }

#/html/body/div/div[2]/div[1]/div[1]/div/a[1]
