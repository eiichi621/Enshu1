import networkx as nx
import matplotlib.pyplot as plt

g = nx.fast_gnp_random_graph(100,0.8);

total_degree = 0;
for v in g.nodes():
	total_degree += g.degree(v)

# print "sum of degree is:" + str(total_degree)
# print "Number of edges is:" + str(len(g.edges()))

if total_degree == len(g.edges()) * 2:
	print "Akusyu is ok"
else:
	print "Akusyu is NG"

nx.draw(g)
plt.show()