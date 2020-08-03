import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import ParsJobItem

class HhruSpider(scrapy.Spider):
    name = 'hhru'
    allowed_domains = ['hh.ru']

    def __init__(self,vacansy):
        self.start_urls = [f'https://lipetsk.hh.ru/search/vacancy?area=&st=searchVacancy&fromSearch=true&text={vacansy}']

    def parse(self, response: HtmlResponse):
        next_page = response.css('a.HH-Pager-Controls-Next::attr(href)').extract_first()
        job_links = response.xpath('//a[@class="bloko-link HH-LinkModifier"]/@href').extract()
        for link in job_links:
            yield  response.follow(link,callback=self.vacansy_pars)
        yield response.follow(next_page, callback=self.parse)

    def vacansy_pars(self,response:HtmlResponse):
        name = response.xpath('//h1/text()').extract_first()
        salary = response.xpath("//p[@class='vacancy-salary']/span/text()").extract()
        link = response.url
        employer = response.xpath("//a[@data-qa='vacancy-company-name']/span/text()").extract_first()
        source = self.allowed_domains[0]
        yield ParsJobItem(name=name,salary=salary,link=link,employer=employer,source=source)