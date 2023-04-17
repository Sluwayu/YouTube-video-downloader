import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

url = 'https://www.youtube.com/playlist?list=PLlrxD0HtieHjbTjrchBwOVks_sr8EVW1x'
options = Options()
options.headless = True
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 10)
driver.get(url)

wait.until(EC.presence_of_element_located((By.ID, 'video-title')))
driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
wait.until(EC.presence_of_element_located((By.XPATH, '//a[@id="video-title"]')))

video_links = []

links = driver.find_elements(By.XPATH, '//a[@id="video-title"]')
for link in links:
    video_links.append(link.get_attribute('href'))

with open('video_links.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    for link in video_links:
        writer.writerow([link])
print("----SUCCESSFUL")
print(f"-----------ALL 35 PLAYLIST LINK HAS BEEN SAVE TO video_links.csv IN THE FOLDER")

print('------------NOW RUN THE CODE "python download.py"')
