# -*- coding: utf-8 -*-
import scrapy
from spiderdemo.items import SpiderdemoItem

class DoubanspiderSpider(scrapy.Spider):
    name = 'doubanSpider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/top250']

    def parse(self, response):
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")
        for i_item in movie_list:
            douban_item = SpiderdemoItem()
            douban_item['serial_number'] = i_item.xpath(".//div[@class='item']//em/text()").extract_first()
            douban_item['movie_name'] = i_item.xpath(
                ".//div[@class='info']/div[@class='hd']/a/span[1]/text()").extract_first()
            descs = i_item.xpath(".//div[@class='info']//div[@class='hd']/p[1]/text()").extract()
            for i_desc in descs:
                i_desc_str = "".join(i_desc.split())
                douban_item['introduce'] = i_desc_str

            douban_item['star'] = i_item.xpath(".//span[@class='rating_num']/text()").extract_first()
            douban_item['evaluate'] = i_item.xpath(".//div[@class='star']//span[4]/text()").extract_first()
            douban_item['describle'] = i_item.xpath(".//p[@class='quote']/span/text()").extract_first()
            yield douban_item
            # 解析下一页
            next_link = response.xpath("//span[@class='next']/link/@href").extract()
            if next_link:
                next_link = next_link[0]
                yield scrapy.Request("https://movie.douban.com/top250" + next_link, callback=self.parse)
