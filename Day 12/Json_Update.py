import json
with open ('data.json', 'r') as f:
    data = json.load(f)
data['age'] = 26
with open ('data.json', 'w') as f:
    json.dump(data, f)

