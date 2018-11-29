import json

# print(dir(json))

with open('C:\\Users\kumaami3\\Documents\\MyJabberFiles\\atusing2@cisco.com\\guest_card.json', 'r') as obj:
    data = json.load(obj)

    print(data)
