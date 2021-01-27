#! python3
import praw
import pandas as pd
import datetime as dt

topics_dict = {
    "title": [],
    "score": [],
    "id": [],
    "comms_num": [],
    "created": [],
    "body": []
}


reddit = praw.Reddit(client_id='ID',
                     client_secret='Secret Key',
                     user_agent='username',
                     username='username',
                     password='password')

subreddit = reddit.subreddit('wallstreetbets')

top_subreddit = subreddit.top(limit=500)

print(reddit.user.me())

for submission in top_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)

topics_data = pd.DataFrame(topics_dict)

def get_date(created):
    return dt.datetime.fromtimestamp(created)

_timestamp = topics_data["created"].apply(get_date)

topics_data = topics_data.assign(timestamp = _timestamp)

topics_data.to_csv('script_data.csv', index=False)


