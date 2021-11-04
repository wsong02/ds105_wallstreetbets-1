import requests
res = requests.request(
	'GET',
	'https://api.nytimes.com/svc/search/v2/articlesearch.json',
    params={
	'api-key':'t98Dt-EJGv44MvPSuuqxuA',
	'q': 'Bill Gates'
	}

)

print(res.content)