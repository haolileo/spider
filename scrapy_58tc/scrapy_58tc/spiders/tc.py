import scrapy


class TcSpider(scrapy.Spider):
    name = 'tc'
    allowed_domains = ['tongcheng.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91&classpolicy=classify_D']
    start_urls = ['https://tongcheng.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91&classpolicy=classify_D']
    def parse(self, response):
        # 字符串
        # content = response.text
        # 二进制数据
        # content = response.body
        #
        content = response.xpath('/html/head/title/text()')
        print('========================================')
        print(content)