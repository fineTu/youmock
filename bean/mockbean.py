# -*- coding: utf-8 -*-
import json


class MockBean():
    key = ''
    name = ''
    url = ''
    methods = []
    res_code = 200
    res_header = ''
    res_body = ''

    def to_json_obj(self):
        jsonObj = {}
        jsonObj['key'] = self.key
        jsonObj['name'] = self.name
        jsonObj['url'] = self.url
        jsonObj['methods'] = self.methods
        jsonObj['res_code'] = self.res_code
        jsonObj['res_header'] = self._build_headers(self.res_header)
        jsonObj['res_body'] = self.res_body
        return jsonObj

    def to_json_str(self):
        jsonObj = {}
        jsonObj['key'] = self.key
        jsonObj['name'] = self.name
        jsonObj['url'] = self.url
        jsonObj['methods'] = self.methods
        jsonObj['res_code'] = self.res_code
        jsonObj['res_header'] = self._build_headers(self.res_header)
        jsonObj['res_body'] = self.res_body
        return json.dumps(jsonObj)

    @staticmethod
    def _build_headers(header_str):
        headers = header_str.split('\n')
        headers = [ tuple(item.replace('\r','').split(':')) for item in headers]
        return headers