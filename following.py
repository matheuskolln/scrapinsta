from time import sleep
from os import path
from datetime import datetime
from config import login

def get_user_followings(account, amount=100, method='list', print_following='false'):
    """
    account: Account which want to get users followed\n
    amount: Number of users followed to scraping\n
    method: By default is 'list'(returns a list), but can be 'txt' this will write a .txt with users followed\n
    print_following: By default is 'false'(don't print users followed), but can be 'true' this will print users followed
    """
    driver = login() # Getting the info to login and login

    # Going to account page to scraping
    driver.get('https://www.instagram.com/%s' % account)
    sleep(2) 

    # Finding the "button" to list followings
    driver.find_element_by_xpath('//a[contains(@href, "following")]').click()
    sleep(2)

    # Initial time for scraping
    print(datetime.now())
    sleep(1)

    # Checking if method is list, if true creating a list to storage user followed
    if method == 'list':
        list_following = []

    # Scraping one-to-one user followed
    for i in range(1, amount+1):
        sleep(0.2)
        # Finding the username of user followed
        following = driver.find_element_by_xpath('//html/body/div[5]/div/div/div[2]/ul/div/li[{0}]'.format(i))
        
        # Scroll window to find elements
        driver.execute_script("arguments[0].scrollIntoView();", following)

        # Getting the info of following
        following_list = following.text.split()

        # Checking if method is txt, if true creating a .txt file to "save" user followed
        if method == 'txt':
            # Creating a .txt file to "save" followings
            dirname = path.dirname(path.abspath(__file__))
            txtfilename = path.join(dirname, account + "_following.txt")

            # Open file
            f = open(txtfilename,'a')
            following_file = open(account + '_following.txt', 'r')
            list_following = following_file.readlines()

            # Check if string exists in file, if else write in .txt
            str_no_exists = True
            for j in range(0, len(list_following)):
                if str(following_list[0]).strip() == str(list_following[j]).strip():
                    str_no_exists = False
                    break
            
            # Writing in .txt and printing(if printing_following is true)
            if str_no_exists:
                f.write(following_list[0] + "\r\n")
                if print_following == 'true':
                    print('{}: {}'.format(i, following_list[0]))
            elif print_following == 'true' and str_no_exists == False:
                print(str(i) + ": " + following_list[0] + " exists on " + account + "_following.txt")

            # Close file
            f.close()
            following_file.close()

        # Appending to list_following(because method is list), and printing(if printing_following is true)
        else:
            if print_following == 'true':
                print('{}: {}'.format(i, following_list[0]))
            list_following.append(following_list[0])
        # Final time to scraping
        if i == (amount):
            print(datetime.now())

    # Close webdriver
    driver.close()

    if method == 'list':
        return list_following
    else:
        print(account + "_following.txt has been created.")

if __name__ == "__main__":
    followings = 80 # Number of last followings to scraping
    account = "nasa"  # Account to scraping
    get_user_followings(account, followings, print_following='true', method='txt')
