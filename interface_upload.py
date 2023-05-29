import requests

file = {'file': open('baidu.png', 'rb')}

response = requests.post('http://httpbin.org/post', files=file)

print(response.text)
