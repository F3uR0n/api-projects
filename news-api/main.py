import requests

query = input("Which genre of news you want to see?\n")
api = "e4f2dcf84c504f44b0ebf494cf52b893"
url = f"https://newsapi.org/v2/everything?q={query}&from=2025-12-18&sortBy=publishedAt&apiKey={api}"
# print(url)

r = requests.get(url)
data = r.json()
print("Total Result: ", data["totalResults"])

articles = data["articles"]
index=1
for article in articles:
    print(f"{index} {article["author"]} \n {article["url"]} \n" + "-"*40)
    index += 1