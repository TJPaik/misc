#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""docstring summary

"""

from itertools import combinations

import networkx as nx
import numpy as np

name_converter = lambda x: str(sorted(x))


def simp_tree_to_hasse_diag(simp_tree):
    '''
    0 : unmatched
    1 : critical
    2 : regular
    '''
    hasse_diag = nx.DiGraph()
    for el1, el2 in simp_tree.get_filtration():
        hasse_diag.add_nodes_from([
            (name_converter(el1), {"dim": len(el1) - 1, "checked": 0}),
        ])
    for el1, el2 in simp_tree.get_filtration():
        tmp = [el[0] for el in simp_tree.get_boundaries(el1)]
        for el3 in tmp:
            hasse_diag.add_edge(name_converter(el3), name_converter(el1))
    return hasse_diag


def find_matching(hasse_diag):
    while True:
        data = hasse_diag.nodes.data()
        minimal_dim = 10 ** 9

        # find minimal dimension
        for el in data:
            if el[1]['checked'] == 0:
                minimal_dim = min(minimal_dim, el[1]['dim'])

        # check a simplex as a critical simplex
        for el in data:
            if el[1]['checked'] == 0 and el[1]['dim'] == minimal_dim:
                el[1]['checked'] = 1
                break

        doing = False
        for el1, el2 in data:
            if el2['checked'] != 0:
                continue
            doing = True
            faces = list(hasse_diag.predecessors(el1))
            face_check_data = np.asarray([hasse_diag.nodes.data()[el3]['checked'] for el3 in faces])
            tmp = np.where(face_check_data == 0)[0]
            if len(tmp) == 1:
                hasse_diag.nodes.data()[faces[tmp[0]]]['checked'] = 2
                hasse_diag.nodes.data()[el1]['checked'] = 2
                hasse_diag.remove_edge(faces[tmp[0]], el1)
                hasse_diag.add_edge(el1, faces[tmp[0]])
                # print('hm', el1, faces[tmp[0]])
        if not doing:
            break
    return hasse_diag


def make_critical_complex(hasse_diag):
    crit_simplices = [(el1, el2) for el1, el2 in hasse_diag.nodes.data() if el2['checked'] == 1]

    new_hasse_diag = nx.DiGraph()
    new_hasse_diag.add_nodes_from(crit_simplices)

    for el1, el2 in combinations(new_hasse_diag.nodes, 2):
        n_p1 = len(list(nx.all_simple_paths(hasse_diag, el1, el2)))
        n_p2 = len(list(nx.all_simple_paths(hasse_diag, el2, el1)))
        if n_p1 % 2 == 1:
            new_hasse_diag.add_edge(el1, el2)
        if n_p2 % 2 == 1:
            new_hasse_diag.add_edge(el2, el1)
    for el1, el2 in new_hasse_diag.nodes.data():
        el2['checked'] = 0
    return new_hasse_diag
