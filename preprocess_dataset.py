from collections import UserDict
import gzip
import json
import time 
import datetime

def parse(path):
    g = gzip.open(path, 'r')
    for l in g:
        yield json.loads(l)

user_count = {}
item_count = {}

'''
Sort by user id then by timestamp to get preprocessed data
'''

for line in parse('data/goodreads_reviews_spoiler.json.gz'):
    time = line['timestamp']
    u_id = line['user_id']
    i_id = line['book_id']

    if u_id not in user_count:
        user_count[u_id] = 1
    else:
        user_count[u_id] += 1

    if i_id not in item_count:
        item_count[i_id] = 1
    else:
        item_count[i_id] += 1


usermap = {}
u_num = 0
itemmap = {}
i_num = 0
user = {}
# prevent cold-start problem we get rid of reviews or user id with less than 5
for line in parse('data/goodreads_reviews_spoiler.json.gz'):
    date = line['timestamp']
    # print(date)
    date = datetime.datetime.strptime(date, "%Y-%m-%d")
    unix_time = datetime.datetime.timestamp(date)
    # unix_time = time.mktime(datetime.datetime.strptime(date, "%Y/%m/%d").timetuple())
    u_id = line['user_id']
    i_id = line['book_id']

    if user_count[u_id] < 5 or item_count[i_id] < 5:
        continue

    if u_id in usermap:
        userid = usermap[u_id]
    else:
        u_num += 1
        userid = u_num
        usermap[u_id] = userid
        user[userid] = []
    
    if i_id in itemmap:
        itemid = itemmap[i_id]
    else:
        i_num += 1
        itemid = i_num
        itemmap[i_id] = itemid
    
    user[userid].append([unix_time, itemid])

for userid in user.keys():
    user[userid].sort(key=lambda x: x[0])

with open('data/Goodread.txt', 'w') as f:
    for u in user.keys():
        for i in user[u]:
            f.write('{} {}\n'.format(u, i[1]))