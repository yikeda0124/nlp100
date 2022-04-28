from q40 import Morph
from q41 import Chunk, Sentence
from q42 import load_parsed

import pydot
from graphviz import Digraph

if __name__ == '__main__':
    filename = './ai.ja.txt.parsed'

    chunks, sentences = load_parsed(filename)

    sentence = sentences[1]
    edges = []
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
            edges.append([from_chunk, to_chunk])
        n = pydot.Node('node')
        n.fontname = 'IPAGothic'
        g = pydot.graph_from_edges(edges, directed=True)
        g.add_node(n)
        g.write_png('ans44.png')
