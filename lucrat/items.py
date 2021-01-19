import scrapy


class Article(scrapy.Item):
    title = scrapy.Field()  # title of the article
    link = scrapy.Field()  # link to the article
    category = scrapy.Field()  # category the article is under
    date = scrapy.Field()  # date of posting, yy/mm/dd
    author = scrapy.Field()  # author of the article
    tags = scrapy.Field()  # all extra tags, sometimes empty
    content = scrapy.Field()  # the body of the article
