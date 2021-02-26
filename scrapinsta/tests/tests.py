from scrapinsta import Scrapinsta

account = 'nasa' # Account to get info
amount = 5
test = 0
# Instantiate Scrapinsta
s = Scrapinsta()
s.login()
print("Scrapinsta OK!")


# Testing: method = 'list'
try:
    list_followers = s.get_user_followers(account, amount, method='list', print_followers='true')
    print("Method get_user_followers with method = 'list' OK!")
    test += 1
except Exception as e:
    print(e)
    print("!!!!Method get_user_followers with method = 'list' NOT OK!!!!")
    pass

try:
    list_following = s.get_user_followings(account, amount, method='list', print_following='true')
    print("Method get_user_followings with method = 'list' OK!")
    test += 1
except Exception as e:
    print(e)
    print("!!!!Method get_user_followings with method = 'list'NOT OK!!!!")
    pass


# Testing: method = 'txt'

try:
    s.get_user_followings(account, amount, method='txt', print_following='true')
    print("Method get_user_followers with method = 'txt' OK!")
    test += 1
except Exception as e:
    print(e)
    print("!!!!Method get_user_followers with method = 'txt' NOT OK!!!!")
    pass

try:
    s.get_user_followers(account, amount, method='txt', print_followers='true')
    print("Method get_user_followings with method = 'txt' OK!")
    test += 1
except Exception as e:
    print(e)
    print("!!!!Method get_user_followings with method = 'txt' NOT OK!!!!")
    pass


# Testing errors:
#get_user_followers
try:
    list_followers = s.get_user_followers(account, amount, method='list', print_followers='LDSA', sleeptime=0.1)
    print("!!!!Exception to get_user_followers print_followers NOT OK!!!!")
except Exception as e:
    test += 1
    print(e)
    print("Exception to get_user_followers print_followers OK!")
    pass
    
try:
    list_followers = s.get_user_followers(account, amount, method='dsada', print_followers='true', sleeptime=0.1)
    print("!!!!Exception to get_user_followers method NOT OK!!!!")
except Exception as e:
    test += 1
    print(e)
    print("Exception to get_user_followers method OK!")
    pass
    
try:
    list_followers = s.get_user_followers(account, amount, method='list', print_followers='true', sleeptime=-1)
    print("!!!!Exception to get_user_followers sleeptime NOT OK!!!!")
except Exception as e:
    test += 1
    print(e)
    print("Exception to get_user_followers sleeptime OK!")
    pass
    
    
# get_user_followings
try:
    list_followers = s.get_user_followings(account, amount, method='list', print_following='LDSA', sleeptime=0.1)
    print("!!!!Exception to get_user_followings print_following NOT OK!!!!")
except Exception as e:
    test += 1
    print(e)
    print("Exception to get_user_followings print_following OK!")
    pass
    
try:
    list_followers = s.get_user_followers(account, amount, method='dsada', print_following='true', sleeptime=0.1)
    print("!!!!Exception to get_user_followings method NOT OK!!!!")
except Exception as e:
    test += 1
    print(e)
    print("Exception to get_user_followings method OK!")
    pass
    
try:
    list_followers = s.get_user_followers(account, amount, method='list', print_following='true', sleeptime=-1)
    print("!!!!Exception to get_user_followings sleeptime NOT OK!!!!")
except Exception as e:
    test += 1
    print(e)
    print("Exception to get_user_followings sleeptime OK!")
    pass

# Testing quit function
try:
    test += 1
    s.quit()
    print("Method quit OK!")
except Exception as e:
    print(e)
    print("!!!!Method quit NOT OK!!!!")
    pass

print(f'Passed {test} from 11 tests')
