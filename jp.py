import json
import urllib
import time
import os

if not os.path.exists('json'):
	os.makedirs('json')
	
if not os.path.exists('img'):
	os.makedirs('img')

for p in range(1,3):
	print "saving json page_"+str(p)

	urllib.urlretrieve("http://www.easports.com/fifa/ultimate-team/api/fut/item?page="+str(p),"json/"+str(p)+".json")

	time.sleep(2)

	try:
		with open("json/"+str(p)+".json") as jf:
			data=json.load(jf)
	except Exception as e:
		print e 
		pass
        
        for i in range(0,24):

			fn= data["items"][i]["firstName"]
			ln= data["items"][i]["commonName"]
			cn= data["items"][i]["lastName"]
			img=data["items"][i]["headshot"]["imgUrl"]
			club= data["items"][i]["club"]["name"]

			if not ln=="":
				full=ln
			else:
				full=fn+" "+cn

			img_name=full+"-"+club
			if '/' in img_name:
				img_name=img_name.replace('/', '-')
			urllib.urlretrieve(img,"img/"+img_name+"_page_"+str(p)+".png")
			time.sleep(2)	
