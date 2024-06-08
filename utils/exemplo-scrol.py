# my_spider.py
import scrapy
from scrapy_splash import SplashRequest


class ScrollSpider(scrapy.Spider):
    name = 'scroll_spider'
    start_urls = ['http://example.com']  # Substitua pela URL desejada

    lua_script = """
    function main(splash, args)
        splash:set_viewport_size(1024, 768)
        splash:go(args.url)
        splash:wait(2)
        
        local scroll_to = splash:jsfunc("window.scrollTo")
        scroll_to(0, 10000)  -- Scroll down
        splash:wait(2)
        
        return {
            html = splash:html(),
            png = splash:png(),
            har = splash:har(),
        }
    end
    """

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, endpoint='execute', args={'lua_source': self.lua_script})

    def parse(self, response):
        # Extraia os dados desejados aqui
        self.log('Carregando página com scroll')
        self.log(response.body)
