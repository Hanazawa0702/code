# -*- coding: utf-8 -*
import json
import unittest
import sys
sys.path.append(sys.path[0]+'/var/lib/jenkins/workspace/interfaceAPI')

from API.interface import InterfaceTest
from Tools.Json_read import JsonRead

JsonList = []
JsonData = JsonRead("Interface_Data.json").json_read()
JsonList.append(JsonData.get("url"))
JsonList.append(JsonData.get("headers"))


class TestInterfaceCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_city_bj(self):
        # 判断响应结果中包含的字符串，注意转译符号
        result = InterfaceTest(JsonList[0], JsonList[1]).interface_connect()
        self.assertIn("\"city\":\"北京\"", result)

    def test_code_200(self):
        code = InterfaceTest(JsonList[0], JsonList[1]).interface_response_status()
        assert code.status_code == 200

    def test_weather_cityId(self):
        # 返回的响应结果默认为字符串，所以先要将响应结果转化为json数据并实例化后（转化为字典）再断言
        result = InterfaceTest(JsonList[0], JsonList[1]).interface_connect()
        j = json.loads(result)
        self.assertEqual(j['weatherinfo']['cityid'], '101010100')

    def test_size_205(self):
        result = InterfaceTest(JsonList[0], JsonList[1]).interface_connect()
        assert len(result) == 205

    def test_headers_type(self):
        self.assertEqual(InterfaceTest(JsonList[0], JsonList[1]).interface_headers()['Content-Type'], 'text/html')


if __name__ == '__main__':
    unittest.main()
