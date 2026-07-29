import json
data = True
with open ("cities.json","r") as f:
    while data:
        data=f.readline()
        if data=="":
            break
        data = data.strip() # remove \n
        if not data:        # skip blank lines
            continue
        json_data=json.loads(data)
        print(json_data)
        