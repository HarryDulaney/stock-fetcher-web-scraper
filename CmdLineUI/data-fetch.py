import requests

print()
print()
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token 39ac3ca9121471163ff7fe9bb6705e87a72b6352'
}
requestResponse = requests.get("https://api.tiingo.com/api/test/",
                               headers=headers)
message = requestResponse.json()
print(message)

print("Welcome to Stock Info Finder!")
print("---------------------------------")
print("Enter the Stock Symbol and date's you would like to fetch: ")

stockSymbol = str(input())

requestResponse = requests.get(
    "https://api.tiingo.com/tiingo/daily/aapl/prices?startDate=2019-01-02", headers=headers)
print(requestResponse.json())
