# importing the libraries required to decode the HTML page and pull a table from the Web Page

import os
import bs4
import pandas as pd
from selenium import webdriver


PATH = os.path.join('/','C:', 'Users','akudnaver', 'Desktop', 'Machine_Learning', 'Sniffer_Training', 'NLTK')


def table_to_df(table):
    return pd.DataFrame([[td.text for td in row.find_all('td')] for row in soup.find_all('tr')])



res = pd.DataFrame()
head = []
url = "https://www.meteoschweiz.admin.ch/home/messwerte.html"
counter = 0
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome('C:/Users/akudnaver/Desktop/Machine_Learning/Sniffer_Training/NLTK/chromedriver.exe', options=chrome_options)
driver.get(url)

while True:
    print(counter)
    page = driver.get(url)
    soup = bs4.BeautifulSoup(driver.page_source, 'lxml')
    table = driver.find_element_by_xpath('//*[@id="measurementv3-table"]')
    if table is None:
        print("no table 'tableID' found for url {}".format(url))
        print("html content:\n{}\n".format(page.content))
        continue
      
    
    res = res.append(table_to_df(table))
    res.to_csv(os.path.join('C:/Users/akudnaver/Desktop/Machine_Learning/Sniffer_Training/NLTK/',"table.csv"), index=False, sep=',', header=None)
    isempty = res.empty
    print('Is the DataFrame empty :', isempty)
    break
    counter += 1