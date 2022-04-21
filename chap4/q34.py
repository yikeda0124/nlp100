from q30 import load_mecab

if __name__ == '__main__':
    lis = load_mecab('neko.txt.mecab')

    result = []
    tmp_s = ''
    for l in lis:
        if l['pos'] == '名詞':
            tmp_s += l['surface']
        elif not tmp_s == '':
            result.append(tmp_s)
            tmp_s = ''

    print(result)
