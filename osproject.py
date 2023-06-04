# AmirHossein Mokhbery      9911323

import requests
import threading
import pandas
import time
from bs4 import BeautifulSoup

myList = []
listNames = []
listPrice = []
data = {}


def fun1():
    
    url = 'https://mobo.news/pricelist/'
    
    # Send an HTTP request to the website and get the HTML content
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Selects all the html tags in the details-phone-price class and adds them to the listPrice
        price = soup.select('.details-phone-price')
        for i in price:
            listPrice.append(int(i.text.replace(",",'').replace("تومان"," ").replace('\n' , "").replace("                                     ","")))
        
        # Selects all the html tags in the title-phone-span class and adds them to the listNames
        name = soup.select('.title-phone-span')
        for i in name:
            listNames.append(i.text)
        
        # Convert the listPrice and listNames into a dictionary
        data = dict(list(zip(listNames,listPrice)))
        
        # Convert dictionary to dataframe
        df = pandas.DataFrame(list(data.items()), columns=['name', 'Price'])         
        
        print(df)
        
        # find the most expensive and cheapest phone and the average of phones, using `max', `min' and `mean' functions
        most_expensive_phone = df.loc[df['Price'].idxmax()]
        cheapest_phone = df.loc[df['Price'].idxmin()]
        average_price = df['Price'].mean()
        
        print('Most expensive phone:', most_expensive_phone['name'], most_expensive_phone['Price'])
        print('Cheapest phone:', cheapest_phone['name'], cheapest_phone['Price'])
        print('Average price:', average_price)
        print("--------------------------------------------------------")
        
    else:
        print(f'Request failed with status code {response.status_code}')


def fun2():
    
    url = 'https://www.mobile.ir/phones/prices.aspx'

    # Send an HTTP request to the website and get the HTML content
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Selects all the html tags in the price class and adds them to the listPrice
        price = soup.select('.price')
        for i in price:
            listPrice.append(i.text.replace(",",''))
        
        # Selects all the html tags in the phone class and adds them to the listNames
        name = soup.select('.phone')
        for i in name:
            listNames.append(i.text)
        
        # Convert the listPrice and listNames into a dictionary
        data = dict(list(zip(listNames,listPrice)))
        
        # Convert dictionary to dataframe    
        df = pandas.DataFrame(list(data.items()), columns=['name', 'Price'])
        # convert the phone price column to an integer , errors='coerce' means to convert invalid errors to NaN        
        df['Price'] = pandas.to_numeric(df['Price'], errors='coerce')
        # Remove rows containing NaN using dropna function
        df.dropna(subset=['Price'], inplace=True)
        
        print(df)
        
        # find the most expensive and cheapest phone and the average of phones, using `max', `min' and `mean' functions
        most_expensive_phone = df.loc[df['Price'].idxmax()]
        cheapest_phone = df.loc[df['Price'].idxmin()]
        average_price = df['Price'].mean()
        
        print('Most expensive phone:', most_expensive_phone['name'], most_expensive_phone['Price'])
        print('Cheapest phone:', cheapest_phone['name'], cheapest_phone['Price'])
        print('Average price:', average_price)
        print("--------------------------------------------------------")
        
    else:
        print(f'Request failed with status code {response.status_code}')


def fun3():
    
    url = 'https://www.mobile.ir/phones/prices.aspx?page=2'
    
    # Send an HTTP request to the website and get the HTML content
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Selects all the html tags in the price class and adds them to the listPrice
        price = soup.select('.price')
        for i in price:
            listPrice.append(i.text.replace(",",''))
        
        # Selects all the html tags in the phone class and adds them to the listNames
        name = soup.select('.phone')
        for i in name:
            listNames.append(i.text)
        
        # Convert the listPrice and listNames into a dictionary
        data = dict(list(zip(listNames,listPrice)))
        
        # Convert dictionary to dataframe    
        df = pandas.DataFrame(list(data.items()), columns=['name', 'Price'])
        # convert the phone price column to an integer , errors='coerce' means to convert invalid errors to NaN         
        df['Price'] = pandas.to_numeric(df['Price'], errors='coerce')
        # Remove rows containing NaN using dropna function
        df.dropna(subset=['Price'], inplace=True)
        
        print(df)
        
        # find the most expensive and cheapest phone and the average of phones, using `max', `min' and `mean' functions
        most_expensive_phone = df.loc[df['Price'].idxmax()]
        cheapest_phone = df.loc[df['Price'].idxmin()]
        average_price = df['Price'].mean()
        
        print('Most expensive phone:', most_expensive_phone['name'], most_expensive_phone['Price'])
        print('Cheapest phone:', cheapest_phone['name'], cheapest_phone['Price'])
        print('Average price:', average_price)
        print("--------------------------------------------------------")
        
    else:
        print(f'Request failed with status code {response.status_code}')


def main():
    
    # The current time when the code below executes
    start = time.time()
    fun1()
    fun2()
    fun3()
    # The current time when the code below executes
    end = time.time()
    
    print("============================================================")
    print("time : ",end - start)
          
        
if __name__ == '__main__':
    main()
