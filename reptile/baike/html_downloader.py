#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = 'Perlou(perloukevin@gmail.com)'

import urllib2

class HtmlDownloader(object):
    def download(self, url): 
        headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5",\
                 "Referer": 'http://www.baidu.com'}
        req = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(req)
        if (response.getcode() == 200):
            return response.read()
        else:
            return None
