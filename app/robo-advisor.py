# app/robo_advisor.py
import csv
import json
from datetime import datetime
import os

import requests
import dotenv



def to_usd(my_price):
    return "${0:,.2f}".format(my_price)


now = datetime.now()
request_time = now.strftime("%Y/%m/%d %H:%M:%S")

request_url ="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo"
response = requests.get(request_url)

#print(type(response))
#print(response.status_code)
#print(response.text)

parsed_response = json.loads(response.text)
tsd = parsed_response["Time Series (Daily)"]

dates = list(tsd.keys()) #TODO : sort to make sure the data is chronological


latest_day = dates[0]
last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
latest_close = tsd[latest_day]["4. close"]


#get the high price from each day
high_prices = []
low_prices = []
for d in dates:
    high_price = tsd[d]["2. high"]
    high_prices.append(float(high_price))
    
    #low prices now
    low_price = tsd[d]["3. low"]
    low_prices.append(float(low_price))
    pass

#maximum of all the high prices
recent_high = max(high_prices)

#minimum of all the low prices
recent_low = min(low_prices)
#breakpoint()


#quit()

symbol = "0"
symbol_list =[]
while symbol != "done":
    
    symbol = input("Please enter the stock symbols of your choice. When done, type 'done': ")
    
    if float(len(symbol)) <= 5 and symbol.isalpha():
        symbol_list.append(symbol)
        pass
    else:
        print("Error: Please enter a valid stock symbol")
        pass    
        
    
    
    
    pass    

symbol_list.remove("done")


csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")

with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=["city", "name"])
    writer.writeheader() # uses fieldnames set above
    writer.writerow({"city": "New York", "name": "Yankees"})
    writer.writerow({"city": "New York", "name": "Mets"})
    writer.writerow({"city": "Boston", "name": "Red Sox"})
    writer.writerow({"city": "New Haven", "name": "Ravens"})





print("-------------------------")
print("SELECTED SYMBOLS: ", symbol_list)
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: ", request_time)
print("-------------------------")
print("LATEST DAY: ", last_refreshed)
print("LATEST CLOSE: ", to_usd(float(latest_close)))
print("RECENT HIGH: ", to_usd(float(recent_high)))
print("RECENT LOW: ", to_usd(float(recent_low)))
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("WRITING DATA TO CSV: ", csv_file_path)
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")

#csv_file_path = "data/prices.csv" # a relative filepath

