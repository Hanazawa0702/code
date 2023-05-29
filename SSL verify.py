import requests
# 通过一下两行代码即可把警报消除，即使verify=False，报警还是存在的
import urllib3

urllib3.disable_warnings()

response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)
print(response.content.decode('utf-8'))
