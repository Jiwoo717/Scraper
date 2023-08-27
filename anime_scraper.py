from selenium import webdriver
import pandas as pd
import yagmail

driver = webdriver.Chrome(executable_path='C:\Users\kimer\Desktop\Programming\Drivers\Chrome Driver\chromedriver-win64')

driver.get('https://www.animenewsnetwork.com/')

headlines = driver.find_elements_by_class_name('wrap')
headlines_text = [headline.text for headline in headlines]

driver.close()

yag = yagmail.SMTP('kimeric717@email.com', 'My_Password')

yag.send(
    to='kimeric717@email.com',
    subject='Daily Headlines',
    contents=df['Headline'].tolist()
)
