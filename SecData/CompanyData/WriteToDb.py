from CompanyData.db_connection import DbConnections


ticker_text_file = '/Users/ricky/Documents/Python/Accessing-SEC-EDGAR-Data/SecData/CompanyData/Ticker.txt'
cik_text_file = '/Users/ricky/Documents/Python/Accessing-SEC-EDGAR-Data/SecData/CompanyData/CIK.txt'


def create_ticker_tuples():
    ticker_tuples = []

    with open(ticker_text_file) as ticker_file:
        line = ticker_file.readlines()

        # append cleaned up data stored as tuples
        for company in line:
            clean_data = company.replace('\t', ',').replace('\n', ' ').split(',')
            ticker = clean_data[0].strip().upper()
            cik = clean_data[1].strip()
            ticker_tuples.append((cik, ticker))

    return ticker_tuples

def create_cik_tuples():
    cik_tuples = []

    with open(cik_text_file) as cik_file:
        line = cik_file.readlines()

        # append cleaned up data as tuples
        for company in line:
            clean_data = company.replace('\t', ',').replace('\n', ' ').split(':')
            company_name = clean_data[0].strip()
            cik = clean_data[1].strip()

            try:
                cik_tuples.append((int(cik), company_name))
            except Exception as err:
                # print(err)
                pass

    return cik_tuples

create_cik_tuples()
db = DbConnections('CompanyData')
# db.write_data('stockticker', create_ticker_tuples())
db.write_data('ciknames', create_cik_tuples())


