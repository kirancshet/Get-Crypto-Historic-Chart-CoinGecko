
import requests
import os
import json
import time
from random import randint
from datetime import datetime
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt

API_URL = r"https://pro-api.coingecko.com/api/v3/" #Premium Account API URL
API_URL = r"https://api.coingecko.com/api/v3/" # Free Account API URL

#---------------------------------------
#   Convert Date to UNIX Timestamp
#---------------------------------------
def populate_date(date1):

    if isinstance(date1, datetime):                        
        return int(time.mktime(date1.timetuple()))

    elif isinstance(date1, str):            
        date2 = parse(date1)
        return  int(time.mktime(date2.timetuple()))

    return None
  
#-------------------------------------------------
#   Fetch Historical Market Price of a crypto via 
#   CoinGecko
#-------------------------------------------------
def get_historic_price(token:str, start_date:str, end_date:str)->list:
    url = f"{API_URL}/coins/{token}/market_chart/range"

    data = {} #Populate Parameters     
    data['vs_currency'] = 'usd'
    data['from']= populate_date(start_date)  #Convert Date to UNIX Timestamp
    data['to']  = populate_date(end_date)        
    
    headers = {}       
    headers['Content-type'] = 'application/json'
    #headers['x_cg_pro_api_key'] = settings.API_KEY
    
    response = requests.get(url, headers=headers, params=data)

    crypto_info = response.json()
    #print(json.dumps(crypto_info, indent=4))

    crypto_prices = []
    for ind in crypto_info['prices']:
        temp = []            
        date1 = datetime.fromtimestamp(ind[0]/1000.0)
        temp.extend([date1, ind[1]])
        crypto_prices.append(temp)

    return crypto_prices


#-------------------------------------------------
#   Fetch Historical Market Price of a crypto via 
#   CoinGecko for last 12 months and draw a line chart
#-------------------------------------------------

def create_line_chart(token_list):
        
    #crypto_prices should be  lower case
    end_date = datetime.now()
    start_date = end_date - relativedelta(years=1)

    crypto_price = {}
    for token in token_list:           
        crypto_price[token] = get_historic_price(token, start_date, end_date)

    for crypto, prices in crypto_price.items():
        x_axis = [ind[0] for ind in prices] #Date
        y_axis = [ind[1] for ind in prices] #Crypto Prices

        plt.plot(x_axis, y_axis, label=crypto)

    plt.legend() #Show Legend
    plt.title('Crypto Line Chart', fontsize=18) # Add Chart Title
    plt.xlabel('Date', fontsize=12) # Add X-Axis 
    plt.ylabel('Price', fontsize=12) # Add Y-Axis 
    #plt.show() # Show the chart on the screen   

    rand_num = randint(100_000,999_999)
    image_file = f"{os.getcwd()}/output/crpto_chart_{rand_num}.png"

    plt.savefig(image_file, bbox_inches='tight') #Save the chart as an image



token_list = ['bitcoin','ethereum', 'tether', 'usd-coin', 'dogecoin']
create_line_chart(token_list)