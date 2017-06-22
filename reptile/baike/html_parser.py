#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = 'Perlou(perloukevin@gmail.com)'

from bs4 import BeautifulSoup
import urlparse,re

class HtmlParser(object):
    def _get_new_urls(self, page_url, soup):
        new_urls = []
        # links = soup.find_all('a', href=re.compile("view/\d+\.(html|htm)"))
        links = soup.find_all('a', href=re.compile("item/"))

        for link in links:
            url = link['href']
            url = urlparse.urljoin(page_url, url)
            new_urls.append(url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        data = {}
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
        data['title'] = title_node.get_text()
        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_="lemma-summary")
        data['summary'] = summary_node.get_text()
        data['url'] = page_url
        return data


    def parse(self, page_url, html_cont):
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        urls = self._get_new_urls(page_url, soup)
        data = self._get_new_data(page_url, soup)
        return urls, data

