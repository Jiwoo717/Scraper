from selenium import webdriver
import pandas as pd
import yagmail

driver = webdriver.Chrome(executable_path='C:\Users\kimer\Desktop\Programming\Drivers\Chrome Driver\chromedriver-win64')

driver.get('https://www.animenewsnetwork.com/')

headlines = driver.find_elements_by_class_name('headline_class_name')
headlines_text = [headline.text for headline in headlines]
