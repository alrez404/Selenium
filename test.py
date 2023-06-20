import os

from selenium import webdriver
import webdriver_manager
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup
from time import sleep


# url='https://www.homsa.net/rooms/42143'
#
# r=requests.get(url)
# s=BeautifulSoup(r.content,'html.parser')
# a=0
# tags= s.find_all('a',class_='elem')
# for tag in tags:
#     img=tag['href']
#     with open(f'img/{a}.png','wb')as file :
#         im=requests.get(img)
#         file.write(im.content)
#         a+=1
#         print(a)

driver=webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.homsa.net/rooms/42143')

sleep(4)
txt=driver.find_element(By.ID,'about_wrapper').text

print(txt)


