import urllib2
import json

output = open("out.txt","w")

for i in range(2000):
	print "Crawling : " + str(i)
	try:
		url = "http://someurl.com/wp-json/wp/v2/posts/"+str(i)
		json_content = urllib2.urlopen(url)
		content = json.load(json_content)
		output.write(str(i) + "\t" + content["date"] + "\t" + content["link"] + "\n")
		output.flush()
	except:
		pass

