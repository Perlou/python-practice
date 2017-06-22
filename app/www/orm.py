#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Perlou'

import asyncio, logging, aiomysql

def log(sql, args=()):
    logging.info('SQL: %s' % sql)

async def create_pool(loopm **kw):
    logging.info('create database connection pool...')
    global __pool
    __pool = await aiomysql.create_pool(
        host = kw.get('host', 'localhost'),
        port = kw.get('port', 3306),
        user = kw['user'],
        password = kw['password'],
        db = kw['db'],
        charset = kw.get('charset', 'utf8'),
        autocommit = kw.get('')
    )
