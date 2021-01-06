import requests
import json

AUTH = "https://www.reddit.com/api/v1/access_token"
API = "https://oauth.reddit.com"
USER_AGENT = "Reddit News JS by BambooSlayerz"
CREDS = json.loads(open("creds.json").read())

def get_token():
    client_auth = requests.auth.HTTPBasicAuth(CREDS['id'], CREDS['secret'])
    headers = {"User-Agent":USER_AGENT}
    post = {'grant_type':'client_credentials'}
    return requests.post(AUTH, auth=client_auth, data=post, headers=headers).json()["access_token"]


def get(endpoint, token):
    headers = {"Authorization": "bearer " + token,"User-Agent":USER_AGENT} 
    return requests.get(API + endpoint, headers=headers).json()


if __name__ == "__main__":
    events = get("/r/news/?limit=100", get_token())
    for event in events['data']['children']:
        print(event['data']['title'])



