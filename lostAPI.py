import json
import requests
from lostark_api_token import Token

headers = {
    'accept': 'application/json',
    'authorization': Token
}

#url = 'https://developer-lostark.game.onstove.com/news/events'
url = 'https://developer-lostark.game.onstove.com/characters/엉루지/siblings'
response = requests.get(url, headers=headers)
jsonObject = response.json()

print(response)

for list in jsonObject :
    if list.get('ServerName') == '카단':
        print(list)
