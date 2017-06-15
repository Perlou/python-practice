#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

# 获取当前时间
now = datetime.now()
print('now =', now)
print('type(now)=', type(now))

# 用指定日期时间创建datetiem
dt = datetime(2017, 6, 1, 12, 20)
print('dt =', dt)

# 把 datetime 转换成 timestamp
print('datetime -> timestamp:', dt.timestamp())

# 把 timestamp 转换成 datetime
t = dt.timestamp()
print('timestamp -> datetime:', datetime.fromtimestamp(t))
print('timestamp -> datetime as UTC+0', datetime.utcfromtimestamp(t))
