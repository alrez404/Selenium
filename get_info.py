import os
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By

lines_seen = set()  # holds lines already seen
outfile = open('ads-url.txt', "w", encoding='utf-8')
for line in open('test.txt', "r", encoding='utf-8'):
    if line not in lines_seen:  # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()

with open('ads-url.txt', 'r', encoding='utf-8') as f:
    for i in f:
        # driver = webdriver.Chrome(executable_path='chromedriver.exe')
        driver = webdriver.Chrome(ChromeDriverManager().install())

        driver.get(i)
        sleep(2)
        title = driver.find_elements(By.CLASS_NAME, 'file-data')[5].text
        text = driver.find_elements(By.CLASS_NAME, 'col-xs-12')[2].text


        dir = f'ads/{title}'
        try:

            os.mkdir(dir)

        except:
            print('directory created')

        with open(f'ads/{title}/info.txt','a+',encoding='utf-8') as n:
            n.writelines(title)
            n.writelines('\n')
            n.writelines(text)
