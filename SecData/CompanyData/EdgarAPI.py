import requests
import json
import os
from dotenv import load_dotenv

class FinancialData:

    @staticmethod
    def get_api_key():
        env_path = os.path.join(os.path.dirname(__file__), '.env')
        load_dotenv(env_path)
        edgar_api = os.environ.get('edgar_key')

        return edgar_api

    def __init__(self, period):
        self.period = period

    def request_data(self, company_ticker):
        url = 'https://datafied.api.edgar-online.com/v2/corefinancials/{period}.json?primarysymbols={ticker}&appkey={key}'.format(period=self.period, ticker=company_ticker, key=self.get_api_key())
        response = requests.get(url)
        data = json.loads(response.text)

        for item in data['result']['rows']: # [0]['values']
            for value in item['values']:
                print(value)


annual = FinancialData('ann')
# annual.request_data('MSFT')
quarterly = FinancialData('qtr')
quarterly.request_data('MSFT')






