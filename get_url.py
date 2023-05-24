import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# from webdriver_manager.chrome import ChromeDriverManager

driver= webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://iranfile.ir/Search/A4BDC39B-1/%D8%AE%D8%B1%DB%8C%D8%AF_%D8%AA%D9%87%D8%B1%D8%A7%D9%86')



for i in range(0,5):
    url=driver.current_url
    r = requests.get(url)

    s = BeautifulSoup(r.content, 'html.parser')

    tags = s.find_all('a', class_='grd_search_links')
    urls = []

    for tag in tags:
        print(tag)
        b = '/n'
        with open('test.txt', 'a+', encoding='utf-8') as f:
            f.writelines(tag['href'])
            f.writelines('\n')

    driver.find_elements(By.CLASS_NAME,'next')[0].click()

