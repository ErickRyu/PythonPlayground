# -*- coding: utf-8 -*-
import scrapy


class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-brainy-css"
    start_urls = [
        'https://www.brainyquote.com/authors/oscar_wilde/',
    ]

    def parse(self, response):
        for quote in response.css("div.qpos_1_1"):
            yield {
                #'text': quote.css("span.text::text").extract_first(),
                #'author': quote.css("small.author::text").extract_first(),
                #'tags': quote.css("div.tags > a.tag::text").extract()
                'text': quote.css("div.div[1].div.a::text").extract()
            }

        #next_page_url = response.css("li.next > a::attr(href)").extract_first()
        #if next_page_url is not None:
        #    yield scrapy.Request(response.urljoin(next_page_url))

