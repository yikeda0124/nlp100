from q20 import load_json
import re

if __name__ == '__main__':
    article = load_json('jawiki-country.json.gz')
    lis = article.split('\n')
    for l in lis:
        result = re.findall('File|ファイル:(.+?)\|', l)
        for r in result:
            print(r)