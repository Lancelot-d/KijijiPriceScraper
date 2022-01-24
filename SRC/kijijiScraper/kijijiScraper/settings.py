# Scrapy settings for kijijiScraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'kijijiScraper'

SPIDER_MODULES = ['kijijiScraper.spiders']
NEWSPIDER_MODULE = 'kijijiScraper.spiders'


#usefull to simulate a classic web browser and dodge ERROR 403 - acess forbiden
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
}

ROBOTSTXT_OBEY = False

#DUPEFILTER_CLASS = 'scrapy.dupefilters.BaseDupeFilter'
