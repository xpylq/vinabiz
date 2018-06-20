# /usr/bin/env python
# encoding=utf-8
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor
import uuid
import vinabiz.component.dbComponent as dbComponent
from bloom_filter import BloomFilter


class CompanySpider(scrapy.Spider):
    name = "companySpider"

    def __init__(self, name=None, **kwargs):
        self.bloom = BloomFilter(500000, 0.001)
        for url in dbComponent.get_all_company_url():
            self.bloom.add(url)
        super().__init__(name, **kwargs)

    def start_requests(self):
        # 遍历列表url
        for i in range(1800, 9551):
            list_url = "https://vinabiz.org/categories/tinhthanh/ha-noi/310030003100/%s" % str(i)
            yield scrapy.Request(url=list_url, callback=self.parse_list)

    # 解析列表页
    def parse_list(self, response):
        url_list = response.css("h4 a::attr(href)").extract()
        for url in url_list:
            url = "https://vinabiz.org" + url
            if url not in self.bloom:
                yield scrapy.Request(url=url, callback=self.parse_company)

    # 解析详情页
    def parse_company(self, response):
        td_list = response.css("td:not(.bg_table_td):not(.bg_table_th):not(.padding-0)")
        data = {}
        data['guid'] = str(uuid.uuid4())
        data['url'] = response.url
        self.porcess_data(data, td_list, "a1", 0)
        data['name'] = data['a1']
        self.porcess_data(data, td_list, "a2", 1)
        self.porcess_data(data, td_list, "a3", 2)
        self.porcess_data(data, td_list, "a4", 3)
        self.porcess_data(data, td_list, "a5", 4)
        self.porcess_data(data, td_list, "a6", 5)
        data['a7'] = "".join(response.css("div .alert-success::text").extract()).replace("\n", "")
        self.porcess_data(data, td_list, "b1", 7)
        self.porcess_data(data, td_list, "b2", 8)
        self.porcess_data(data, td_list, "b3", 9)
        self.porcess_data(data, td_list, "b4", 10)
        self.porcess_data(data, td_list, "b5", 11)
        self.porcess_data(data, td_list, "b6", 12)
        self.porcess_data(data, td_list, "b7", 13)
        self.porcess_data(data, td_list, "b8", 14)
        self.porcess_data(data, td_list, "b9", 15)
        self.porcess_data(data, td_list, "b10", 16)
        self.porcess_data(data, td_list, "b11", 17)
        self.porcess_data(data, td_list, "b12", 18)
        self.porcess_data(data, td_list, "b13", 19)
        self.porcess_data(data, td_list, "b14", 20)
        self.porcess_data(data, td_list, "c1", 21)
        self.porcess_data(data, td_list, "c2", 22)
        self.porcess_data(data, td_list, "c3", 23)
        self.porcess_data(data, td_list, "c4", 24)
        self.porcess_data(data, td_list, "c5", 25)
        self.porcess_data(data, td_list, "c6", 26)
        dbComponent.add_company(data)

    def porcess_data(self, data, td_list, key, td_list_index):
        try:
            result = ''
            text_list = td_list[td_list_index].css("::text").extract()
            for text in text_list:
                result += text
            result = result.replace("\n", "")
            result = result.replace("'", "\\\'")
            data[key] = result
        except Exception as e:
            data[key] = ""

if __name__ == "__main__":
    configure_logging({"LOG_FORMAT": "%(levelname)s: %(message)s"})
    runner = CrawlerRunner(get_project_settings())
    d = runner.crawl(CompanySpider)
    d.addBoth(lambda _: reactor.stop())
    reactor.run()  # the script will block here until the crawling is finished
