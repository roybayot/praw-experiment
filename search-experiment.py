#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 23:56:14 2016

@author: ue
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

results=reddit.search('whatever', subreddit=None, sort=None, syntax=None, period=None)

for x in results:
    print x