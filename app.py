
from flask import Flask,request
from flask import render_template
import json
import requests
import lxml.etree as etree


app = Flask(__name__)

@app.route("/v2",methods=['GET'])
def index():

    msg = '{"message":"Not Found" , "status":404}'
    output = json.loads(msg)
    print(output["status"])
    return json.dumps(output , indent=4, sort_keys=True)

@app.route("/v2/version",methods=['GET'])
def version():
    msg = '{"api": "c0re_api", "author":"kearol", "website": "c0re.moe" ,"version" :"v0.1"}'
    output = json.loads(msg)
    return  json.dumps(output, indent=4, sort_keys=True)


if __name__ == "__main__":
    app.run( port=9205)



