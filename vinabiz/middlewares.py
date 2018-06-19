# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random


# 通用的middleware
class CommenMiddleware(object):
    def __init__(self, agents):
        self.agents = agents
        self.proxy = None

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist("USER_AGENTS"))

    def process_request(self, request, spider):
        if self.proxy:
            request.meta["proxy"] = self.proxy
        request.headers["User-Agent"] = random.choice(self.agents)

    def process_response(self, request, response, spider):
        return response
