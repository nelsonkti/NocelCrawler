# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NocelcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # title
    # 内容
    context = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()

