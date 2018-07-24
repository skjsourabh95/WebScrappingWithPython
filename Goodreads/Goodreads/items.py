# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GoodreadsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    bookName=scrapy.Field()
    author=scrapy.Field()
    rating=scrapy.Field()
    noOfReviews=scrapy.Field()
    votes=scrapy.Field()
    description=scrapy.Field()
    publisher=scrapy.Field()
    bookFormat=scrapy.Field()
    noOfPages=scrapy.Field()
    isbn=scrapy.Field()
    awards=scrapy.Field()
    
