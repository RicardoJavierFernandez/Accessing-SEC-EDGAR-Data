import requests
import json
import os
from dotenv import load_dotenv

class FinancialData:

    def __init__(self, period):
        self.period = period

    @staticmethod
    def get_api_key():
        env_path = os.path.join(os.path.dirname(__file__), '.env')
        load_dotenv(env_path)
        edgar_api = os.environ.get('edgar_key')

        return edgar_api

    def request_data(self, company_ticker):
        url = 'https://datafied.api.edgar-online.com/v2/corefinancials/{period}.json?primarysymbols={ticker}&appkey={key}'.format(period=self.period, ticker=company_ticker, key=self.get_api_key())
        response = requests.get(url)
        data = json.loads(response.text)

        for item in data['result']['rows']:  # [0]['values']
            for value in item['values']:
                print(value)


annual = FinancialData('ann')
# annual.request_data('MSFT')
quarterly = FinancialData('qtr')
# quarterly.request_data('MSFT')


# Test to see if we can make multiple requests
def multiple_companies_data(object):
    company_tickers = ['AAPL', 'MSFT', 'BA']

    for company in company_tickers:
        object.request_data(company)

# multiple_companies_data(quarterly)







