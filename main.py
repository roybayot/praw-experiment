# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import praw

user_agent = "test program by /u/thenightskygazer"
app_id = "lw3n2hzJaaHsKQ"
app_secret = "4cHszCDERGvbIZOTx-elkWRqOq0"
app_uri = "https://127.0.0.1:65010/authorize_callback"
scopes = "account creddits edit flair history identity livemanage modconfig modcontributors modflair modlog modothers modposts modself modwiki mysubreddits privatemessages read report save submit subscribe vote wikiedit wikiread"
app_scopes = 'all app scopes'


reddit = praw.Reddit(user_agent=user_agent,\
                client_id=app_id,\
                client_secret=app_secret,\
                redirect_uri=app_uri)

#for submission in reddit.subreddit('learnpython').hot(limit=10):
#    print submission.title
#r.set_oauth_app_info(app_id, app_secret, app_uri)
#r.get_authorize_url('...', scopes, True)
#r.refresh_access_information(app_refresh)
#print('Logged in')

#%%
urls = []
subreddit = reddit.subreddit("AMA")
for submission in subreddit.hot(limit=10):
    print(submission.title) # Output: the title of the submission
    print(submission.ups) # Output: upvote count
    print(submission.id) # Output: the ID of the submission
    print(submission.url)
    urls.append(submission.url)

#%%    
#for one_url in urls:
#    submission = reddit.submission(url=one_url)
#    
#    for top_level_comment in submission.comments:
#        print(top_level_comment.body)