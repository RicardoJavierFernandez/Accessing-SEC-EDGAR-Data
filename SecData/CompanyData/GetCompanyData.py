import requests


class SecData:

    def __init__(self):
        self.ticker_url = 'https://www.sec.gov/include/ticker.txt'
        self.cik_url = 'https://www.sec.gov/Archives/edgar/cik-lookup-data.txt'

    def get_ticker_data(self):
        # Make a request to the SEC website and store the data for Ticker and CIK
        ticker_request = requests.get(self.ticker_url)
        ticker_data = ticker_request.text

        return ticker_data

    def get_cik_data(self):
        # Make a request to the SEC website and store data for CIK and company name
        cik_request = requests.get(self.cik_url)
        cik_data = cik_request.text

        return cik_data

    def write_to_text_file(self):

        # Name the file path of the text files
        ticker_text_file = '/Users/ricky/Documents/Python/SecData/CompanyData/Ticker.txt'
        cik_text_file = '/Users/ricky/Documents/Python/SecData/CompanyData/CIK.txt'

        # Write the data to the text files
        with open(ticker_text_file, 'w') as file1:
                file1.write(self.get_ticker_data())
        with open(cik_text_file, 'w') as file2:
            file2.write(self.get_cik_data())



