import requests
from lostark_api_token import Token

headers = {
        'accept': 'application/json',
        'authorization': Token
    }
def getJsonObjectFromResponse(url):
    response = requests.get(url, headers=headers)
    jsonObject = response.json()
    return jsonObject

def getCharacterInfo(character_name):
    url = f'https://developer-lostark.game.onstove.com/characters/{character_name}/siblings'
    jsonObject = getJsonObjectFromResponse(url)
    return jsonObject

def getArmories(character_name, details = None):
    url = f'https://developer-lostark.game.onstove.com/armories/characters/{character_name}/{details}'
    jsonObject = getJsonObjectFromResponse(url)
    return jsonObject
