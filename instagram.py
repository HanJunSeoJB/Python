from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from urllib.request import urlretrieve


url = "https://www.instagram.com/p/CqE4HAhLjX5/"
name = "김채원"

driver = webdriver.Chrome()
driver.get(url)
time.sleep(10)
image = driver.find_element(By.CSS_SELECTOR, "img[class*='x5yr21d']").get_attribute('src')
urlretrieve(image, name + '.jpg')
print("Done!")
driver.close()
