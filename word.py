import requests
import http.client
import json
import urllib.parse
import os
from dotenv import load_dotenv
load_dotenv()
# NESTED LOOPS
# https://www.youtube.com/watch?v=oQfNYqz8pLs

apikey = os.environ.get('XRapidAPIKey')
apihost = os.environ.get('XRapidAPIHost')


url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
print('Enter word to find')
word_to_find = input()
querystring = {"term": f"{word_to_find}"}

headers = {
    "X-RapidAPI-Key": f"{apikey}",
    "X-RapidAPI-Host": f"{apihost}"
}


response = requests.request("GET", url, headers=headers, params=querystring)
json_data = response.json()
with open('personal.json', 'w') as json_file:
    json.dump(json_data, json_file, indent=4, sort_keys=True)
json_data_value_content = json_data['list']
# print(json_data_value_content[1])

# PRINT FIRST ONLY
first_meaning = json_data_value_content[1]
print(first_meaning['definition'])


# for definition in json_data_value_content:
#     print(definition['definition'])
#     print('---------------------')
