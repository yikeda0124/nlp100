from q30 import load_mecab
from collections import Counter
import matplotlib.pyplot as plt

if __name__ == '__main__':
    lis = load_mecab('neko.txt.mecab')
    surface_lis =  [d['surface'] for d in lis]
    c = Counter(surface_lis)
    plt.hist(c.values(),  range = (1,10))
    plt.savefig("word_hist.png")
