import tree_utils
import stratoML
import calc_bm_likelihood as brownian
import node_opt

tree = tree_utils.read_tree("../test_data/fossils_strat.tre")
ranges = tree_utils.read_strat("../test_data/fossils_strat.txt")
tree_utils.match_strat(tree,ranges)
ranges = None

tree_utils.init_heights_strat(tree)
print tree.get_newick_repr(True)

print -stratoML.hr97_loglike(tree,lam=1.0)
#print tree.get_newick_repr(True)

opt = stratoML.optim_lambda_heights(tree,ranges)

#print opt
t1= tree.get_newick_repr(True)
t2= opt[0].get_newick_repr(True)
print t1
