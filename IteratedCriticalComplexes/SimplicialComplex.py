#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""docstring summary

"""

from gudhi.simplex_tree import SimplexTree


def Torus():
    st = SimplexTree()
    st.insert([0, 3, 7])
    st.insert([0, 2, 7])
    st.insert([3, 4, 8])
    st.insert([3, 7, 8])
    st.insert([4, 0, 2])
    st.insert([2, 4, 8])
    st.insert([2, 7, 5])
    st.insert([2, 1, 5])
    st.insert([7, 5, 6])
    st.insert([7, 6, 8])
    st.insert([1, 2, 8])
    st.insert([1, 6, 8])
    st.insert([0, 1, 3])
    st.insert([1, 3, 5])
    st.insert([3, 4, 5])
    st.insert([4, 5, 6])
    st.insert([0, 1, 6])
    st.insert([0, 4, 6])
    return st


def DunceHat():
    st = SimplexTree()
    st.insert([1, 3, 5])
    st.insert([1, 5, 6])
    st.insert([1, 3, 6])
    st.insert([2, 3, 5])
    st.insert([3, 6, 7])
    st.insert([2, 3, 7])
    st.insert([2, 4, 5])
    st.insert([4, 5, 6])
    st.insert([4, 6, 8])
    st.insert([6, 7, 8])
    st.insert([1, 7, 8])
    st.insert([1, 2, 4])
    st.insert([1, 2, 7])
    st.insert([1, 3, 4])
    st.insert([3, 4, 8])
    st.insert([2, 3, 8])
    st.insert([1, 2, 8])
    return st


def S2():
    st = SimplexTree()
    st.insert([0, 1, 2])
    st.insert([0, 2, 3])
    st.insert([0, 3, 4])
    st.insert([0, 4, 1])
    st.insert([1, 1, 2])
    st.insert([1, 2, 3])
    st.insert([1, 3, 4])
    st.insert([1, 4, 1])
    return st


def ExampleOfBook():
    st = SimplexTree()
    st.insert([2, 4, 5])
    st.insert([0, 4, 5])
    st.insert([0, 4, 6])
    st.insert([0, 1, 6])
    st.insert([2, 3])
    st.insert([4, 3])
    st.insert([6, 3])
    return st
