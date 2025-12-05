from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def try_find_element(by, value, timeout=5):
        try:
            element = driver.find_element(by, value)
            return element
        except:
            return None

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "localhost:9222") # Use the port from step 1

driver = webdriver.Chrome(options=chrome_options) # ("C:\Users\faris\Desktop\auto_apply_bot\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver.get("https://ae.indeed.com/")

job_title = driver.find_element(By.XPATH, '//*[@id="text-input-what"]')
location = driver.find_element(By.XPATH, '//*[@id="text-input-where"]')

job_title.click()
time.sleep(0.2)
job_title.clear()
time.sleep(0.2)
job_title_close = try_find_element(By.XPATH, '//*[@id="jobsearch"]/div/div[1]/div/div[1]/div/div/span/span[2]/button')
if job_title_close:
    job_title_close.click()
time.sleep(0.2)
job_title.send_keys("ai engineer")

location.click()
time.sleep(0.2)
location.clear()
time.sleep(0.2)
location_close = try_find_element(By.XPATH, '//*[@id="jobsearch"]/div/div[1]/div/div[3]/div/div/span/span[2]/button')
if location_close:
    location_close.click()
time.sleep(0.2)
location.send_keys("Abu Dhabi")

search_button = driver.find_element(By.XPATH, '//*[@id="jobsearch"]/div/div[2]/button')
search_button.click()

# https://ae.indeed.com/jobs?q=ai+engineer&l=Abu+Dhabi&sc=0kf%3Aattr%287EQCZ%7CCF3CP%7CVDTG7%252COR%29%3B&from=searchOnDesktopSerp