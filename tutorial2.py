from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


PATH = "/usr/local/Caskroom/chromedriver/83.0.4103.39/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://tim.blog/")

link = driver.find_element_by_partial_link_text("Psychedelics")
link.click()

try:
    main = WebDriverWait(driver, 7).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Sam Harris"))
    )
    element.click()
except:
    driver.quit()
