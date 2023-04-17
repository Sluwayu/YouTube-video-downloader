import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

with open("video_links.csv") as f:
    reader = csv.reader(f)
    num_downloaded = 0
    for row in reader:
        LINK = row[0]
        if not LINK:
            continue
        url = f'https://en.savefrom.net/387/{LINK}'
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        wait = WebDriverWait(driver, 20)
        driver.get(url)
        driver.maximize_window()
        download = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="sf_result"]/div/div/div[2]/div[2]/div[1]/a')))
        download.send_keys(Keys.ENTER)
        time.sleep(250)
        driver.quit()  # close the current window and quit the browser
        num_downloaded += 1
        print(f"Download completed for link {num_downloaded}: {LINK}")
        
print(f"Downloaded {num_downloaded} videos. Follow me on Twitter @VikChukwuemeka!")
