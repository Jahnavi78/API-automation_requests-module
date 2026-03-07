import requests
import json
import random
import string

base_url= "https://jsonplaceholder.typicode.com"
auth_token = "Bearer 1981bd04e4b63b567847cae77994fdf8b13225c9f34f8caca297ad8b26dc0509"
def generate_random_string():
    str_len= 20
    random_string= ''.join(random.choice(string.ascii_lowercase) for _ in range(str_len))
    return random_string

#GET Request
def get_request():
    url= base_url + "/todos/1"
    print("get url:", url)
    headers= {"authorization": auth_token}
    response = requests.get(url, headers= headers)
    assert response.status_code ==200
    json_data= response.json()
    print("type of json_data:", type(json_data))
    #dumps will convert python dict to json str
    json_str= json.dumps(json_data, indent=4)
    print("type of json_str:", type(json_str))
    print("json GET response: ", json_str)
    print("GET request is done")
    print("==================================================")

def post_request():
    url= base_url + "/todos"
    print("post url:", url)
    headers= {"authorization": auth_token}
    data= {
      "userId": 1,
      "id": 1,
      "title": generate_random_string(),
      "completed": False
            }
    response = requests.post(url, json=data, headers=headers)
    json_data= response.json()
    json_str= json.dumps(json_data, indent=4)
    print("json POST response body:", json_str)
    user_id=json_data["userId"]
    print("user_id:", user_id)
    assert response.status_code ==201
    assert "completed" in json_data
    assert json_data["completed"]== False
    print("POST/create user is done")
    print("===============================================")
    return user_id

def put_request(user_id):
    url= base_url + f"/todos/{user_id}"
    print("PUT url:", url)
    headers= {"authorization": auth_token}
    data={
      "userId": 1,
      "id": 1,
      "title": generate_random_string(),
      "completed": False
           }
    response= requests.put(url, json=data, headers=headers)
    json_data= response.json()
    json_str= json.dumps(json_data, indent=4)
    print("json PUT response body:", json_str)
    assert response.status_code == 200
    assert json_data["userId"] == user_id
    assert json_data["completed"] == False
    print("PUT request is done")
    print("=================================================")

def delete_request(user_id):
    url= base_url +f"/todos/{user_id}"
    print("DELETE url:", url)
    headers= {"authorization": auth_token}
    response= requests.delete(url, headers= headers)
    #in actual scenarios, delete return 204...as this is test api this is returning 200 which is fine
    assert response.status_code == 200
    print("DELETE request is done")
    print("============================================================")




#get_request()
user_id=post_request()
put_request(user_id)
delete_request(user_id)
