from q30 import load_mecab
from collections import Counter
import matplotlib.pyplot as plt

if __name__ == '__main__':
    lis = load_mecab('neko.txt.mecab')

    surface_lis = [l['surface'] for l in lis]
    c = Counter(surface_lis)
    target = list(zip(*c.most_common(10)))
    plt.bar(*target)
    plt.savefig("word_freq.png")