import json
data = json.load(open('thumbsup.json'))
for item in data[1][0]:
    print(item[1] + ' ' + item[3])
