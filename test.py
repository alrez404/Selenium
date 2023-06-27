from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://web.telegram.org/z/')

input('[+] After login and select your group or channel press Enter : ')

# click on add user button
add_user_button = driver.find_elements(By.CLASS_NAME, 'primary')[1]
add_user_button.click()
sleep(1)

# send keys on search box
add_user_search = driver.find_elements(By.CLASS_NAME, 'form-control')[3]
add_user_search.send_keys('eng')
sleep(1)

# click label for ticked used javascript
driver.execute_script("""document.getElementsByTagName('label')[1].click()""")
sleep(1)

# click added user button used javascript
add_user_button_channel = driver.find_element(By.XPATH, "//button[@aria-label='Add users']")
add_user_button_channel.click()
