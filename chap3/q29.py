from q20 import load_json
import re
import requests

if __name__ == '__main__':
    article = load_json('jawiki-country.json.gz')
    lis = article.split('\n')
    d = {}
    for l in lis:
        result = re.search('\|(.+)\s=\s*(.+)', l)
        if result:
            d[result[1]] = result[2]

    url = "https://commons.wikimedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "titles": "File:" + d['国旗画像'],
        "prop": "imageinfo",
        "iiprop":"url"
    }
    data = requests.Session().get(url=url, params=params).json()
    pages = data['query']['pages']
    for k, v in pages.items():
        print(v['imageinfo'][0]['url'])