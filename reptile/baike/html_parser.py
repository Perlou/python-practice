#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = 'Perlou(perloukevin@gmail.com)'

from bs4 import BeautifulSoup
import re
import urllib.parse

class HtmlParser(object):
    def paser(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding = 'utf-8')
        # new_urls = self._get_new_urls(page)

