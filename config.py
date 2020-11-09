from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from cryptography.fernet import Fernet
from getpass import getpass

def login():
    # Getting username and password to login
    user = input('Username: ')
    password = getpass('Password: ')
    # Encrypting password
    bpass = bytes(password, 'utf-8')
    key = Fernet.generate_key()
    f = Fernet(key)

    password_crypted = f.encrypt(bpass)

    # Configuring and running webdriver
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D57"')
    driver = webdriver.Chrome(ChromeDriverManager().install())

    # Getting the login page of instagram
    driver.get('https://www.instagram.com/accounts/login/')
    sleep(3)

    # Finding inputs to login on instagram
    user_input = driver.find_element_by_css_selector("input[name='username']")
    password_input = driver.find_element_by_css_selector("input[name='password']")

    # Inserting username and password to login
    user_input.send_keys(user)
    password_input.send_keys(str(f.decrypt(password_crypted), 'utf-8'))

    # Finding login button and clicking in him
    login_button = driver.find_element_by_xpath("//button[@type='submit']")
    login_button.click()
    sleep(3) 
    
    return driver
