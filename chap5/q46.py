from q40 import Morph
from q41 import Chunk, Sentence
from q42 import load_parsed


if __name__ == '__main__':
    filename = './ai.ja.txt.parsed'

    chunks, sentences = load_parsed(filename)

    with open('ans46.txt', 'w') as f:
        for sentence in sentences:
            for chunk in sentence.chunks:
                    for morph in chunk.morphs:
                        if morph.pos == '動詞':
                            tmp_ans1, tmp_ans2 = [], []
                            for src in chunk.srcs:
                                tmp_str = ''
                                for m in sentence.chunks[src].morphs:
                                    tmp_str += m.surface
                                    if m.pos == '助詞':
                                        tmp_ans1.append(m.surface)
                                        tmp_ans2.append(tmp_str)
                            if len(tmp_ans1):
                                ans1 = sorted(list(set(tmp_ans1)))
                                ans2 = sorted(list(set(tmp_ans2)))
                                print(morph.base, *ans1, *ans2, sep='\t', file=f)

