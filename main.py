from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(
    'https://accounts.google.com/ServiceLogin/signinchooser?service=mail&passive=1209600&osid=1&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%3Fzx%3Dgux0hpjvd8rw&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%3Fzx%3Dgux0hpjvd8rw&emr=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin#inbox')
sleep(2)

input('[+] after login press Enter : ')
subject = input('[+] please Enter your subject : ')

list_gmail = []
with open('gmail.text', 'r') as File:
    for gmail in File:
        list_gmail.append(gmail.strip())

list_massage = []
with open('massage.text', 'r', encoding='utf-8') as File:
    for massage in File:
        list_massage.append(massage.strip())

for gmail in list_gmail:

    # click on type email
    driver.find_elements(By.CLASS_NAME, "L3")[2].click()
    sleep(1)

    # send gmail address
    Gmail = driver.find_elements(By.CLASS_NAME, 'agP')[0]
    Gmail.send_keys(gmail)
    Gmail.send_keys(Keys.ENTER)
    sleep(1)

    # send subject in fild
    driver.find_elements(By.CLASS_NAME, 'aoT')[0].send_keys(subject)
    sleep(1)

    # send massage in fild
    driver.find_elements(By.CLASS_NAME, "tS-tW")[0].send_keys(massage)
    sleep(1)

    # click send email
    driver.find_elements(By.CLASS_NAME, 'aoO')[0].click()
    sleep(1)
    print(50 * '_')
    print('[+] gmail was send to {}'.format(gmail))
    print(50 * '_')
