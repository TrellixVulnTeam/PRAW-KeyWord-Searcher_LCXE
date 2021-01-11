import praw
import time
from requests.exceptions import HTTPError, ConnectionError, Timeout

reddit = praw.Reddit(client_id='OECYB-E6JD01mg',
                     client_secret='BVZEzZ7_Y9B1qo7frGQ_IHvfha3vPA',
                     username='KeyWordBot1000',
                     password='BR1rZ@Co',
                     user_agent='keywordbot')

my_gpu_sub = reddit.submission(url='https://www.reddit.com/user/HaydenR50/comments/ktap3c/'
                                   'gpu_availability_bot_thread/?utm_source=share&utm_medium=web2x&context=3')
new_bpc = reddit.subreddit('buildapcsales').new(limit=1)

timer = .5
errors = 1
while True:
    try:
        time.sleep(timer)
        for submission in new_bpc:
            if 'RTX' in submission.title or '[Restock]' in submission.title:
                my_gpu_sub.reply('An RTX Card/Restock has been mentioned: ' + submission.url)
        timer = .5
        errors = 1
    except(HTTPError, ConnectionError, Timeout) as e:
        if errors == 1:
            my_gpu_sub.reply('Problem Occurred! This has occurred only once.')
        else:
            my_gpu_sub.reply('Problem Occurred! This has occurred ' + str(errors) + ' times. Reddit may be down.')
        timer = (errors * 300)
        errors += 1
