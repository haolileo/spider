import scrapy

from ..items  import ScrapyMovieItem


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['www.ygdy8.net']
    start_urls = ['https://www.ygdy8.net/html/gndy/oumei/index.html']

    def parse(self, response):
        print('===============================')
        div_list = response.xpath('//div[@class="co_content8"]//td[2]//a[2]')

        for div in div_list:
            # 获取第一页的图片和要点击的链接
            name = div.xpath('./text()').extract_first()
            src = div.xpath('./@href').extract_first()
            # 第二页的url
            url = 'https://www.ygdy8.net'+ src
            print(name,url)
            # 对第二页的链接进行访问
            yield scrapy.Request(url=url,callback=self.parse_second,meta={'name':name})
    def parse_second(self, response):
        # 注意如果拿不到数据的情况下一般先检查xpath的语法是否正确，有些标签可能会识别不出来
        src = response.xpath('//*[@id="Zoom"]//img/@src').extract_first()
        # 接收到请求的meta参数值
        name = response.meta['name']
        movie = ScrapyMovieItem(src=src,name=name)
        yield movie