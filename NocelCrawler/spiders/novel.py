# -*- coding: utf-8 -*-
import scrapy
from NocelCrawler.items import NocelcrawlerItem


class NovelSpider(scrapy.Spider):
    name = 'novel'
    allowed_domains = ['www.118book.com']
    # start_urls = ['https://www.118book.com/book/62/936.html']
    start_urls = ['https://www.118book.com/book/80']

    def parse(self, response):
        for i in range(1704, 1276383):
            next = response.urljoin('{0:03d}.html'.format(i))
            yield scrapy.Request(next, meta={'url': next}, callback=self.parser)

    def parser(self, response):
        # print('1==============12312312===================')

        item = NocelcrawlerItem()
        movies = response.xpath('//*[@id="wrapper"]/div[5]')
        title = movies.xpath('//div/div[2]/h1/text()').extract()

        context = response.xpath('//*[@id="content"]/text()').extract()


        item['title'] = title
        item['context'] = ''.join(context)
        item['url'] = response.meta['url']

        return item


# def parse(self, response):
#     item = NocelcrawlerItem()
#     movies = response.xpath('//*[@id="wrapper"]/div[5]')
#     title = movies.xpath('//div/div[2]/h1/text()').extract()[0]
#
#     context = response.xpath('//*[@id="content"]/text()').extract()
#     item['title'] = title
#     item['context'] = context
#
#     print('23123123123')
#     print(title)
#     print(context)
#     yield item
