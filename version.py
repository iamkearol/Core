#/usr/bin/python3.6 
import json
def version():
	msg = '{"api": "c0re_api", "author":"kearol", "website": "c0re.moe" ,"version" :"v0.1"}'
	output = json.loads(msg)
	return  json.dumps(output, indent=4, sort_keys=True)
