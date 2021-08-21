import scrapy
from scrapy.http import HtmlResponse
from lerua.items import LeruaItem
from scrapy.loader import ItemLoader


class LeruaSpiderSpider(scrapy.Spider):
    name = 'lerua_spider'
    allowed_domains = ['leroymerlin.ru']

    def __init__(self):
        self.start_urls = ["https://leroymerlin.ru/catalogue/shapki-rukavicy-i-tapochki-dlya-bani/"]

    def parse(self, response: HtmlResponse):
        links = response.xpath('//section/div/div/div[1]/a/@href').extract()

        full_links = []

        for link in links:
            sj_url = 'https://leroymerlin.ru'
            new_link = sj_url + link
            full_links.append(new_link)

        for full_link in full_links:
            yield response.follow(full_link, callback=self.parse_ads)

    def parse_ads(self, response: HtmlResponse):
        loader = ItemLoader(item=LeruaItem(), response=response)

        loader.add_css("name", 'h1[class = "header-2"] ::text')

        loader.add_xpath('photos', '//div[6]/div[1]/div[2]/div/div/div/div/uc-pdp-card-ga-enriched/uc-pdp-media-carousel/img[1]/@src')

        loader.add_css('price',
                      'uc-pdp-price-view[class = "primary-price"] ::text')

        yield loader.load_item()



