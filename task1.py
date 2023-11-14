'''
    NAME : PRATHAM K GUJJAR
    PHASE 1:
        TASK 1:
            Create a csv dataset using python , pandas and any public api
    SOURCE OF PUBLIC API: GITHUB
'''
#IMPORTING THE NECESSSSARY LIBRARY
import json
import pandas as pd
import requests

#REQUESTING THE API AND GETTING THE DATA IN THE FORM OF JSON
url = 'https://api.coincap.io/v2/assets'
response = requests.get(url)
data = response.json()

#TAKING THE RELEVENT DATA FROM THE JSON FORMAT
coin=[]
for item in data['data']:
  coin_data={
      'Name': item['name'],
      'Symbol' : item['symbol'],
      'Market_Cap(USD)' : item['marketCapUsd'],
      'Price_(USD)': item['priceUsd'],
      'Percentage_Change': item['changePercent24Hr']
  }
  coin.append(coin_data)

# CREATING A DATAFRAME AND MAKE A CSV FILE
dataFrame=pd.DataFrame(coin)
dataFrame.to_csv('cryptocoins.csv', index=False)

print("CONGRADULATION YOU HAVE GOT IT DONE RIGHT!!!")
