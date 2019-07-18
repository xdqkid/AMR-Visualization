#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
xdqkid
https://github.com/xdqkid/AMR-Visualization
'''

from graphviz import Digraph
import shutil
import os
import sys
import random

def convert2graph(amr_lines, amr_count):
    # Preprocess bracket
    amr_lines = ' '.join(amr_lines)
    newline = ''
    quotes = False
    for ele in amr_lines:
        if ele == '\"':
            quotes = not quotes
        if ele == '(' and quotes:
            ele = '&lt;'
        if ele == ')' and quotes:
            ele = '&gt;'
        newline += ele

    line = newline.replace('(', ' ( ') \
                .replace(')', ' ) ') \
                .replace('  ', ' ').split()
    # Check Format
    count = 0
    for ele in line:
        if ele == '(':
            count += 1
        if ele == ')':
            count -= 1
        if count < 0:
            print('[Error]Too many right bracket )')
            exit()
    if count != 0:
        print('[Error]Too many left bracket (')
        exit()
    relations = []
    concept_map = {}
    build_relations(line, relations=relations, concept_map=concept_map)
    # Postprocess bracket
    for key in concept_map.keys():
        concept_map[key] = concept_map[key] \
                            .replace('&lt;', '(') \
                            .replace('&gt;', ')')
    draw(relations, concept_map, amr_count)


def build_relations(line, relations=[], concept_map={}):
    if len(line) == 1:
        while True:
            id = str(random.randint(0, 1000))
            name = concept_map.get(id)
            if name == None:
                break
        concept_map[id] = line[0]
        return id
    line = line[1:-1]
    alen = len(line)
    id = line[0]
    concept_map[id]=line[2]
    idx = 3
    while idx < alen:
        relation = line[idx]
        search = idx + 1
        count = 0
        while search < alen:
            if line[search] == '(':
                count += 1
            if line[search] == ')':
                count -= 1
            if count == 0:
                break
            search += 1
        son_id = build_relations(line[idx+1:search+1], relations=relations, concept_map=concept_map)
        relations += [(id, son_id, relation)]
        idx = search + 1
    return id


def draw(relations, concept_map, amr_count):
    filename = './output/' + str(amr_count) + '.txt'
    f = Digraph('AMR-Graph', filename=filename)
    f.attr(rankdir='TB')
    for a, b, l in relations:
        f.node(a, concept_map[a])
        f.node(b, concept_map[b])
        f.edge(a, b, l)
    f.render(filename=filename, view=False)

def load_amr(fpath):
    try:
        shutil.rmtree('./output/*')
        os.mkdir('./output')
    except Exception:
        pass
    with open(fpath, mode='r', encoding='utf-8') as fp:
        amr_lines = []
        amr_count = 0
        for line in fp:
            if line.startswith('#'):
                continue
            if line.strip() == '':
                if len(amr_lines) != 0:
                    convert2graph(amr_lines, amr_count)
                    amr_count += 1
                    amr_lines = []
                continue
            amr_lines += [line.strip()]
        if len(amr_lines) != 0:
            convert2graph(amr_lines, amr_count)


if __name__ == "__main__":
    load_amr('test.txt' if len(sys.argv) == 1 else sys.argv[1])
