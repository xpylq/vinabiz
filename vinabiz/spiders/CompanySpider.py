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
        self.bloom = BloomFilter(1000000, 0.001)
        for url in dbComponent.get_all_company_url():
            self.bloom.add(url)
        print("bloomFilter初始化完毕")
        super().__init__(name, **kwargs)

    def start_requests(self):
        # category
        file = open("category.txt", "r", encoding="utf-8")
        for url in file.readlines():
            url = url.replace("\n", "")
            yield scrapy.Request(url=url, callback=self.parse_list)
        print("start_requests 初始化完毕")

    # 解析列表页
    def parse_list(self, response):
        next_url = response.css(".PagedList-skipToNext a::attr(href)").extract_first()
        if (next_url is not None) and (next_url != ''):
            next_url = "https://vinabiz.org" + next_url
            yield scrapy.Request(url=next_url, callback=self.parse_list)
        url_list = response.css("h4 a::attr(href)").extract()
        for url in url_list:
            url = "https://vinabiz.org" + url
            if url not in self.bloom:
                yield scrapy.Request(url=url, callback=self.parse_company)

    # 解析详情页
    def parse_company(self, response):
        td_list = response.css("#wid-detail-info td")
        index = 0
        data = {}
        data['guid'] = str(uuid.uuid4()).replace("-", "")
        data['url'] = response.url
        while index < td_list.__len__():
            td = td_list[index]
            if td.css("::attr(class)").extract_first() == "bg_table_td":
                index += 1
                content = self.porcess_content(td_list[index])
                title = td.css("::text").extract_first()
                # BUSINESS
                if title == 'Tên chính thức':
                    data['official_name'] = content
                if title == 'Tên giao dịch':
                    data['trading_name'] = content
                if title == 'Mã doanh nghiệp':
                    data['business_code'] = content
                if title == 'Ngày cấp':
                    data['date_range'] = content
                if title == 'Cơ quan thuế quản lý':
                    data['tax_authorities_manage'] = content
                if title == 'Ngày bắt đầu hoạt động':
                    data['date_of_commencement_of_operation'] = content
                if title == 'Trạng thái':
                    data['status'] = content
                # CONTACT
                if title == 'Địa chỉ trụ sở':
                    data['office_address'] = content
                if title == 'Điện thoại':
                    data['phone1'] = content
                if title == 'Fax':
                    data['fax'] = content
                if title == 'Email':
                    data['email'] = content
                if title == 'Website':
                    data['website'] = content
                if title == 'Người đại diện':
                    data['representative'] = content
                if title == 'Điện thoại':
                    data['phone2'] = content
                if title == 'Địa chỉ người đại diện':
                    data['representative_address'] = content
                if title == 'Giám đốc':
                    data['manager'] = content
                if title == 'Điện thoại giám đốc':
                    data['phone_director'] = content
                if title == 'Địa chỉ giám đốc':
                    data['address_director'] = content
                if title == 'Kế toán':
                    data['accountant'] = content
                if title == 'Điện thoại kế toán':
                    data['phone_accounting'] = content
                if title == 'Địa chỉ kế toán':
                    data['account_address'] = content
                # INDUSTRY
                if title == 'Ngành nghề chính':
                    data['main_job'] = content
                if title == 'Lĩnh vực kinh tế':
                    data['economic_field'] = content
                if title == 'Loại hình kinh tế':
                    data['type_of_economic'] = content
                if title == 'Loại hình tổ chức':
                    data['type_of_organization'] = content
                if title == 'Cấp chương':
                    data['class_chapters'] = content
                if title == 'Loại khoản':
                    data['item_type'] = content
            index += 1
        dbComponent.add_company(data)

    def porcess_content(self, td):
        try:
            result = ''
            text_list = td.css("::text").extract()
            for text in text_list:
                result += text
            result = result.replace("\n", "")
            result = result.replace("'", "\\\'")
        except Exception as e:
            print(e)
        return result


if __name__ == "__main__":
    configure_logging({"LOG_FORMAT": "%(levelname)s: %(message)s"})
    runner = CrawlerRunner(get_project_settings())
    d = runner.crawl(CompanySpider)
    d.addBoth(lambda _: reactor.stop())
    reactor.run()  # the script will block here until the crawling is finished
