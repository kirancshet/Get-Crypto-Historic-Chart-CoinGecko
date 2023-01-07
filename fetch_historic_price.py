#-------------------------------------------------------------------------------
# Name      :   fetch_historic_price.py
# Purpose   :   This Python script takes crypto tokens and 
#               fetch historic data via CoinGecko in Python
# Author    :   Kiran Chandrashekhar
# Webste    :   https://sapnaedu.com
# Created   :   26-Dec-2022
#-------------------------------------------------------------------------------

import conf as settings
import requests
import json
import time
from datetime import datetime
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta

#---------------------------------------------------------
#   Fetch Historic Market Price of a crypto from CoinGecko
#   Get the API Key here: https://CoinGecko.com/
#   Please refer to the complete API documentation here: 
#   https://www.coingecko.com/en/api
#---------------------------------------------------------

class Crypto_Historic_Price:
    def __init__(self, currency='usd'):
        self.currency = currency.lower()
        self.base_url = r'https://pro-api.coingecko.com/api/v3'  #Premium Account API URL
        self.base_url = r'https://api.coingecko.com/api/v3'      #Free Account  
    
    #---------------------------------------
    #   Convert Date to UNIX Timestamp
    #---------------------------------------
    def populate_date(self, date1):
     
        if isinstance(date1, datetime):                        
            return int(time.mktime(date1.timetuple()))

        elif isinstance(date1, str):            
            date2 = parse(date1)
            return  int(time.mktime(date2.timetuple()))

        return None
  

    #-------------------------------------------------
    #   Fetch Historic Market Price of a crypto via 
    #   CoinGecko
    #-------------------------------------------------
    def get_historic_price(self, token:str, start_date:str, end_date:str)->list:
        url = f"{self.base_url}/coins/{token}/market_chart/range"

        data = {} #Populate Parameters     
        data['vs_currency'] = self.currency
        data['from']= self.populate_date(start_date)
        data['to']  = self.populate_date(end_date)        
        
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
  

def main():
    
    obj = Crypto_Historic_Price(currency='USD')
    token = 'bitcoin'
    end_date = datetime.now()
    start_date = end_date - relativedelta(years=1)
    price = obj.get_historic_price(token, start_date, end_date)
    
    print(price)

   
    
if __name__ == '__main__':
    main()
    print("Done")