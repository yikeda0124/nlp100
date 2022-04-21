from q30 import load_mecab
from collections import Counter
import matplotlib.pyplot as plt

if __name__ == '__main__':
    lis = load_mecab('neko.txt.mecab')
    surface_lis =  [d['surface'] for d in lis]
    d = {}
    for i in range(1, len(surface_lis)-1):
        if surface_lis[i] == '猫':
            if d.get(surface_lis[i-1]) is not None:
                d[surface_lis[i-1]] += 1
            else:
                d[surface_lis[i-1]] = 1
            if d.get(surface_lis[i+1]) is not None:
                d[surface_lis[i+1]] += 1
            else:
                d[surface_lis[i+1]] = 1
    sorted = sorted(d.items(), key = lambda item: item[1], reverse = True)
    data_x, data_y = [], []
    for i in range(10):
        data_x.append(sorted[i][0])
        data_y.append(sorted[i][1])
    plt.bar(data_x, data_y)
    plt.savefig("neko.png")

