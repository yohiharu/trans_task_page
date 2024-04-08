#!/usr/bin/python3

import requests

from get_key import return_apikey

API_KEY = return_apikey()

def translation(key, text, target_lang):
    data = {
            'auth_key' : key,
            'text' : text,
            'source_lang' : "JA",
            "target_lang": target_lang
            }
    r = requests.post("https://api-free.deepl.com/v2/translate", data=data)
    j = r.json()
    translated_sentence = j["translations"][0]["text"]
    return translated_sentence
