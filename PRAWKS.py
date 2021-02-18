import praw, time, datetime
from re import search, sub


c_id=''
c_secret=''
u_agent=''
uname=''
passwd=''
subreddit='valheim'
keywords = ['weapon','stone', 'axe', 'wood', 'hate', 'building']

#reddit API auth
reddit = praw.Reddit(client_id=c_id, client_secret=c_secret, user_agent=u_agent, username=uname, password=passwd)


def keywordSearch(subreddit):
    keywordMatches={}
    for comment in reddit.subreddit(subreddit).stream.comments():
        for keyword in keywords:
            if search(keyword, comment.body):
                match = str(comment.body) + '\n' + str(comment.submission.url) + '\n'
                if str(comment.body) not in keywordMatches:
                    with open("keywordHits.txt", "a+", encoding='utf-8') as txt:
                        txt.writelines(match)
                        txt.close
                    print("Matches logged to file @" + str(datetime.datetime.now()))
                    keywordMatches[str(comment.body)] = str(comment.submission.url)

print("Starting script at " + str(datetime.datetime.now()))
keywordSearch(subreddit)

     