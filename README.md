# Get Historical MarketPrice from CoinGecko in Python

Python script takes a list of crypto tokens and fetch Historic data via CoinGecko REST API in Python

## Table of Contents

- [Description](#description)
- [Prerequisites](#prerequisites)
- [Project Structure](#structure)
- [Usage](#usage)
- [Contact](#contact)

## Description <a name = "description"></a>

This Python takes a list of tokens and fetch Historic data for the last 1 year. We shall fetch the Historic data via CoinGecko API. Once the data is downloaded, we will display the data as a line-graph chart in Python

### Prerequisites <a name = "prerequisites"></a>

- Add your CoinGecko API key in the conf.py
- Install requests and matplotlib library via `pip`

    `pip install requests matplotlib`
  
## Usage <a name = "usage"></a>

python generate_crypto_chart.py


## Project Structure  <a name = "structure"></a>

The entire project follows the below folder structure:

    .
    ├── conf.py                             # CoinGecko Configuration File
    ├── fetch_historic_price.py             # Fetch Historic crypto price via CoinGecko API
    ├── generate_crypto_chart.py            # Generate line-chart of list of Crypto tokens
    └── README.md


## Contact <a name = "contact"></a>

Follow me for more updates here:

- [Article](https://sapnaedu.com/how-to-send-sms-via-vonage-in-python/)
- [Twitter](https://twitter.com/sapnaedu)
- [Website](https://www.sapnaedu.com)
- [LinkedIn](https://www.linkedin.com/in/kiranchandrashekhar/)
- [Email](mailto:kiran.chandrashekhar@gmail.com)
