from q40 import Morph
from q41 import Chunk, Sentence

def load_parsed(filename):
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

    return chunks, sentences

if __name__ == '__main__':
    filename = './ai.ja.txt.parsed'

    chunks, sentences = load_parsed(filename)

    sentence = sentences[1]
    for chunk in sentence.chunks:
        if int(chunk.dst) != -1:
            from_chunk, to_chunk = '', ''
            for morph in chunk.morphs:
                if morph.pos == '記号':
                    continue
                from_chunk += morph.surface
            for morph in sentence.chunks[chunk.dst].morphs:
                if morph.pos == '記号':
                    continue
                to_chunk += morph.surface
            print(from_chunk, to_chunk, sep='\t')