#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 21:55:40 2016

@author: ue
"""

import praw

user_agent = "test program by /u/thenightskygazer"
app_id = "lw3n2hzJaaHsKQ"
app_secret = "4cHszCDERGvbIZOTx-elkWRqOq0"
app_uri = "https://127.0.0.1:65010/authorize_callback"
scopes = "account creddits edit flair history identity livemanage modconfig modcontributors modflair modlog modothers modposts modself modwiki mysubreddits privatemessages read report save submit subscribe vote wikiedit wikiread"
app_scopes = 'all app scopes'


#key in the submission ID of the Reddit thread you want to scrape
sub_id = "5fkwvk"

def get_replies(comment, reply_list):
    """ recursive function that goes through the reply tree of a comment """
    reply_list.append({"id": comment.id, "comment": comment.body})
    
    if len(comment._replies) > 0:
        for r in comment._replies:
            get_replies(r, reply_list)
    return reply_list




#state your purpose for conducting the comment scrape
reddit = praw.Reddit(user_agent=user_agent,\
                client_id=app_id,\
                client_secret=app_secret,\
                redirect_uri=app_uri)

submission = reddit.get_submission(submission_id=sub_id)



""" this is a costly operation due to reddit's limits but is necessary
    to get all comments and prevent errors in script """

submission.replace_more_comments(limit=None, threshold=0)

# final array for writing to file
final = []
for comment in submission.comments:
    """ loops through all comments to submission """
    x = []  # array that holds the comment and all replies

    # get all replies and append it to our array for writing to file
    final.append(get_replies(comment, x))

with open('comments.csv', 'a') as outf:
    """ open file and write to it """
    # 2 dimension array needs two for loops
    for ele in final:
        for ele2 in ele:
            # write to file in the proper comma delimited format, one per line
            outf.write(u"{0},{1}\n".format(ele2['id'], ele2['comment']).encode('utf-8'))