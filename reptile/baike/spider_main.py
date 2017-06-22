#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = 'Perlou(perloukevin@gmail.com)'

import url_manager, html_outputer, html_downloader, html_parser

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmloutPuter()

    # 调度函数
    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()
            html_cont = self.downloader.download(new_url)

            # 数据解析
            new_urls, new_data = self.parser.parse(new_url, html_cont)
            self.urls.add_new_urls(new_urls)
            self.outputer.collect_data(new_data)

        # 输出数据
        self.outputer.output_html()

if __name__ == '__main__':
    root_url = 'http://baike.baidu.com/view/21087.htm'
#     obj_spider =
