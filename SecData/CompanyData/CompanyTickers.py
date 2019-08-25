import requests
import re
import psycopg2
from .GetCompanyData import SecData

ticker_text_file = '/Users/ricky/Documents/Python/SecData/CompanyData/Ticker.txt'
cik_text_file = '/Users/ricky/Documents/Python/SecData/CompanyData/CIK.txt'

ticker_tuples = []
cik_tuples = []

def create_ticker_tuples():
    with open(ticker_text_file) as ticker_file:
        line = ticker_file.readlines()

        # append cleaned up data stored as tuples
        for company in line:
            clean_data = company.replace('\t', ',').replace('\n', ' ').split(',')
            ticker = clean_data[0].strip().upper()
            cik = clean_data[1].strip()
            ticker_tuples.append((ticker, cik))

def create_cik_tuples():
    with open(cik_text_file) as cik_file:
        line = cik_file.readlines()

        # append cleaned up data as tuples
        for company in line:
            clean_data = company.replace('\t', ',').replace('\n', ' ').split(':')
            company_name = clean_data[0].strip()
            cik = clean_data[1].strip()
            cik_tuples.append((cik, company_name))



