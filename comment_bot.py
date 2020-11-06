user = 'nasa'
followers = open(user + '_followers.txt', 'r')
list = followers.readlines()
count = 0
for i in range(0, len(list)):
    for j in range(0, len(list)):
        if i != j:
            count += 1
            print(str(count) + ": @" + list[i].strip() + " @" + list[j].strip())
followers.close()