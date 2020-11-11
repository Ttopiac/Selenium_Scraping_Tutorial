from time import sleep
import requests
from bs4 import BeautifulSoup
# import pandas as pd
input = 'cleaned_raw.csv'
output = 'decathlon_final.csv'
def get_price(url):
    print(url)
    sleep(0.1)
    headers = {'User-Agent': 'Mozilla/5.0'}
    page = requests.get(url, headers = headers)
    print(page, )
    soup = BeautifulSoup(page.content, 'lxml')
    results = soup.find('span', class_='a-size-medium a-color-price priceBlockBuyingPriceString')
    print(results)
    if results:
        return results.string
    else:
        return ''
    #results = soup.find(text='DATE OF BIRTH')
# urls = ['https://www.worldathletics.org/athletes/athlete=305840', 'https://www.worldathletics.org/athletes/athlete=279278']
# for url in urls:
#     print(get_DOB(url))
def get_list_of_price(product_id):
    url = "https://www.amazon.com/gp/offer-listing/" + str(product_id) + "/"
    print(url)
    sleep(0.1)
    headers = {'User-Agent': 'Mozilla/5.0'}
    page = requests.get(url, headers = headers)
    print(page, )
    soup = BeautifulSoup(page.content, 'lxml')
    results = soup.find_all('span', class_='a-size-large a-color-price olpOfferPrice a-text-bold')
    print(results)
    if results:
        return [result.string.strip() for result in results]
    else:
        return ''

print(get_price("https://www.amazon.com/dp/B08BB9RWXD"))
print(get_list_of_price("B08BB9RWXD"))
print(get_list_of_price("B08L5M9BTJ"))

