from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from jobparser import settings
from jobparser.spiders.hhry import HhruSpider
from jobparser.spiders.superjobru import SuperjobruSpider

if __name__ == '__main__':
    vacansy = 'Python'
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(HhruSpider,vacansy=vacansy)
    process.crawl(SuperjobruSpider, vacansy=vacansy)
    process.start()