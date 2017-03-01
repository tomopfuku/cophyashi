import string, sys
from phylo3 import Node

"""
this takes a newick string as instr
and reads the string and makes the 
nodes and returns the root node
"""
def read_tree_string(instr):
	root = None
	index = 0
	nextchar = instr[index]
	start = True
	keepgoing = True
	curnode = None
	while keepgoing == True:
		if nextchar == "(":
			if start == True:
				root = Node()
				curnode = root
				start = False
			else:
				newnode = Node()
				curnode.add_child(newnode)
				curnode = newnode
		elif nextchar == ',':
			curnode = curnode.parent
		elif nextchar == ")":
			curnode = curnode.parent
			index += 1
                        nextchar = instr[index]
                        name = ""
			while True:
				if nextchar == ',' or nextchar == ')' or nextchar == ':' \
					or nextchar == ';' or nextchar == '[':
					break
				name += nextchar
				index += 1
				nextchar = instr[index]
			curnode.label = name
			index -= 1
		elif nextchar == ';':
			keepgoing = False
			break
		elif nextchar == ":":
			index += 1
			nextchar = instr[index]
			brlen = ""
			while True:
				if nextchar == ',' or nextchar == ')' or nextchar == ':' \
					or nextchar == ';' or nextchar == '[':
					break
				brlen += nextchar
				index += 1
				nextchar = instr[index]
			curnode.length = float(brlen)
			curnode.old_length = float(brlen)
			index -= 1
		elif nextchar == ' ':
			index += 1
			nextchar = instr[index]
		else: # this is an external named node
			newnode = Node()
			curnode.add_child(newnode)
			curnode = newnode
			curnode.istip = True
			name = ""
			while True:
				if nextchar == ',' or nextchar == ')' or nextchar == ':' \
					or nextchar == ';' or nextchar == '[':
					break
				name += nextchar
				index += 1
				nextchar = instr[index]
			curnode.label = name
			index -= 1
		if index < len(instr) - 1:
			index += 1
		nextchar = instr[index]
	return root


if __name__ == "__main__":
    s = "(a:3,(b:1e-05,c:1.3)int_|_and_33.5:5)root;"
    n2 = read_tree_string(s)
    print n2.get_newick_repr(True)
