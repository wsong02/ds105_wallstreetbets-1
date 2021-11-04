import requests
base_url = 'https://www.reddit.com/'
data = {'grant_type': 'password', 'username': ds105_WSB, 'password': ftu8uac9edb_TKM1yua}
auth = requests.auth.HTTPBasicAuth(t98Dt-EJGv44MvPSuuqxuA,2pBomcTda4lwfox1J3aUMQKhEgtKHg)
r = requests.post(base_url + 'api/v1/access_token',
                  data=data,
                  headers={'user-agent': 'APP-NAME by REDDIT-USERNAME'},
		  auth=auth)
d = r.json()