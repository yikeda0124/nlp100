from q20 import load_json
import re

if __name__ == '__main__':
    article = load_json('jawiki-country.json.gz')
    lis = article.split('\n')
    d = {}
    for l in lis:
        result = re.search('\|(.+)\s=\s*(.+)', l)
        if result is not None:
            d[result[1]]=result[2]
            r1 = result[1].replace('\'', '')
            r2 = result[2].replace('\'', '')
            re1 = re.sub('\[\[(.+?)\]\]', '', r1)
            re2 = re.sub('\[\[(.+?)\]\]', '', r2)
            res1 = re.sub('<ref(.+)', '', re1)
            res2 = re.sub('<ref(.+)', '', re2)
            print(res1, res2)