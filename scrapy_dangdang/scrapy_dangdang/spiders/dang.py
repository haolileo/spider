import scrapy
from ..items import ScrapyDangdangItem

class DangSpider(scrapy.Spider):
    name = 'dang'
    allowed_domains = ['search.dangdang.com']
    start_urls = ['http://search.dangdang.com/?key=%B4%F3%CA%FD%BE%DD&act=input']

    base_url = 'http://search.dangdang.com/?key=%B4%F3%CA%FD%BE%DD&act=input&page_index='
    page = 1

    def parse(self, response):
        print('==========================================')
        # src = response.xpath('//ul[@class="bigimg"]/li/a/img/@src')
        # name = response.xpath('//ul[@class="bigimg"]/li/a/img/@alt')
        # price = response.xpath('//ul[@class="bigimg"]/li/p[3]/span[1]/text()')
        li_list = response.xpath('//ul[@class="bigimg"]/li')
        for li in li_list:
            # 第一张图片使用的是src标签，其他的图片使用的是data-original标签
            src = li.xpath('.//a/img/@data-original').extract_first()# 懒加载选择这个标签
            if src: # 如果src不为空则继续使用src
                src = src
            else:   # 如果src为空则使用这个xpath路径
                src = li.xpath('.//a/img/@src').extract_first()
            name = li.xpath('.//a/img/@alt').extract_first()
            price = li.xpath('.//p[3]/span[1]/text()').extract_first()
            book = ScrapyDangdangItem(src=src,name=name,price=price)
            # 获取一个book信息就将其交给管道pipelines
            yield book

        if self.page < 100:
            self.page+=1
            url = self.base_url + str(self.page)
            # 调用parse方法
            # 这个就是scrapy的get请求,其中callback是需要执行的函数
            yield scrapy.Request(url=url,callback=self.parse)