# -*- coding: utf-8 -*-
"""
Module: classifier.py
Description: Weighted multi-class classifier mapping exam questions
             to specific syllabus domains, including legacy/deprecated topics.
"""

import re


class SyllabusClassifier:
    """
    Classifies questions into official GATE CS/IT syllabus sections
    using keyword, regex, and domain-weighting heuristics.
    """

    SECTIONS = {
        1: "Section 1: Engineering Mathematics",
        2: "Section 2: Digital Logic",
        3: "Section 3: Computer Organization and Architecture",
        4: "Section 4: Programming and Data Structures",
        5: "Section 5: Algorithms",
        6: "Section 6: Theory of Computation",
        7: "Section 7: Compiler Design",
        8: "Section 8: Operating Systems",
        9: "Section 9: Databases",
        10: "Section 10: Computer Networks",
        11: "Section 11: Legacy & Deprecated Topics",
    }

    # Keyword weights per section: (keyword, weight)
    RULES = {
        11: [
            ('cocomo', 10), ('kloc', 10), ('waterfall', 10), ('spiral development', 10),
            ('coupling', 8), ('cohesion', 8), ('srs document', 10), ('function point', 10),
            ('cyclomatic complexity', 9), ('code walkthrough', 10), ('code inspection', 10),
            ('<table border', 10), ('rowspan', 10), ('colspan', 10), ('white-box', 9),
            ('black-box testing', 9), ('equivalence class partitioning', 10)
        ],
        7: [
            ('ll(1)', 10), ('lr(1)', 10), ('slr', 10), ('lalr', 10), ('shift-reduce', 10),
            ('syntax-directed', 10), ('s-attributed', 10), ('l-attributed', 10),
            ('intermediate code', 9), ('basic block', 9), ('liveness', 9), ('live variable', 9),
            ('parsing table', 10), ('parse tree', 8), ('derivation tree', 8),
            ('lexical analyzer', 9), ('token stream', 9), ('handle', 8), ('backpatching', 10),
            ('3-address', 9), ('three-address', 9), ('activation record', 8), ('lexical scoping', 8)
        ],
        6: [
            ('dfa', 10), ('nfa', 10), ('turing machine', 10), ('context-free language', 10),
            ('context-free grammar', 10), ('regular expression', 9), ('regular language', 9),
            ('pda', 9), ('pushdown', 9), ('undecidable', 9), ('decidability', 9),
            ('recursively enumerable', 10), ('pumping lemma', 10), ('cfg', 7)
        ],
        8: [
            ('page fault', 10), ('paging', 9), ('page table', 9), ('page replacement', 10),
            ('virtual memory', 9), ('semaphore', 10), ('critical section', 10),
            ('deadlock', 9), ('banker', 10), ('round robin', 8), ('srtf', 9), ('sjf', 9),
            ('fcfs', 8), ('fork()', 10), ('disk scheduling', 10), ('sstf', 10),
            ('c-look', 10), ('inode', 10), ('time quantum', 9), ('preemptive scheduling', 8),
            ('context switch', 8)
        ],
        9: [
            ('relational algebra', 10), ('tuple relational', 10), ('select *', 10),
            ('from student', 8), ('functional dependenc', 10), ('bcnf', 10), ('3nf', 10),
            ('2nf', 10), ('candidate key', 10), ('superkey', 10), ('lossless', 9),
            ('b+ tree', 9), ('b-tree', 8), ('serializability', 10), ('serializable', 10),
            ('2pl', 10), ('two phase locking', 10), ('foreign key', 9), ('er model', 9)
        ],
        10: [
            ('tcp', 9), ('udp', 9), ('ipv4', 10), ('datagram', 9), ('subnet', 10),
            ('cidr', 10), ('routing protocol', 9), ('distance vector', 10), ('link state', 10),
            ('csma/cd', 10), ('sliding window', 10), ('stop-and-wait', 10), ('go-back-n', 10),
            ('selective repeat', 10), ('dns', 8), ('http', 8), ('socket api', 10),
            ('mac address', 9), ('arp', 9), ('token ring', 9)
        ],
        3: [
            ('pipelined', 9), ('pipeline', 9), ('hazard', 8), ('clock cycle', 8), ('cpi', 9),
            ('cache memory', 9), ('cache hit', 9), ('direct mapped', 10), ('set associative', 10),
            ('miss penalty', 9), ('tag field', 9), ('addressing mode', 9), ('instruction format', 9),
            ('dma controller', 10), ('interrupt', 7), ('word-addressable', 9),
            ('byte-addressable', 8), ('alu', 8), ('micro-operation', 9)
        ],
        2: [
            ('karnaugh', 10), ('k-map', 10), ('boolean function', 9), ('minterm', 10),
            ('maxterm', 10), ('sum-of-products', 9), ('product-of-sums', 9), ('multiplexer', 9),
            ('decoder', 9), ('flip-flop', 10), ('counter', 8), ("2's complement", 10),
            ('ieee-754', 10), ('floating point', 8), ('ripple-carry', 9), ('full adder', 9)
        ],
        4: [
            ('#include', 8), ('printf', 8), ('singly-linked', 10), ('doubly linked', 10),
            ('binary search tree', 9), ('bst', 8), ('max-heap', 8), ('min-heap', 8),
            ('inorder', 8), ('preorder', 8), ('postorder', 8), ('stack', 7), ('queue', 7),
            ('recursion', 7), ('int main', 7), ('void main', 7)
        ],
        5: [
            ('quicksort', 10), ('mergesort', 10), ('heapsort', 10), ('bubble sort', 9),
            ('time complexity', 8), ('recurrence relation', 8), ('asymptotic', 9),
            ('spanning tree', 9), ('mst', 9), ('dijkstra', 10), ('shortest path', 9),
            ('bellman-ford', 10), ('hash table', 8), ('linear probing', 9),
            ('dynamic programming', 9), ('knapsack', 9), ('bfs', 7), ('dfs', 7)
        ],
        1: [
            ('matrix', 6), ('determinant', 8), ('eigenvalue', 9), ('eigenvector', 9),
            ('linear equations', 8), ('rank', 7), ('lu decomposition', 10), ('probability', 7),
            ('poisson', 9), ('normal distribution', 9), ('random variable', 8), ('variance', 8),
            ('limit', 6), ('derivative', 7), ('integral', 7), ('polynomial', 6),
            ('group', 6), ('subgroup', 8), ('lattice', 8), ('partial order', 8),
            ('chromatic', 9), ('eulerian', 9), ('planar', 8), ('permutation', 7),
            ('tautology', 8), ('predicate', 8)
        ],
    }

    def classify(self, text: str) -> int:
        """
        Computes a score for each section based on matched weighted terms.
        Returns the section ID with the highest score (defaults to 1: Mathematics).
        """
        t = text.lower()

        scores = {sec_id: 0 for sec_id in self.SECTIONS}

        for sec_id, rule_list in self.RULES.items():
            for kw, weight in rule_list:
                if kw in t:
                    scores[sec_id] += weight

        # Sort by score descending
        best_section = max(scores, key=scores.get)
        if scores[best_section] == 0:
            return 1  # Default fallback
        return best_section

    def get_section_name(self, sec_id: int) -> str:
        return self.SECTIONS.get(sec_id, "Unknown Section")
