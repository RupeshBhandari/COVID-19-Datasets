import requests
import json
import pandas as pd

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "fd544906eemsh58b064f09dbc569p1183abjsn8777ff646fd4",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }


x = json.loads(requests.request("GET", url, headers=headers).text)
# print (json.dumps(x, indent=5))

d = x['response']
print(d)
df = pd.DataFrame(d)
print(df['tests'])

df.to_csv('dd.csv')
