from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import yagmail


# Setting up Chrome driver options
driver_path = 'C:/Users/kimer/Desktop/Programming/Drivers/Chrome Driver/chromedriver-win64'
options = Options()
options.binary_location = driver_path

# Initialize Chrome driver
driver = webdriver.Chrome(options=options)

driver.get('https://www.animenewsnetwork.com/')

headlines = driver.find_elements(By.CLASS_NAME, 'wrap')
headlines_text = [headline.text for headline in headlines]

df = pd.DataFrame(headlines_text, columns=['Headline'])
df = df[~df['Headline'].str.contains("Keyword_to_exclude")]

yag = yagmail.SMTP('YourEmail@gmail.com', 'Password')
yag.send(
    to='kimeric717@email.com',
    subject='Daily Headlines',
    contents=df['Headline'].tolist()
)
