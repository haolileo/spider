import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫的名字 用于爬虫的时候使用的值
    name = 'baidu'
    # 允许访问的域名
    allowed_domains = ['www.baidu.com']
    # 起始的url值，是在allowed_domains的前面添加http://，并在后面加上/
    start_urls = ['http://www.baidu.com/']

    # 这里的response就相当于urllib.request.urlopen()或者是requests.get()
    def parse(self, response):
        content = response.xpath('/html/head/title/text()')
        print('========================================')
        print(content)
