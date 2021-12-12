import requests
import json

payload = {
       "first_name": "Pedro", 
        "city": "Port Melisaport", 
        "state": "Delaware", 
        "postcode": "62769-4228"
        }

r = requests.post('https://reqres.in/api/users', json=payload)

f = open('data.json')
data = json.load(f)

if r.json()['first_name'] in data['first_name'] and r.json()['city'] in data['city'] and r.json()['state'] in data['state'] and r.json()['postcode'] in data['postcode']:
    print('Exist')
else:
    print('Not Exist')

f.close()

