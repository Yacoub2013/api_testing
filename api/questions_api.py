import json

from api.client import Client


class Api(Client):
    USERS = '/users'
    BASE_URL = 'https://reqres.in/api'

    def list_users(self):
        url = self.BASE_URL + self.USERS + '?page=2'
        return self.get(url)

    def single_user_not_found(self):
        url = self.BASE_URL + self.USERS + '/23'
        return self.get(url)

    def single_user(self):
        url = self.BASE_URL + self.USERS + '/2'
        return self.get(url)

    def create(self, name: str, jop: str):
        url = self.BASE_URL + self.USERS
        payload = json.dumps({
            "name": F"{name}",
            "jop": F"{jop}"
        })
        headers = {
            'Content-Type': 'application/json'
        }
        return self.post(url, headers, payload)

    def delete_user(self, id: int):
        url = self.BASE_URL + self.USERS + F'/{id}'
        return self.delete(url)

    # def reg(self, email, password):
    #     url = self.BASE_URL + '/register'
    #     payload = json.dumps({
    #         "email": F"{email}",
    #         "password": F"{password}"
    #     })
    #     headers = {
    #         'Content-Type': 'application/json'
    #     }
    #     return self.post(url, payload, headers)

    def reg(self, email, password):
        url = self.BASE_URL + "/register"
        payload = json.dumps({
            "email": F"{email}",
            "password": F"{password}"
        })
        headers = {
            "Content-Type": "application/json"
        }
        return self.post(url, headers, payload)


api = Api()  # будем импортировать api
