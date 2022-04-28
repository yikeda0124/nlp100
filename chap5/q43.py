from q40 import Morph
from q41 import Chunk, Sentence
from q42 import load_parsed

if __name__ == '__main__':
    filename = './ai.ja.txt.parsed'

    chunks, sentences = load_parsed(filename)

    sentence = sentences[1]
    for chunk in sentence.chunks:
        if int(chunk.dst) == -1:
            from_chunk, to_chunk = '', ''
            from_flg, to_flg = False, False
            for morph in chunk.morphs:
                if morph.pos == '記号':
                    continue
                if morph.pos == '名詞':
                    from_flg = True
                from_chunk += morph.surface
            for morph in sentence.chunks[chunk.dst].morphs:
                if morph.pos == '記号':
                    continue
                if morph.pos == '動詞':
                    to_flg = True
                to_chunk += morph.surface
            if from_flg and to_flg:
                print(from_chunk, to_chunk, sep='\t')