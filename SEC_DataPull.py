import urllib.request
import shutil
import collections


# Documentation url: https://www.sec.gov/edgar/searchedgar/accessing-edgar-data.htm
# JSON url: https://www.sec.gov/Archives/edgar/full-index/index.json

class SecDirectory:
    """Class to create different index requests to SEC data website

    sec_url: The url request including the index file requested
    sec_archieves_url: The url path to the archivies. Concatenate with the file path in the index file.

    """

    def __init__(self, sec_index):
        self.sec_url = "https://www.sec.gov/Archives/edgar/full-index/" + sec_index + ".idx"
        self.sec_archieves_url = "https://www.sec.gov/Archives/"

    def url_request(self, text_file):
        # Retrieve data from SEC website and store it in a text file
        with urllib.request.urlopen(sec_url) as response, open(text_file, 'wb') as file:
            shutil.copyfileobj(response, file)

# -------------------------------------------------------------------------------
# SEC urls to data text files
sec_url = "https://www.sec.gov/Archives/edgar/full-index/form.idx"
sec_archieves_url = "https://www.sec.gov/Archives/"


# File path to the text file we will write to and read from
text_file_path = "C:/Users/Ricardo/Downloads/SEC_Test.txt"

# Retrieve data from SEC website and store it in a text file
with urllib.request.urlopen(sec_url) as response, open(text_file_path, 'wb') as file:
    shutil.copyfileobj(response, file)

# Store the text data in a file object
data = open(text_file_path, 'r')

# -------------------------------------------------------------------------------
# List variables that will hold the data from the data pull 
financial_filings = [] # stores only the lines in the text file with 10-Q or 10-K in the line
filings_lists = [] # stores elements in financial_filings as individual lists

# -------------------------------------------------------------------------------
# Loop through the text file, any line that has 10-Q or 10-K characters in it are stored in a list
for line in data:
    if '10-K' in line or '10-Q' in line:
        financial_filings.append(line)

# -------------------------------------------------------------------------------
# Loop through the 10-Q and 10-K list and split the string element so that each element is stored as a list
for filing in financial_filings:
    filings_lists.append(filing.split())


filings_attributes = ['form_type', 'cik', 'date_filed', 'file']
CompanyFiling = collections.namedtuple('CompanyFiling', ' '.join(filings_attributes))
final_filings_list = []
cik_id = set()

# -------------------------------------------------------------------------------
# Loop through the filings_list list and convert to a named tuple
for item in filings_lists:
    if item[0] in '10-Q' or item[0] in '10-K': # Filters out companies that have 'NT' in the string (more than likely a foreign company)
        cik_identifier = item[-3]
        cik_id.add(cik_identifier)# CIK number in list
        cik_identifier = CompanyFiling(item[0],
                                       item[-3],
                                       item[-2],
                                       item[-1])
        final_filings_list.append(cik_identifier)

##for filing in final_filings_list:
##    print(filing.cik, filing.form_type, str(sec_archieves_url + filing.file))
        
