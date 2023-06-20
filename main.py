import os
from selenium import webdriver
import webdriver_manager
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup as soup
from time import sleep


driver=webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.homsa.net/search?campaign=northern-Iran')

sleep(1)

driver.find_elements(By.CLASS_NAME,'pagination-nav')[3].click()

sleep(1)

page=driver.find_elements(By.CLASS_NAME,'pagination-page')[5].text

sleep(1)
a=0
driver.find_elements(By.CLASS_NAME,'pagination-nav')[0].click()

pages=int(page)

for i in range(0,pages):
    for x in range(0, 24):
        sleep(5)
        driver.find_elements(By.CLASS_NAME, 'card-image')[x].click()
        sleep(5)

        titr=driver.find_elements(By.CLASS_NAME,'overflow')[0].text
        dir=f'ads/{titr}'
        os.mkdir(dir)
        sleep(1)
        page_url = driver.current_url
        r = requests.get(page_url)
        soupe = soup(r.content, 'html.parser')
        tags=soupe.find_all('a',class_='elem')
        for tag in tags:
            ta=tag['href']
            with open(f'ads/{titr}/{a}.jpg','wb')as file:
                img=requests.get(ta)
                file.write(img.content)
                a+=1

        p0=driver.find_elements(By.CLASS_NAME,'property_options-info')[0].text
        p1=driver.find_elements(By.CLASS_NAME,'lang-chang-label')[0].text
        p2=driver.find_elements(By.CLASS_NAME, 'property_options-info')[1].text
        p3=driver.find_elements(By.CLASS_NAME, 'property_options-info')[2].text

        try:
            driver.find_elements(By.CLASS_NAME,'about-more-btn')[0].click()

        except:
            continue

        p4 = driver.find_element(By.ID, 'about_wrapper').text
        driver.find_elements(By.CLASS_NAME,'expandable-trigger-more')[0].click()
        p5=driver.find_elements(By.CLASS_NAME,'collapsedSection')[0].text
        p6=driver.find_elements(By.CLASS_NAME,'amenities_section')[1].text

        try:
            driver.find_elements(By.CLASS_NAME,'collapse-trigger')[1].click()

        except:
            continue

        p7 = driver.find_element(By.ID, 'property_rules').text

        with open(f'ads/{titr}/info.txt','w+',encoding='utf-8')as File:
           File.writelines(titr)
           File.write('\n')
           File.writelines(p0)
           File.write('\n')
           File.writelines(p1)
           File.write('\n')
           File.writelines(p2)
           File.write('\n')
           File.writelines(p3)
           File.write('\n')
           File.writelines(p4)
           File.write('\n')
           File.writelines(p5)
           File.write('\n')
           File.writelines(p6)
           File.write('\n')
           File.writelines(p7)

        driver.back()

















