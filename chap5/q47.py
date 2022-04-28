from q40 import Morph
from q41 import Chunk, Sentence
from q42 import load_parsed


if __name__ == '__main__':
    filename = './ai.ja.txt.parsed'

    chunks, sentences = load_parsed(filename)

    with open('ans47.txt', 'w') as f:
        for sentence in sentences:
            for chunk in sentence.chunks:
                    for morph in chunk.morphs:
                        if morph.pos == '動詞':
                            use_flag = False
                            tmp_ans1 = ""
                            tmp_ans2 = []
                            for src in chunk.srcs:
                                if len(sentence.chunks[src].morphs) == 2 and sentence.chunks[src].morphs[0].pos1 == 'サ変接続' and sentence.chunks[src].morphs[1].surface == 'を':
                                    if not use_flag:
                                        tmp_ans1 = sentence.chunks[src].morphs[0].surface + sentence.chunks[src].morphs[1].surface + morph.base
                                        use_flag = True
                                else:
                                    for m in sentence.chunks[src].morphs:
                                        if m.pos == '助詞':
                                            tmp_ans2.append(m.surface)

                                if use_flag:
                                    ans2 = sorted(list(set(tmp_ans2)))
                                    print(tmp_ans1, *ans2, sep='\t', file=f)