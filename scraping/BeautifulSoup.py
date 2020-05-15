'''
Cool snippets that may help in the future.
Beautiful Soup is a tool to analyze html/xml documents.
Mostly used for scraping data from the web.
'''
import os
import csv
import requests
from lxml import html
from datetime import datetime
from bs4 import BeautifulSoup

months = {"Jan":'01',"Feb":'02',"Mar":'03',"Apr":'04',
          "May":'05', "Jun":'06', "Jul":'07',"Aug":'08',
          "Sep":'09', "Oct":'10', "Nov":'11', "Dec":'12'}

## Function that reformats date
def date_formatting(date):
    date = date.replace('th', '').replace('st','').replace('nd','').replace('rd','').split(' ')
    date[1] = months[date[1]]
    if int(date[0]) < 10: date[0] = '0' + date[0]
    return '/'.join(date)

# Function that takes url of a token, and return all required data
def get_token_data(url):

    # Requesting a page for a token
    page = requests.get(url)
    tree = html.fromstring(page.content)
    soup = BeautifulSoup(page.content, 'html.parser')

    ## Checking if the page is available
    try:
        if tree.xpath(PAGE_NOT_FOUND) == ['404']:
            return None
    except:
        pass

    # Retrieving rating
    suspicious_block_check = soup.findAll('div', {'class': 'class_name'})
    if len(suspicious_block_check):
        rating = tree.xpath(XPATH)[0]
    else:
        rating = tree.xpath(XPATH)[0]

    # Retrieving token Name
    try: token_name = tree.xpath(XPATH)[0]
    except:
        try: token_name = tree.xpath(XPATH)[0]
        except: token_name = 'Unknown'

    # Retrieving Main table
    raw_first_table = soup.findAll('div', {'class': CLASS_NAME})[1:]
    first_table = []
    for row in raw_first_table:
        first_table.append(row.text.replace('\n','').replace('\t','').strip().replace(';',''))

    # Retrieving Financial table (divide to left and right block)
    financial_table = []
    
    # Retrieving left block of Financial table
    raw_financial_table_left = soup.findAll(class_=TABLE_FINANCIAL_CLASS_LEFT)[0]
    for row in raw_financial_table_left:
        if row in ['\n', ' ']:
            continue
        for subrow in row:
            if subrow in [' ', 'Token info', 'No info on token.']:
                continue
            if subrow.text in ['']:
                continue
            if subrow.text == 'Type':
                financial_table.append('Type - Financial')
                continue
            financial_table.append(subrow.text.replace('\n','').replace('\t','').strip().replace(';',''))
    
    # Retrieving right block of Financial table
    raw_financial_table_right = soup.findAll(class_=TABLE_FINANCIAL_CLASS_RIGHT)[0]
    for row in raw_financial_table_right:
        if row in ['\n', ' ']:
            continue
        for subrow in row:
            if subrow in [' ', 'Investment info', 'No additional info.']:
                continue
            financial_table.append(subrow.text.replace('\n','').replace('\t','').strip().replace(';',''))

    # Returning data from both tables + rating value
    return first_table + financial_table + ['Rating', rating, 'Token Name', token_name]

# Generating a name for output file as a timestamp
# Format: day(int) month(str) year(int)

date = datetime.now()
output_file = '{}_{}_{}_{}:{}.csv'.format(
    str(date.day), MONTHS[date.month - 1], str(date.year), str(date.hour), str(date.minute))

# Creating the file
with open(output_file, 'a') as f:
    first = True
    writer = csv.writer(f)
    iterations = 1

    try:  # Going through each page of search page
            
        for i in range(startPage, endPage + 1):
            token_list_page = requests.get(
                SEARCH_URL[:31] + str(i) + SEARCH_URL[31:])
            soup = BeautifulSoup(token_list_page.content, 'html.parser')
            
            raw_token_list = soup.findAll('a', {'class': 'name notranslate'})

            try:  # Going through each token link and retriving all required data for token
                for token_link in raw_token_list:
                    token_url = DOMAIN + token_link['href']
                    token_row = get_token_data(token_url)
                    if not token_row:
                        continue
                    # Writing a row for each token

                    if first:
                        writer.writerow(COLUMNS)
                        first = False
                    temp_row = [''] * len(COLUMNS)

                    for k in range(0, len(token_row), 2):
                        if token_row[k] in ['preICO start', 'preICO end', 'ICO start', 'ICO end']:
                            temp_row[COLUMNS.index(token_row[k])] = date_formatting(token_row[k + 1])
                            if token_row[k] == 'preICO start': temp_row[28] = token_row[k + 1]
                            elif token_row[k] == 'preICO end': temp_row[29] = token_row[k + 1]
                            elif token_row[k] == 'ICO start': temp_row[30] = token_row[k + 1]
                            else: temp_row[31] = token_row[k + 1]

                        else:
                            temp_row[COLUMNS.index(token_row[k])] = token_row[k + 1]
                    writer.writerow(temp_row)
                iterations += 1
                print("Scraped page #" + str(i))
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)