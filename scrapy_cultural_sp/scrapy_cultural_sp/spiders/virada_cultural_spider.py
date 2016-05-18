from scrapy.selector import Selector
from scrapy.http import Request
from scrapy_cultural_sp.items import Atracao
from scrapy.contrib.spiders import CrawlSpider


class ViradaCulturalSpider(CrawlSpider):
    name = "virada_cultural"
    start_urls = ["http://www.viradaculturalpaulista.sp.gov.br/cidades"]

    def parse(self, response):
        body_sel = Selector(response)
        urls_cidade = body_sel.xpath("//div[@class='list-cities']//ul//li//a/@href").extract()

        for url in urls_cidade:
            yield Request(url, self.parse_atracao)
