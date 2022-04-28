class Morph:
  def __init__(self, morph):
    surface, attr = morph.split('\t')
    attr = attr.split(',')
    self.surface = surface
    self.base = attr[6]
    self.pos = attr[0]
    self.pos1 = attr[1]

if __name__ == '__main__':
    filename = './ai.ja.txt.parsed'

    with open(filename, mode='r') as f:
        lines = f.readlines()

    results = []
    tmp_morphs = []

    for line in lines:
        if line[0] == '*':
            continue
        elif line != 'EOS\n':
            tmp_morphs.append(Morph(line))
        elif len(tmp_morphs) != 0:
            results.append(tmp_morphs)
            tmp_morphs = []

    for m in results[1]:
        print(m.surface, m.base, m.pos, m.pos1)