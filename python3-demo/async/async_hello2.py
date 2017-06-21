#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import asyncio

@asyncio.coroutine
def hello():
    print('hello! (%s)' % threading.currentThread())
    yield from asyncio.sleep(2)
    print('hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
