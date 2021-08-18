from selenium import webdriver
import time
import random 

PATH = "./chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://popcat.click/")
neko = driver.find_element_by_id("app")

"""
#無休息時間
c=0
while c<1:
    neko.click()
"""

#隨機點擊次數及休息時間
click_random = int(random.random()*500)
sec_random = int(random.random()*5)

c = 0
while c < 1:
    for i in range(click_random):
        neko.click()
    time.sleep(sec_random)