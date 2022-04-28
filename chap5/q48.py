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
                path = []
                tmp_str = ''
                for morph in chunk.morphs:
                    if morph.pos != '記号':
                        tmp_str += morph.surface
                path.append(tmp_str)
                while chunk.dst != -1:
                    tmp_str = ''
                    for morph in sentence.chunks[chunk.dst].morphs:
                        if morph.pos != '記号':
                            tmp_str += morph.surface
                    path.append(tmp_str)
                    chunk = sentence.chunks[chunk.dst]
                print(' -> '.join(path))
