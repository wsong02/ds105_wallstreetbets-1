import praw as praw

reddit = praw.Reddit(
    client_id="0GFgVgByJ065sadDY62Q4g",
    client_secret="KfE32h3JMcZPLSF3UmYMJMsJbrXcaQ",
    password="ftu8uac9edb_TKM1yua",
    user_agent="testscript_for_WSB",
    username="ds105_WSB",
)

wsb = reddit.subreddit('wallstreetbets')
for submission in wsb.search('Daily Discussion Thread for', sort='new', time_filter='all', limit=500):
    if 'Daily Discussion Thread for' in submission.title:
        print(submission.title)