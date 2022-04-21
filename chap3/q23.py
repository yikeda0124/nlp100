from q20 import load_json
import re

if __name__ == '__main__':
    article = load_json('jawiki-country.json.gz')
    lis = article.split('\n')
    for l in lis:
        if re.search('==+', l):
            level = l.count('=')//2 - 1
            result = l.replace('=','')
            print(result, level)