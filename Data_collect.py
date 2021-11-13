import praw as praw
import pandas as pd

reddit = praw.Reddit(
    client_id="0GFgVgByJ065sadDY62Q4g",
    client_secret="KfE32h3JMcZPLSF3UmYMJMsJbrXcaQ",
    password="ftu8uac9edb_TKM1yua",
    user_agent="testscript_for_WSB",
    username="ds105_WSB",
)

posts_df = pd.DataFrame()

# post = reddit.submission('qskqik')
# post.comments.replace_more(limit=None)
# posts_df = posts_df.append({
#     'id':post.id,
#     'title':post.title,
#     'score':post.score,
#     'top_level_comments': list(post.comments)
# }, ignore_index=True)

wsb = reddit.subreddit('wallstreetbets')
for submission in wsb.search('Daily Discussion Thread for', sort='new', time_filter='all', limit=500):
    if 'Daily Discussion Thread for ' in submission.title:
        if 'June' in submission.title or 'July' in submission.title:
            #I need title, id, comments, score, put into posts_df
            submission.comments.replace_more(limit=None)
            posts_df = posts_df.append({
                'id':submission.id,
                'title':submission.title,
                'score':submission.score,
                'top_level_comments': list(submission.comments)
            }, ignore_index=True)


posts_df.to_csv(r'posts.csv')

comments_df = pd.DataFrame()
for posts in posts_df.itertuples():
    for comment in posts.top_level_comments:
        comments_df = comments_df.append({
            'id':comment.id,
            'post_id':comment.link_id,
            'body':comment.body,
            'score':comment.score
        }, ignore_index=True)

comments_df.to_csv(r'comments.csv')
