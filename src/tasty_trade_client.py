import requests

class TastyTradeClient():
    def __init__(self, username, password, url = 'https://api.tastyworks.com'):
        self.session_token = None
        self.username = username
        self.password = password
        self.url = url
    
    def create_session(self):
        response = requests.post(f'{self.url}/sessions', json={
            'login': self.username,
            'password': self.password,
            'remember_me': False,
            'remember_token': 'remember_token'
        })
        self.session_token = response.json()['data']['session-token']
        return self.session_token
    
    def get_equity_option_chains(self, symbol):
        if not self.session_token:
            self.create_session()
        response = requests.get(f'{self.url}/option-chains/{symbol}/nested', headers={
            'Authorization': self.session_token
        })

        return response.json()
    
    def get_futures_option_chains(self, symbol):
        if not self.session_token:
            self.create_session()
        response = requests.get(f'{self.url}/futures-option-chains/{symbol}/nested', headers={
            'Authorization': self.session_token
        })

        return response.json()