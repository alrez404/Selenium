from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://web.telegram.org/?legacy=1#/')

name_contact = []
with open('name_contact.text', 'r', encoding='utf-8') as File:
    for name in File:
        name_contact.append(name)

input('[+] After login and select your group or channel press Enter : ')

try:
    for name in name_contact:
        # click on header group or channel
        driver.find_elements(By.CLASS_NAME,'tg_head_btn')[4].click()
        sleep(2)
        # click on invite memebers
        driver.find_elements(By.CLASS_NAME,"md_modal_section_link")[0].click()
        sleep(2)
        # send name on search box
        driver.find_elements(By.CLASS_NAME,'contacts_modal_search_field')[0].send_keys(name)
        sleep(2)
        # click on contact
        driver.find_elements(By.CLASS_NAME,'contacts_modal_contact')[0].click()
        sleep(2)
        # click on next
        driver.find_elements(By.CLASS_NAME,'btn-md-primary')[0].click()
except:
    print('we fucked up')