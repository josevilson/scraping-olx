# %%

from scrapy.crawler import CrawlerProcess

from olx.olx.spiders.olx_data import OlxCollector


# %%
def main():
    process = CrawlerProcess()
    process.crawl(OlxCollector)
    process.start()
    print("fim")
    print("fim")

if __name__ == '__main__':
    main()