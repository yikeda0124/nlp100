from q30 import load_mecab
from collections import Counter
import matplotlib.pyplot as plt
import math

if __name__ == '__main__':
    lis = load_mecab('neko.txt.mecab')
    surface_lis =  [d['surface'] for d in lis]
    c = Counter(surface_lis)
    v_lis = [kv[1] for kv in c.most_common()]
    log_x_lis = []
    log_v_lis = []
    for i in range(len(v_lis)):
        if v_lis[i] != 0:
            log_x_lis.append(math.log(i+1))
            log_v_lis.append(math.log(v_lis[i]))
    plt.scatter(log_x_lis, log_v_lis)
    plt.savefig("ziph.png")