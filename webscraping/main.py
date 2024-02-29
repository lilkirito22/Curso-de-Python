from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()

#para manter o navegador aberto
options.add_experimental_option("detach", True)

Service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(options=options,service=Service)

url = "https://www.google.com.br/"
driver.get(url)

WebDriverWait(driver, 5).until(
  EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear()
input_element.send_keys("books to scrape" + Keys.ENTER)

WebDriverWait(driver, 5).until(
  EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Books to Scrape"))
)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Books to Scrape")
link.click()





