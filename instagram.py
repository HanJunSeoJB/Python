from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from urllib.request import urlretrieve
from selenium.webdriver.chrome.options import Options

url = "https://www.instagram.com/p/CpZOMuTodY7/"
name = "윈터"

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)
time.sleep(10)
image = driver.find_element(By.CSS_SELECTOR, "img[class*='x5yr21d']").get_attribute('src')
urlretrieve(image, name + '.jpg')
print("Done!")
driver.close()

