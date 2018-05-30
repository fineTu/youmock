# -*- coding: utf-8 -*-
import json


class DataLoader(object):

    def __init__(self, file_path):
        self.file_path = file_path
        self.mock_obj = self._load_project_file(file_path)
        self.mock_map = self._build_mock_map(self.mock_obj)

    def _build_mock_map(self, jsonObj):
        resMap = {}
        for mock_obj in jsonObj.get('mocks'):
            print mock_obj
            print mock_obj.get(u'url')
            for method in mock_obj.get(u'methods'):
                resMap[DataLoader.build_mock_key(mock_obj.get(u'url'),method)] = mock_obj

        return resMap

    def _load_project_file(self, file_path):
        jsonfile = open(file_path, 'r')
        jsonObj = json.loads(jsonfile.read())
        jsonfile.close()
        return jsonObj

    def _sync_data(self):
        self.mock_obj = self._load_project_file(self.file_path)
        self.mock_map = self._build_mock_map(self.mock_obj)

    def add_mock(self, mock_bean):
        mocks = self.mock_obj.get('mocks',[])
        mocks.append(mock_bean.to_json_obj())
        for method in mock_bean.methods:
            self.mock_map[DataLoader.build_mock_key(mock_bean.url, method)] = mock_bean.to_json_obj()
        self._persist()
        self._sync_data()

    def del_mock(self, key):
        index, mock = self._find_mock_in_file(key=key)
        mocks = self.mock_obj.get('mocks', [])
        del mocks[index]
        self._persist()
        return mock

    def query_mock(self, url, methods):
        key = DataLoader.build_mock_key(url, methods)
        return self.mock_map.get(key)

    def update_mock(self,url, methods, mock):
        key = DataLoader.build_mock_key(url, methods)
        index, old_mock = self._find_mock_in_file(key)
        old_mock['response'] = mock.get('response')
        old_mock['name'] = mock.get('name')
        self._persist()

    def _find_mock_in_file(self, key):
        mocks = self.mock_obj.get('mocks', [])
        for index in range(0,len(self.mock_obj.get('mocks',[]))):
            mock = mocks[index]
            if cmp(key, DataLoader.build_mock_key(mock.get('url'),mock.get('methods'))) == 0:
                return index, mock

    @classmethod
    def build_mock_key(cls, url, methods):
        methods_str = '['
        if isinstance(methods,list):
            methods_str += ','.join(methods)
        elif isinstance(methods,str) or isinstance(methods,unicode):
            methods_str += methods
        methods_str += ']'
        return methods_str + '-' + url

    def _persist(self):
        temp_str = ''
        try:
            json_file = open(self.file_path, 'r')
            temp_str = json_file.read()
            json_file.close()
            json_file = open(self.file_path, 'w')
            json_file.write(json.dumps(self.mock_obj, indent=4, sort_keys=False))
        except Exception as e:
            print e
            json_file.write(temp_str)
        finally:
            json_file.close()


