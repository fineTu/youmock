# -*- coding: utf-8 -*-
import os

from flask import Flask,request
import json
from flask import render_template

# from web import main
from bean.mockbean import MockBean
from service.dataloader import DataLoader

app = Flask(__name__, template_folder="template")
# app.register_blueprint(main)

mockMap = None
base_dir = os.path.dirname(__file__)
data_loader = DataLoader(base_dir+'/finance_mock.json')

@app.route("/mock/<url>",methods=['GET','POST'])
def dispatch(url):
    mockObj = mockMap.get(url)
    method = request.method
    print method
    if method not in mockObj.get(u'methods'):
        return 'method not match', 405
    return mockObj.get(u'response')


@app.route("/index",methods=['GET','POST'])
def index():
    return render_template('index.html',mock_obj=data_loader.mock_obj)


@app.route("/new",methods=['GET','POST'])
def new():
    return render_template('add_mock.html')


# @app.route("/save",methods=['GET','POST'])
# def save():
#     mock_bean = MockBean()
#     mock_bean.name
#     data_loader.add_mock()
#     return render_template('index.html', mock_obj=data_loader.mock_obj)


def buildMockMap(jsonObj):
    resMap = {}
    for mockObj in jsonObj.get("mocks"):
        print mockObj
        print mockObj.get(u'url')
        resMap[mockObj.get(u'url')] = mockObj
    return resMap

if __name__ == '__main__':
    base_dir = os.path.dirname(__file__)
    print base_dir
    jsonfile = open(base_dir+'/finance_mock.json','r')
    jsonObj = json.loads(jsonfile.read())
    jsonfile.close()
    mockMap = buildMockMap(jsonObj)
    app.debug=True
    app.run(host='0.0.0.0',port=8080)