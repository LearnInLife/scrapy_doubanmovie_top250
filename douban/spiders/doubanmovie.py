# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem


class DoubanmovieSpider(scrapy.Spider):
    name = 'doubanmovie'
    allowed_domains = ['movie.douban.com']
    url = 'https://movie.douban.com/top250?start='
    offset = 0

    start_urls = [
        url + str(offset)
    ]

    def parse(self, response):
        item = DoubanItem()

        # movies = response.xpath("//div[@class='info']")
        movies = response.xpath("//div[@class='item']")
        for each in movies:
            # 排名
            item['rank'] = each.xpath("./div[@class='pic']/em/text()").extract()[0]
            info = each.xpath("./div[@class='info']")
            # 标题
            item['title'] = info.xpath(".//span[@class='title'][1]/text()").extract()[0]
            # 基本信息
            item['actor_info'] = info.xpath("./div[@class='bd']/p/text()").extract()[0].replace('\n', '').replace(' ',
                                                                                                                  '')
            item['movie_info'] = info.xpath("./div[@class='bd']/p/text()").extract()[1].replace('\n', '').replace(' ',
                                                                                                                  '')
            # 评分
            item['star'] = \
                info.xpath("./div[@class='bd']/div[@class='star']/span[@class='rating_num']/text()").extract()[0]
            # 简介
            quote = info.xpath("./div[@class='bd']/p[@class='quote']/span/text()").extract()
            if len(quote) != 0:
                item['quote'] = quote[0]
            else:
                item['quote'] = ''

            yield item

        if self.offset < 225:
            self.offset += 25
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
