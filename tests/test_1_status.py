from http import HTTPStatus
import requests


def test_1_status():
    url = 'https://reqres.in/api/users?page=2'
    response = requests.get(url)
    # assert response.status_code == 200 #парсим ответ
    assert response.status_code == HTTPStatus.OK

# def test_2_register():
#     url = 'https://reqres.in/api/ririster'
#     res_post = requests.get(url)
#     res_post.





