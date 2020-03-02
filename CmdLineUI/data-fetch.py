import requests
import pandas as pd
from pandas.io.json import json_normalize


print()
print()
# Test api connection and print affirmation
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token 39ac3ca9121471163ff7fe9bb6705e87a72b6352'
}
requestResponse = requests.get("https://api.tiingo.com/api/test/",
                               headers=headers)
responseDict = requestResponse.json()
if responseDict.get('message') == 'You successfully sent a request':
    print('***Connection established, ready to get stock data!****')

print()

print("Welcome to Stock Info Finder!")
print("-------------------------------------------------------------------------a--")
print("Enter the Ticker Symbol for the stock you would like to fetch: ")
ticker = str(input())

print("Enter the start date like this: 2019-01-02")
start_date = str(input())

print("Enter the end date like this: 2020-01-02")
end_date = str(input())

resturl = "https://api.tiingo.com/tiingo/daily/{}/prices?startDate={}&endDate={}"

requestResponse = requests.get(resturl.format(
    ticker, start_date, end_date), headers=headers)

ready_data = requestResponse.__reduce__()

json_normalize(ready_data)
