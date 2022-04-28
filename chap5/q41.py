from q40 import Morph

class Chunk:
    def __init__(self, morphs, dst):
        self.morphs = morphs
        self.dst = dst
        self.srcs = []

class Sentence:
    def __init__(self, chunks):
        self.chunks = chunks
        for i, chunk in enumerate(self.chunks):
            if chunk.dst != -1:
                self.chunks[chunk.dst].srcs.append(i)

if __name__ == '__main__':
    filename = './ai.ja.txt.parsed'

    with open(filename, mode='r') as f:
        lines = f.readlines()

    chunks, tmp_morphs, sentences = [], [], []

    for line in lines:
        if line[0] == '*':
            if len(tmp_morphs) > 0:
                chunks.append(Chunk(tmp_morphs, dst))
                tmp_morphs = []
            dst = int(line.split(' ')[2][:-1])
        elif line != 'EOS\n':
            tmp_morphs.append(Morph(line))
        elif len(tmp_morphs) != 0:
            chunks.append(Chunk(tmp_morphs, dst))
            sentences.append(Sentence(chunks))
            tmp_morphs, chunks = [], []

    for chunk in sentences[1].chunks:
        print([m.surface for m in chunk.morphs], chunk.dst, chunk.srcs)