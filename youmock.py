# -*- coding: utf-8 -*-
import os
import re

from flask import Flask,request
import json

from flask import redirect
from flask import render_template

# from web import main
from bean.mockbean import MockBean
from service.dataloader import DataLoader

app = Flask(__name__, template_folder="template")
# app.register_blueprint(main)

base_dir = os.path.dirname(os.path.realpath(__file__))
data_loader = DataLoader(base_dir+'/data/_mock.json')

@app.errorhandler(404)
def root(error):
    url = request.url
    p = re.compile(r'http://.+?/')
    m = p.match(url)
    url = url[m.end():]
    if "mock/" == url[0:5]:
        mockObj = data_loader.query_mock(url[5:], request.method)
        if mockObj == None:
            return 'method not match', 405
        return mockObj.get(u'res_body')
    # mockObj = data_loader.query_mock(url,request.method)
    # if mockObj == None:
    #     return 'method not match', 405
    return "404"

@app.route("/mock/<url>",methods=['GET','POST'])
def dispatch(url):
    mockObj = data_loader.query_mock(url,request.method)
    if mockObj == None:
        return 'method not match', 405
    return mockObj.get(u'response')


@app.route("/index",methods=['GET','POST'])
def index():
    return render_template('index.html',mock_obj=data_loader.mock_obj)


@app.route("/new",methods=['GET', 'POST'])
def new():
    return render_template('add_mock.html')


@app.route("/save",methods=['GET', 'POST'])
def save():
    mock_bean = MockBean()
    mock_bean.key = DataLoader.build_mock_key(request.form['url'], request.form.getlist('methods'))
    mock_bean.name = request.form['name']
    mock_bean.url = request.form['url']
    mock_bean.methods = request.form.getlist('methods')
    mock_bean.res_code = 200
    mock_bean.res_header = request.form['header']
    mock_bean.res_body = request.form['body']
    data_loader.add_mock(mock_bean)

    return redirect('/index')

@app.route("/del/<key>",methods=['GET', 'POST'])
def delete(key):
    data_loader.del_mock(key)
    return redirect('/index')

if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=8080)