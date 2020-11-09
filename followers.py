from time import sleep
from os import path
from datetime import datetime
from config import login

def get_user_followers(account, amount=100, method='list', print_followers='false'):
    """
    account: Account which want to get user followers\n
    amount: Number of followers to scraping\n
    method: By default is 'list'(returns a list), but can be 'txt' this will write a .txt with user followers\n
    print_followers: By default is 'false'(don't print followers), but can be 'true' this will print followers
    """
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
    
    # Checking if method is list, if true creating a list to storage followers
    if method == 'list':
        list_followers = []

    # Scraping one-to-one follower
    for i in range(1, amount+1):
        sleep(0.2)
        # Finding the follower username
        follower = driver.find_element_by_xpath('//html/body/div[5]/div/div/div[2]/ul/div/li[{0}]'.format(i))
        
        # Scroll window to find elements
        driver.execute_script("arguments[0].scrollIntoView();", follower)

        # Getting the info of follower
        follower_list = follower.text.split()

        # Checking if method is txt, if true creating a .txt file to "save" followers
        if method == 'txt':
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
            
            # Writing in .txt and printing(if printing_followers is true)
            if str_no_exists:
                f.write(follower_list[0] + "\r\n")
                if print_followers == 'true':
                    print('{}: {}'.format(i, follower_list[0]))
            elif print_followers == 'true' and str_no_exists == False:
                print(str(i) + ": " + follower_list[0] + " exists on " + account + "_followers.txt")

            # Close file
            f.close()
            followers_file.close()

        # Appending to list_followers(because method is list), and printing(if printing_followers is true) 
        else:
            if print_followers == 'true':
                print('{}: {}'.format(i, follower_list[0]))
            list_followers.append(follower_list[0])

        # Final time to scraping
        if i == (amount):
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
    get_user_followers(account, followers, print_followers='true', method='txt')