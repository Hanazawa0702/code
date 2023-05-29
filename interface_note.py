import requests

# Get请求方式

# -------------------------------------------------
# GET不带参数请求
response = requests.get("https://www.baidu.com")

print(response.url)
print(response.status_code)
print(response.text)
# -------------------------------------------------
'''
# -------------------------------------------------

# GET带参数请求
url = "https://www.baidu.com"
#params = {"id": 1001}
params = {"id": "1001, 1002"}
#params = {"id": 1001, "kw": "北京"}

response = requests.get(url, params = params)

print(response.text)
# -------------------------------------------------
'''
# Post请求方式
'''
# data格式，直接定义为字典使用
# response = requests.post(url,data=None,json=None)
data = {'parameter1':'12345','parameter2':'23456'}
response = requests.post('http://example.com',data=data)
'''
'''
# json格式，用json.dumps()函数将字典转为JSON串即可
url = 'http://www.example/post'
s = json.dumps({'key1': 'value1', 'key2': 'value2'})
r = requests.post(url, data=s)
print (r.text)
'''
# 其他请求方式
'''
response = requests.put(url,data={"Key":"Value"})
response = requests.delete(url)
response = requests.head(url)
response = requests.options(url)

response.status_code 状态码
response.url 请求url
response.encoding 查看响应头部字符编码
response.headers 头信息
response.cookies cookie信息
response.text 文本形式的响应内容
response.content.decode('utf-8') 字节形式的响应内容
response.json() json形式的响应内容
'''