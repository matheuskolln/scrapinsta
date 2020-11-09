from scrapinsta import Scrapinsta

account = 'nasa' # Account to get info
amount = 50 

# Instantiate Scrapinsta
s = Scrapinsta()

# Testing: method = 'list'
list_followers = s.get_user_followers(account, amount, method='list', print_followers='true')
list_following = s.get_user_followings(account, amount, method='list', print_following='true')

# Testing: method = 'txt'
s.get_user_followings(account, amount, method='txt', print_following='true')
s.get_user_followers(account, amount, method='txt', print_followers='true')