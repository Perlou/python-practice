#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = 'Perlou(perloukevin@gmail.com)'

import urllib.request

class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        res = urllib.request.urlopen(url)
        if response.getcode() != 200
            return None

        return response.read()
