import requests
import json

URL = "http://127.0.0.1:8000/stuapi/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}
    r = requests.get(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)
#get_data()
# create/post


def post_data():
    data = {
        'name': 'Rahul',
        'roll': 100,
        'city': 'Kalburgi'
    }
    headers = {'content-Type':'application/json'}

    json_data = json.dumps(data)
    r = requests.post(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)
#post_data()


def update_data():
    data = {
        'id': 4,
        'name': 'kohali',
        'roll': 1010,
        'city': 'navi Mumbai'
    }
    headers = {'content-Type':'application/json'}

    json_data = json.dumps(data)
    r = requests.put(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)
update_data()


def delete_data():
    data = {
        'id': 2,
    }
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)
#delete_data()
