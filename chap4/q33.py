from q30 import load_mecab

if __name__ == '__main__':
    lis = load_mecab('neko.txt.mecab')

    result = []
    for i in range(1, len(lis)-1):
        if (lis[i-1]['pos'] == '名詞' and lis[i]['surface'] == 'の' and lis[i+2]['pos'] == '名詞'):
            result.append(lis[i-1]['surface'] + lis[i]['surface'] + lis[i+1]['surface'])

    print(result)