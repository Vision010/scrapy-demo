from  scrapy import cmdline
# 输出未过滤的页面信息
cmdline.execute('scrapy crawl doubanSpider -o movielist.csv -s FEED_EXPORT_ENCIDING=utf-8'.split())