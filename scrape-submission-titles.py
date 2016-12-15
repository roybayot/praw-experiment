#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 23:32:32 2016

@author: ue
"""
import praw
from praw.models import MoreComments

user_agent = "test program by /u/thenightskygazer"
app_id = "lw3n2hzJaaHsKQ"
app_secret = "4cHszCDERGvbIZOTx-elkWRqOq0"
app_uri = "https://127.0.0.1:65010/authorize_callback"
scopes = "account creddits edit flair history identity livemanage modconfig modcontributors modflair modlog modothers modposts modself modwiki mysubreddits privatemessages read report save submit subscribe vote wikiedit wikiread"
app_scopes = 'all app scopes'

sub_id_1 = "5fg24t"
sub_id_0 = "5fkwvk"

reddit = praw.Reddit(user_agent=user_agent,\
                client_id=app_id,\
                client_secret=app_secret,\
                redirect_uri=app_uri)

subreddit = reddit.subreddit('AskReddit')

for submission in subreddit.stream.submissions():
    print(submission.id)
    print(submission.title)