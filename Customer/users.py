import time
import json
import requests


class User:
    """
    This is the user log in class. Hits the log in endpoint and returns an auth token
    """

    def __init__(self, host):
        """
        :rtype: object
        """
        self.auth_token = None
        self.host = host

    def login(self):
        endpoint = "/customer/login"
        url = self.host + endpoint
        body = {'username': "andrewJackson1836@al.com",
                'password': '12345',
                'grant_type': 'password',
                'scope': 'payment,global'
                }

        response = requests.post(url, data=body)
        return response

    def signup(self):
        endpoint = "/customer/signup"
        url = self.host + endpoint
        body = {'first_name': 'python-user',
                'last_name': 'test',
                'email': "python_guy22@al.com",
                'password': 'pythondude',
                'grant_type': 'password',
                'scope': 'payment,global'}
        response = requests.post(url, data=body)

        return response

    def get_user_auth(self, response_object):
        self.auth_token = response_object["token"]
        # print(self.user_auth)
        return self.auth_token
