from time import sleep
from os import path
from datetime import datetime
from config import login

def get_user_followers(account, amount=100, method='list', print_followers='false'):
    if method not in ('txt', 'list'):
        print("You need to pass a method like 'get_user_followers(account, amount, method=method)' who is txt or list")
        return
    driver = login() # Getting the info to login and login

    # Going to account page to scraping
    driver.get('https://www.instagram.com/%s' % account)
    sleep(2) 

    # Finding the "button" to list followers
    driver.find_element_by_xpath('//a[contains(@href, "followers")]').click()
    sleep(2)

    # Initial time for scraping
    print(datetime.now())
    sleep(1)
    if method == 'list':
        list_followers = []
    # Scraping one-to-one follower
    for i in range(1, amount):
        sleep(0.2)
        # Finding the follower username
        follower = driver.find_element_by_xpath('//html/body/div[5]/div/div/div[2]/ul/div/li[{0}]'.format(i))
        
        # Scroll window to find elements
        driver.execute_script("arguments[0].scrollIntoView();", follower)

        # Getting the info of follower
        follower_list = follower.text.split()
        if method == 'txt':
            # Creating a .txt file to "save" followers
            dirname = path.dirname(path.abspath(__file__))
            txtfilename = path.join(dirname, account + "_followers.txt")

            # Open file
            f = open(txtfilename,'a')
            followers_file = open(account + '_followers.txt', 'r')
            list_followers = followers_file.readlines()

            # Check if string exists in file, if else write in .txt
            str_no_exists = True
            for j in range(0, len(list_followers)):
                if str(follower_list[0]).strip() == str(list_followers[j]).strip():
                    str_no_exists = False
                    break
            
            # Printing follower username and if he exists
            if str_no_exists:
                f.write(follower_list[0] + "\r\n")
                if print_followers == 'true':
                    print('{}: {}'.format(i, follower_list[0]))
            elif print_followers == 'true' and str_no_exists == False:
                print(str(i) + ": " + follower_list[0] + " exists on " + account + "_followers.txt")

            # Close file
            f.close()
            followers_file.close()

        else:
            if print_followers == 'true':
                print('{}: {}'.format(i, follower_list[0]))
            list_followers.append(follower_list[0])
        # Final time to scraping
        if i == (amount-1):
            print(datetime.now())
    # Close webdriver
    driver.close()

    if method == 'list':
        return list_followers
    else:
        print(account + "_followers.txt has been created.")

if __name__ == "__main__":
    followers = 80 # Number of last followers to scraping
    account = "nasa"  # Account to scraping
    followers_list = get_user_followers(account, followers)
    print(followers_list)