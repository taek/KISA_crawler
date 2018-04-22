import logging   # for logging
from logging.handlers import TimedRotatingFileHandler   # for logging

import scrapy

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

# setting the foramt for file handler
parse_fh.setFormatter(formatter)

# setting the level for each handler
parse_fh.setLevel(logging.DEBUG)

# adding the handlers
crawler_logger.addHandler(parse_fh)


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
        crawler_logger.info("The url of the target is: {}".format(page))