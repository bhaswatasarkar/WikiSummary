import requests

def extract_image(base_url):
    title = base_url.rsplit('/', 1)[-1]
    api = "https://en.wikipedia.org/w/api.php?action=query&prop=pageimages&format=json&piprop=original&titles="+title
    response = requests.get(api).json()
    return list(response["query"]["pages"].values())[0]["original"]["source"]
