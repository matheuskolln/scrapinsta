from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from os import path, getcwd
from datetime import datetime
from cryptography.fernet import Fernet
from getpass import getpass

class Scrapinsta:
    def __init__(self):
        pass

    def __login(self):
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

    def get_user_followers(self, account, amount=100, method='list', print_followers='false'):
        """
        account: Account which want to get user followers\n
        amount: Number of followers to scraping\n
        method: By default is 'list'(returns a list), but can be 'txt' this will write a .txt with user followers\n
        print_followers: By default is 'false'(don't print followers), but can be 'true' this will print followers
        """
        if method not in ('txt', 'list'):
            raise ValueError("Parameter method need to be 'txt' or 'list'.")
        if print_followers not in ('false', 'true'):
            raise ValueError("Parameter print_followers need to be 'false' or 'true'.")

        driver = self.__login() # Getting the info to login and login

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
                dirname = getcwd()
                txtfilename = path.join(dirname, account + "_followers.txt")

                # Open file
                f = open(txtfilename,'a')
                followers_file = open(txtfilename, 'r')
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
            return

    def get_user_followings(self, account, amount=100, method='list', print_following='false'):
        """
        account: Account which want to get users followed\n
        amount: Number of users followed to scraping\n
        method: By default is 'list'(returns a list), but can be 'txt' this will write a .txt with users followed\n
        print_following: By default is 'false'(don't print users followed), but can be 'true' this will print users followed
        """
        if method not in ('txt', 'list'):
            raise ValueError("Parameter method need to be 'txt' or 'list'.")
        if print_following not in ('false', 'true'):
            raise ValueError("Parameter print_following need to be 'false' or 'true'.")
        driver = self.__login() # Getting the info to login and login

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
                dirname = getcwd()
                txtfilename = path.join(dirname, account + "_following.txt")

                # Open file
                f = open(txtfilename,'a')
                following_file = open(txtfilename, 'r')
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
