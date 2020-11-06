from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from os import path
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager

following = 100 # Number of following accounts to scraping
account = "nasa"  # Account to scraping

user = "JKuhdsa89" # Username to login in instagram
password = "JKuhdsa8933" # Password for the username account 

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
password_input.send_keys(password)

# Finding login button and clicking in him
login_button = driver.find_element_by_xpath("//button[@type='submit']")
login_button.click()
sleep(3) 

# Going to account page to scraping
driver.get('https://www.instagram.com/%s' % account)
sleep(2) 

# Finding the "button" to list following accounts
driver.find_element_by_xpath('//a[contains(@href, "following")]').click()
sleep(2)

# Initial time for scraping
print(datetime.now())
sleep(1)

# Scraping one-to-one followed
for i in range(1, following):
    sleep(0.2)
    # Finding the followed username
    followed = driver.find_element_by_xpath('//html/body/div[5]/div/div/div[2]/ul/div/li[{0}]'.format(i))
    
    # Scroll window to find elements
    driver.execute_script("arguments[0].scrollIntoView();", followed)

    # Getting the info of followed
    followed_list = followed.text.split()

    # Creating a .txt file to "save" following
    dirname = path.dirname(path.abspath(__file__))
    txtfilename = path.join(dirname, account + "_following.txt")

    # Check if file exists
    file_exists = path.isfile(txtfilename)

    # Open file and write followed's username
    f = open(txtfilename,'a')
    f.write(str(followed_list[0]) + "\r\n")

    # Close file and print followed's username
    f.close()
    print('{};{}'.format(i, followed_list[0]))

    # Final time to scraping
    if i == (following-1):
        print(datetime.now())

# Close webdriver
driver.close()
