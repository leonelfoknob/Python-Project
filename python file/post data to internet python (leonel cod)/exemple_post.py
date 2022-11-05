
import serial
import time
import requests
import urllib3, urllib
import urllib.request as urllib2
#import urllib2, urllib
mydata=[('one','1'),('two','2')]    #The first is the var name the second is the value
mydata=urllib.parse.urlencode(mydata).encode("utf-8")
path='https://datamakinafleo.000webhostapp.com/add_data.php'    #the url you want to POST to
req=urllib.request.urlopen(path, mydata)
#req.add_header("Content-type", "application/x-www-form-urlencoded","Cache-Control", "no-cache")
page=urllib2.urlopen(req).read()
print (page)