#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""docstring summary

"""

import json

from SimplicialComplex import Torus
from functions import simp_tree_to_hasse_diag, find_matching, make_critical_complex

if __name__ == '__main__':
    initial_simplicial_complex = Torus()

    initial_hasse_diagram = simp_tree_to_hasse_diag(initial_simplicial_complex)
    new_hasse_diagram = initial_hasse_diagram.copy()

    while True:
        hasse_diagram = new_hasse_diagram
        hasse_diagram = find_matching(hasse_diagram)
        new_hasse_diagram = make_critical_complex(hasse_diagram)
        if len(new_hasse_diagram.edges) == 0:
            break

    homology = dict()
    for node in new_hasse_diagram.nodes:
        node = json.loads(node)
        if len(node) in homology:
            homology[len(node)] += 1
        else:
            homology[len(node)] = 1

    print('betti numbers')
    for dim, betti in sorted(homology.items(), key=lambda x: x[0]):
        print(f'H_{dim - 1} : {betti}', end='\t\t')
