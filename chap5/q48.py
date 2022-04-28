from q40 import Morph
from q41 import Chunk, Sentence
from q42 import load_parsed


if __name__ == '__main__':
    filename = './ai.ja.txt.parsed'

    chunks, sentences = load_parsed(filename)

    sentence = sentences[1]
    for chunk in sentence.chunks:
        for morph in chunk.morphs:
            if morph.pos == '名詞':
                path = [''.join(morph.surface for morph in chunk.morphs if morph.pos != '記号')]
                while chunk.dst != -1: 
                    path.append(''.join(morph.surface for morph in sentence.chunks[chunk.dst].morphs if morph.pos != '記号'))
                    chunk = sentence.chunks[chunk.dst]
                print(' -> '.join(path))
