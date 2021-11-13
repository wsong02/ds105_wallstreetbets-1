import praw as praw
import pandas as pd

reddit = praw.Reddit(
    client_id="0GFgVgByJ065sadDY62Q4g",
    client_secret="KfE32h3JMcZPLSF3UmYMJMsJbrXcaQ",
    password="ftu8uac9edb_TKM1yua",
    user_agent="testscript_for_WSB",
    username="ds105_WSB",
)

post_df = pd.DataFrame()

wsb = reddit.subreddit('wallstreetbets')
for submission in wsb.search('Daily Discussion Thread for', sort='new', time_filter='all', limit=500):
    if 'Daily Discussion Thread for' in submission.title:
        if 'June' in submission.title or 'July' in submission.title:
            #I need title, id, comments, score, put into post_df
            post_df = post_df.append({
                'id':submission.id,
                'title':submission.title,
                'score':submission.score,
                'comments':submission.comments
            }, ignore_index=True)

print(post_df)

for comments in post_df:
    