from selenium import webdriver
from time import sleep
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
driver=webdriver.Chrome(r"")#put the path of your chrome driver in the double quotes
driver.get('https://instagram.com/')
WebDriverWait(driver,30).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.f0n8F ')))
username_type = driver.find_element_by_xpath("//input[@name=\"username\"]")
username_type.send_keys("")#Enter your username in double quotes
password_type = driver.find_element_by_xpath("//input[@name=\"password\"]")
password_type.send_keys("")#Enter your password in double quotes
log_in = driver.find_element_by_xpath("//button[@type='submit']")
log_in.click()
WebDriverWait(driver,30).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '._6q-tv')))
dp=driver.find_element_by_xpath("//img[@class='_6q-tv']")
dp.click()
sleep(2)
profile=driver.find_element_by_class_name('_7UhW9')
profile.click()
WebDriverWait(driver,30).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '._81NM2')))
follow=driver.find_element_by_xpath("//a[@class=' _81NM2']")
follow.click()
sleep(2)
scroll_box = driver.find_element_by_xpath("//div[@class='isgrP']")
allfoll=int(driver.find_elements_by_xpath("//span[@class='g47SY lOXF2']")[1].text) 
for i in range(int(allfoll/12)):
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_box)
        sleep(random.randint(500,1000)/1000)
        links = scroll_box.find_elements_by_tag_name('a')
        print("Extracting followers %",round((i/(allfoll/12)*100),2),"from","%100")

followers = [name.text for name in links if name.text != '']
close = driver.find_elements_by_xpath("//button[@class='wpO6b ']")[1]
close.click()
followin=driver.find_elements_by_xpath("//a[@class=' _81NM2']")[1]
followin.click()
sleep(2)
scroll_box2 = driver.find_element_by_xpath("//div[@class='isgrP']")
allfollin=int(driver.find_elements_by_xpath("//span[@class='g47SY lOXF2']")[1].text) 
for i in range(int(allfollin/12)):
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_box2)
        sleep(random.randint(500,1000)/1000)
        links2 = scroll_box2.find_elements_by_tag_name('a')
        print("Extracting following %",round((i/(allfollin/12)*100),2),"from","%100")
following = [name.text for name in links2 if name.text != '']
close = driver.find_elements_by_xpath("//button[@class='wpO6b ']")[1]
close.click()
print([user for user in following if user not in followers])
driver.close()
