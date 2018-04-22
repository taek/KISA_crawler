# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MycrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    code_number = scrapy.Field()



# import scrapy
# from scrapy.loader.processors import Compose, TakeFirst

# def filter_utf(value):
#     if isinstance(value, unicode):
#         return value.encode('utf-8')


# class MycrawlerItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     name = scrapy.Field(output_processor=Compose(TakeFirst(), filter_utf))
#     code_number = scrapy.Field(output_processor=Compose(TakeFirst(), filter_utf))
