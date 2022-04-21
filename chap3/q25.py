from q20 import load_json
import re

if __name__ == '__main__':
    article = load_json('jawiki-country.json.gz')
    lis = article.split('\n')
    d = {}
    for l in lis:
        result =  re.search('\|(.+)\s=\s*(.+)', l)
        if result is not None:
            print(l)
            d[result[1]]=result[2]
    print(d)