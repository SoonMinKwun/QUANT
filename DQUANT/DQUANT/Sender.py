import json
import urllib2

data = {
            'ids': ["milan", "rome","florence"]
}

req = urllib2.Request('http://127.0.0.1:8000/value/')
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps(data))