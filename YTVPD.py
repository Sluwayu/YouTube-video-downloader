print("----------- PASTE THE PLAYLIST LINK BELOW AND HIT ENTER ON YOUR KEYBOARD")
link = input(">> ")

import csv
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


options = Options()
options.headless = True

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = Options())
wait = WebDriverWait(driver, 10)
url = (link)

def fetch():
    driver.get(url)
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
    print(f"-----------ALL PLAYLIST LINK HAS BEEN SAVE TO video_links.csv IN THE FOLDER")

# print('------------NOW RUN THE CODE "python download.py"')
def download():
    with open("video_links.csv") as f:
        reader = csv.reader(f)
        num_downloaded = 0
        for row in reader:
            LINK = row[0]
            if not LINK:
                continue
            url = f'https://en.savefrom.net/387/{LINK}'
            driver.get(url)
            print("driver opened")
            driver.maximize_window()
            driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            time.sleep(10)
            
           
            download = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[4]/div/div/div[2]/div[2]/div[1]/a')))
            download.send_keys(Keys.ENTER)
            time.sleep(20)
            # driver.quit()  # close the current window and quit the browser
            num_downloaded += 1
            print(f"Download completed for link {num_downloaded}")
        print(f"Downloaded {num_downloaded} videos. Follow me on Twitter @VikChukwuemeka")

fetch()
download()