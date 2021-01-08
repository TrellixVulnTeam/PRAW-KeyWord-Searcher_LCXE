import praw

reddit = praw.Reddit(client_id='OECYB-E6JD01mg',
                     client_secret='BVZEzZ7_Y9B1qo7frGQ_IHvfha3vPA',
                     username='KeyWordBot1000',
                     password='BR1rZ@Co',
                     user_agent='keywordbot')

my_gpu_sub = reddit.submission(url='https://www.reddit.com/user/HaydenR50/comments/ktap3c/'
                                   'gpu_availability_bot_thread/?utm_source=share&utm_medium=web2x&context=3')
new_bpc = reddit.subreddit('buildapcsales').new(limit=10)

for submission in new_bpc:
    if '[GPU]' in submission.title or '[gpu]' in submission.title:
        reply_text = 'Here is a GPU Card Available: ' + submission.url
        my_gpu_sub.reply(reply_text)
