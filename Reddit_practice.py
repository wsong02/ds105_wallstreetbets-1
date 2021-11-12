
import requests

# note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'
auth = requests.auth.HTTPBasicAuth('0GFgVgByJ065sadDY62Q4g', 'KfE32h3JMcZPLSF3UmYMJMsJbrXcaQ')

# here we pass our login method (password), username, and password
data = {'grant_type': 'password',
        'username': 'ds105_WSB',
        'password': 'ftu8uac9edb_TKM1yua'}

# setup our header info, which gives reddit a brief description of our app
headers = {'User-Agent': 'MyBot/0.0.1'}

# send our request for an OAuth token
res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)

# convert response to JSON and pull access_token value
TOKEN = res.json()['access_token']

# add authorization to our headers dictionary
headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

# while the token is valid (~2 hours) we just add headers=headers to our requests
requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

res = requests.get('https://oauth.reddit.com/r/wallstreetbets/hot',headers=headers).json()
print(res)