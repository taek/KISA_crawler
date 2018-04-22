# -*- coding: utf-8 -*-

import logging   # for logging
from logging.handlers import TimedRotatingFileHandler   # for logging

import scrapy
from scrapy.loader import ItemLoader   # for item loader

from mycrawler.items import MycrawlerItem   # to load items for iteam loader

# log file setting
REGULAR_LOG_FILE = "StockCrawler-log.log"   # all logs will be saved to this file
crawler_logger = logging.getLogger()
formatter = logging.Formatter('%(asctime)s %(levelname)-8s: [%(name)-12s] %(message)s')
# crawler_logger.setLevel(logging.DEBUG)

parse_fh = TimedRotatingFileHandler(
                                    # handler for all logs, and rotated at midnight and keep upto backup logs of the past 7 days
                                    REGULAR_LOG_FILE,
                                    when='midnight',
                                    interval=1,
                                    backupCount=7
                                )

parse_fh.setFormatter(formatter)   # setting the format for file handler
parse_fh.setLevel(logging.DEBUG)   # setting the level for each handler
crawler_logger.addHandler(parse_fh)   # adding the handlers


class StockCrawler(scrapy.Spider):
    name = "stock"

    def start_requests(self):
        urls = [
            'http://vip.mk.co.kr/price/005930',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        page = response.url
        crawler_logger.info("The url of the target is: {}".format(page))   # logging example

        item_loader = ItemLoader(item=MycrawlerItem(), response=response)
        item_loader.add_xpath('name', '//font[@class="f1"]/text()')   #  response.xpath('//font[@class="f1"]/text()').extract_first().encode('utf-8')
        item_loader.add_xpath('code_number', '//font[@class="f2"]/text()')

        return item_loader.load_item()