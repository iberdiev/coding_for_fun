'''
Cool snippets that may help in the future.
Selenium is a tool to automate web browser activities.
Mostly used for scraping, immitate human activity and automation of processes.
'''

from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import time
import os.path
import csv

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(" - incognito")
dimensions = {'width': 1293, 'height': 741}
browser = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver", chrome_options=chrome_options)
with open('input.csv', 'r') as file:
    reader = csv.reader(file)
    output_file = str(datetime.now())[:19] + '.csv'
    exists = True if os.path.exists(output_file) else False
    with open(output_file, 'a') as f:
        writer = csv.writer(f)
        if not exists:
            writer.writerow(["COLUMN NAMES ROW"])
        for row in reader:
            search_word = row[0]
            browser.get(url)
            browser.set_window_size(dimensions['width'],dimensions['height'])
            WebDriverWait(browser, 20).until(
                ec.visibility_of_element_located((By.XPATH, search_box)))
            browser.find_element_by_xpath(search_box).send_keys(search_word)
            browser.find_element_by_xpath(search_button).click()
            time.sleep(1)

            clickable_link = browser.find_elements_by_class_name('shop-sales')
            if len(clickable_link) > 0: clickable_link = clickable_link[0].find_elements_by_tag_name('a')
            else:
                print("Not clickable link for shop", search_word)
                continue
            if len(clickable_link) == 1: browser.get(clickable_link[0].get_attribute('href'))
            else:
                print("Not clickable link for shop", search_word)
                continue
            
            while starting_page != 1:
                starting_page -= 1
                WebDriverWait(browser, 20).until(
                    ec.visibility_of_element_located((By.XPATH, navigation_buttons)))
                button = browser.find_element_by_xpath(navigation_buttons).find_elements_by_tag_name('li')[-1]
                if not button.is_enabled():
                    print("There is no starting page available for this shop")
                else: button.click()
            while ending_page >= 0:
                ending_page -= 1
                if review_page == 15: break
                print(search_word, 'SALES_PAGE:', review_page)
                review_page += 1
                WebDriverWait(browser, 20).until(
                    ec.visibility_of_element_located((By.XPATH, sales_grid)))
                raw_sales = browser.find_element_by_xpath(
                    sales_grid).find_elements_by_tag_name('li')
                for raw_sale in raw_sales:
                    raw_sale.text
                    link = raw_sale.find_elements_by_tag_name('a')[-1].get_attribute('href')
                    writer.writerow([a,b,c])
                button = browser.find_element_by_xpath(navigation_buttons).find_elements_by_tag_name('li')[-1]
                if not button.is_enabled(): break
                button.click()