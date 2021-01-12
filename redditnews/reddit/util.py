import json
from requests import post, get, auth
from .credentials import *

AUTH = "https://www.reddit.com/api/v1/access_token"
API = "https://oauth.reddit.com"

def get_token():
    client_auth = auth.HTTPBasicAuth(ID, SECRET)
    headers = {"User-Agent": USER_AGENT}
    data = {'grant_type':'client_credentials'}
    return post(AUTH, auth=client_auth, data=data, headers=headers).json()["access_token"]

def get_events(endpoint, token):
    ret = {}
    headers = {"Authorization": "bearer " + token,"User-Agent":USER_AGENT} 
    response = get(API + endpoint, headers=headers).json()
    for post in response['data']['children']:
        event = post['data']

        ret[event['title']] = {
            "ups" : event['ups'], # number of up votes
            "downs" : event['downs'], # number of down votes
            "upvote_ratio" : event['upvote_ratio'], # up vote ratio
            "score" : None, #TODO: Potentially make request here for analyzing sentiment
            "created" : event['created_utc'] #unix time stamp
        }

    return ret

if __name__ == "__main__":
    events = get_events("/r/news/?limit=100", get_token())
    print(events)
