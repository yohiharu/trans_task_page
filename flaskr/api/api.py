#!/usr/bin/python3

import requests

from api.get_key import return_apikey

API_KEY = return_apikey()

def translation(text, target_lang):
    data = {
            'auth_key' : API_KEY,
            'text' : text,
            'source_lang' : "JA",
            "target_lang": target_lang
            }
    r = requests.post("https://api-free.deepl.com/v2/translate", data=data)
    j = r.json()
    translated_sentence = j["translations"][0]["text"]
    return translated_sentence
