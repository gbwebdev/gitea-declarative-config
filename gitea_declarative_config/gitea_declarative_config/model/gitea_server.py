"""Gitea Server Model Class Module
"""

import logging
import requests
from gitea_declarative_config.model._singleton_meta import SingletonMeta


import git

logger = logging.getLogger("default")

class GiteaServer(metaclass=SingletonMeta):
    """Gitea Server Model Class
    """
    def __init__(self):
        self._raw_url = None
        self._token = None
        self._user = None
        self._password = None
        self._base_url = None
        self._api_url = None
        self._client = None
    
    def _set_urls(self):
        if self._raw_url is not None \
             and self._token is not None:
            if self._base_url is None :
                self._base_url = self._raw_url.replace("://", f"://{self._token}@")
            if self._api_url is None :
                self._api_url = f"{self._raw_url}/api/v1"

    def ready(self):
        if self._raw_url  and self._token and self._base_url and self._api_url :
       
            headers = {'Authorization': f'token {self.token}'}
            endpoint = '/user/repos'  # Endpoint to list repositories of the authenticated user

            url = self._api_url + endpoint
            response = requests.get(url, headers=headers)  # TODO : remove verify=False in prod !

            if response.status_code == 200:
                return True
        
        return False
    
    def assert_ready(self):
        if not self.ready():
            raise Exception("Cannot connect to git server.")
    
    @property
    def client(self):
        self.assert_ready()
        return self._client
    

    @property
    def raw_url(self) -> str:
        return self._raw_url
    
    @raw_url.setter
    def raw_url(self, raw_url: str):
        self._raw_url = raw_url
        self._set_urls()

    @property
    def token(self) -> str:
        return self._token
    
    @token.setter
    def token(self, token: str):
        self._token = token
        self._set_urls()

    @property
    def user(self) -> str:
        return self._user
    
    @user.setter
    def user(self, user: str):
        self._user = user
    
    @property
    def password(self) -> str:
        return self._password
    
    @password.setter
    def password(self, password: str):
        self._password = password

    @property
    def base_url(self) -> str:
        return self._base_url
    
    @base_url.setter
    def base_url(self, base_url: str):
        self._base_url = base_url
        self._set_urls()
