BOT_NAME = 'quotesbot'

LOG_LEVEL='ERROR'
#
SPIDER_MODULES = ['quotesbot.spiders']
NEWSPIDER_MODULE = 'quotesbot.spiders'

ROBOTSTXT_OBEY = True

# 기사 내용 크롤링시 MongoDBPipeline 설정
ITEM_PIPELINES = {'quotesbot.pipelines.MongoDBPipeline': 300,}

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "quotes_crawl"
MONGODB_COLLECTION = "quotes"
