import MeCab

def load_mecab(filename):
    with open(filename) as f:
        text = f.read().split('\n')
    
    result = []
    for l in text:
        if l == 'EOS':
            continue
        ls = l.split('\t')
        tmp_d = {}
        if len(ls) <= 1:
            continue
        tmp = ls[1].split(',')
        tmp_d = {'surface':ls[0], 'base':tmp[6], 'pos':tmp[0], 'pos1':tmp[1]}
        result.append(tmp_d)
    
    return result

if __name__ == '__main__':
    lis = load_mecab('neko.txt.mecab')
    print(lis)