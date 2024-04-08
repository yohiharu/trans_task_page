#!/usr/bin/python3

import os
from os.path import join, dirname
from dotenv import load_dotenv

def return_apikey():
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    API_KEY = os.environ.get("API_KEY")
    return API_KEY

if __name__ ==  "__main__":
    output = return_apikey()
    print(output)
