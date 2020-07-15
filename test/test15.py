#python json
import json

data = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com'
}

jsonStr = json.dumps(data)
print(data)
print(jsonStr)