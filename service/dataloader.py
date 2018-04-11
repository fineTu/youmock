# -*- coding: utf-8 -*-
import json


class DataLoader(object):

    def __init__(self, file_path):
        self.file_path = file_path
        self.mock_obj = self.load_project_file(file_path)
        self.mock_map = self.build_mock_map(self.mock_obj)

    def build_mock_map(self, jsonObj):
        resMap = {}
        for mock_obj in jsonObj.get('mocks'):
            print mock_obj
            print mock_obj.get(u'url')
            resMap[self._build_mock_key(mock_obj.get(u'url'),mock_obj.get(u'methods'))] = mock_obj
        return resMap

    def load_project_file(self, file_path):
        jsonfile = open(file_path, 'r')
        jsonObj = json.loads(jsonfile.read())
        jsonfile.close()
        return jsonObj

    def add_mock(self, mock_bean):
        mocks = self.mock_obj.get('mocks',[])
        mocks.append(mock_bean.to_json_obj)
        self.mock_map[self._build_mock_key(mock_bean.get('url'),mock_bean.get('methods'))] = mock_bean.to_json_obj
        self._persist()

    def del_mock(self, key):
        index, mock = self._find_mock(key=key)
        mocks = self.mock_obj.get('mocks', [])
        del mocks[index]
        return mock

    def query_mock(self, key):
        return self._find_mock(key=key)[1]

    def update_mock(self, key, mock):
        index, old_mock = self._find_mock(key=key)
        old_mock['response'] = mock.get('response')
        old_mock['name'] = mock.get('name')

    def _find_mock(self, url, methods, key=''):
        if ''.equals(key):
            key = self._build_mock_key(url,methods)

        mocks = self.mock_obj.get('mocks', [])
        for index in range(0,len(self.mock_obj.get('mocks',[]))):
            mock = mocks[index]
            if key.equals(self._build_mock_key(mock.get('url'),mock.get('method'))):
                return index, mock

    @staticmethod
    def _build_mock_key(url, methods):
        methods_str = '['
        for method in methods:
            methods_str += method
        methods_str += ']'
        return methods_str + '-' + url

    def _persist(self):
        json_file = open(self.file_path, 'w')
        json_file.write(json.dumps(self.mock_obj))
        json_file.close()


