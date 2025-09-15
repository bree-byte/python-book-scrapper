
# Let us start by importing every library needed for the project
import requests
from bs4 import BeautifulSoup
import json

# Scrape products
url = "https://books.toscrape.com/"
response = requests.get(url)# we are getting everything from the above website
soup = BeautifulSoup(response.text, 'html.parser')
#print(soup)
products = soup.find_all('article', class_='product_pod')[:10]
#print(products)

data = [] #lets create an empty list and assign it to data
for product in products:
    name = product.find('h3').find('a')['title'].strip()
    price_str = product.find('p', class_='price_color').text.strip()
    #print(price_str)
    price_gbp = float(price_str.replace('Â£', ''))  #converting the price written to a number hence remove the GBP sign
    print(type(price_gbp))##experienced an error trying to convert to KES
    data.append({'name': name, 'price_gbp': price}) #create the library of this and assigning it to data
    #print(data)

# I will be using the exchange rate api to get the api key
#I put the api key in the .env file

def get_currency():
    url = f"https://v6.exchangerate-api.com/v6/1f8ecc6fdcbd5ea7d6ff3413/latest/USD"
    response = requests.get(url)
    if response.status_code == 200:
        data2 = response.json()
        kes_rate = data2.get('conversion_rates', {}).get('KES')
        if kes_rate:
            return f"The exchange rate from GBP to KES is {kes_rate} at {data2['time_last_update_utc']}."
        else:
            return "Exchange for KES not found"
    else:
        return "Could not retrieve the exchange rate information."

print(get_currency())# to see the exchange rate as at the time you are running this

#let us loop through the data we had established
for book in data:
    book['price_kes'] = round(book['price_gbp'] * 129.235, 2)  # Adds key to book dict!

print(f"Books_prices (KES): {[book['price_kes'] for book in data]}")#update data with the new currency price and assigning it to variable price_kes
#open or create a file, with a file name as books_prices.json → the filename.
# w is writing mode ,use utf-8 to make sure special characters are saved correctly

with open("books_prices.json", "w", encoding="utf-8") as f:# f is the variable name for the opened file
#data is the list we had created up there,f is the opened file,indent is spacing for readability and ensure_ascii is so that the money symbols can also be written
    json.dump(data, f, indent=4, ensure_ascii=False)

print(" Data is saved to books_prices.json")

print('To be continued with the other optional work for the project')
