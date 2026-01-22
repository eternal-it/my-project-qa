import requests

def test_created_new_post():

    unique_title = "Test Post Day 5"
    new_post = {
        "title": unique_title,
        "body": "Этот пост создан в рамках обучения в 5 день!",
        "userId": 1
    }

    creat_response = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post)
    assert creat_response.status_code == 201

    creat_data = creat_response.json()
    creat_id = creat_data["id"]

    list_response = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert list_response.status_code == 200
    list_data = list_response.json()
    
    assert any(post["id"] == creat_id and post["title"] == unique_title for post in list_data)





    