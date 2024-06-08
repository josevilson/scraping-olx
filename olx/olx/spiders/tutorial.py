from pathlib import Path

import scrapy


class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://www.zyte.com/blog/']

    def parse(self, response):
        for title in response.css('.free-text.z-text-blog-title'):
            yield {'title aaaaaaa': title.css('div::text').get()}

        for next_page in response.css('a.next'):
            yield response.follow(next_page, self.parse)