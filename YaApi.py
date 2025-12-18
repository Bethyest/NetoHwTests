import requests
import configparser


def add_token(token):
    config = configparser.ConfigParser()
    config.add_section('tokens')
    config.set('tokens', 'ya_disk', token)
    with open('settings.ini', 'w') as config_file:
        config.write(config_file)

def delete_token(text):
    with open('settings.ini', 'w') as f:
        f.write(text)

class YDConnector:

    def __init__(self, token):
        self.headers = {'Authorization': f'OAuth {token}'}
        self.base_url = 'https://cloud-api.yandex.net/v1/disk/resources'

    def create_folder(self, folder_name):
        params = {
            'path': folder_name
        }
        response = requests.put(self.base_url, params=params, headers=self.headers)
        print(response.status_code)
        return response


    def delete(self, path):
        params = {
            'path': path
        }
        response = requests.delete(self.base_url, params=params, headers=self.headers)
        print(response.status_code)
        return response


add_token('Enter your token')
config = configparser.ConfigParser()
config.read('settings.ini')
dogs_adder = YDConnector(config['tokens']['ya_disk'])
dogs_adder.create_folder('papka')
dogs_adder.delete('papka')
delete_token('Your token will be here')



