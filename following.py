from time import sleep
from os import path
from datetime import datetime
from config import login

following = 80 # Number of following accounts to scraping
account = "nasa"  # Account to scraping

driver = login() # Getting the info to login and login

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

    # Open file and write follower's username
    f = open(txtfilename,'a')
    followings_file = open(account + '_following.txt', 'r')
    list_followers = followings_file.readlines()

    # Check if string exists in file, if else write in .txt
    str_no_exists = True
    for j in range(0, len(list_followers)):
        if str(followed_list[0]).strip() == str(list_followers[j]).strip():
            str_no_exists = False
            break
    
    # Printing followed username and if he exists
    if str_no_exists:
        f.write(followed_list[0] + "\r\n")
        print('{}: {}'.format(i, followed_list[0]))
    else:
        print(str(i) + ": " + followed_list[0] + " exists on " + account + "_following.txt")

    # Close file
    f.close()
    followings_file.close()
    # Final time to scraping
    if i == (following-1):
        print(datetime.now())

# Close webdriver
driver.close()
