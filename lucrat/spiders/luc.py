import scrapy
import time
from scrapy.loader import ItemLoader
from lucrat.items import Article
from datetime import datetime


class LucSpider(scrapy.Spider):
    name = 'luc'
    allowed_domains = ['lucrat.net']
    start_urls = ['https://blog.lucrat.net/']

    def parse(self, response):
        # get all categories, parse them one by one

        categories = response.xpath("//div[@id='categories-3']/ul/li/a/@href").getall()
        for cat in categories:
            yield response.follow(cat, self.parse_category)

    def parse_category(self, response):
        # for each category, get every article on every page

        category_name = response.xpath("//h1/text()").get()
        links = response.xpath("//a[@class='mybutton']/@href").getall()
        for link in links:
            yield response.follow(link, self.parse_article, cb_kwargs=dict(category_name=category_name))

        next_page = response.xpath("//a[text()='следваща']/@href").get()
        if next_page:
            yield response.follow(next_page, self.parse_category)

    def parse_article(self, response, category_name):
        # get all the data from the article

        item = ItemLoader(item=Article(), response=response)

        title = response.xpath("//h1/text()").get()
        data = response.xpath("//div[@class='pagesmeta']/descendant-or-self::*/text()").getall()

        date = data[0][:-2]
        date_dict = {
            "януари": "January",
            "февруари": "February",
            "март": "March",
            "април": "April",
            "май": "May",
            "юни": "June",
            "юли": "July",
            "август": "August",
            "септември": "September",
            "октомври": "October",
            "ноември": "November",
            "декември": "December",
        }

        date = date.split(" ")
        for key in date_dict.keys():
            if date[1] == key:
                date[1] = date_dict[key]
        date = " ".join(date)

        # reformat date
        date_time_obj = datetime.strptime(date, '%d %B %Y')
        date = date_time_obj.strftime("%y/%m/%d")

        author = data[2][9:]
        if not author:
            author = data[3]
            tags = data[5:]
        else:
            tags = data[4:]

        tags = [tag for tag in tags if tag != category_name and tag.strip() != ',']
        tags = ", ".join(tags)

        content = response.xpath("//div[@class='entry-content']/descendant-or-self::*/text()").getall()
        content = [text.strip() for text in content if text.strip()]
        content = " ".join(content)

        item.add_value('title', title)
        item.add_value('link', response.url)
        item.add_value('date', date)
        item.add_value('author', author)
        item.add_value('category', category_name)
        item.add_value('tags', tags)
        item.add_value('content', content)

        return item.load_item()
