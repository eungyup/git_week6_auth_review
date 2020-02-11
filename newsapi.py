import requests
import secrets


base_url = "https://newsapi.org/v2/top-headlines"

params = {
    "q": "new hampshire",
    "apiKey": secrets.NEWSAPI_KEY
}

response = requests.get(base_url, params)
# print(response)
result = response.json()
# print(result)
result_article = result['articles']
# print("\n\nresult_article:",result_article)

for a_dict in result_article:
    print(a_dict['title']," - ", a_dict['source']['name'])