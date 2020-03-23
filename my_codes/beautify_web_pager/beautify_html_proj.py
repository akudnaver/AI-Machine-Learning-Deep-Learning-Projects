# importing the libraries required to access the HTML page and pull a table from a Web Page.
# This code expects users to have fair amount of knowledge on how to read through the HTML body,tags,classes. You can refer
# the below links to develope an understanding of HTML page and for some basic foundation on Python Beautiful Soup functionality. 

import os
import bs4
import pandas as pd
from selenium import webdriver

# Choose a working directory 

PATH = os.path.join('/','C:/', 'Users','akudnaver', 'Desktop')

# Download the chromedriver.exe file and specif the path under PATH_CHROME
PATH_CHROME = 'specify the path to chromedriver.exe' 

# Here is a quick definition/function to iterate over each rows ='tr' under a table body of your choice. We are basically
# reading through the table rows from the webpage.

def table_to_df(table):
    return pd.DataFrame([[td.text for td in row.find_all('td')] for row in soup.find_all('tr')])

res = pd.DataFrame()

# Here we are only interested in the website under variable 'URL' , i will try to make it generic in my next project for
# you to download all the tables from any webpage using Beautiful soup function.

url = "https://www.meteoschweiz.admin.ch/home/messwerte.html"
counter = 0

# We will be using the selenium webdriver function to start the webpage we are interested to work with here. 
chrome_options = webdriver.ChromeOptions()

# A sandbox is security mechanism used to run an application in a restricted environment. 
# If an attacker is able to exploit the browser in a way that lets him run arbitrary code on the machine, 
# the sandbox would help prevent this code from causing damage to the system. But in our case we would like to disbale 
# the sandbox just to serve our purpose.
chrome_options.add_argument('--no-sandbox')

# Selenium python binding provides a simple API to write the functional tests using Selenium webdriver, with the help
# of this tool, you can extract any element out of the webpage in a convenient way and as well you can perform tests on the
# webpage, of your choice.

# In the below code we are creating an instance of Chrome webdriver and setting the URL our choice we wish to work with.

driver = webdriver.Chrome(PATH, chrome_options=chrome_options)
driver.get(url)


# In the below segment of code we are going to pull the table of our interest from the webpage.
while True:
    print("=========================================================\n")
    print("The task is completed , you can access the CSV file now")
    print("=========================================================\n")
    page = driver.get(url)
    soup = bs4.BeautifulSoup(driver.page_source, 'lxml')
    table = driver.find_element_by_xpath('//*[@id="measurementv3-table"]')
    if table is None:
        print("no table 'tableID' found for url {}".format(url))
        print("html content:\n{}\n".format(page.content))
        continue
      
    # In the below code we will convert the table to a dataframe and save it in a CSV file
    res = res.append(table_to_df(table))
    res.dropna(axis=0,inplace=True)
    res.to_csv(os.path.join(PATH,"table.csv"), index=False, sep=',', header=None)
    break
    counter += 1
