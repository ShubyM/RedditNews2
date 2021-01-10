import json
from requests import post, get, auth

AUTH = "https://www.reddit.com/api/v1/access_token"
API = "https://oauth.reddit.com"
USER_AGENT = "Reddit News JS by BambooSlayerz"
CREDS = json.loads(open("creds.json").read())

def get_token():
    client_auth = auth.HTTPBasicAuth(CREDS['id'], CREDS['secret'])
    headers = {"User-Agent": USER_AGENT}
    data = {'grant_type':'client_credentials'}
    return post(AUTH, auth=client_auth, data=data, headers=headers).json()["access_token"]

def get_events(endpoint, token):
    ret = {}
    headers = {"Authorization": "bearer " + token,"User-Agent":USER_AGENT} 
    data = get(API + endpoint, headers=headers).json()
    for event in data['data']['children']:
        event = event['data']
            
        ret[event['title']] = {
            "ups" : event['ups'],
            "downs" : event['downs'],
            "upvote_ratio" : event['upvote_ratio'],
            "score" : None, #TODO: Potentially make request here
            "created" : event['created_utc'] #unix time stamp
        }

    return ret

if __name__ == "__main__":
    events = get_events("/r/news/?limit=100", get_token())
