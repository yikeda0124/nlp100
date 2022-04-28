from q40 import Morph
from q41 import Chunk, Sentence
from q42 import load_parsed


if __name__ == '__main__':
    filename = './ai.ja.txt.parsed'

    chunks, sentences = load_parsed(filename)

    with open('ans45.txt', 'w') as f:
        for sentence in sentences:
            for chunk in sentence.chunks:
                    for morph in chunk.morphs:
                        if morph.pos == '動詞':
                            tmp_ans = []
                            for src in chunk.srcs:
                                for m in sentence.chunks[src].morphs:
                                    if m.pos == '助詞':
                                        tmp_ans.append(m.surface)
                            if len(tmp_ans):
                                ans = sorted(list(set(tmp_ans)))
                                print(morph.base, *ans, file=f)

