import requests
res = requests.request(
	'GET',
	'https://api.nytimes.com/svc/search/v2/articlesearch.json',
    params={
	'api-key':'ZH1qAxxoXFtNXE9ueyMpBZT17NVSfAoU',
	'q': 'Bill Gates'
	}

)

print(res.content)