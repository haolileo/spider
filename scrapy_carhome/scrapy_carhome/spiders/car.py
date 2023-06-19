import scrapy


class CarSpider(scrapy.Spider):
    name = 'car'
    allowed_domains = ['car.autohome.com.cn/price/brand-36.html']
    start_urls = ['https://car.autohome.com.cn/price/brand-36.html']

    def parse(self, response):
        print('==================================')
        name_list = response.xpath('//*[@class="main-title"]/a/text()')
        price_list = response.xpath('//*[@class="lever-price red"]/span/text()')
        for i in range(len(name_list)):
            name = name_list[i].extract()
            price = price_list[i].extract()
            print(name+','+price)