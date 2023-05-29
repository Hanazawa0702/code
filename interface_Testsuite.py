# -*- coding: utf-8 -*
import sys
sys.path.append(sys.path[0]+'/var/lib/jenkins/workspace/interfaceAPI')
import time
import unittest
from Case import interface_assert
from XTestRunner import HTMLTestRunner

suit = unittest.TestSuite()
'''
# 方法一，单独用例导入TestSuite
suit.addTest(interface_assert.TestInterfaceCase('test_city_bj'))
suit.addTest(interface_assert.TestInterfaceCase('test_headers_type'))
suit.addTest(interface_assert.TestInterfaceCase('test_weather_cityId'))
'''
# 方法二，多条导入
# suit.addTests([interface_assert.TestInterfaceCase('test_city_bj'), interface_assert.TestInterfaceCase('test_headers_type'), interface_assert.TestInterfaceCase('test_weather_cityId')])

# 方法三，将用例整理成列表后导入
tests = [
    interface_assert.TestInterfaceCase('test_city_bj'),
    interface_assert.TestInterfaceCase('test_headers_type'),
    interface_assert.TestInterfaceCase('test_weather_cityId')
]
suit.addTests(tests)

# 方法四，指定加载目录下的全部文件名为test开头的测试用例
# unittest.defaultTestLoader.discover("./Case",pattern="test*.py")
file_path = "./Report/{}.html".format(time.strftime("%Y-%m-%d %H_%M_%S"))
r = HTMLTestRunner(stream=open(file_path, "wb"),  # 打开一个报告文件，将句柄传给stream；当路径为空时创建一个新的文件（新增测试报告）
                   tester="Hanazawa0702",             # 报告中显示的测试人员
                   description="接口测试报告",       # 报告中显示的描述信息
                   title="自动化测试报告")
r.run(suit)
