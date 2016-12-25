#!/usr/bin/python
# -*- coding: UTF-8 -*-

import httplib, urllib
params = urllib.urlencode({"test": "bonjour"})
headers = {"Content-type": "application/json", "Accept": "text/plain"}
conn = httplib.HTTPConnection("localhost:8080")
conn.request("POST", "/api/v1/addrecord/2", params, headers)
response = conn.getresponse()
print response.status, response.reason
data = response.read()
conn.close()
