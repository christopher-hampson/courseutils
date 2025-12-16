

# Import DFA and NFA objects from the automata library 
from automata.fa.dfa import DFA
from automata.fa.nfa import NFA

# Import hashlib for checking solutions
from hashlib import md5
from networkx import weisfeiler_lehman_graph_hash as wlhash, union_all
check_soln = lambda soln, hash : md5(str(soln).encode("utf-8")).hexdigest() == hash
DFA_hash = lambda A: wlhash(union_all([G:=A._get_digraph(),((X:=G.copy()).remove_node(A.initial_state) or X),((X:=G.copy()).remove_nodes_from(A.final_states) or X)],rename=('G1#', 'G2#','G3#')))
check_DFA_soln = lambda A, hash: DFA_hash(A.minify()) == hash

# Feel free to import any additional libraries that you will find useful
import itertools