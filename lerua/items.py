import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Compose


def price_func(price_x):
    price_x = price_x[5] + price_x[7] + '/' + price_x[9]
    return price_x


class LeruaItem(scrapy.Item):
    _id = scrapy.Field()
    name = scrapy.Field(input_processor=MapCompose(lambda x: str(x)),
                        output_processor=TakeFirst())

    photos = scrapy.Field()

    price = scrapy.Field(output_processor=Compose(price_func))
    pass
