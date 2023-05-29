import json
import sys
sys.path.append(sys.path[0]+'\..')

# 传入Data文件夹下的json文件后，返回json数据
class JsonRead:
    def __init__(self, filename):
        self.filepath = "./Data/" + filename

    def json_read(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            return json.load(f)


if __name__ == '__main__':
    print(JsonRead("Interface_Data.json").json_read())
