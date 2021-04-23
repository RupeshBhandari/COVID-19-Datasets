import requests
import json
import pandas as pd
import os
import time
from datetime import datetime
import datetime as dt
# Countries:
countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Anguilla', 'Antigua-and-Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia-and-Herzegovina', 'Botswana', 'Brazil', 'British-Virgin-Islands', 'Brunei', 'Bulgaria', 'Burkina-Faso', 'Burundi', 'Cabo-Verde', 'Cambodia', 'Cameroon', 'Canada', 'CAR', 'Caribbean-Netherlands', 'Cayman-Islands', 'Chad', 'Channel-Islands', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Costa-Rica', 'Croatia', 'Cuba', 'Cura&ccedil;ao', 'Cyprus', 'Czechia', 'Denmark', 'Diamond-Princess', 'Diamond-Princess-', 'Djibouti', 'Dominica', 'Dominican-Republic', 'DRC', 'Ecuador', 'Egypt', 'El-Salvador', 'Equatorial-Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Faeroe-Islands', 'Falkland-Islands', 'Fiji', 'Finland', 'France', 'French-Guiana', 'French-Polynesia', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hong-Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Isle-of-Man', 'Israel', 'Italy', 'Ivory-Coast', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall-Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'MS-Zaandam', 'MS-Zaandam-', 'Myanmar', 'Namibia', 'Nepal', 'Netherlands', 'New-Caledonia', 'New-Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North-Macedonia', 'Norway', 'Oman', 'Pakistan', 'Palestine', 'Panama', 'Papua-New-Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto-Rico', 'Qatar', 'R&eacute;union', 'Romania', 'Russia', 'Rwanda', 'S-Korea', 'Saint-Kitts-and-Nevis', 'Saint-Lucia', 'Saint-Martin', 'Saint-Pierre-Miquelon', 'Samoa', 'San-Marino', 'Sao-Tome-and-Principe', 'Saudi-Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra-Leone', 'Singapore', 'Sint-Maarten', 'Slovakia', 'Slovenia', 'Solomon-Islands', 'Somalia', 'South-Africa', 'South-Sudan', 'Spain', 'Sri-Lanka', 'St-Barth', 'St-Vincent-Grenadines', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Trinidad-and-Tobago', 'Tunisia', 'Turkey', 'Turks-and-Caicos', 'UAE', 'Uganda', 'UK', 'Ukraine', 'Uruguay', 'US-Virgin-Islands', 'USA', 'Uzbekistan', 'Vanuatu', 'Vatican-City', 'Venezuela', 'Vietnam', 'Wallis-and-Futuna', 'Western-Sahara', 'Yemen', 'Zambia', 'Zimbabwe']

url = "https://covid-193.p.rapidapi.com/history"
headers = {
    'x-rapidapi-key': "fd544906eemsh58b064f09dbc569p1183abjsn8777ff646fd4",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

# Date Operations
dates = []

dt1 = dt.datetime(2020, 6, 12)
dt2 = dt.datetime(2020, 12, 30)
delta = dt2 - dt1

for i in range(0, delta.days):
    dt1 = dt1 + dt.timedelta(1)
    date_time = dt1.strftime("%Y-%m-%d")
    dates.append(date_time)   
    




cases = []
deaths = []
try:
    for date in dates:
        for country in countries:
            querystring = {"country":f"{country}","day":f"{date}"}
            response = requests.request("GET", url, headers=headers, params=querystring)
            d = response.json()
            # print(d['response'])
            # CHeck for files:
            if os.path.exists(f'{country}'):
                pass
            else:
                os.mkdir(f'{country}')
                os.mkdir(f'{country}/cases')
                os.mkdir(f'{country}/deaths')
            for i in d['response']:
                cases.append(i['cases'])
                deaths.append(i['deaths'])
                df_cases = pd.DataFrame(cases)
                df_deaths = pd.DataFrame(deaths)
                with open(f"{country}/cases/{querystring['day']}.md", 'w') as f:
                    f.write(df_cases.to_markdown())
                    print(f"{country} 's cases for {date} is done!")
                with open(f"{country}/deaths/{querystring['day']}.md", 'w') as f:
                    f.write(df_deaths.to_markdown())
                    print(f"{country} 's deaths for {date} is done!")
            os.system('git add .')
            os.system("git commit -m 'update'")
            os.system('git push')
            print(f"{country}'s data updated in Git Repo")        
            time.sleep(20)
finally:
    os.system('git add .')
    os.system("git commit -m 'update'")
    os.system('git push')
