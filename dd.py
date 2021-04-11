import requests
import json
import pandas as pd
import os

url = "https://covid-193.p.rapidapi.com/history"

querystring = {"country":"usa","day":"2020-06-02"}

headers = {
    'x-rapidapi-key': "fd544906eemsh58b064f09dbc569p1183abjsn8777ff646fd4",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

d =response.json()
r = json.dumps(d, indent=6)


with open('data.json', 'w') as f:
    json.dump(d, f)

os.system('git add .')
os.system("git commit -m 'update'")
os.system('git push')