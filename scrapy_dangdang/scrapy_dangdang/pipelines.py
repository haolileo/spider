# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import urllib.request

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# 如果想使用pipelines就必须要在setting中调整设置
class ScrapyDangdangPipeline:
    # 在爬虫文件开始前所执行的方法
    def open_spider(self,spider):
        self.fp = open('book.json','a',encoding='utf-8')
    # item就是yield后面的book对象
    def process_item(self, item, spider):
        # # 以下的这种方式并不推荐因为对于文件的操作过于频繁
        # # write方法必须要是字符串，不能是其他类型
        # with open('book.json','a',encoding='utf-8') as fp:
        #     fp.write(str(item))
        self.fp.write(str(item))
        return item
    # 在爬虫文件执行完后执行的方法
    def close_spider(self,spider):
        self.fp.close()

# 多条管道开启
class DangDangDownloadPipeline:
    def process_item(self,item,spider):

        url = 'http:' + item.get('src')
        filename = './spiders/books/' + item.get('name') + '.jpg'
        urllib.request.urlretrieve(url=url,filename=filename)

        return item