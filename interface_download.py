import requests

response = requests.get("https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png")

with open('baidu.png', 'wb') as f:
    f.write(response.content)
    f.close()
