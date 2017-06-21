#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio

@asyncio.coroutine
def hello():
    print('hello')

    r = yield from asyncio.sleep(1)
    print('hello2')

loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
loop.close()
