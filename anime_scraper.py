import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import yagmail

# Get pass and email from os
email = os.environ.get('EMAIL')
password = os.environ.get('PASSWORD')

# Setting up Chrome driver options
driver_path = 'C:/Users/kimer/Desktop/Programming/Drivers/Chrome Driver/chromedriver-win64'
options = Options()
options.binary_location = driver_path
options.add_argument("--headless")  # Run in headless mode

# Initialize Chrome driver
driver = webdriver.Chrome(options=options)

try:
    driver.get('https://www.animenewsnetwork.com/')
    headlines = driver.find_elements(By.CLASS_NAME, 'wrap')
    headlines_text = [headline.text for headline in headlines]
    df = pd.DataFrame(headlines_text, columns=['Headline'])
    df = df[~df['Headline'].str.contains("Keyword_to_exclude")]
finally:
    driver.quit()  # Close browser

# Load previously seen headlines
previous_headlines = set()
if os.path.exists('previous_headlines.txt'):
    with open('previous_headlines.txt', 'r') as f:
        previous_headlines = set(f.read().splitlines())

# Filter new headlines
new_headlines = [headline for headline in df['Headline'].tolist() if headline not in previous_headlines]

# If there are new headlines, send an email
if new_headlines:
    yag = yagmail.SMTP(EMAIL, PASSWORD)
    yag.send(
        to=email
        subject='New Anime Headlines',
        contents='\n'.join(new_headlines)
    )

    # Save the new headlines
    with open('previous_headlines.txt', 'a') as f:
        for headline in new_headlines:
            f.write(f"{headline}\n")
