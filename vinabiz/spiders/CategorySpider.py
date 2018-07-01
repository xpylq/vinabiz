import scrapy
import re
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor

url_list = []


class CategorySpider(scrapy.Spider):
    name = 'categorySpider'

    def start_requests(self):
        yield scrapy.Request(url="https://vinabiz.org/categories/tinhthanh/", callback=self.parse_category,
                             meta={"deep": 1})

    def parse_category(self, response):

        for url in response.css('.btn-labeled ::attr(href)').extract():
            url = "https://vinabiz.org" + url
            deep = response.meta['deep']
            if deep < 3:
                deep += 1
                yield scrapy.Request(url=url, callback=self.parse_category, meta={"deep": deep})
            else:
                url_list.append(url)


if __name__ == "__main__":
    configure_logging({"LOG_FORMAT": "%(levelname)s: %(message)s"})
    runner = CrawlerRunner(get_project_settings())
    d = runner.crawl(CategorySpider)
    d.addBoth(lambda _: reactor.stop())
    reactor.run()  # the script will block here until the crawling is finished
    file = open("category_bk.txt", "w", encoding="utf-8")
    for url in set(url_list):
        file.write(url)
        file.write("\n")
    file.close()
