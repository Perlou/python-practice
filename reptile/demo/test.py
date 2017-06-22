import urllib2

url = 'http://www.meimeifa.com'

# first

# res1 = urllib2.urlopen(url)

# print res1.getcode()
# print len(res1.read())

# second

req1 = urllib2.Request(url)
req1.add_header('user-agent', 'Mozilla/5.0')
res2 = urllib2.urlopen(req1)
print res2.getcode()
print len(res2.read())


# third


