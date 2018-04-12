# -*- coding: utf-8 -*-
import json


class MockBean():
    name = ''
    url = ''
    methods = []
    res_code = 200
    response = ''

    def to_json_obj(self):
        jsonObj = {}
        jsonObj['name'] = self.name
        jsonObj['url'] = self.url
        jsonObj['methods'] = self.methods
        jsonObj['res_code'] = self.res_code
        jsonObj['response'] = self.response
        return jsonObj

    def to_json_str(self):
        jsonObj = {}
        jsonObj['name'] = self.name
        jsonObj['url'] = self.url
        jsonObj['methods'] = self.methods
        jsonObj['res_code'] = self.res_code
        jsonObj['response'] = self.response
        return json.dumps(jsonObj)