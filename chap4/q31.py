from q30 import load_mecab

if __name__ == '__main__':
    lis = load_mecab('neko.txt.mecab')
    
    result = []
    for l in lis:
        if l['pos'] == '動詞':
            result.append(l['surface'])
    print(result)

