import scrapy
from Goodreads.items import GoodreadsItem
from datetime import datetime
import re

class GoodRead(scrapy.Spider):
    name='book_spider'
    start_urls=["https://www.goodreads.com/list/show/88.Best_Fantasy_Books_of_the_21st_Century"]
    npages=2
    for i in range(2,npages+2):
        start_urls.append("https://www.goodreads.com/list/show/88.Best_Fantasy_Books_of_the_21st_Century?page="+str(i)+"")
    def parse(self,response):
        for href in response.xpath("//a[contains(@class,'bookTitle')]//@href"):
            url="https://www.goodreads.com"+href.extract()
            yield scrapy.Request(url,callback=self.parse_dir_contents)
    def parse_dir_contents(self,response):
        item=GoodreadsItem()
        item['bookName']=response.xpath("//h1[contains(@id,'bookTitle')]/text()").extract()[0].strip()
        item['author']= response.xpath("//a[contains(@class,'authorName')]/span[contains(@itemprop,'name')]/text()").extract()[0].strip()
        item['rating']=response.xpath("//span[contains(@class,'value rating')]/span[contains(@class,'average')]/text()").extract()[0].strip()
        item['noOfReviews']=response.xpath("//a[contains(@class,'gr-hyperlink')]/span[contains(@class,'count value-title')]/text()").extract()[0].strip()
        item['votes']=response.xpath("//a[contains(@class,'gr-hyperlink')]/span[contains(@class,'votes value-title')]/text()").extract()[0].strip()
        item['description']= "".join(response.xpath("//div[contains(@id,'description')]/span[contains(@id,'freeText')]/text()").extract())
        item['publisher']="".join(response.xpath("//div[contains(@id,'details')]/div[contains(@class,'row')]/text()").extract()).strip().replace(',',"")
        item['bookFormat']=response.xpath("//div[contains(@class,'row')]/span[contains(@itemprop,'bookFormat')]/text()").extract()[0]
        item['noOfPages']= response.xpath("//div[contains(@class,'row')]/span[contains(@itemprop,'numberOfPages')]/text()").extract()[0]
        item['isbn']=response.xpath("//div[contains(@class,'clearFloats')]/div[contains(@class,'infoBoxRowItem')]/text()").extract()[1].strip()
        item['awards']=response.xpath("//div[contains(@class,'infoBoxRowItem')]/a[contains(@class,'award')]/text()").extract()
        yield item