
import json

import scrapy
from parsel import Selector
from scrapy_splash import SplashRequest


class OlxCollector(scrapy.Spider):
    name = "olx"

    start_urls = [f"http://localhost:8050/render.html?url=https://www.olx.com.br/estado-sp/sao-paulo-e-regiao?q=forno&o={i}&timeout=10&wait=0.5" for i in range(11) if i]
    # start_urls = [f"https://www.olx.com.br/estado-sp/sao-paulo-e-regiao?q=forno&o={i}" for i in range(11) if i]
     
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 0.5})

    def parse(self, response):
        response = Selector(text=response.text)
        data = response.xpath("//script[@id='__NEXT_DATA__']/text()").get()
        # print(data)
        html = json.loads(data)
        houses = html.get('props').get('pageProps').get('ads')
        
        return houses
                
        
        
        # print(data)
        # yield {data}

        # for next_page in response.css('a.next'):
        #     yield response.follow(next_page, self.parse)