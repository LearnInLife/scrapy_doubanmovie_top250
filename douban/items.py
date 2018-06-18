# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # 电影排名
    rank = scrapy.Field()
    # 电影标题
    title = scrapy.Field()
    # 导演主演信息
    actor_info = scrapy.Field()
    # 影片类型 地区 时间信息
    movie_info = scrapy.Field()
    # 评分
    star = scrapy.Field()
    # 简介
    quote = scrapy.Field()
