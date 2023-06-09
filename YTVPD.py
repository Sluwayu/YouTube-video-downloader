# COLLECT INPUT FROOM USER
print("----------- PASTE THE PLAYLIST LINK BELOW AND HIT ENTER ON YOUR KEYBOARD")
link = input(">> ")

# DEPENDENCIES
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

# HEADLESS MODE
options = Options()
options.headless = True

# WEB DRIVER ACTIVATION
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = Options())
wait = WebDriverWait(driver, 10)
url = (link)

# FUNCTION TO FETCH LINK FROM TARGET YOUTUBE PLAYLIST VIA THE LINK COLLECTED FROM THE USER
def fetch():
    driver.get(url)
    # MAX WINDOW  FOR BETTER PERFORMANCE
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    # WAITING TO FIND ELEMENT
    wait.until(EC.presence_of_element_located((By.XPATH, '//a[@id="video-title"]')))

    # LIST
    video_links = []

    links = driver.find_elements(By.XPATH, '//a[@id="video-title"]')
    for link in links:
        video_links.append(link.get_attribute('href'))
    #CREATING CSV FILE TO SAVE SCRAPPED LINKS
    with open('video_links.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        for link in video_links:
            writer.writerow([link])
    print("----SUCCESSFUL")
    print(f"-----------ALL PLAYLIST LINK HAS BEEN SAVE TO video_links.csv IN THE FOLDER")

# FUNCTION TO READ LINK AND DOWNLOAD 
def download():
    # TO READ CSV FILE FOR SAVE LINK
    with open("video_links.csv") as f:
        reader = csv.reader(f)
        num_downloaded = 0
        for row in reader:
            LINK = row[0]
            if not LINK:
                continue
            url = f'https://en.savefrom.net/387/{LINK}'
            # TO OPEN NEW TAB FOR DOWNLOAD
            driver.get(url)
            print("driver opened")
            driver.maximize_window()
            driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            time.sleep(10)
            # DONLOAD BTN
            download = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[4]/div/div/div[2]/div[2]/div[1]/a')))
            download.send_keys(Keys.ENTER)
            time.sleep(20)
            # driver.quit()  # close the current window and quit the browser
            num_downloaded += 1
            print(f"Download completed for link {num_downloaded}")
        print(f"Downloaded {num_downloaded} videos. Follow me on Twitter @VikChukwuemeka")
        
# CALLING FUNCTION
fetch()
download()