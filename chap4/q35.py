from q30 import load_mecab
from collections import Counter

if __name__ == '__main__':
    lis = load_mecab('neko.txt.mecab')

    surface_lis = [l['surface'] for l in lis]
    c = Counter(surface_lis)
    print(c)